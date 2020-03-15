from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo.views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TodoViewSet, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
