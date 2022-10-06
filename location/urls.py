from django.urls import path
from .views import ListLocationView, DetailLocationView, DetailRegionView, DetailLeisureView, ListPostView, \
    CreatePostView, Profile
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('posts/', ListPostView.as_view(), name='posts'),
    path('create/', CreatePostView.as_view(template_name='location/add_location.html'), name='create_location'),
    path('', ListLocationView.as_view(), name='locations'),
    path('locations/<int:pk>', DetailLocationView.as_view(), name='location'),
    path('regions/<str:slug>', DetailRegionView.as_view(), name='region'),
    path('leisure/<str:slug>', DetailLeisureView.as_view(), name='leisure'),
    path('profile/', Profile.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
