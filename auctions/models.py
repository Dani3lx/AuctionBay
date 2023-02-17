from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# Listing names are unique
class Listing(models.Model):
    listing_name = models.CharField(primary_key=True, max_length=64)
    listing_desc = models.CharField(max_length=256)
    starting_bid = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.TimeField(auto_now=False, auto_now_add=False)

class Bid(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)