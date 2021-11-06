from rest_framework.viewsets import ModelViewSet
from courses.models import Course
from courses.serializers import CourseSerializer, CreateCourseSerializer, DetailCourseSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = DetailCourseSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseSerializer
        
        if self.action == 'retrieve' and self.request.user.is_staff:
            return DetailCourseSerializer
        
        if self.action == 'update':
            return CreateCourseSerializer