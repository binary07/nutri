from rest_framework import routers
from .viewsets import (
    ContactViewSet,
    AppointmentViewSet
)

router = routers.SimpleRouter()
router.register('contact', ContactViewSet)
router.register('appointment', AppointmentViewSet)

urlpatterns = router.urls
