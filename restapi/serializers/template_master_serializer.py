from rest_framework import serializers

from restapi.models.template_master import TemplateMaster

from restapi.serializers.template_content_serializer import (
    TemplateContentSerializer
)


class TemplateMasterSerializer(serializers.ModelSerializer):

    template_content = TemplateContentSerializer(
        read_only=True
    )

    class Meta:

        model = TemplateMaster

        fields = "__all__"