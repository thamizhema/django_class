from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="h"),
    path('login/', views.login, name='l'),
    path('signup/', views.signup, name='s'),
    path('deleteuser/<str:docId>', views.deleteUser, name='deleteUser')
]
