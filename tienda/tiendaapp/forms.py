from django import forms

class CascoFormulario(forms.Form):

    marca = forms.CharField()
    tipo = forms.CharField()
    talle = forms.CharField()
    precio = forms.FloatField()

class CamperaFormulario(forms.Form):


    marca = forms.CharField()
    tipo = forms.CharField()
    talle = forms.CharField()
    precio = forms.FloatField ()


class GuanteFormulario(forms.Form):

    marca = forms.CharField()
    tipo = forms.CharField()
    talle = forms.CharField()
    precio = forms.FloatField()