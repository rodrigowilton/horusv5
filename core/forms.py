from django import forms
from core.models import Condominios, Unidades
from .models import Internets


class InternetsForm(forms.ModelForm):
    class Meta:
        model = Internets
        fields = '__all__'  # Ou liste os campos desejados aqui


class CondominioForm(forms.Form):
    unidade = forms.ModelChoiceField(
        label='Unidades',
        queryset=Unidades.objects.all(),
    )

    class Meta:
        model = Condominios
        fields = '__all__'


