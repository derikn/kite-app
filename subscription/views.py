from django.http import HttpResponse
from django.views import generic
from . import models
from .forms import SubscriberForm
from django.utils import timezone
from django.contrib import messages
from braces import views

class IndexView(views.FormValidMessageMixin,
	generic.CreateView):

	model = models.Subscriber
	form_class = SubscriberForm

	def get_form_valid_message(self):
        	return u"Thanks for checking us out. Subscribed with {0}!".format(self.object.email)

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.sub_date = timezone.now()
		self.object.save()
		return super(IndexView, self).form_valid(form)