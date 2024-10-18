from django.urls import path
from . import views

urlpatterns = [
    path('',views.Register,name='register'),
    path('login/', views.login, name='login'),
    path('home',views.Homepage,name='Homepage'),
    path('profile/', views.profile_details, name='profile_details'),
    path('login/',views.login,name='logout'),
    path('details/', views.datas, name='datas'),
    path('delete/<int:profile_id>/',views.deleteview, name='delete'),
    path('details/', views.deleteview, name='cancel'),
    path('overview/<int:profile_id>/',views.overview, name='okay'),
    path('update/<int:profile_id>/',views.updateview,name='update'),
    path('search/',views.search,name='search'),
    path('view/',views.totalview,name='totalview')
]