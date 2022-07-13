# from django.contrib.auth import authenticate, login, logout
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

# Post ListView
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView

from announce.forms import (AnnounceForm, AnnounceCarForm, AnnounceOtherForm, AnnounceFurnitureApplianceForm,
                            AnnouncePhoneTabletForm, AnnounceElectronicForm, AnnounceAnimalForm,
                            AnnounceBeautyWellnessForm, AnnounceFashionClothesForm, AnnounceServiceDeliveryForm,
                            AnnounceEventForm, AnnounceFormationForm, AnnounceEmployForm, AnnounceImmovableForm)
from announce.models import (Announce, AnnounceCar, ImageAnnounceOther, AnnounceOther, ImageAnnounceCar,
                             AnnounceFurnitureAppliance, ImageAnnounceFurnitureAppliance, AnnouncePhoneTablet,
                             ImageAnnouncePhoneTablet, AnnounceElectronic, ImageAnnounceElectronic, AnnounceAnimal,
                             ImageAnnounceAnimal, AnnounceBeautyWellness, ImageAnnounceBeautyWellness,
                             ImageAnnounceFashionClothes, AnnounceFashionClothes, AnnounceServiceDelivery,
                             ImageAnnounceServiceDelivery, AnnounceEvent, ImageAnnounceEvent, AnnounceFormation,
                             ImageAnnounceFormation, AnnounceEmploy, ImageAnnounceEmploy, AnnounceImmovable,
                             ImageAnnounceImmovable)

template_index = 'page/userprofile_detail.html'


# template_index = 'base/search.html'
# template_index = 'base.html'

# new
@require_http_methods(['POST'])
def search(request):
    if 'search' in request.GET:
        q = request.GET['search']
        results = Announce.objects.filter(title__icontains=q)
        context = {'posts': results}
    else:
        results = Announce.objects.none()
        context = {'posts': results}
    return render(request, 'index.html', context)


class HomeTemplateView(TemplateView):
    template_name = 'announce-index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = AnnounceOther.objects.all()
        return context


def search_announce(request):
    template = 'index.html'
    if 'q' in request.GET:
        q = request.GET['q']
        results = Announce.objects.filter(Q(Q(title__icontains=q) | Q(tags__name__icontains=q))).order_by('-created')
    else:
        results = Announce.objects.all().order_by('-created')
    context = {'posts': results}
    if request.htmx:
        template = 'page/search_results.html'
    return render(request, template, context)


class AnnounceListView(ListView):
    model = Announce
    template_name = 'index.html'

    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get("q")
        search_vector = SearchVector("title", "tags")
        search_query = SearchQuery(query)
        results = (Announce.objects.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)).filter(
            search=search_query).order_by("-rank"))
        return results


# **********************************Announce DetailView*******************************************

class AnnounceOtherDetailView(DetailView):
    model = AnnounceOther

    # template_name = 'post/post_detail.html'

    def get_object(self, **kwargs):
        return get_object_or_404(AnnounceOther, id=self.kwargs.get('id'))

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['posts'] = Post.objects.get()


class AnnounceImmovableDetailView(AnnounceOtherDetailView):
    model = AnnounceImmovable

    def get_object(self, **kwargs):
        return get_object_or_404(AnnounceImmovable, id=self.kwargs.get('id'))


# ****************************************    Create Announce  *********************************************************
class AnnounceOtherCreateView(CreateView):
    model = AnnounceOther
    form_class = AnnounceOtherForm
    template_name = 'announce_form.html'

    # def get(self, request, *args, **kwargs):
    #     m = AnnounceCar
    #     f = AnnounceCar
    #     return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        announceother = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceOther.objects.create(announce=announceother, images=image)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Sign up'
        return context

    def get_success_url(self):
        return reverse('index')


class AnnounceImmovableCreateView(AnnounceOtherCreateView):
    model = AnnounceImmovable
    form_class = AnnounceImmovableForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceImmovable.objects.create(announce=post, images=image)
        return super().form_valid(form)


class AnnounceCarCreateView(AnnounceOtherCreateView):
    model = AnnounceCar
    form_class = AnnounceCarForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceCar.objects.create(post=post, images=image)
        return super().form_valid(form)


class AnnounceFurnitureApplianceCreateView(AnnounceOtherCreateView):
    model = AnnounceFurnitureAppliance
    form_class = AnnounceFurnitureApplianceForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceFurnitureAppliance.objects.create(post=post, images=image)
        return super().form_valid(form)


class AnnouncePhoneTabletCreateView(AnnounceOtherCreateView):
    model = AnnouncePhoneTablet
    form_class = AnnouncePhoneTabletForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnouncePhoneTablet.objects.create(post=post, images=image)
        return super().form_valid(form)


class AnnounceElectronicCreateView(AnnounceOtherCreateView):
    model = AnnounceElectronic
    form_class = AnnounceElectronicForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceElectronic.objects.create(post=post, images=image)
        return super().form_valid(form)


class AnnounceAnimalCreateView(AnnounceOtherCreateView):
    model = AnnounceAnimal
    form_class = AnnounceAnimalForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceAnimal.objects.create(post=post, images=image)
        return super().form_valid(form)


class AnnounceBeautyWellnessCreateView(AnnounceOtherCreateView):
    model = AnnounceBeautyWellness
    form_class = AnnounceBeautyWellnessForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceBeautyWellness.objects.create(post=post, images=image)
        return super().form_valid(form)


class AnnounceFashionClothesCreateView(AnnounceOtherCreateView):
    model = AnnounceFashionClothes
    form_class = AnnounceFashionClothesForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceFashionClothes.objects.create(post=post, images=image)
        return super().form_valid(form)


class AnnounceServiceDeliveryCreateView(AnnounceOtherCreateView):
    model = AnnounceServiceDelivery
    form_class = AnnounceServiceDeliveryForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceServiceDelivery.objects.create(post=post, images=image)
        return super().form_valid(form)


class AnnounceEventCreateView(AnnounceOtherCreateView):
    model = AnnounceEvent
    form_class = AnnounceEventForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceEvent.objects.create(post=post, images=image)
        return super().form_valid(form)


class AnnounceFormationCreateView(AnnounceOtherCreateView):
    model = AnnounceFormation
    form_class = AnnounceFormationForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceFormation.objects.create(post=post, images=image)
        return super().form_valid(form)


class AnnounceEmployCreateView(AnnounceOtherCreateView):
    model = AnnounceEmploy
    form_class = AnnounceEmployForm

    def form_valid(self, form):
        post = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ImageAnnounceEmploy.objects.create(post=post, images=image)
        return super().form_valid(form)


# ************************************************************************************************************


# class ImagesCreateView(TemplateView):
#     template_name = 'post/create_images.html'
#
#     def post(self, *args, **kwargs):
#         try:
#             images = self.request.FILES.getlist('images')
#             announce = Announce.objects.get(id=self.kwargs['pk'])
#             for image in images:
#                 announce_images = Images.objects.create(post=Announce, images=image)
#             return redirect('index')
#         except Exception as e:
#             print(e)


class AnnounceUpdate(UpdateView):
    model = Announce
    form_class = AnnounceForm

    def get_object(self, **kwargs):
        return get_object_or_404(Announce, id=self.kwargs.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Update'
        return context

    def get_success_url(self):
        return reverse('index')


class AnnounceDeleteView(DeleteView):
    model = Announce

    def get_object(self, **kwargs):
        return get_object_or_404(Announce, id=self.kwargs.get('id'))

    def get_success_url(self):
        return reverse('post-list')
