from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', TemplateView.as_view(template_name="main/index.html"), name='index'),
    path('uploads/', views.model_form_upload, name='model_form_upload'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('register', views.RegisterUserView.as_view(), name='register'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
