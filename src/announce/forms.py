from django.forms import ModelForm
from django import forms

from announce.models import (AnnounceCar, AnnounceOther, AnnouncePhoneTablet, AnnounceFormation,
                             AnnounceFurnitureAppliance, AnnounceElectronic, AnnounceAnimal, AnnounceBeautyWellness,
                             AnnounceFashionClothes, AnnounceServiceDelivery, AnnounceEvent, AnnounceEmploy,
                             AnnounceImmovable)


class FormCategory:

    def __init__(self):
        self.model = None

    def model_category(self, request):

        choix = request.GET.get('category')
        if choix == 'car':
            self.model = AnnounceCar
        elif choix == 'tabl':
            self.model = AnnouncePhoneTablet
        elif choix == 'formation':
            self.model = AnnounceFormation
        else:
            self.model = AnnounceOther
        return self.model


class AnnounceForm(ModelForm):
    images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'multiple': True,
        'class': 'form-control',
        'id': 'files',
        'name': 'files[]'
    }))

    class Meta:
        model = AnnounceOther
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 99px',
                'placeholder': 'Description',
                'name': '',
                'id': '',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price'
            }),
            'thumbnail': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'file',
                'style': ''

            }),

        }


class AnnounceOtherForm(AnnounceForm):
    class Meta:
        model = AnnounceOther
        fields = '__all__'


class AnnounceCarForm(AnnounceForm):
    class Meta:
        model = AnnounceCar
        fields = '__all__'


class AnnounceFurnitureApplianceForm(AnnounceForm):
    class Meta:
        model = AnnounceFurnitureAppliance
        fields = '__all__'


class AnnouncePhoneTabletForm(AnnounceForm):
    class Meta:
        model = AnnouncePhoneTablet
        fields = '__all__'


class AnnounceElectronicForm(AnnounceForm):
    class Meta:
        model = AnnounceElectronic
        fields = '__all__'


class AnnounceAnimalForm(AnnounceForm):
    class Meta:
        model = AnnounceAnimal
        fields = '__all__'


class AnnounceBeautyWellnessForm(AnnounceForm):
    class Meta:
        model = AnnounceBeautyWellness
        fields = '__all__'


class AnnounceFashionClothesForm(AnnounceForm):
    class Meta:
        model = AnnounceFashionClothes
        fields = '__all__'


class AnnounceServiceDeliveryForm(AnnounceForm):
    class Meta:
        model = AnnounceServiceDelivery
        fields = '__all__'


class AnnounceEventForm(AnnounceForm):
    class Meta:
        model = AnnounceEvent
        fields = '__all__'


class AnnounceFormationForm(AnnounceForm):
    class Meta:
        model = AnnounceFormation
        fields = '__all__'


class AnnounceEmployForm(AnnounceForm):
    class Meta:
        model = AnnounceEmploy
        fields = '__all__'


class AnnounceImmovableForm(AnnounceForm):
    class Meta:
        model = AnnounceImmovable
        fields = '__all__'
