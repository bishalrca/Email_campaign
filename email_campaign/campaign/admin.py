from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import EmailList, Subscriber, Campaign

admin.site.register(EmailList)
admin.site.register(Subscriber)
admin.site.register(Campaign)
