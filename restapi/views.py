from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


from restapi.services.template_master_service import (
    create_template_master,
    get_all_template_masters,
    get_template_master_by_id,
    update_template_master,
    delete_template_master,
    get_complete_template_data
)

@api_view(["GET", "POST"])
def template_master_list_create(request):

    if request.method == "GET":

        search = request.GET.get("search")

        status = request.GET.get("status")

        page = int(request.GET.get("page", 1))

        page_size = int(request.GET.get("page_size", 2))

        data = get_all_template_masters(
        search=search,
        status=status,
        page=page,
        page_size=page_size
        )

        return Response({
            "status": True,
            "message": "Templates fetched successfully",
            "data": data})

    elif request.method == "POST":

        response = create_template_master(request.data)

        return Response({
            "status": True,
            "message": "Template created successfully",
            "data": response})



@api_view(["GET", "PUT", "DELETE"])
def template_master_detail(request, template_id):

    response = get_template_master_by_id(template_id)
    if request.method == "GET":

        response = get_template_master_by_id(template_id)

        return Response(response)

    elif request.method == "PUT":

        response = update_template_master(
            template_id,
            request.data
        )

        return Response(response)

    elif request.method == "DELETE":

        response = delete_template_master(template_id)

        return Response(response)
    

# Template_content_Services

from restapi.services.template_content_service import (
    create_template_content,
    get_all_template_contents,
    get_template_content_by_id,
    update_template_content,
    delete_template_content
)

@api_view(["GET", "POST"])
def template_content_list_create(request):

    if request.method == "GET":

        response = get_all_template_contents()

        return Response(response)

    elif request.method == "POST":

        response = create_template_content(request.data)

        return Response(response)



@api_view(["GET", "PUT", "DELETE"])
def template_content_detail(request, template_content_id):

    if request.method == "GET":

        response = get_template_content_by_id(
            template_content_id
        )

        return Response(response)

    elif request.method == "PUT":

        response = update_template_content(
            template_content_id,
            request.data
        )

        return Response(response)

    elif request.method == "DELETE":

        response = delete_template_content(
            template_content_id
        )

        return Response(response)
    

@api_view(["GET"])
def complete_template_detail(request, template_id):

    response = get_complete_template_data(
        template_id
    )

    return Response(response)

from restapi.services.template_section_service import (
    create_template_section,
    get_all_template_sections,
    get_template_section_by_id,
    update_template_section,
    delete_template_section,
    reorder_template_sections
)

from restapi.services.template_field_service import (
    create_template_field,
    get_all_template_fields,
    get_template_field_by_id,
    update_template_field,
    delete_template_field,
    reorder_template_fields
)


# ─── TEMPLATE SECTION VIEWS ───────────────────────────────────────────────────

@api_view(["GET", "POST"])
def template_section_list_create(request, template_id):
    if request.method == "GET":
        response = get_all_template_sections(template_id)
        return Response(response)
    elif request.method == "POST":
        data = request.data.copy()
        data["template"] = template_id
        response = create_template_section(data)
        return Response(response)


@api_view(["GET", "PUT", "DELETE"])
def template_section_detail(request, section_id):
    if request.method == "GET":
        response = get_template_section_by_id(section_id)
        return Response(response)
    elif request.method == "PUT":
        response = update_template_section(section_id, request.data)
        return Response(response)
    elif request.method == "DELETE":
        response = delete_template_section(section_id)
        return Response(response)


@api_view(["PUT"])
def template_section_reorder(request, template_id):
    response = reorder_template_sections(request.data.get("sections_order", []))
    return Response(response)


# ─── TEMPLATE FIELD VIEWS ─────────────────────────────────────────────────────

@api_view(["GET", "POST"])
def template_field_list_create(request, section_id):
    if request.method == "GET":
        response = get_all_template_fields(section_id)
        return Response(response)
    elif request.method == "POST":
        data = request.data.copy()
        data["section"] = section_id
        response = create_template_field(data)
        return Response(response)


@api_view(["GET", "PUT", "DELETE"])
def template_field_detail(request, field_id):
    if request.method == "GET":
        response = get_template_field_by_id(field_id)
        return Response(response)
    elif request.method == "PUT":
        response = update_template_field(field_id, request.data)
        return Response(response)
    elif request.method == "DELETE":
        response = delete_template_field(field_id)
        return Response(response)


@api_view(["PUT"])
def template_field_reorder(request, section_id):
    response = reorder_template_fields(request.data.get("fields_order", []))
    return Response(response)