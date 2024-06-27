from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InlineAddonsConfig(AppConfig):
    name = 'inline_addons'
    verbose_name = _("Inline Addons")
