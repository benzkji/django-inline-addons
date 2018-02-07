# -*- coding: utf-8 -*-
# from django.test import override_settings
from django.test.testcases import TestCase
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

    # TODO: test different actions with selenium (edit existing inline, add new, remove)
    # TODO: test for no extra empty inline object add!
