from .models import details
from django.forms import ModelForm

class details_forms(ModelForm):
    class Meta:
        model=details
        fields='__all__'

        