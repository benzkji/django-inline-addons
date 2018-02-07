from django import forms
from django.contrib import admin
from django.forms import widgets
from django.contrib.admin.options import InlineModelAdmin


class PopupInline(InlineModelAdmin):
    template = 'inline_addons/popup_inline.html'
    extra = 0

    @property
    def media(self):
        js = (
            'inline_addons/js/inline_popup_handling.js',
        )
        css = {
            'all': (
                'inline_addons/css/popup_inline.css',
            )
        }
        original_media = super(PopupInline, self).media
        return original_media + widgets.Media(js=js, css=css)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(PopupInline, self).get_formset(request, obj, **kwargs)
        formset.parent_obj = obj
        return formset


class PopupInlineAdmin(admin.ModelAdmin):
    popup_response_template = 'inline_addons/popup_inline_response.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # TODO: raise wrong configured when no fk_name!
        if (db_field.name == self.fk_name):
            fk_field = getattr(self.model, self.fk_name)
            return forms.ModelChoiceField(queryset=fk_field.get_queryset(), widget=forms.HiddenInput())
        else:
            return super(PopupInlineAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
