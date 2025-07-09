"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inicial/', views.inicial, name='inicial'),
    path('perfil/', views.perfil, name='perfil'),
    path('cursos/<int:area_id>/', views.cursos, name='cursos'),
    path('cadastro_curso/', views.cadastro_curso, name='cadastro_curso'),
    path('editar_curso/<int:id>', views.editar_curso, name='editar_curso'),
    path('deletar_curso/<int:id>', views.deletar_curso, name='deletar_curso'),
    path('register_usuario/', views.register_usuario, name='register_usuario'),
    path('login_usuario/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('areas/', views.areas, name='areas'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)