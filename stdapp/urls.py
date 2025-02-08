
from django.urls import path
from stdapp import views
from .views import student_signup
from .views import StudentList,StudentData

urlpatterns = [
    
    path('members/', views.members, name='members'),
    path('StudentList/',StudentList),
    path('StudentData/',StudentData.as_view()),
    path('signup/',student_signup, name='student_signup'),
]