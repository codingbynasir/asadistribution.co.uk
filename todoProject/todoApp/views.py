from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, Http404
from .forms import CreateForm, SignUpForm
from django.views import View
from .models import Todo
# Create your views here.
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('todo:index')
        return render(request, 'login.html')
    def post(self, request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        auth=authenticate(request, username=username, password=password)
        if auth is not None:
            login(request,auth)
            return redirect('todo:index')
        else:
            return redirect('todo:login')



class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('todo:index')
        return render(request, 'register.html',{"form":SignUpForm})
    def post(self, request):
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registrations is completed")
            return redirect('todo:register')
        else:
            messages.error(request, "Sorry, Registration is not done yet")
            return redirect('todo:register')


class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            list=Todo.objects.filter(author__username=request.user.username)
            s=request.GET.get("s")
            if s:
                list=list.filter(is_completed=False)
            return render(request, 'index.html',{"list":list})
        else:
            return redirect('todo:login')

class Create(View):
    def get(self, request):
        if request.user.is_authenticated:
            form=CreateForm
            return render(request, 'add.html', {"form":form})
        else:
            return redirect('todo:login')
    def post(self, request):
        user=get_object_or_404(User,username=request.user.username)
        form=CreateForm(request.POST)
        if form.is_valid():
            sts=form.save(commit=False)
            sts.author=user
            sts.save()
            messages.success(request, 'Todo is added')
            return redirect('todo:add')
        else:
            messages.error(request, 'Todo is not added')
            return redirect('todo:add')

class Update(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            try:
                todo=get_object_or_404(Todo,pk=pk,author__username=request.user.username)
                form=CreateForm(instance=todo)
                return render(request, 'add.html', {"form":form})
            except:
                raise Http404("Request can not handled now")
        else:
            return redirect('todo:login')

    def post(self, request, pk):
        td=get_object_or_404(Todo, id=pk)
        usr=get_object_or_404(User, username=request.user.username)
        form=CreateForm(request.POST, instance=td)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author = usr
            instance.save()
            messages.success(request, 'Todo is updated')
            return redirect('todo:update', pk)
        else:
            messages.error(request, 'Todo is not updated')
            return redirect('todo:update', pk)

def delete(request, pk):
    if request.user.is_authenticated:
        try:
            td = get_object_or_404(Todo, pk=pk, author__username=request.user.username)
            td.delete()
            messages.success(request, "To do is deleted")
            return redirect('todo:index')
        except:
            raise Http404("Request can not handled now")
    else:
        return redirect('todo:login')

def completed(request, pk):
    if request.user.is_authenticated:
        try:
            td = get_object_or_404(Todo, pk=pk, author__username=request.user.username)
            if td.is_completed:
                td.is_completed=False
                td.save()
                messages.success(request, "Marked as not completed")
            else:
                td.is_completed=True
                td.save()
                messages.success(request, "Marked as completed")
            return redirect('todo:index')
        except:
            raise Http404("Request can not handled now")
    else:
        return redirect('todo:login')

def Logout(request):
    logout(request)
    return redirect('todo:login')