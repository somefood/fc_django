"""fc_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fcuser.views import index, RegisterView, LoginView
from product.views import ProductList, ProductCreate, ProductDetail
from order.views import OrderCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()), # 클래스는 as_view() 함수 이용해야함
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()), # int 형일 때 pk라는 변수에 저장됨
    path('product/create/', ProductCreate.as_view()),
    path('order/create/', OrderCreate.as_view()),
]
