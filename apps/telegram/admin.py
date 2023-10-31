from django.contrib import admin
from apps.telegram.models import TelegramUser, Contacts
# Register your models here.
admin.site.register(TelegramUser)
admin.site.register(Contacts)


