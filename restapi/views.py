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

        data = get_all_template_masters()

        return Response(data)

    elif request.method == "POST":

        response = create_template_master(request.data)

        return Response(response)
    

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