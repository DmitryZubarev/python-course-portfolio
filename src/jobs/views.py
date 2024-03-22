from django.views.generic import ListView, DetailView

from jobs.models import Job


class IndexJobsListView(ListView):
    model = Job


class IndexJobDetailedView(DetailView):
    model = Job
