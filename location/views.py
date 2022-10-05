from django.shortcuts import render
from django.views.generic import ListView, DetailView

from location.models import Location, Region, Leisure, Image


class ListPostView(ListView):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        regions = Region.objects.all()
        context = {
            'posts': locations,
            'regions': regions,
        }
        return render(request, 'location/all_posts.html', context)


class ListLocationView(ListView):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        data = {}
        for items in locations:
            data['location'] = items
            data['image'] = Image.objects.filter(location=items)
        regions = Region.objects.all()
        context = {
            'locations': data,
            'regions': regions,

        }
        return render(request, 'location/index.html', context)


class DetailLocationView(DetailView):
    def get(self, request, pk, *args, **kwargs):
        location = Location.objects.get(id=pk)
        regions = Region.objects.all()
        region = Region.objects.get(location=location)
        leisure = Leisure.objects.get(location=location)
        images = Image.objects.filter(location=location)
        context = {
            'location': location,
            'regions': regions,
            'region': region,
            'leisure': leisure,
            'images': images
        }

        return render(request, 'location/detail.html', context)


class DetailRegionView(DetailView):
    def get(self, request, slug, *args, **kwargs):
        regions = Region.objects.all()
        region = Region.objects.get(slug=slug)
        locations = Location.objects.filter(region=region)
        context = {
            'region': region,
            'regions': regions,
            'location': locations
        }

        return render(request, 'location/detail_region.html', context)


class DetailLeisureView(DetailView):
    def get(self, request, slug, *args, **kwargs):
        leisure = Leisure.objects.get(slug=slug)
        locations = Location.objects.filter(leisure=leisure)
        regions = Region.objects.all()
        context = {
            'leisure': leisure,
            'locations': locations,
            'regions': regions
        }

        return render(request, 'location/lesure_detail.html', context)
