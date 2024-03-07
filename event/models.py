from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

RATING = ((1, "Highly Dissatisfied"), (2, "Dissatisfied"), (3, "Neutral"), (4, "Satisfied"), (5, "Highly Satisfied"))

# Create your models here.

class Interests(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    keywords = models.ManyToManyField(Interests)
    max_participation = models.PositiveIntegerField(blank=True, null=True)
    event_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
       ordering = ["-date"]


    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bio = models.TextField()
    username = models.CharField(max_length=50, unique=True)
    interests = models.ManyToManyField(Interests)
    events = models.ManyToManyField(Event)
    # profile_image
    
    def __str__(self):
        return self.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, username=instance.username)


class Review(models.Model):
    title = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="Review_title")
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="User_name")
    reviewbody = models.TextField()
    rating = models.IntegerField(choices=RATING, default=5)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-rating"]

    def __str__(self):
        return f"Review {self.reviewbody} by {self.user}"