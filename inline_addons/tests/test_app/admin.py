from django.contrib import admin
from django import forms

from inline_addons.admin import PopupInline, PopupInlineAdmin
from inline_addons.tests.test_app.models import InlineModel1, InlineModel2, MasterModel


class InlineModel1Inline(admin.StackedInline):
    model = InlineModel1


class InlineModel2Inline(PopupInline):
    model = InlineModel2
    # fields = ['title']
    exclude = ['title', ]
    extra = 0

    class Media:
        js = ('inline_addons/js/inline_popup_handling.js', )


class MasterModelAdmin(admin.ModelAdmin):
    inlines = [InlineModel1Inline, InlineModel2Inline]


class InlineModel2Admin(PopupInlineAdmin):
    fk_name = 'master'


admin.site.register(InlineModel2, InlineModel2Admin)
admin.site.register(MasterModel, MasterModelAdmin)
