from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Posts/', include('Posts.urls')),
    path('Users/', include('Users.urls'))
]
