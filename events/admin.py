from django.contrib import admin

# Register your models here.
from .models import Events
admin.site.register(Events,)
from .models import Registration

admin.site.register(Registration)