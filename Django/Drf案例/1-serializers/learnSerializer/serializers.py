from rest_framework import serializers

from learnSerializer.models import Blog, Goods


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    b_title = serializers.CharField()
    b_content = serializers.CharField()

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.b_title = validated_data.get('b_title',instance.b_title)
        instance.b_content = validated_data.get('b_content',instance.b_content)
        instance.save()

        return instance


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id','g_name','g_price']

