from django.forms import ModelForm
from result_pi.models import Busca

class FormPesquisa(ModelForm):
    class Meta:
        model = Busca
        fields=['palavra','datainicio','datafim']