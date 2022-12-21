from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

# path('login/', login , name= "login"),
urlpatterns = [
    path('',home, name="detect-news"),
    path('feedback/',news_feedback, name="feedback"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='news/index.html'), name='logout'),
    path('signup/', SignupView.as_view() , name= "signup"),
    path('follow',follow ,name='follow'),
    path('follows', follows, name="follows"),
    path('addnew', new , name="addnew")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)