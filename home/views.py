from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from . models import petList
from .forms import NoteForm
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView , CreateView ,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.contrib.auth.views import LoginView ,LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
class ModelsignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = '/hell'

    # def get(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #            return redirect("note.list")
    #     return super().get(request, *args, **kwargs)


class loginInterfaceView(LoginView):
    template_name = 'home/login.html'

class logoutInterfaceView(LogoutView):
    template_name ='home/logout.html'


class ModelView(TemplateView):
    template_name = "home/landingpage.html"
    login_url='/admin'

class ModelListView(LoginRequiredMixin,ListView):
    model = petList
    template_name = "home/petlist.html"
    context_object_name= 'notes'
    login_url='/login'

    # def get_gueryset(self):
    #      return self.request.user.notes.all()


class ModelDetailView(DetailView):
    model = petList
    template_name = "home/petdetails.html"
    context_object_name ='note'

class ModelCreateView(CreateView):
    model = petList
    template_name = "home/noteForm.html"
    form_class= NoteForm
    success_url='/d/'
    login_url = "/login"
    
    # def form_valid(self, form):
    #    self.object = form.save(commit=False)
    #    self.object = self.request.user
    #    self.object.save()
    #    return HttpResponseRedirect(self.get_success_url())

class ModelUpdateView(UpdateView):
    model = petList
    form_class= NoteForm
    success_url='/d/'
    template_name = "home/noteForm.html"


class ModelDeleteView(LoginRequiredMixin, DeleteView):
    model = petList
    success_url = '/d/'
    template_name='home/notedelet.html'
