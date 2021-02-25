from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('result/<int:id>/', views.result, name='result'),
    path('<github_username>/<repo_name>/', views.repo_url_view, name='repo_url'),
]
