from django import forms
from .models import Property, PropertyImages, RealEstateAgency, Agent


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('property_type', 'property_desc', 'prop_address1', 'prop_address2', 'prop_city', 'prop_state',
                  'prop_zip', 'area', 'year_built', 'price', 'no_of_beds', 'no_of_baths', 'floor_type', 'prop_image',)


class PropertyImagesForm(forms.ModelForm):

    class Meta:
        model = PropertyImages
        fields = ('image', 'img_desc',)


class RealEstateAgencyForm(forms.ModelForm):

    class Meta:
        model = RealEstateAgency
        fields = ('agency_name', 'agency_email', 'agency_phone', 'agency_address1', 'agency_address2', 'agency_city',
                  'agency_state', 'agency_zip',)


class AgentForm(forms.ModelForm):
    agent_desc = forms.CharField(widget=forms.Textarea, label='Bio', required=False)
    date_of_birth = forms.DateField(widget=forms.DateInput(format='%m-%d-%Y', attrs={'placeholder': 'mm/dd/yyyy'}))
    member_since = forms.DateField(widget=forms.DateInput(format='%m-%d-%Y', attrs={'placeholder': 'mm/dd/yyyy'}))

    class Meta:
        model = Agent
        fields = ('agent_phone', 'date_of_birth', 'member_since', 'agency', 'agent_desc', 'agent_image')


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
