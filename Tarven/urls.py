from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view  # type: ignore
from drf_yasg import openapi  # type: ignore
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="TarVen",
        default_version='v1',
        description="Документация к вашему API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('Posts/', include('Posts.urls')),
    path('Likes/', include('Likes.urls')),
    path('Users/', include('Users.urls')),
<<<<<<< HEAD
    path('conversations/', include('Chats.urls')),
    path('Comments/', include('Comments.urls'))
=======
    path('Comments/', include('Comments.urls')),

>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
