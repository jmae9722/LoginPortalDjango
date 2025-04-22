from django.contrib import admin
from django.urls import path, include  # ✅ include is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # ✅ This connects to your app
]
