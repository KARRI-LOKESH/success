from django.contrib import admin
from django.urls import path,include
from stdapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('disp/',views.display),
    path('student/',include('stdapp.urls'))
]