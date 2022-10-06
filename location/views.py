import itertools

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Value, Avg
from location.models import Location, Region, Leisure, Image


User = get_user_model()


class ListPostView(ListView):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        regions = Region.objects.all()

        for location in locations:
            location.images = location.image.all()

        context = {
            'posts': locations,
            'regions': regions,
            'user': request.user
        }
        return render(request, 'location/all_posts.html', context)


class ListLocationView(ListView):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        new_locations = Location.objects.all().order_by('-created_at')[:3]
        regions = Region.objects.all()

        for i in new_locations:
            i.images = i.image.all()

        for location in locations:
            location.images = location.image.all()
        context = {
            'locations': locations,
            'regions': regions,
            'new_locations': new_locations
        }
        return render(request, 'location/index.html', context)


class DetailLocationView(DetailView):
    def get(self, request, pk, *args, **kwargs):
        location = Location.objects.get(id=pk)
        context = {
            'location': location,
            'regions': Region.objects.all(),
            'region': Region.objects.get(location=location),
            'leisure': Leisure.objects.get(location=location),
            'images': Image.objects.filter(location=location)
        }

        return render(request, 'location/detail.html', context)


class DetailRegionView(DetailView):
    def get(self, request, slug, *args, **kwargs):
        region = Region.objects.get(slug=slug)
        context = {
            'region': region,
            'regions': Region.objects.all(),
            'location': Location.objects.filter(region=region)
        }

        return render(request, 'location/detail_region.html', context)


class DetailLeisureView(DetailView):
    def get(self, request, slug, *args, **kwargs):
        leisure = Leisure.objects.get(slug=slug)
        context = {
            'leisure': leisure,
            'locations': Location.objects.filter(leisure=leisure),
            'regions': Region.objects.all()
        }

        return render(request, 'location/lesure_detail.html', context)


class Profile(DetailView):
    def get(self, request, *args, **kwargs):
        profile = request.user
        regions = Region.objects.all()
        context = {
            'profile': profile,
            'regions': regions
        }
        return render(request, 'location/profile.html', context)
