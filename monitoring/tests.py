"""Monitoring Unit Test."""
from __future__ import absolute_import

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.test.client import Client

from .factories import LogEntryFactory, LogFactory

TEST_URLS = [
    # (url, status_code, text_on_page)
    ('/monitoring/dashboard/', 200, 'Version Information'),
    ('/admin/admin/logentry/', 200, 'Select log entry to change'),
    ('/admin/admin/logentry/1/', 200, 'Change log entry'),
    ('/admin/admin/logentry/1/delete/', 403, '403 Forbidden'),
]


class WorkingURLsTest(TestCase):
    """Visit URLs on the site to ensure they are working."""

    def setUp(self):
        """Create data and login test client"""
        user_model = get_user_model()
        user_content_type = ContentType.objects.get_for_model(user_model)
        for i in range(3):
            log_entry = LogEntryFactory.create()
            log_entry.content_type = user_content_type
            log_entry.save()
        for i in range(6):
            LogFactory.create()

        self.user = user_model.objects.create_user('john',
                                                   'john@montypython.com',
                                                   'password')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.client = Client()
        self.client.login(username='john', password='password')

    def test_urls(self):
        """Visit each URL in turn"""
        for url, status_code, expected_text in TEST_URLS:
            response = self.client.get(url, secure=True)
            self.assertEqual(response.status_code,
                             status_code,
                             'URL %s: Unexpected status code, got %s expected %s' %
                             (url, response.status_code, status_code))
            if response.status_code == 200:
                self.assertContains(response,
                                    expected_text,
                                    msg_prefix='URL %s' % (url))

