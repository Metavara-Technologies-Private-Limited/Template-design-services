from django.contrib import admin

# Register your models here.

from .models.template_master import TemplateMaster
from .models.template_content import TemplateContent
from .models.template_section import TemplateSection
from .models.template_field import TemplateField


admin.site.register(TemplateMaster)
admin.site.register(TemplateContent)
admin.site.register(TemplateSection)
admin.site.register(TemplateField)