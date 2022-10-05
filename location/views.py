from django.shortcuts import render
from django.views.generic import ListView, DetailView

from location.models import Location, Region, Leisure


class ListLocationView(ListView):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        context = {
            'locations': locations
        }
        return render(request, '#', context)


class DetailLocationView(DetailView):
    def get(self, request, pk, *args, **kwargs):
        location = Location.objects.get(id=pk)
        context = {
            'location': location
        }

        return render(request, '#', context)


class DetailRegionView(DetailView):
    def get(self, request, slug, *args, **kwargs):
        region = Region.objects.get(slug=slug)
        locations = Location.objects.filter(region=region)
        context = {
            'region': region,
            'locations': locations
        }

        return render(request, 'templates/region.html', context)


class DetailLeisureView(DetailView):
    def get(self, request, slug, *args, **kwargs):
        leisure = Leisure.objects.get(slug=slug)
        locations = Location.objects.filter(leisure=leisure)
        context = {
            'leisure': leisure,
            'location': locations
        }

        return render(request, '#', context)
