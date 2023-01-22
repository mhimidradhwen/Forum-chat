from django.contrib import admin

# Register your models here.
from .models import Message ,Sender

admin.site.register(Sender)
admin.site.register(Message)