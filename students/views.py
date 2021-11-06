from rest_framework.viewsets import ModelViewSet
from students.models import Student
from students.serializers import StudentSerializer, CreateStudentSerializer, DetailStudentSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = DetailStudentSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return StudentSerializer
        
        if self.action == 'retrieve' and self.request.user.is_staff:
            return DetailStudentSerializer
        
        if self.action == 'update':
            return CreateStudentSerializer
