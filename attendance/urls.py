 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.homePage),
    path('deleteSubject/<int:subject_id>/', views.deleteSub),
    path('updateAttendance/<int:subject_id>/<int:attended>/', views.updateAttendance),
]
