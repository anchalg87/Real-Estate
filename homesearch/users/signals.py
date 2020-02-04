from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, UserInfo
from homesapp.models import Agent


@receiver(post_save, sender=UserInfo)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_agent:
            profile = Agent.objects.create(user=instance)
            profile.save()
        else:
            profile = Profile.objects.create(user=instance)
            profile.save()
