from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Issue)
admin.site.register(Politician)
admin.site.register(AppUser)
