from django.contrib import admin

# Register your models here.

from .models.template_master import TemplateMaster
from .models.template_content import TemplateContent


admin.site.register(TemplateMaster)
admin.site.register(TemplateContent)