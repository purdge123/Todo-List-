from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Ensure this includes 'users.urls'
    path('api/', include('tasks.urls')),  # Ensure this includes 'tasks.urls'
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Only one namespace
]

# Optional: Add a root path that points to a default view or landing page
from django.views.generic import TemplateView

urlpatterns += [
    path('', TemplateView.as_view(template_name='index.html')),  # Ensure you have an 'index.html' in your templates directory
]
