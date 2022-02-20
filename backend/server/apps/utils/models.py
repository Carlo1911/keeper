from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampMixin(models.Model):
    """
    Abstract base class for created and updated timestamps.
    """

    created_at = models.DateTimeField(
        _('Created'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _('Updated'),
        auto_now=True,
    )

    class Meta:
        abstract = True
