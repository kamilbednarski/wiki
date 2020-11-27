from django.urls import path

from . import views

# Add app name to differentiate multiple apps in project
app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>/', views.entry, name='entry')
]