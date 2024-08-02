# Generated by Django 5.0.6 on 2024-06-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0005_adminprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofile',
            name='admin_address',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='adminprofile',
            name='admin_email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='adminprofile',
            name='admin_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='adminprofile',
            name='admin_phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
