# Generated by Django 4.0.4 on 2022-07-06 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('announce', '0002_announceother_alter_imageannounceanimal_images_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnounceImmovable',
            fields=[
                ('area', models.IntegerField()),
                ('number_pieces', models.IntegerField()),
                ('furniture', models.BooleanField()),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail')),
                ('published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.category')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.locality')),
                ('notation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announcenotation')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.immovabletype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='imageannounceanimal',
            old_name='announce_animal',
            new_name='announce',
        ),
        migrations.RenameField(
            model_name='imageannouncebeautywellness',
            old_name='announce_beauty_wellness',
            new_name='announce',
        ),
        migrations.RenameField(
            model_name='imageannouncecar',
            old_name='announce_car',
            new_name='announce',
        ),
        migrations.RenameField(
            model_name='imageannounceelectronic',
            old_name='announce_electronic',
            new_name='announce',
        ),
        migrations.RenameField(
            model_name='imageannounceemploy',
            old_name='announce_employ',
            new_name='announce',
        ),
        migrations.RenameField(
            model_name='imageannounceevent',
            old_name='announce_event',
            new_name='announce',
        ),
        migrations.RenameField(
            model_name='imageannouncefashionclothes',
            old_name='announce_fashion_clothes',
            new_name='announce',
        ),
        migrations.RenameField(
            model_name='imageannounceformation',
            old_name='announce_formation',
            new_name='announce',
        ),
        migrations.RenameField(
            model_name='imageannouncefurnitureappliance',
            old_name='announce_furniture_appliance',
            new_name='announce',
        ),
        migrations.RenameField(
            model_name='imageannounceother',
            old_name='announce_other',
            new_name='announce',
        ),
        migrations.RenameField(
            model_name='imageannouncephonetablet',
            old_name='announce_electronic',
            new_name='announce',
        ),
        migrations.RenameField(
            model_name='imageannounceservicedelivery',
            old_name='announce_service_delivery',
            new_name='announce',
        ),
        migrations.CreateModel(
            name='ImageAnnounceImmovable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='announce/announce_car')),
                ('announce', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='announce.announceimmovable')),
            ],
        ),
    ]