from django.forms import ModelForm
from .models import Crud

class CrudForm(ModelForm):
    class Meta:
        model = Crud
        fields = [
            'item', 'completed'
        ]
