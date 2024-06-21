"""
URL configuration for moneydrop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from game import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/', include('game.urls')),
    path('', views.home, name='home'),
    path('spectator/', views.spectator_view, name='spectator'),
    path('signup/', views.player_signup, name='player_signup'),  # Exemple de vue pour l'inscription du joueur
    path('login/', views.player_login, name='player_login'),
    
]
