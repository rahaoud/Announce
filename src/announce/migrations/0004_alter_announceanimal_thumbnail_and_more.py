# Generated by Django 4.0.4 on 2022-07-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0003_announceimmovable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announceanimal',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announcebeautywellness',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announcecar',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announceelectronic',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announceemploy',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announceevent',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announcefashionclothes',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announceformation',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announcefurnitureappliance',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announceimmovable',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announceother',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announcephonetablet',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
        migrations.AlterField(
            model_name='announceservicedelivery',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='announce/thumbnail'),
        ),
    ]
