from django.contrib import admin
from .models import UserProfile
from .models import items

# Register your models here.
from .models import Extras
admin.site.register(Extras)
admin.site.register(UserProfile)
admin.site.register(items)