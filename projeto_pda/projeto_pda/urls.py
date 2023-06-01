"""
URL configuration for projeto_pda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# import para funcionar os arquivos estaticos
from django.conf import settings
from django.conf.urls.static import static
from projeto_pda.views import index, livros, sites

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('livros/', livros),
    path('sites/', sites),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
