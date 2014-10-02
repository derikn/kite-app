from django.contrib import admin
from subscription.models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    fields = ['sub_date', 'email']

admin.site.register(Subscriber, SubscriberAdmin)