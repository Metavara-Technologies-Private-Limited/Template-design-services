from django.db import models
from .template_section import TemplateSection


class TemplateField(models.Model):

    FIELD_TYPE_CHOICES = [
        ("TEXT", "Text"),
        ("DATE", "Date"),
        ("BOOLEAN", "Boolean"),
        ("DECIMAL", "Decimal"),
        ("TIME", "Time"),
        ("DROPDOWN", "Dropdown"),
        ("UPLOAD", "Upload File"),
        ("DIVIDER", "Divider"),
    ]

    section = models.ForeignKey(
        TemplateSection,
        on_delete=models.CASCADE,
        related_name="template_fields"
    )

    field_type = models.CharField(
        max_length=20,
        choices=FIELD_TYPE_CHOICES
    )

    sublabel = models.CharField(max_length=255, blank=True, null=True)

    is_mandatory = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    column_position = models.PositiveIntegerField(default=1)

    # Stores type-specific properties as JSON
    # TEXT     → {"line_type": "SINGLE/MULTI"}
    # BOOLEAN  → {"boolean_type": "YES_NO/TRUE_FALSE"}
    # DECIMAL  → {"default_value": "", "unit": "", "min_value": "", "max_value": ""}
    # DROPDOWN → {"selection_type": "SINGLE/MULTI", "options": ["Option 1", "Option 2"]}
    # UPLOAD   → {"allowed_formats": [], "upload_limit": "", "min_size": "", "max_size": ""}
    # DATE     → {}
    # TIME     → {}
    properties = models.JSONField(default=dict, blank=True)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.section.title} - {self.sublabel} ({self.field_type})"

    class Meta:
        db_table = "template_field"
        ordering = ["order"]