from functools import partial

from django import forms
from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.contrib.auth.admin import UserAdmin
from django.forms.models import InlineForeignKeyField, modelformset_factory, BaseInlineFormSet
from django.template.defaultfilters import capfirst
from django.urls import reverse

from inline_addons.tests.test_app.models import MasterModel, InlineModel2


class PopupInline(InlineModelAdmin):
    template = 'inline_addons/popup_inline.html'
