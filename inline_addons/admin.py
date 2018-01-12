from functools import partial

from django import forms
from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.forms.models import InlineForeignKeyField, modelformset_factory, BaseInlineFormSet

from inline_addons.tests.test_app.models import MasterModel


class PopupInlineForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PopupInlineForm, self).__init__(*args, **kwargs)
        print self.fields


class VisibleInlineForeignKeyField(InlineForeignKeyField):
    widget = forms.Select


class PopupInlineFormSet(BaseInlineFormSet):

    def add_fields(self, form, index):
        print "formset:"
        print form.fields
        # print form.get_fieldset()
        super(PopupInlineFormSet, self).add_fields(form, index)
        print form.fields
        # print form.get_fieldset()
        form.fields['master'] = forms.ModelChoiceField(queryset=MasterModel.objects.all())


class PopupInline(InlineModelAdmin):
    template = 'inline_addons/popup_inline.html'
    form = PopupInlineForm
    formset =  PopupInlineFormSet

    def get_fields(self, request, obj=None):
        return ['master', 'title', ]

    def zzz_get_formset(self, request, **kwargs):
        """
        Returns a FormSet class for use on the changelist page if list_editable
        is used.
        """
        defaults = {
            "formfield_callback": partial(self.formfield_for_dbfield, request=request),
        }
        defaults.update(kwargs)
        print "its here!"
        return modelformset_factory(
            self.model, self.get_changelist_form(request), extra=0,
            fields=self.list_editable,
            widgets={self.fk_name: forms.ChoiceField}
            **defaults
        )