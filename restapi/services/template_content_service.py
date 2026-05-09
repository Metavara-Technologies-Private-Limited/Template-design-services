from restapi.models.template_content import TemplateContent

from restapi.serializers.template_content_serializer import (
    TemplateContentSerializer
)


def create_template_content(data):

    serializer = TemplateContentSerializer(data=data)

    if serializer.is_valid():

        serializer.save()

        return {
            "status": True,
            "message": "Template Content Created Successfully",
            "data": serializer.data
        }

    return {
        "status": False,
        "errors": serializer.errors
    }


def get_all_template_contents():

    template_contents = TemplateContent.objects.all()

    serializer = TemplateContentSerializer(
        template_contents,
        many=True
    )

    return serializer.data


def get_template_content_by_id(template_content_id):

    try:

        template_content = TemplateContent.objects.get(
            id=template_content_id
        )

        serializer = TemplateContentSerializer(
            template_content
        )

        return {
            "status": True,
            "data": serializer.data
        }

    except TemplateContent.DoesNotExist:

        return {
            "status": False,
            "message": "Template Content Not Found"
        }


def update_template_content(template_content_id, data):

    try:

        template_content = TemplateContent.objects.get(
            id=template_content_id
        )

    except TemplateContent.DoesNotExist:

        return {
            "status": False,
            "message": "Template Content Not Found"
        }

    serializer = TemplateContentSerializer(
        template_content,
        data=data
    )

    if serializer.is_valid():

        serializer.save()

        return {
            "status": True,
            "message": "Template Content Updated Successfully",
            "data": serializer.data
        }

    return {
        "status": False,
        "errors": serializer.errors
    }


def delete_template_content(template_content_id):

    try:

        template_content = TemplateContent.objects.get(
            id=template_content_id
        )

        template_content.delete()

        return {
            "status": True,
            "message": "Template Content Deleted Successfully"
        }

    except TemplateContent.DoesNotExist:

        return {
            "status": False,
            "message": "Template Content Not Found"
        }