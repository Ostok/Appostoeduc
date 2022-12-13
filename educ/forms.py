from django import forms
from django.forms import ModelForm
from educ.models import Estudiante
from educ.models import Eje
from educ.models import Inscripcion



class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingrese su nombre'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingrese su Email'
            }
        )
    )
    mensaje = forms.CharField(
        label='Mensaje',
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Max. 200 caracteres',
                'rows':5
            }
        )
    )
    
    
class EstudianteForm(forms.ModelForm):
    
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'apellido' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'email' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'dni' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
        
    
   