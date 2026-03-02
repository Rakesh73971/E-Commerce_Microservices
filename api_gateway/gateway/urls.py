from django.urls import re_path
from .views import (
    ProxyView,
    USER_SERVICE_URL,
    PRODUCT_SERVICE_URL,
    ORDER_SERVICE_URL,
)

proxy = ProxyView.as_view()

urlpatterns = [
    re_path(r"^users(?:/(?P<path>.*))?$", proxy, {"service_url": USER_SERVICE_URL}),
    re_path(r"^products(?:/(?P<path>.*))?$", proxy, {"service_url": PRODUCT_SERVICE_URL}),
    re_path(r"^orders(?:/(?P<path>.*))?$", proxy, {"service_url": ORDER_SERVICE_URL}),
]