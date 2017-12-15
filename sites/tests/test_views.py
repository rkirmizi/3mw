from django.test import TestCase
from sites.models import Site
from django.urls import reverse
from .test_models import SITE_NAME, A1, B1, A2, B2, A_SUM, A_AVG

SITE_2_NAME = 'Y Site'


class SiteViewTestCase(TestCase):
    def setUp(self):
        # Site object without site detail
        Site.objects.create(name=SITE_NAME)
        # Site object with site details
        self.site = Site.objects.create(name=SITE_2_NAME)
        self.site.sitedetail_set.create(a=A1, b=B1)
        self.site.sitedetail_set.create(a=A2, b=B2)

    def test_redirect(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_sites(self):
        response = self.client.get(reverse('sites-list'))
        self.assertEqual(response.status_code, 200)

    def test_empty_average(self):
        response = self.client.get(reverse('sites-list'))
        pk = response.context_data['site_list'].get(name=SITE_NAME).pk
        response = self.client.get(reverse('sites-detail', kwargs={'pk': pk}))
        avg = response.context_data['object'].a_avg
        self.assertEqual(avg, '')

    def test_empty_sum(self):
        response = self.client.get(reverse('sites-list'))
        pk = response.context_data['site_list'].get(name=SITE_NAME).pk
        response = self.client.get(reverse('sites-detail', kwargs={'pk': pk}))
        a_sum = response.context_data['object'].a_sum
        self.assertIsNone(a_sum)

    def test_average(self):
        response = self.client.get(reverse('sites-detail', kwargs={'pk': self.site.pk}))
        avg = response.context_data['object'].a_avg
        self.assertEqual(avg, A_AVG)

    def test_sum(self):
        response = self.client.get(reverse('sites-detail', kwargs={'pk': self.site.pk}))
        a_sum = response.context_data['object'].a_sum
        self.assertEqual(a_sum, A_SUM)