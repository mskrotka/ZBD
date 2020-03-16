from django.forms import ModelForm
from .models import Wplyw


class FlowForm(ModelForm):
    class Meta:
        model = Wplyw
        fields = ['name', 'flow', 'how_much', 'category']  # użyte w formularzu
