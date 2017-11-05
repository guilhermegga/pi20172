from django.forms import ModelForm
from core.models import Post
from core.models import Busca



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','texto']


class BuscaForms(ModelForm):
    class Meta:
        model = Busca
        fields = ['palavra']