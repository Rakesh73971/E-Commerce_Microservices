import requests
from django.http import JsonResponse
from django.views import View


USER_SERVICE = "http://localhost:8000"
PRODUCT_SERVICE = "http://localhost:8001"
ORDER_SERVICE = "http://localhost:8002"


class ProxyView(View):

    def dispatch(self, request, service_url, path):

        url = f"{service_url}/{path}"

        headers = {
            "Authorization": request.headers.get("Authorization", "")
        }

        response = requests.request(
            method=request.method,
            url=url,
            headers=headers,
            data=request.body
        )

        return JsonResponse(response.json(), status=response.status_code, safe=False)