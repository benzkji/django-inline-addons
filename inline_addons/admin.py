from django import forms
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin


class PopupInline(InlineModelAdmin):
    template = 'inline_addons/popup_inline.html'


class PopupInlineAdmin(admin.ModelAdmin):
    popup_response_template = 'inline_addons/popup_inline_response.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # TODO: raise wrong configured when no fk_name!
        if (db_field.name == self.fk_name):
            fk_field = getattr(self.model, self.fk_name)
            return forms.ModelChoiceField(queryset=fk_field.get_queryset(), widget=forms.HiddenInput())
        else:
            return super(PopupInlineAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
