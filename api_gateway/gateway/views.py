import os
import requests
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://localhost:8000/users")
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://localhost:8001/products")
ORDER_SERVICE_URL = os.getenv("ORDER_SERVICE_URL", "http://localhost:8002/orders")


def _join_url(base_url: str, path: str | None) -> str:
    base = base_url.rstrip("/")
    if not path:
        return base
    return f"{base}/{path.lstrip('/')}"


@method_decorator(csrf_exempt, name="dispatch")
class ProxyView(View):

    def dispatch(self, request, service_url, path=None):

        url = _join_url(service_url, path)

        headers = {
            "Authorization": request.headers.get("Authorization", ""),
            "Content-Type": request.headers.get("Content-Type", "application/json"),
        }

        try:
            response = requests.request(
                method=request.method,
                url=url,
                headers=headers,
                params=request.GET,
                data=request.body,
                timeout=15,
            )
        except requests.RequestException as exc:
            return JsonResponse(
                {"detail": "Upstream service unreachable", "error": str(exc)},
                status=502,
            )

        try:
            data = response.json()
        except ValueError:
            data = {"detail": response.text}

        return JsonResponse(data, status=response.status_code, safe=False)