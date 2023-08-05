from django import forms

#modelos que queremos validar
from .models import Tarea

class TareaForm(forms.ModelForm):
  class Meta: 
    model = Tarea
    exclude = []
  