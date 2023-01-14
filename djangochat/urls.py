from django.contrib import admin
from django.urls import path, include
from room.views import add_room

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('admin/', admin.site.urls),
    path('addroom/', add_room , name='add_room'),


]
