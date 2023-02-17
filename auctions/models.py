from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    listing_name = models.CharField(max_length=64)
    listing_desc = models.CharField(max_length=256)
    starting_bid = models.IntegerField()
    post_date = models.TimeField(auto_now=False, auto_now_add=False)

class Bid(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

class Comment(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()