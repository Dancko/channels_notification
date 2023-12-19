
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from notifications import consumers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("notifications.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




websocket_urlpatterns = [
    path("ws/notifications/", consumers.NotificationConsumer.as_asgi()),
]
