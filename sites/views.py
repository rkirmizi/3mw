from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Site


class SiteListView(ListView):
    model = Site


class SiteDetailView(DetailView):
    model = Site


class SummaryView(ListView):
    model = Site
    template_name = 'sites/summary_list.html'


class SummaryAverageView(ListView):
    model = Site
    template_name = 'sites/summary_average_list.html'