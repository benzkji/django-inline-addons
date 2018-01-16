# -*- coding: utf-8 -*-
# from django.test import override_settings
from django.test.testcases import TestCase

from inline_addons.tests.test_app.models import MasterModel

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from inline_addons.tests.utils.django_utils import create_superuser


class AdminTestCase(TestCase):
    """
    check some basic admin views
    TODO: check with custom User Model!
    """
    def setUp(self):
        self.superuser = create_superuser()
        self.client.login(username='admin', password='secret')

    def tearDown(self):
        pass

    def test_inline_model_detail_view(self):
        obj = MasterModel(title='test')
        obj.save()
        url = reverse('admin:test_app_mastermodel_change', args=(obj.id, ))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    # TODO: popup change view
