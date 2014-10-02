from __future__ import absolute_import
import datetime
from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Div, HTML, Field
from . import models	


class SubscriberForm(forms.ModelForm):
    class Meta:
        fields = ('email',)
        model = models.Subscriber

    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'email',
            ButtonHolder(
                Submit('subscribe', 'Subscribe', css_class='btn-primary')
            )
        )