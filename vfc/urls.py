from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('main', views.main, name='main'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('complete_signup', views.complete_signup, name='complete_signup'),
    path('marriage_updater', views.marriage_updater, name='marriage_updater'),
    #path('points_updater', views.points_updater, name='points_updater'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
