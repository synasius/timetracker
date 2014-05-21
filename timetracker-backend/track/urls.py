from rest_framework import routers
from .views import ActivityViewSet, TimeEntryViewSet

router = routers.DefaultRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'track', TimeEntryViewSet)

urlpatterns = router.urls
