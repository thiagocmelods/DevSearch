from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            email = user.email,
            name=user.first_name,            
        )

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    

post_save.connect(createProfile, sender=User)
post_save.connect(deleteUser, sender=Profile)
