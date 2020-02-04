from django.db import models
from django_enumfield import enum
from django.conf import settings
from django.core.validators import validate_email
from phone_field import PhoneField
from django.urls import reverse
from PIL import Image

# Create your models here.


class PriceType(enum.Enum):
    Full = 0
    Annually = 1
    Monthly = 2


class PropertyType(models.Model):
    prop_type = models.CharField(max_length=200)

    def __str__(self):
        return self.prop_type


class RealEstateAgency(models.Model):
    agency_name = models.CharField(max_length=200)
    agency_email = models.EmailField(unique=True, validators=[validate_email, ])
    agency_phone = PhoneField(null=True)
    agency_address1 = models.CharField(max_length=200)
    agency_address2 = models.CharField(max_length=200, blank=True)
    agency_city = models.CharField(max_length=100)
    agency_state = models.CharField(max_length=3)
    agency_zip = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agency_name


class Agent(models.Model):
    agent_phone = PhoneField(null=True, blank=True)
    agent_desc = models.TextField(null=True, blank=True)
    member_since = models.DateField(null=True)
    date_of_birth = models.DateField(null=True)
    agency = models.ForeignKey(RealEstateAgency, on_delete=models.CASCADE, null=True)
    agent_image = models.ImageField(default='default.jpg', upload_to='agent_pics', blank=True)
    IsActive = models.BooleanField(default=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.agent_image.path).convert('RGB')

        if img.height > 120 or img.width > 120:
            output_size = (120, 120)
            img.thumbnail(output_size)
            img.save(self.agent_image.path)


class Property(models.Model):
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, null=True)
    property_desc = models.TextField(blank=True)
    prop_address1 = models.CharField(max_length=200)
    prop_address2 = models.CharField(max_length=200, blank=True)
    prop_city = models.CharField(max_length=100)
    prop_state = models.CharField(max_length=3)
    prop_zip = models.CharField(max_length=10)
    prop_image = models.ImageField(default='property.jpg', upload_to='cover_pics', blank=True)
    area = models.DecimalField(max_digits=19, decimal_places=2,default=0.00)
    year_built = models.SmallIntegerField(default=1900)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    no_of_beds = models.IntegerField(default=0)
    no_of_baths = models.IntegerField(default=0)
    floor_type = models.CharField(max_length=200)
    IsShared = models.BooleanField(default=False)
    IsRental = models.BooleanField(default=False)
    rent_term = models.CharField(max_length=100, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prop_address1

    def get_absolute_url(self):
        return reverse('prop-detail', kwargs={'pk': self.pk})


class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(default='property.jpg', upload_to='property_pics', blank=True)
    img_desc = models.CharField(max_length=200, default='image', blank=True)

    def __str__(self):
        return self.img_desc

