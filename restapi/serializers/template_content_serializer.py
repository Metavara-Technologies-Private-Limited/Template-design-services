from rest_framework import serializers
from restapi.models.template_content import TemplateContent

class TemplateContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TemplateContent
        fields = "__all__"



        