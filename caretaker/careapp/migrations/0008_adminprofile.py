# Generated by Django 5.0.6 on 2024-06-06 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0007_delete_adminprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='admin_profiles/')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
