from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm

def index(request):
    return render(request, 'index.html', {'email':request.session.get('user')})

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/' # 성공 시 이동

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/' # 성공 시 이동

    def form_valid(self, form): # 유효성 검사 끝났을 때,
        self.request.session['user'] = form.email

        return super().form_valid(form)