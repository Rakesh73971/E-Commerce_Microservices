from django.urls import path
from .views import ProxyView

proxy = ProxyView.as_view()

urlpatterns = [
    path("users/<path:path>", proxy, {"service_url": "http://localhost:8000"}),
    path("products/<path:path>", proxy, {"service_url": "http://localhost:8001"}),
    path("orders/<path:path>", proxy, {"service_url": "http://localhost:8002"}),
]