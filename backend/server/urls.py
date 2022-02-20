from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import (
    include,
    path,
    re_path,
)
from django.views.i18n import JavaScriptCatalog
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

admin.site.site_header = 'Keeper Solutions Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^admin/jsi18n/', JavaScriptCatalog.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# API URLS
urlpatterns += [
    path('api/v1/', include('server.api_router')),
]

if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
