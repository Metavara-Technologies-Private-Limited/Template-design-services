from django.urls import path
from restapi.views import (
    template_master_list_create,
    template_master_detail,
    template_content_list_create,
    template_content_detail,
    complete_template_detail,
    template_section_list_create,
    template_section_detail,
    template_section_reorder,
    template_field_list_create,
    template_field_detail,
    template_field_reorder,
)

urlpatterns = [

    # ─── TEMPLATE MASTER ──────────────────────────────────────────────────────
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

    # ─── TEMPLATE CONTENT ─────────────────────────────────────────────────────
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

    # ─── TEMPLATE FULL DATA ───────────────────────────────────────────────────
    path(
        "template-full-data/<int:template_id>/",
        complete_template_detail,
        name="template-full-data"
    ),

    # ─── TEMPLATE SECTION ─────────────────────────────────────────────────────
    path(
        "template-master/<int:template_id>/sections/",
        template_section_list_create,
        name="template-section-list-create"
    ),
    path(
        "template-section/<int:section_id>/",
        template_section_detail,
        name="template-section-detail"
    ),
    path(
        "template-master/<int:template_id>/sections/reorder/",
        template_section_reorder,
        name="template-section-reorder"
    ),

    # ─── TEMPLATE FIELD ───────────────────────────────────────────────────────
    path(
        "template-section/<int:section_id>/fields/",
        template_field_list_create,
        name="template-field-list-create"
    ),
    path(
        "template-field/<int:field_id>/",
        template_field_detail,
        name="template-field-detail"
    ),
    path(
        "template-section/<int:section_id>/fields/reorder/",
        template_field_reorder,
        name="template-field-reorder"
    ),
]