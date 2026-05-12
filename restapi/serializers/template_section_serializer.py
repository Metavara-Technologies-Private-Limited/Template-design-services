from rest_framework import serializers
from restapi.models.template_section import TemplateSection
from restapi.serializers.template_field_serializer import TemplateFieldSerializer


class TemplateSectionSerializer(serializers.ModelSerializer):

    template_fields = TemplateFieldSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = TemplateSection
        fields = "__all__"