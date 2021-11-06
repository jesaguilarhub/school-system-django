from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet)

urlpatterns = router.urls