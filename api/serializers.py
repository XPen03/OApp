from  rest_framework import serializers
from .models import Picture

class PictureSerializer(serializers.ModelSerializer):
    #get_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M')
    class Meta:
        model = Picture
        fields = (
            'id',
            'timestamp',
            'name',         #name of the person in the picture
            'pill',         #number of the pill in the picture
            'matches',
            )
