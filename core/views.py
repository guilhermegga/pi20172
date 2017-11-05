import json
from django.shortcuts import render,redirect
from core.models import Post
from core.forms import PostForm
from core.forms import BuscaForms

from core.service import sentimentos
# Create your views here.
def home(request):
    return redirect(todos_posts)

def todos_posts(request):
    posts = Post.objects.all().order_by('-id')
    return render(request,'core/lista_post.html',{"posts": posts})

def novo(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(todos_posts)

    return render(request,'core/novo.html',{'form':form})

def atualiza(request,id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None,instance=post)

    if form.is_valid():
        form.save()
        return redirect(todos_posts)

    return render(request,'core/novo.html',{'form':form})

def deletar(request,id):

    post = Post.objects.get(id=id)
    post.delete()

    return redirect(todos_posts)

def teste_grafico(request):
    form = BuscaForms(request.POST or None)
    context ={}

    if request.method == 'POST':
        if form.is_valid():
            analisados = sentimentos(form['palavra'].value())
            names = analisados['datas']
            prices = analisados['polaridade']
            context = {
                'names':json.dumps(names),
                'prices':json.dumps(prices),
            }
            return render(request, 'core/grafico.html', context)

    return render(request, 'core/grafico.html', {"form":form})