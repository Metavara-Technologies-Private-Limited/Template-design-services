from restapi.models.template_field import TemplateField
from restapi.serializers.template_field_serializer import TemplateFieldSerializer


def create_template_field(data):
    serializer = TemplateFieldSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {
            "status": True,
            "message": "Template Field Created Successfully",
            "data": serializer.data
        }
    return {
        "status": False,
        "errors": serializer.errors
    }


def get_all_template_fields(section_id):
    fields = TemplateField.objects.filter(
        section=section_id,
        is_deleted=False
    ).order_by("order")
    serializer = TemplateFieldSerializer(fields, many=True)
    return {
        "status": True,
        "data": serializer.data
    }


def get_template_field_by_id(field_id):
    try:
        field = TemplateField.objects.get(
            id=field_id,
            is_deleted=False
        )
        serializer = TemplateFieldSerializer(field)
        return {
            "status": True,
            "data": serializer.data
        }
    except TemplateField.DoesNotExist:
        return {
            "status": False,
            "message": "Template Field Not Found"
        }


def update_template_field(field_id, data):
    try:
        field = TemplateField.objects.get(
            id=field_id,
            is_deleted=False
        )
    except TemplateField.DoesNotExist:
        return {
            "status": False,
            "message": "Template Field Not Found"
        }
    serializer = TemplateFieldSerializer(
        field,
        data=data,
        partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return {
            "status": True,
            "message": "Template Field Updated Successfully",
            "data": serializer.data
        }
    return {
        "status": False,
        "errors": serializer.errors
    }


def delete_template_field(field_id):
    try:
        field = TemplateField.objects.get(
            id=field_id,
            is_deleted=False
        )
        field.is_deleted = True
        field.save()
        return {
            "status": True,
            "message": "Template Field Deleted Successfully"
        }
    except TemplateField.DoesNotExist:
        return {
            "status": False,
            "message": "Template Field Not Found"
        }


def reorder_template_fields(fields_order):
    # fields_order = [{"id": 1, "order": 0}, {"id": 2, "order": 1}]
    try:
        for item in fields_order:
            TemplateField.objects.filter(
                id=item["id"],
                is_deleted=False
            ).update(order=item["order"])
        return {
            "status": True,
            "message": "Fields Reordered Successfully"
        }
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }