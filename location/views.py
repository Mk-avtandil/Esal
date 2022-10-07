import itertools


from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from location.forms import CreateLocationForm, CreateCommentForm
from location.models import Location, Region, Leisure, Image, Comment


class CreatePostView(CreateView):
    def get(self, request, *args, **kwargs):
        location_form = CreateLocationForm()
        user = request.user
        context = {
            'location_form': location_form,
            'user': user
        }
        return render(request, 'location/add_location.html', context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = CreateLocationForm(request.POST)
            if form.is_valid():
                location = form.save(commit=False)
                location.author = request.user
                location.save()
                for image in request.FILES.getlist('image'):
                    Image.objects.create(image=image, location=location)
            return ListLocationView.get(request, *args, **kwargs)
        return render(request, 'location/add_location.html')


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
    @staticmethod
    def get(request, *args, **kwargs):
        locations = Location.objects.all()
        new_locations = Location.objects.all().order_by('-created_at')[:3]
        regions = Region.objects.all()

        for location in new_locations:
            location.images = location.image.all()

        for location in locations:
            location.images = location.image.all()
        context = {
            'locations': locations,
            'regions': regions,
            'new_locations': new_locations
        }
        return render(request, 'location/index.html', context)


class DetailLocationView(DetailView):
    def post(self, request, pk):
        location = Location.objects.get(pk=pk)
        if request.method == 'POST':
            form = CreateCommentForm(request.POST)
            if form.is_valid():
                comment = Comment(
                    author=request.user,
                    text=form.cleaned_data["text"],
                    location=location
                )
                comment.save()
        return self.get(request, pk)

    def get(self, request, pk, *args, **kwargs):
        location = Location.objects.get(id=pk)
        form = CreateCommentForm()
        context = {
            'form': form,
            'location': location,
            'regions': Region.objects.all(),
            'region': Region.objects.get(location=location),
            'leisure': Leisure.objects.get(location=location),
            'images': Image.objects.filter(location=location),
            'comments': Comment.objects.filter(location=location)
        }

        return render(request, 'location/detail.html', context)


class DetailRegionView(DetailView):
    def get(self, request, slug, *args, **kwargs):
        region = Region.objects.get(slug=slug)
        locations = Location.objects.filter(region=region)

        for location in locations:
            location.images = location.image.all()
        context = {
            'region': region,
            'regions': Region.objects.all(),
            'location': locations
        }

        return render(request, 'location/detail_region.html', context)


class DetailLeisureView(DetailView):
    def get(self, request, slug, *args, **kwargs):
        leisure = Leisure.objects.get(slug=slug)
        locations = Location.objects.filter(leisure=leisure)

        for location in locations:
            location.images = location.image.all()

        context = {
            'leisure': leisure,
            'locations': locations,
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
