from restapi.models.template_master import TemplateMaster
from restapi.serializers.template_master_serializer import TemplateMasterSerializer


def create_template_master(data):

    serializer = TemplateMasterSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return {
            "status": True,
            "message": "Template Master Created Successfully",
            "data": serializer.data
        }

    return {
        "status": False,
        "errors": serializer.errors
    }

def get_all_template_masters(
    search=None,
    status=None,
    page=1,
    page_size=2
):

    templates = TemplateMaster.objects.all()

    if search:

        templates = templates.filter(
            template_name__icontains=search
        )

    if status:

        templates = templates.filter(
            status=status
        )

    start = (page - 1) * page_size

    end = start + page_size

    templates = templates[start:end]

    serializer = TemplateMasterSerializer(
        templates,
        many=True
    )

    return serializer.data



def get_template_master_by_id(template_id):

    try:

        template = TemplateMaster.objects.get(id=template_id)

        serializer = TemplateMasterSerializer(template)

        return {
            "status": True,
            "data": serializer.data
        }

    except TemplateMaster.DoesNotExist:

        return {
            "status": False,
            "message": "Template Master Not Found"
        }
    

def update_template_master(template_id, data):

    try:

        template = TemplateMaster.objects.get(id=template_id)

        serializer = TemplateMasterSerializer(
            template,
            data=data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return {
                "status": True,
                "message": "Template Master Updated Successfully",
                "data": serializer.data
            }

        return {
            "status": False,
            "errors": serializer.errors
        }

    except TemplateMaster.DoesNotExist:

        return {
            "status": False,
            "message": "Template Master Not Found"
        }
    
def delete_template_master(template_id):

    try:

        template = TemplateMaster.objects.get(id=template_id)
        #template.is_deleted = True
        #template.save()
        template.delete()

        return {
            "status": True,
            "message": "Template Master Deleted Successfully"
        }

    except TemplateMaster.DoesNotExist:

        return {
            "status": False,
            "message": "Template Master Not Found"
        }
    

def get_complete_template_data(template_id):

    try:

        template = TemplateMaster.objects.get(
            id=template_id
        )

        serializer = TemplateMasterSerializer(
            template
        )

        return {
            "status": True,
            "data": serializer.data
        }

    except TemplateMaster.DoesNotExist:

        return {
            "status": False,
            "message": "Template Not Found"
        }