from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser
from utils.models import TimestampMixin


class WebBookmark(TimestampMixin, models.Model):
    title = models.CharField(_('Title'), max_length=255)
    url = models.URLField(_('URL'), max_length=255)
    public = models.BooleanField(_('Public'), default=True)
    user = models.ForeignKey(
        CustomUser, verbose_name=_('User'), on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Web Bookmark')
        verbose_name_plural = _('Web Bookmarks')
