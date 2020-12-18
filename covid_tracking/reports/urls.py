from rest_framework.routers import DefaultRouter
from .views import ReportViewSet
from rest_framework import routers


router = DefaultRouter()

router.register(
    "reports_json",
    ReportViewSet,
    basename="report_json"
)

urlpatterns = router.urls

app_name = "reports"