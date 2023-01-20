# Generated by Django 4.1.4 on 2022-12-24 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('image', models.ImageField(default='astrax23/images/speaker_images/default.jpg', upload_to='images/speakers_images')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
              ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False, verbose_name='ID')),
              ('name',models.TextField()),
              ('website',models.TextField()),
              ('type',models.TextField()),
              ('image', models.ImageField(default='astrax23/images/sponsor_images/default.jpg', upload_to='images/sponsor_images')),
            ],
        )

    ]