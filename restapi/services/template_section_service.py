from restapi.models.template_section import TemplateSection
from restapi.serializers.template_section_serializer import TemplateSectionSerializer


def create_template_section(data):
    serializer = TemplateSectionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {
            "status": True,
            "message": "Template Section Created Successfully",
            "data": serializer.data
        }
    return {
        "status": False,
        "errors": serializer.errors
    }


def get_all_template_sections(template_id):
    sections = TemplateSection.objects.filter(
        template=template_id,
        is_deleted=False
    ).order_by("order")
    serializer = TemplateSectionSerializer(sections, many=True)
    return {
        "status": True,
        "data": serializer.data
    }


def get_template_section_by_id(section_id):
    try:
        section = TemplateSection.objects.get(
            id=section_id,
            is_deleted=False
        )
        serializer = TemplateSectionSerializer(section)
        return {
            "status": True,
            "data": serializer.data
        }
    except TemplateSection.DoesNotExist:
        return {
            "status": False,
            "message": "Template Section Not Found"
        }


def update_template_section(section_id, data):
    try:
        section = TemplateSection.objects.get(
            id=section_id,
            is_deleted=False
        )
    except TemplateSection.DoesNotExist:
        return {
            "status": False,
            "message": "Template Section Not Found"
        }
    serializer = TemplateSectionSerializer(
        section,
        data=data,
        partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return {
            "status": True,
            "message": "Template Section Updated Successfully",
            "data": serializer.data
        }
    return {
        "status": False,
        "errors": serializer.errors
    }


def delete_template_section(section_id):
    try:
        section = TemplateSection.objects.get(
            id=section_id,
            is_deleted=False
        )
        section.is_deleted = True
        section.save()
        return {
            "status": True,
            "message": "Template Section Deleted Successfully"
        }
    except TemplateSection.DoesNotExist:
        return {
            "status": False,
            "message": "Template Section Not Found"
        }


def reorder_template_sections(sections_order):
    # sections_order = [{"id": 1, "order": 0}, {"id": 2, "order": 1}]
    try:
        for item in sections_order:
            TemplateSection.objects.filter(
                id=item["id"],
                is_deleted=False
            ).update(order=item["order"])
        return {
            "status": True,
            "message": "Sections Reordered Successfully"
        }
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }