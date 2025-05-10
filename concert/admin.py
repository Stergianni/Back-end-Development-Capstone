# from django.contrib import admin

# # Register your models here.
# admin.site.register(Concert)
# from .models import Concert
from django.contrib import admin
from .models import Concert, Photo, Song, ConcertAttending  # <-- This line was missing

admin.site.register(Concert)
admin.site.register(Photo)
admin.site.register(Song)
admin.site.register(ConcertAttending)
