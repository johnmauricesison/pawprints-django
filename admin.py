from django.contrib import admin
from .models import AnimalReport
from .models import UserProfile
from .models import Event

admin.site.register(AnimalReport)
admin.site.register(UserProfile)
admin.site.register(Event)

