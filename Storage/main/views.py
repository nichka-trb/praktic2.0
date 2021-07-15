from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Document
from .forms import DocumentForm, RegisterUserForm, LoginUserForm


def home(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'main/home.html', {'documents': documents})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=True)
            doc.user = request.user
            doc.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'main/model_form_upload.html', {
        'form': form
    })


class UserLoginView(LoginView):
    template_name = 'main/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')
