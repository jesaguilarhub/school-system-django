from rest_framework.serializers import ModelSerializer
from courses.models import Course

class CourseSerializer(ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['id', 'name']

class DetailCourseSerializer(ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'
    
class CreateCourseSerializer(ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'