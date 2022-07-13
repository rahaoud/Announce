# import uuid
# from django.db import models
# # Create your models here.
# from users.models import MyUser
#
#
# # *************************--The Category --***********************************
# class Category(models.Model):
#     name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)
#
#     def __str__(self):
#         return self.name
#
#
# # ***************************--Immovable--***************************************
#
# class ImmovableType(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class Immovable(models.Model):
#     type = models.ForeignKey(ImmovableType, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     area = models.IntegerField()
#     number_pieces = models.IntegerField()
#     furniture = models.BooleanField()
#
#     def __str__(self):
#         return self.type.name
#
#
# # **************************--Furniture--********************************************
# class FurnitureApplianceType(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class FurnitureAppliance(models.Model):
#     conditions = [
#         ('new', 'New'),
#         ('utilize', 'Utilize'),
#         ('other', 'Other'),
#     ]
#     type = models.ForeignKey(FurnitureApplianceType, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     condition = models.CharField(max_length=300, choices=conditions)
#
#     def __str__(self):
#         return self.type.name
#
#
# # *************************************--Car--**********************************************
# class CarType(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class CarModel(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class CarMarque(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class CarFuel(models.Model):
#     name = models.CharField(max_length=25)
#
#     def __str__(self):
#         return self.name
#
#
# class CarGenre(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class Car(models.Model):
#     transmissions = [
#         ('automatic', 'Automatic'),
#         ('manual', 'Manual'),
#         ('other', 'Other'),
#     ]
#     conditions = [
#         ('new', 'New'),
#         ('occasion', 'Occasion'),
#         ('other', 'Other'),
#     ]
#     type = models.ForeignKey(CarType, on_delete=models.CASCADE)
#     genre = models.ForeignKey(CarGenre, on_delete=models.CASCADE)
#     # category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
#     marque = models.ForeignKey(CarMarque, on_delete=models.CASCADE)
#     fuel = models.ForeignKey(CarFuel, on_delete=models.CASCADE)
#     transmission = models.CharField(max_length=15, choices=transmissions)
#     year = models.IntegerField()
#
#     def __str__(self):
#         return self.type.name
#
#     class Meta:
#         abstract = True
#
#
# # **********************************************--Phone end Tablet--****************************
#
# class PhoneTabletType(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class PhoneTabletModel(models.Model):
#     name = models.CharField(max_length=25)
#
#     def __str__(self):
#         return self.name
#
#
# class PhoneTabletMarque(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class PhoneTablet(models.Model):
#     type = models.ForeignKey(PhoneTabletType, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     model = models.ForeignKey(PhoneTabletModel, on_delete=models.CASCADE)
#     marque = models.ForeignKey(PhoneTabletMarque, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.type
#
#
# # ***************************************-Electronic-***************************
# class ElectronicType(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class ElectronicModel(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class ElectronicMarque(models.Model):
#     name = models.CharField(max_length=25)
#
#     def __str__(self):
#         return self.name
#
#
# class Electronic(models.Model):
#     type = models.ForeignKey(ElectronicType, on_delete=models.CASCADE)
#     model = models.ForeignKey(ElectronicModel, on_delete=models.CASCADE)
#     marque = models.ForeignKey(ElectronicMarque, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.type.name
#
#
# # ***************************************-Animal-***************************
#
# class AnimalType(models.Model):
#     name = models.CharField(max_length=50)
#
#
# class Animal(models.Model):
#     genres = [
#         ('masculine', 'Masculine'),
#         ('feminine', 'Feminine'),
#         ('masculine_and_feminine', 'Masculine end Feminine'),
#     ]
#     type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     genre = models.CharField(max_length=30, choices=genres)
#
#     def __str__(self):
#         return self.name
#
#
# # ***************************************-Beauty and wellness-***************************
#
# class BeautyWellnessType(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class BeautyWellness(models.Model):
#     type = models.ForeignKey(BeautyWellnessType, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.type.name
#
#
# # ***************************************-Fashion and clothes -***************************
#
# class FashionClothesType(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class FashionClothes(models.Model):
#     conditions = [
#         ('new', 'New'),
#         ('utilize', 'Utilize'),
#         ('other', 'Other'),
#     ]
#     type = models.ForeignKey(FashionClothesType, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     condition = models.CharField(max_length=15, choices=conditions)
#
#     def __str__(self):
#         return self.type.name
#
#
# # ***************************************-Service Delivery-***************************
#
# class ServiceDeliveryType(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class ServiceDelivery(models.Model):
#     type = models.ForeignKey(ServiceDeliveryType, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.type.name
#
#
# # ***************************************-Event-***************************
#
# class EventType(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name
#
#
# class Event(models.Model):
#     type = models.ForeignKey(ElectronicType, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     locale = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.type.name
#
#
# # ***************************************-Formation-***************************
#
# class FormationType(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name
#
#
# class Formation(models.Model):
#     conditions = [
#         ('offer', 'Offer'),
#         ('demand', 'Demand'),
#         ('other', 'Other'),
#     ]
#     type = models.ForeignKey(FormationType, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     statu = models.CharField(max_length=10, choices=conditions)
#
#     def __str__(self):
#         return self.type.name
#
#
# # ***************************************-Employ-***************************
#
# class EmployType(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class Diploma(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class Employ(models.Model):
#     conditions = [
#         ('offer', 'Offer'),
#         ('demand', 'Demand'),
#         ('other', 'Other'),
#     ]
#     genres = [
#         ('masculine', 'Masculine'),
#         ('feminine', 'Feminine'),
#         ('masculine_and_feminine', 'Masculine end Feminine'),
#     ]
#     type = models.ForeignKey(EmployType, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     diploma = models.ForeignKey(Diploma, on_delete=models.CASCADE)
#     statu = models.CharField(max_length=15, choices=conditions)
#     genre = models.CharField(max_length=30, choices=genres)
#
#     def __str__(self):
#         return self.type.name
#
#
# # ***************************--Locality--***************************************
# class LocalityCountry(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class LocalityTown(models.Model):
#     name = models.CharField(max_length=50, )
#
#
# class LocalityCommon(models.Model):
#     name = models.CharField(max_length=150)
#     country = models.ForeignKey(LocalityCountry, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class LocalityPiece(models.Model):
#     name = models.CharField(max_length=50)
#
#
# class Locality(models.Model):
#     country = models.ForeignKey(LocalityCountry, on_delete=models.CASCADE)
#     town = models.ForeignKey(LocalityTown, on_delete=models.CASCADE)
#     common = models.ForeignKey(LocalityCommon, on_delete=models.CASCADE)
#     piece = models.ForeignKey(LocalityPiece, on_delete=models.CASCADE)
#
#
# # ****************************************-Announce-*****************************************
#
# class AnnounceType(models.Model):
#     name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)
#
#     def __str__(self):
#         return self.name
#
#
# class AnnounceNotation(models.Model):
#     notation = models.IntegerField()
#
#
# class Announce(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
#     user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)
#     locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
#     type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
#     title = models.CharField(max_length=128, blank=False)
#     description = models.TextField(blank=False)
#     price = models.IntegerField(blank=False)
#     thumbnail = models.ImageField(upload_to='post/thumbnail', blank=True, null=True)
#     published = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     notation = models.ForeignKey(AnnounceNotation, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#     def get_thumbnail_url(self):
#         if self.thumbnail:
#             thumbnail = self.thumbnail.url
#             return thumbnail
#         else:
#             return ''
#
#     # class Meta:
#     #     abstract = True
#
#
# # class Images(models.Model):
# #     announce = models.ForeignKey(AnnounceCar, on_delete=models.CASCADE, null=True, blank=True)
# #     images = models.ImageField(upload_to='post/images')
#
#     # def __str__(self):
#     #     return self.post.title
#
#
# class AnnounceCar(Announce, Car):
#     announce_car = models.CharField(max_length=30)
#
#
