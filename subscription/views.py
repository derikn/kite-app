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
	form_valid_message = "Thanks for your interest. We'll keep you posted with updates!"

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.sub_date = timezone.now()
		self.object.save()
		return super(IndexView, self).form_valid(form)