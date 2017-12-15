from django.test import TestCase
from sites.models import Site

SITE_NAME = 'X Site'
A1, B1 = 10, 20
A2, B2 = 20, 40
A_AVG = (A1 + A2) / 2
A_SUM = A1 + A2
B_AVG = (B1 + B2) / 2
B_SUM = B1 + B2


class SiteTestCase(TestCase):
    def setUp(self):
        Site.objects.create(name=SITE_NAME)

    def test_site_objects_count(self):
        self.assertEqual(Site.objects.count(), 1)

    def test_get_site(self):
        site = Site.objects.get(name=SITE_NAME)
        self.assertEqual(site.name, SITE_NAME)


class SiteDetailTestCase(TestCase):
    def setUp(self):
        self.site = Site.objects.create(name=SITE_NAME)
        self.site.sitedetail_set.create(a=A1, b=B1)
        self.site.sitedetail_set.create(a=A2, b=B2)

    def test_get_first_site_detail(self):
        first_detail = self.site.sitedetail_set.first()
        self.assertEqual(first_detail.a, A1)

    def test_average_a(self):
        self.assertEqual(self.site.a_avg, A_AVG)

    def test_sum_a(self):
        self.assertEqual(self.site.a_sum, A_SUM)

    def test_average_b(self):
        self.assertEqual(self.site.b_avg,B_AVG)

    def test_sum_b(self):
        self.assertEqual(self.site.b_sum, B_SUM)