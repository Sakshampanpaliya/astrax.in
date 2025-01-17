# Generated by Django 4.1.4 on 2023-02-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('long_description', models.TextField()),
                ('team_size', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('rulebook_link', models.URLField()),
                ('Registration_link', models.URLField()),
                ('submission_link', models.URLField()),
                ('image', models.ImageField(default='astrax23/images/events_images/default.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('image', models.ImageField(default='astrax23/images/speaker_images/default.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('website', models.TextField()),
                ('type', models.TextField()),
                ('image', models.ImageField(default='astrax23/images/sponsor_images/default.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Position_of_head', models.CharField(max_length=100)),
                ('insta_link', models.URLField(default='https://www.youtube.com/watch?v=33Xe3z8L73A')),
                ('linkedin_link', models.URLField(default='https://www.youtube.com/watch?v=33Xe3z8L73A')),
                ('image', models.ImageField(default='astrax23/images/team_images/default.jpg', upload_to='images/')),
            ],
        ),
    ]
