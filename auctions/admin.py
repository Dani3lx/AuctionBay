from django.contrib import admin

from .models import Listing, Watchlist, Comment

# Register your models here.
admin.site.register(Listing)
admin.site.register(Watchlist)
admin.site.register(Comment)
