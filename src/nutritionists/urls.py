from rest_framework import routers
from .viewsets import (
	SpecialtyViewSet,
	NutritionistViewSet,
)

router = routers.SimpleRouter()
router.register('specialties', SpecialtyViewSet)
router.register('nutritionists', NutritionistViewSet)

urlpatterns = router.urls