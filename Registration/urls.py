from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('successful-submission/', views.SuccesfulSubmissionView.as_view(), name='successful'),
    path('participants/', views.ParticipantsView.as_view(), name='participants'),
    path('participants/edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('participants/delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
]