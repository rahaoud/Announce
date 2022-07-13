"""deals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path

from deals import settings
from announce.views import (AnnounceListView, AnnounceOtherCreateView, AnnounceUpdate,
                            AnnounceDeleteView, search_announce, search,
                            HomeTemplateView, AnnounceCarCreateView, AnnounceFurnitureApplianceCreateView,
                            AnnouncePhoneTabletCreateView, AnnounceElectronicCreateView, AnnounceAnimalCreateView,
                            AnnounceBeautyWellnessCreateView, AnnounceFashionClothesCreateView,
                            AnnounceServiceDeliveryCreateView, AnnounceEventCreateView, AnnounceFormationCreateView,
                            AnnounceEmployCreateView, AnnounceImmovableCreateView)

urlpatterns = [
    path('dg', HomeTemplateView.as_view(), name='index'),

    path('d', AnnounceListView.as_view(), name='home-page'),
    # path('detail<str:id>/', AnnounceDetailView.as_view(), name='post-detail'),

    # ********************************** Create url ****************************************************************

    path('', AnnounceOtherCreateView.as_view(), name='other-create'),
    path('immovable', AnnounceImmovableCreateView.as_view(), name='immovable-create'),
    path('Car', AnnounceCarCreateView.as_view(), name='car-create'),
    path('furniture appliance', AnnounceFurnitureApplianceCreateView.as_view(), name='furniture-appliance-create'),
    path('Phone & Tablet', AnnouncePhoneTabletCreateView.as_view(), name='phon-tablet-create'),
    path('electronic', AnnounceElectronicCreateView.as_view(), name='electronic-create'),
    path('animal', AnnounceAnimalCreateView.as_view(), name='animal-create'),
    path('beauty & wellness', AnnounceBeautyWellnessCreateView.as_view(), name='beauty-wellness-create'),
    path('fashion & clothes', AnnounceFashionClothesCreateView.as_view(), name='fashion-clothes-create'),
    path('service delivery', AnnounceServiceDeliveryCreateView.as_view(), name='service-delivery-create'),
    path('event', AnnounceEventCreateView.as_view(), name='event-create'),
    path('formation', AnnounceFormationCreateView.as_view(), name='formation-create'),
    path('employ', AnnounceEmployCreateView.as_view(), name='employ-create'),

    # *************************************  Detail url **************************************************************

    # path('create_images<str:id>/', ImagesCreateView.as_view(), name='images-create'),
    path('update<str:id>/', AnnounceUpdate.as_view(), name='post-update'),
    path('delete<str:id>/', AnnounceDeleteView.as_view(), name='post-delete'),
]

htmx_patterns = [
    path('c', search, name='search'),
    path('j', search_announce, name='search-post'),  # INDEX PAGE
]

urlpatterns += htmx_patterns
