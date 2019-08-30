from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic.edit import FormView

class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

