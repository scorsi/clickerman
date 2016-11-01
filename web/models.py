from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Address(models.Model):
    alias = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    line1 = models.TextField()
    line2 = models.TextField(null=True, blank=True)
    postcode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.name()


class Media(models.Model):
    file = models.FileField(upload_to="medias/%Y/%m/%d/")
    date_uploaded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.file


class SocialNetwork(models.Model):
    name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=100, blank=True)
    url = models.URLField()
    is_shareable = models.BooleanField()
    is_followable = models.BooleanField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_birthday = models.DateField(null=True, blank=True)
    addresses = models.ManyToManyField(Address, blank=True)
    medias = models.ManyToManyField(Media, blank=True)
    social_networks = models.ManyToManyField(SocialNetwork, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Enterprise(models.Model):
    name = models.CharField(max_length=100)
    siren = models.CharField(max_length=50)
    url = models.URLField()
    is_active = models.BooleanField()
    date_joined = models.DateField(auto_now_add=True)
    date_deleted = models.DateField()
    addresses = models.ManyToManyField(Address, blank=True)
    medias = models.ManyToManyField(Media, blank=True)
    users = models.ManyToManyField(User, blank=True)
    social_networks = models.ManyToManyField(SocialNetwork, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey('Category', blank=True, null=True)
    medias = models.ManyToManyField(Media, blank=True)

    def __str__(self):
        return self.name


class Bundle(models.Model):
    enterprise = models.ForeignKey(Enterprise)
    name = models.CharField(max_length=100)
    description = models.TextField()
    total_value = models.IntegerField()
    date_started = models.DateField()
    date_ended = models.DateField()
    STATUS_CHOICES = (
        ('0', 'Draft'),
        ('1', 'Waiting'),
        ('2', 'Validated'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True)
    medias = models.ManyToManyField(Media, blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name


class Prize(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE, null=False)
    medias = models.ManyToManyField(Media, blank=True)

    def __str__(self):
        return self.name


class PrizePosition(models.Model):
    prize = models.ForeignKey(Prize, null=False)
    position = models.PositiveSmallIntegerField(default=1)
