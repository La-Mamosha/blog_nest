from django.contrib import admin
from django.urls import path, include
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from blogs import views as BlogsViews # Carpeta Blog

urlpatterns = [
    #Admin 
    path('admin/', admin.site.urls),
    # Inicio de la aplicacion
    path('', views.home, name='home'),
    # Categorias 
    path('category/', include('blogs.urls')),
    #SLUG
    path('blog/<slug:slug>', BlogsViews.blogs, name='blogs'),
    #Busqueda
    path('blogs/search', BlogsViews.search, name='search'),
    #User
    path('register/', views.register, name='register'),
    #Login
    path('login/', views.login, name='login'),
    #Logout
    path('logout/', views.logout, name='logout'),
    ###########################################################################################################################################
    #Dashboard
    path('dashboard/', include('dashboards.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
