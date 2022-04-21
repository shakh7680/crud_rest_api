from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at', 'updated_at')

    def to_representation(self, instance):
        data = super(PostSerializer, self).to_representation(instance)
        lan_code = self.context['lan_code']
        print(lan_code)
        if lan_code:
            data['title'] = instance.translations.get(language_code=lan_code).title
        return data



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)