from rest_framework import serializers

from .models import WebBookmark


class WebBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebBookmark
        fields = '__all__'
        read_only_fields = ('id',)

    def validate(self, attrs):
        request = self.context.get('request')
        if request and request.user != attrs['user']:
            raise serializers.ValidationError(
                {'user': 'You cannot create a web bookmark for another user.'}
            )
        return attrs
