
from django.forms import ModelForm
from . models import TodoList


class todoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = [
            'item', 'completed'
        ]