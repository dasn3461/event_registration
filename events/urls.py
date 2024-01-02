from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'events', views.EventViewSet, basename='event')
router.register(r'registrations', views.RegistrationViewSet, basename='registration')


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('create_event/', views.create_event, name='create_event'),

    #API URLS
    
    path('api/', include(router.urls)),

]