# djanog-inline-addons

[![Build Status](https://travis-ci.org/bnzk/django-inline-addons.svg "Build Status")](https://travis-ci.org/bnzk/django-inline-addons/)
[![PyPi Version](https://img.shields.io/pypi/v/django-inline-addons.svg "PyPi Version")](https://pypi.python.org/pypi/django-inline-addons/)
[![Licence](https://img.shields.io/pypi/l/django-inline-addons.svg "Licence")](https://pypi.python.org/pypi/django-inline-addons/)

### Implemented
- popup inlines

### Needed

- make django inlines more consistent with it's delete behaviour

### Bonus

- inlines for non admin change views

## Usage

In your settings, add to `INSTALLED_APPS`

    INSTALLED_APPS = [
        ...
        'inline_addons',
        ...
    ]

### Popup Inlines

Instead of stacked or tabular inlines, you'll use a PopupInline. You'll further need to register your inline
model with the normal admin.site, otherwise the opened popup cannt show you a add-/changeform. For now, this means that
the model will show up in django admin dashboard and in my_app's app overview. Hope to find a way to hide it.

    from django.contrib import admin
    from inline_addons.admin import PopupInline, PopupInlineAdmin

    from my_app.models import ParentModel, InlineModel


    class InlineModelInline(PopupInline):
        model = InlineModel2
        # popup only: for now, no fields can be edited in the "inline" itself, make sure they are
        # all excluded! one day, this might be automated...
        exclude = ['title', ]
        # if you dont, PopupInline will enforce extra=0
        # other values are not tested / supported
        extra = 0


    class ParentModelAdmin(admin.ModelAdmin):
        inlines = [InlineModelInline, ]


    class InlineModelAdmin(PopupInlineAdmin):
        # this is needed, will not work otherwise
        fk_name = 'parent'


    admin.site.register(InlineModel, InlineModelAdmin)
    admin.site.register(ParentModel, ParentModelAdmin)
