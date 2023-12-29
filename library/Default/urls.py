from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('signin/',views.signin,name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name='signout'),
    path('book/<int:id>', views.ebooks, name='book'),
    path('request/<int:id>', views.request, name='request'),
    path('profile/',views.profile,name="profile"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('about/', views.about, name="about"),
    path('contact',views.contact,name="contact")
]