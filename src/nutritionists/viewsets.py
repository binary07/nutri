"""."""
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .serializers import (
	SpecialtySerializer,
	NutritionistSerializer,
)
from .models import (
	Specialty,
	Nutritionist,
)


class SpecialtyViewSet(ModelViewSet):

    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class NutritionistViewSet(ModelViewSet):

    queryset = Nutritionist.objects.all()
    serializer_class = NutritionistSerializer
    search_fields = ['license', 'degree']
    filter_backends = (filters.SearchFilter,)
