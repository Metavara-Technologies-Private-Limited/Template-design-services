from rest_framework import serializers
from restapi.models.template_field import TemplateField


class TemplateFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = TemplateField
        fields = "__all__"