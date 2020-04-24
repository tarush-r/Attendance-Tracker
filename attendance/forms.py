from django.forms import ModelForm, TextInput
from .models import Subject

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields=['name']
        widgets={'name': TextInput(attrs={'class':'input', 'placeholder':'Enter Subject ', 'size':60})}