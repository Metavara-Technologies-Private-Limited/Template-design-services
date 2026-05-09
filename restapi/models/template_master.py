from django.db import models

class TemplateMaster(models.Model):

    # -------- CHOICES -------- #

    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("BOTH", "Both"),
    ]

    USER_TYPE_CHOICES = [
        ("DOCTOR", "Doctor"),
        ("NURSE", "Nurse"),
        ("ADMIN", "Admin"),
    ]

    TEMPLATE_TYPE_CHOICES = [
        ("TEXT", "Text"),
        ("FORM", "Form"),
    ]

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    ]

    MODULE_CHOICES = [
        ("LEAD", "Lead"),
        ("PATHOLOGY", "Pathology"),
        ("RADIOLOGY", "Radiology"),
        ("EXAMINATION", "Examination"),
        ("INVESTIGATION", "Investigation"),
        ("SURGERY", "Surgery"),
        ("OUTCOME", "Outcome"),
    ]

    # -------- MAIN FIELDS -------- #

    template_code = models.CharField(max_length=50, unique=True, blank=True)

    template_name = models.CharField(max_length=255, unique=True)

    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)

    service_name = models.CharField(max_length=255)

    template_type = models.CharField(max_length=20, choices=TEMPLATE_TYPE_CHOICES)

    # Multi-module mapping (SOW requirement)
    module_mapping = models.JSONField(default=list)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ACTIVE")

    # -------- COMMON FIELDS -------- #

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # -------- AUTO TEMPLATE CODE -------- #

    def save(self, *args, **kwargs):
        if not self.template_code:
            last = TemplateMaster.objects.order_by('id').last()
            if last:
                new_id = last.id + 1
            else:
                new_id = 1
            self.template_code = f"TMP-{new_id:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.template_code} - {self.template_name}"