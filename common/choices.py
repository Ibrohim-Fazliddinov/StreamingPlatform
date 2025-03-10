from django.db import models
from django.utils.translation import gettext_lazy as _

class PublishStateChoices(models.TextChoices):
    PRIVATE = "PRV", _("PRIVATE")
    PUBLISHED = "PUB", _("PUBLISHED")
    DRAFT = "DRF", _("DRAFT")
    MODERATE = "MOD", _("MODERATE")
    ARCHIVED = "ARC", _("ARCHIVED")
