from django.urls import path
from . import views

urlpattern = [
    path('', views.IndexView.as_view()),
    path('/register/', views.RegisterView.as_view()),
    path('/successful-submission/', views.SuccessfulSubmissionView.as_view()),
    path('/participants', views.ParticipantView.as_view()),
    path('/participants/edit/', views.EditView.as_view()),
    path('/participants/delete/', views.DeleteView.as_view())
]