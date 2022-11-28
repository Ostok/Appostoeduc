from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Email')
    mensaje = forms.CharField(label='Mensaje (max. 200 car.)',max_length=200)