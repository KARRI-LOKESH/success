from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from stdapp import views
from .views import student_signup,student_login
from .views import StudentList,StudentData

urlpatterns = [
    
    path('members/', views.members, name='members'),
    path('StudentList/',StudentList),
    path('StudentData/',StudentData.as_view()),
    path('signup/',student_signup, name='student_signup'),
    path('login/', student_login, name='student_login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # type: ignore
