from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('edit/<int:pk>/', views.UpdateRetro.as_view(), name='edit'),
    path('create/', views.CreateRetro.as_view(), name='create'),
    path('delete/<int:pk>', views.DeleteRetro.as_view(), name='delete'),
    path('feedback/', views.RetroFeedback.as_view(), name='feedback'),

]