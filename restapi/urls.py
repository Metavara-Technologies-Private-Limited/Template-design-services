from django.urls import path
from django.urls import path

from restapi.views import (template_master_list_create,
                            template_master_detail,
                            template_content_list_create,
                            template_content_detail,
                            complete_template_detail
                            )


urlpatterns = [

    path(
        "template-master/",
        template_master_list_create,
        name="template-master-list-create"
    ),

    path(
       "template-master/<int:template_id>/",
       template_master_detail,
       name="template-master-detail"
    ),

    path(
    "template-content/",
    template_content_list_create,
    name="template-content-list-create"
    ),

    path(
    "template-content/<int:template_content_id>/",
    template_content_detail,
    name="template-content-detail"
    ),

    path(
    "template-full-data/<int:template_id>/",
    complete_template_detail,
    name="template-full-data"
    ),
]