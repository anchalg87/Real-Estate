from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from .forms import ContactForm, PropertyForm
from .models import Property, PropertyType, Agent, RealEstateAgency
from users.models import UserInfo

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['anchu.gupta@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Thank you for contacting us!')
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, "contactus.html", {'form': form})

@login_required
def sellproperty(request):
    if request.user.is_agent:
        if request.method == 'POST':
            form = PropertyForm(request.POST)
            if form.is_valid():
                user = UserInfo.objects.filter(username=request.user.username).first()
                agent = Agent.objects.filter(user=user.id).first()
                form_obj = form.save(commit=False)
                form_obj.agent = agent
                form_obj.save()
                messages.success(request, 'Property Added')
                return redirect('home')
        else:
            form = PropertyForm()
        return render(request, 'homesapp/sell_property.html', {'form': form})
    else:
        return HttpResponse('Please login as an agent to create a listing.')


class PropertiesView(ListView):
    template_name = 'homesapp/buy.html'
    paginate_by = 10

    def get_queryset(self):
        properties = None
        city = self.request.GET.get("city", "")
        ptype = self.request.GET.get("ptype", "")
        beds = self.request.GET.get("beds", "")
        if city != "":
            properties = Property.objects.filter(prop_city=city).order_by('-date_created')
        if ptype != "":
            ptypes = PropertyType.objects.filter(prop_type=ptype).first()
            properties = Property.objects.filter(property_type=ptypes.id).order_by('-date_created')
        if beds != "":
            properties = Property.objects.filter(no_of_beds=beds).order_by('-date_created')
        if properties:
            return properties
        else:
            return Property.objects.all().order_by('-date_created')


class AgentsView(ListView):
    template_name = 'homesapp/find_agent.html'
    paginate_by = 10

    def get_queryset(self):
        agents = None
        city = self.request.GET.get("city", "")
        agent_name = self.request.GET.get("name", "")
        if city != "":
            agency = RealEstateAgency.objects.filter(agency_city=city).first()
            agents = Agent.objects.filter(agency=agency.id)
        if agent_name != "":
            name = agent_name.split(" ")
            fname = name[0]
            lname = name[1]
            user = UserInfo.objects.filter(first_name=fname, last_name=lname).first()
            agents = Agent.objects.filter(user_id=user.id)
        if agents:
            return agents
        else:
            return Agent.objects.all().order_by('user__first_name')


class PropertyDetail(DetailView):
    model = Property
    template_name = 'homesapp/propertydetail.html'


class AgentDetail(DetailView):
    model = Agent
    template_name = 'homesapp/agentdetail.html'


class PropertyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Property
    fields = ['property_type', 'property_desc', 'prop_address1', 'prop_address2', 'prop_city', 'prop_state',
              'prop_zip', 'area', 'year_built', 'price', 'no_of_beds', 'no_of_baths', 'prop_image']

    def form_valid(self, form):
        form.instance.agent.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.agent.user:
            return True
        return False


class PropertyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Property
    success_url = '/buy/'

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.agent.user:
            return True
        return False