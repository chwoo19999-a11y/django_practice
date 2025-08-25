# polls/urls.py (새 파일 생성!)
from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
]
# polls/views.py