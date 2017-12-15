from django.db import models
from django.db.models import Sum, Avg
from django.urls import reverse

class Site(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sites-detail', args=[str(self.pk)])


    # This one is made with Python, instead of Django Model Aggregations.
    # As you requested in the project requirements.
    @property
    def a_avg(self):
        avg = self.sitedetail_set.values_list('a', flat=True)
        if avg.exists():
            return sum(avg) / avg.count()
        return ''

    # @property
    # def a_avg(self):
    #     return self.sitedetail_set.aggregate(a_avg=Avg('a'))['a_avg']

    @property
    def b_avg(self):
        return self.sitedetail_set.aggregate(b_avg=Avg('b'))['b_avg']

    @property
    def a_sum(self):
        return self.sitedetail_set.aggregate(a_sum=Sum('a'))['a_sum']

    @property
    def b_sum(self):
        return self.sitedetail_set.aggregate(b_sum=Sum('b'))['b_sum']


class SiteDetail(models.Model):
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    a = models.DecimalField(max_digits=4, decimal_places=2)
    b = models.DecimalField(max_digits=4, decimal_places=2)
