from django.db import models
from .template_master import TemplateMaster


class TemplateSection(models.Model):

    COLUMN_LAYOUT_CHOICES = [
        ("ONE", "1 Column"),
        ("TWO", "2 Column"),
        ("THREE", "3 Column"),
    ]

    template = models.ForeignKey(
        TemplateMaster,
        on_delete=models.CASCADE,
        related_name="template_sections"
    )

    title = models.CharField(max_length=255)

    column_layout = models.CharField(
        max_length=10,
        choices=COLUMN_LAYOUT_CHOICES,
        default="ONE"
    )

    show_divider = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.template.template_name} - {self.title}"

    class Meta:
        db_table = "template_section"
        ordering = ["order"]