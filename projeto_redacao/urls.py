from django.conf.urls import include, url
from django.contrib import admin
from controle_de_frequencia import views


admin.autodiscover()  # DON'T TOUCH THIS LINE


urlpatterns = [
    # Examples:
    # url(r'^$', 'transparency.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'alunos/', views.alunos, name='alunos'),
    url(r'voluntarios/', views.voluntarios, name='voluntarios'),
    url(r'post/', views.post, name='post'),
    url(r'$^', views.home, name='home'),
]
