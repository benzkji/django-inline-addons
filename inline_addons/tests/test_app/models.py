from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class MasterModel(models.Model):
    title = models.CharField(
        max_length=128
    )
    test1 = models.ForeignKey(
        'test_app.MasterModel',
        null = True,
        default = None,
        blank = True,
    )

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class InlineModel1(models.Model):
    master = models.ForeignKey(MasterModel)
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class InlineModel2(models.Model):
    master = models.ForeignKey(MasterModel)
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title
