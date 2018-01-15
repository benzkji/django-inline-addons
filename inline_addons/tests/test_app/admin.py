from django.contrib import admin
from django import forms

from inline_addons.admin import PopupInline
from inline_addons.tests.test_app.models import InlineModel1, InlineModel2, MasterModel


class InlineModel1Inline(admin.StackedInline):
    model = InlineModel1


class InlineModel2Inline(PopupInline):
    model = InlineModel2
    fields = []
    exclude = ['title', ]

    class Media:
        js = ('inline_addons/js/inline_popup_handling.js', )


class MasterModelAdmin(admin.ModelAdmin):
    inlines = [InlineModel1Inline, InlineModel2Inline]


class InlineModel2Admin(admin.ModelAdmin):
    popup_response_template = 'inline_addons/popup_inline_response.html'
    fk_name = 'master'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # TODO: raise wrong configured when no fk_name!
        if (db_field.name == self.fk_name):
            fk_field = getattr(self.model, self.fk_name)
            print fk_field.get_queryset()

            return forms.ModelChoiceField(queryset=fk_field.get_queryset(), widget=forms.HiddenInput())
        else:
            return super(InlineModel2Admin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(InlineModel2, InlineModel2Admin)
admin.site.register(MasterModel, MasterModelAdmin)
