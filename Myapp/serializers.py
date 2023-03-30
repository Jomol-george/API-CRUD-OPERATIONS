from rest_framework.serializers import ModelSerializer
from Myapp.models import Mmodel
class Empserializer(ModelSerializer):
    class Meta:
        model=Mmodel
        fields='__all__'
    