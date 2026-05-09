from django.db import models
from .template_master import TemplateMaster

class TemplateContent(models.Model):

    template= models.OneToOneField(
        TemplateMaster,
        on_delete=models.CASCADE,
        related_name="template_content"
    )

    text_content = models.TextField(blank=True, null=True)

    form_schema = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.template.template_name