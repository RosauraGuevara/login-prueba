from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

class UserCreateAndLoginView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("task:index")

    def form_valid(self, form):
        response = super().form_valid(form)
       # username = form.cleaned_data.get("username")
       # age = form.cleaned_data.get("age")
        email = form.cleaned_data.get("email")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(
            email=email,
            # username=username,
            password=raw_pw, 
            #age=age,
        )
        login(self.request, user)
        return response