from rest_framework import routers
from .viewsets import (
    PatientViewSet,
    DiseaseViewSet,
    SymptomViewSet,
    MedicalRecordViewSet,
)

router = routers.SimpleRouter()
router.register('patients', PatientViewSet)
router.register('diseases', DiseaseViewSet)
router.register('symptoms', SymptomViewSet)
router.register('medicalrecords', MedicalRecordViewSet)

urlpatterns = router.urls
