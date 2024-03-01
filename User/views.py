from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserLoginForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import UserModel

def home(request):
    return HttpResponse('Hello This my home page')


class RegistrationView(LoginRequiredMixin, CreateView):
    template_name = 'User/register.html'
    form_class = UserRegisterForm 
    success_url = reverse_lazy('home')  # Redirect to the login page after successful registration

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Replace 'home' with the URL name of your desired redirection page
        return super().dispatch(request, *args, **kwargs)

class CustomLoginView(LoginView):
    template_name = 'User/login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserList(ListView):
    model = UserModel
    template_name = 'User/userlist.html'
    context_object_name = 'user'
    
    #https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django
    def get_queryset(self):
        current_user = self.request.user
        queryset = UserModel.objects.filter(email=current_user.email)  # Use current_user.email to match the email field
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Include the current user in the context data
        return context
    