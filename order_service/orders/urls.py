from .views import OrderItemViewSet,OrderViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('orders',OrderViewSet,basename='orders')
router.register('orderitems',OrderItemViewSet,basename='orderitems')

urlpatterns = router.urls