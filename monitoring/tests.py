"""Monitoring Unit Test."""
from __future__ import absolute_import

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth import get_user_model

TEST_URLS = [
    # (url, status_code, text_on_page)
    ('/monitoring/dashboard/', 200, 'Version Information'),
]


class WorkingURLsTest(TestCase):
    """Visit URLs on the site to ensure they are working."""

    def test_urls(self):
        """Visit each URL in turn"""
        self.user = get_user_model().objects.create_user('john',
                                                         'john@montypython.com',
                                                         'password')
        self.user.is_staff = True
        self.user.save()
        self.client = Client()
        self.client.login(username='john', password='password')
        for url, status_code, expected_text in TEST_URLS:
            response = self.client.get(url)
            self.assertEqual(response.status_code,
                             status_code,
                             'URL %s: Unexpected status code, got %s expected %s' %
                                (url, response.status_code, 200))
            if response.status_code == 200:
                self.assertContains(response,
                                    expected_text,
                                    msg_prefix='URL %s' % (url))

