from django.contrib import admin

# Register your models here.
from announce.models import (Announce, LocalityCommon, LocalityCountry, Category,
                             FurnitureApplianceType, FurnitureAppliance, CarType,
                             CarModel, CarMarque, CarFuel, CarGenre, Car, PhoneTabletType,
                             PhoneTabletModel, PhoneTabletMarque, PhoneTablet, Immovable, ImmovableType, ElectronicType,
                             ElectronicModel, ElectronicMarque, Electronic, AnimalType, Animal, BeautyWellnessType,
                             BeautyWellness, FashionClothesType, FashionClothes, ServiceDeliveryType, ServiceDelivery,
                             EventType, Event, FormationType, Formation, EmployType, Diploma, Employ, LocalityTown,
                             LocalityPiece, Locality, AnnounceType, AnnounceNotation,
                             )

from django.contrib import admin
from datetime import timedelta


# *************************--The Category --***********************************

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# **********************--Immovable--***********************

@admin.register(ImmovableType)
class ImmovableTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

#
# @admin.register(Immovable)
# class ImmovableAdmin(admin.ModelAdmin):
#     list_display = ('type', 'category', 'area', 'number_pieces', 'furniture')


# **********************--Furniture--***********************
@admin.register(FurnitureApplianceType)
class TypeFurnitureApplianceAdmin(admin.ModelAdmin):
    list_display = ('name',)


# @admin.register(FurnitureAppliance)
# class FurnitureApplianceAdmin(admin.ModelAdmin):
#     list_display = ('type', 'category', 'condition')


# *************************--Car--****************************************
@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarMarque)
class CarMarqueAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarFuel)
class CarFuelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarGenre)
class CarGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


# @admin.register(Car)
# class CarAdmin(admin.ModelAdmin):
#     list_display = ('type', 'model', 'marque', 'genre', 'fuel', 'transmission', 'year')


# *******************************************--Phone Tablet--*****************************************
@admin.register(PhoneTabletType)
class PhoneTabletTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PhoneTabletModel)
class PhoneTabletModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PhoneTabletMarque)
class PhoneTabletMarqueAdmin(admin.ModelAdmin):
    list_display = ('name',)


# @admin.register(PhoneTablet)
# class PhoneTabletAdmin(admin.ModelAdmin):
#     list_display = ('type', 'category', 'model', 'marque')


# ****************************************-Electronic-**************************************

@admin.register(ElectronicType)
class ElectronicTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ElectronicModel)
class ElectronicModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ElectronicMarque)
class ElectronicMarqueAdmin(admin.ModelAdmin):
    list_display = ('name',)


# @admin.register(Electronic)
# class ElectronicAdmin(admin.ModelAdmin):
#     list_display = ('type', 'category', 'model', 'marque')


# ******************************************--Animal--*********************************************
@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

#
# @admin.register(Animal)
# class AnimalAdmin(admin.ModelAdmin):
#     list_display = ('type', 'category', 'name', 'genre',)


# *********************************************--Beauty and Wellness--***************************************************

@admin.register(BeautyWellnessType)
class BeautyWellnessTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

#
# @admin.register(BeautyWellness)
# class BeautyWellnessAdmin(admin.ModelAdmin):
#     list_display = ('type', 'category')


# ******************************************--Fashion and clothes--*********************************************
@admin.register(FashionClothesType)
class FashionClothesTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


# @admin.register(FashionClothes)
# class FashionClothesAdmin(admin.ModelAdmin):
#     list_display = ('type', 'category', 'condition')


# ******************************************--Service Delivery--*********************************************
@admin.register(ServiceDeliveryType)
class ServiceDeliveryTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


# @admin.register(ServiceDelivery)
# class ServiceDeliveryAdmin(admin.ModelAdmin):
#     list_display = ('type', 'category',)


# ******************************************--EventType--*********************************************

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ('type', 'category', 'start_date', 'end_date', 'locale')


# ******************************************--Formation--*********************************************
@admin.register(FormationType)
class FormationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


# @admin.register(Formation)
# class FormationAdmin(admin.ModelAdmin):
#     list_display = ('type', 'category', 'statu')


# ******************************************--Employ--*********************************************
@admin.register(EmployType)
class EmployTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Diploma)
class DiplomaAdmin(admin.ModelAdmin):
    list_display = ('name',)


# @admin.register(Employ)
# class EmployAdmin(admin.ModelAdmin):
#     list_display = ('type', 'category', 'diploma', 'statu', 'genre',)


# ******************************************--Locality--*********************************************

@admin.register(LocalityCountry)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(LocalityTown)
class TownAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(LocalityCommon)
class CommonAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name',)


@admin.register(LocalityPiece)
class PieceAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ('country', 'town', 'common', 'piece')


# **************************************************--Announce_-**********************************************************

@admin.register(AnnounceType)
class AnnounceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(AnnounceNotation)
class AnnounceNotationAdmin(admin.ModelAdmin):
    list_display = ('notation',)


# @admin.register(Announce)
# class AnnounceAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user', 'get_utc',)
#
#     search_fields = ('title',)
#     list_filter = ('created',)
#     empty_value_display = '-empty field-'
#
#     def get_utc(self, obj):
#         return obj.created + timedelta(minutes=330)
#
#     get_utc.short_description = 'Created (UTC)'

#
# @admin.register(Images)
# class ImagesAdmin(admin.ModelAdmin):
#     list_display = ('images',)
