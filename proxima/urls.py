from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('register/', user_views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('view_profile', user_views.ProfileTemplateView.as_view(), name='view_profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

