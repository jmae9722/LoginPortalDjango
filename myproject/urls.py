from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('__reload__/', include('django_browser_reload.urls')),  # 🔥 hot reload URL
    path('', include('myapp.urls')),  # Include your app routes
]
