from django.urls import path, include
from . views import authView, home
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ("", home, name = "home"),  # Página inicial protegida por login
    path ('signup/', authView, name = "authView" ),  # Inclui as URLs do aplicativo baseLogin
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticação do Django
    path('logout/', LogoutView.as_view(), name='logout'),  # Rota de logout
]