from django.conf.urls import url, include
from django.contrib import admin
from alunos import views
from django.contrib.auth import views as auth_views


admin.autodiscover()  # DON'T TOUCH THIS LINE

urlpatterns = [
    # django.auth views
    url(r'^login/$', auth_views.login, {
        'template_name': 'alunos/login.html',
    }, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),

    # Social OAuth logins
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    url(r'home', views.home, name='home'),
    url(r'isencao', views.isencao, name='isencao'),
    url(r'redacao', views.redacao, name='redacao'),
    url(r'emprestimos', views.emprestimos, name='emprestimos'),
    url(r'biblioteca', views.biblioteca, name='biblioteca'),
    url(r'^alunos/login/$', views.redirect_to_home, name='redirect_to_home'),
    url(r'$^', views.home, name='home'),

]

