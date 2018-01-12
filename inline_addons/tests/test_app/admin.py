from django.contrib import admin

from inline_addons.admin import PopupInline
from inline_addons.tests.test_app.models import InlineModel1, InlineModel2, MasterModel


class InlineModel1Inline(admin.StackedInline):
    model = InlineModel1


class InlineModel2Inline(PopupInline):
    model = InlineModel2


class MasterModelAdmin(admin.ModelAdmin):
    inlines = [InlineModel1Inline, InlineModel2Inline]


admin.site.register(MasterModel, MasterModelAdmin)