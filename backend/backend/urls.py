
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('api/', include('api.urls')),

    path("api/auth/", include("djoser.urls")),  # Handles user registration, etc.
    path("api/auth/", include("djoser.urls.jwt")),  # JWT login/logout


    path("htmx/", include('htmx.urls')),
    path('fetch/', include('fetch.urls')),
    path('', include('chat.urls')),
    path('', TemplateView.as_view(template_name="root.html")),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)