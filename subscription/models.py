from django.db import models
from django.core.urlresolvers import reverse

class Subscriber(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    sub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
		return reverse('sub:home')