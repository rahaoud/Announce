# Generated by Django 4.0.4 on 2022-07-03 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AnnounceAnimal',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('masculine', 'Masculine'), ('feminine', 'Feminine'), ('masculine_and_feminine', 'Masculine end Feminine')], max_length=30)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnounceBeautyWellness',
            fields=[
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnounceCar',
            fields=[
                ('transmission', models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual'), ('other', 'Other')], max_length=15)),
                ('year', models.IntegerField()),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnounceElectronic',
            fields=[
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnounceEmploy',
            fields=[
                ('statu', models.CharField(choices=[('offer', 'Offer'), ('demand', 'Demand'), ('other', 'Other')], max_length=15)),
                ('genre', models.CharField(choices=[('masculine', 'Masculine'), ('feminine', 'Feminine'), ('masculine_and_feminine', 'Masculine end Feminine')], max_length=30)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnounceEvent',
            fields=[
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('locale', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnounceFashionClothes',
            fields=[
                ('condition', models.CharField(choices=[('new', 'New'), ('utilize', 'Utilize'), ('other', 'Other')], max_length=15)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnounceFormation',
            fields=[
                ('statu', models.CharField(choices=[('offer', 'Offer'), ('demand', 'Demand'), ('other', 'Other')], max_length=10)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnounceFurnitureAppliance',
            fields=[
                ('condition', models.CharField(choices=[('new', 'New'), ('utilize', 'Utilize'), ('other', 'Other')], max_length=300)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnounceNotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncePhoneTablet',
            fields=[
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnounceServiceDelivery',
            fields=[
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnounceType',
            fields=[
                ('name', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='BeautyWellnessType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CarFuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='CarGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarMarque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ElectronicMarque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ElectronicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ElectronicType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EmployType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FashionClothesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='FormationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FurnitureApplianceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ImmovableType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LocalityCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LocalityPiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LocalityTown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneTabletMarque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneTabletModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneTabletType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDeliveryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LocalityCommon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.localitycountry')),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.localitycommon')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.localitycountry')),
                ('piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.localitypiece')),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.localitytown')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnounceServiceDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='post/images')),
                ('announce_service_delivery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announceservicedelivery')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnouncePhoneTablet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='post/images')),
                ('announce_electronic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announcephonetablet')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnounceFurnitureAppliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='post/images')),
                ('announce_furniture_appliance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announcefurnitureappliance')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnounceFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='post/images')),
                ('announce_formation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announceformation')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnounceFashionClothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='post/images')),
                ('announce_fashion_clothes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announcefashionclothes')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnounceEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='post/images')),
                ('announce_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announceevent')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnounceEmploy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='post/images')),
                ('announce_employ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announceemploy')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnounceElectronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='post/images')),
                ('announce_electronic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announceelectronic')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnounceCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='post/images')),
                ('announce_car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announcecar')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnounceBeautyWellness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='post/images')),
                ('announce_beauty_wellness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announcebeautywellness')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnounceAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='post/images')),
                ('announce_animal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announceanimal')),
            ],
        ),
        migrations.AddField(
            model_name='announceservicedelivery',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category'),
        ),
        migrations.AddField(
            model_name='announceservicedelivery',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality'),
        ),
        migrations.AddField(
            model_name='announceservicedelivery',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation'),
        ),
        migrations.AddField(
            model_name='announceservicedelivery',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.servicedeliverytype'),
        ),
        migrations.AddField(
            model_name='announceservicedelivery',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announcephonetablet',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category'),
        ),
        migrations.AddField(
            model_name='announcephonetablet',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality'),
        ),
        migrations.AddField(
            model_name='announcephonetablet',
            name='marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.phonetabletmarque'),
        ),
        migrations.AddField(
            model_name='announcephonetablet',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.phonetabletmodel'),
        ),
        migrations.AddField(
            model_name='announcephonetablet',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation'),
        ),
        migrations.AddField(
            model_name='announcephonetablet',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.phonetablettype'),
        ),
        migrations.AddField(
            model_name='announcephonetablet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announcefurnitureappliance',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category'),
        ),
        migrations.AddField(
            model_name='announcefurnitureappliance',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality'),
        ),
        migrations.AddField(
            model_name='announcefurnitureappliance',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation'),
        ),
        migrations.AddField(
            model_name='announcefurnitureappliance',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.furnitureappliancetype'),
        ),
        migrations.AddField(
            model_name='announcefurnitureappliance',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announceformation',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category'),
        ),
        migrations.AddField(
            model_name='announceformation',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality'),
        ),
        migrations.AddField(
            model_name='announceformation',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation'),
        ),
        migrations.AddField(
            model_name='announceformation',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.formationtype'),
        ),
        migrations.AddField(
            model_name='announceformation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announcefashionclothes',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category'),
        ),
        migrations.AddField(
            model_name='announcefashionclothes',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality'),
        ),
        migrations.AddField(
            model_name='announcefashionclothes',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation'),
        ),
        migrations.AddField(
            model_name='announcefashionclothes',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.fashionclothestype'),
        ),
        migrations.AddField(
            model_name='announcefashionclothes',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announceevent',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category'),
        ),
        migrations.AddField(
            model_name='announceevent',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality'),
        ),
        migrations.AddField(
            model_name='announceevent',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation'),
        ),
        migrations.AddField(
            model_name='announceevent',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.electronictype'),
        ),
        migrations.AddField(
            model_name='announceevent',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announceemploy',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category'),
        ),
        migrations.AddField(
            model_name='announceemploy',
            name='diploma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.diploma'),
        ),
        migrations.AddField(
            model_name='announceemploy',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality'),
        ),
        migrations.AddField(
            model_name='announceemploy',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation'),
        ),
        migrations.AddField(
            model_name='announceemploy',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.employtype'),
        ),
        migrations.AddField(
            model_name='announceemploy',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announceelectronic',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category'),
        ),
        migrations.AddField(
            model_name='announceelectronic',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality'),
        ),
        migrations.AddField(
            model_name='announceelectronic',
            name='marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.electronicmarque'),
        ),
        migrations.AddField(
            model_name='announceelectronic',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.electronicmodel'),
        ),
        migrations.AddField(
            model_name='announceelectronic',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation'),
        ),
        migrations.AddField(
            model_name='announceelectronic',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.electronictype'),
        ),
        migrations.AddField(
            model_name='announceelectronic',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announcecar',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category'),
        ),
        migrations.AddField(
            model_name='announcecar',
            name='fuel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.carfuel'),
        ),
        migrations.AddField(
            model_name='announcecar',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.cargenre'),
        ),
        migrations.AddField(
            model_name='announcecar',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality'),
        ),
        migrations.AddField(
            model_name='announcecar',
            name='marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.carmarque'),
        ),
        migrations.AddField(
            model_name='announcecar',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.carmodel'),
        ),
        migrations.AddField(
            model_name='announcecar',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation'),
        ),
        migrations.AddField(
            model_name='announcecar',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.cartype'),
        ),
        migrations.AddField(
            model_name='announcecar',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announcebeautywellness',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category'),
        ),
        migrations.AddField(
            model_name='announcebeautywellness',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality'),
        ),
        migrations.AddField(
            model_name='announcebeautywellness',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation'),
        ),
        migrations.AddField(
            model_name='announcebeautywellness',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.beautywellnesstype'),
        ),
        migrations.AddField(
            model_name='announcebeautywellness',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announceanimal',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category'),
        ),
        migrations.AddField(
            model_name='announceanimal',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality'),
        ),
        migrations.AddField(
            model_name='announceanimal',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation'),
        ),
        migrations.AddField(
            model_name='announceanimal',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.animaltype'),
        ),
        migrations.AddField(
            model_name='announceanimal',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
