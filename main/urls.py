from main import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('games/', views.games, name='games'),
    path('contact/', views.contact, name='contact'),
    path('single/', views.single, name='single'),
    path('single1/', views.single1, name='single1'),
    path('single2/', views.single2, name='single2'),
    path('features/', views.features, name='features'),
    path('action/', views.action, name='action'),
    path('others/', views.others, name='others'),
    path('racing/', views.racing, name='racing'),
    path('rpg/', views.rpg, name='rpg'),
    path('rts/', views.rts, name='rts'),
    path('shooting/', views.shooting, name='shooting'),
    path('sports/', views.sports, name='sports'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
 
]