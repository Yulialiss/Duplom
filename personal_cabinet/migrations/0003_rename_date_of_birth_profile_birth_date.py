# Generated by Django 5.1.3 on 2024-12-28 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_cabinet', '0002_profile_bio_profile_location_profile_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='date_of_birth',
            new_name='birth_date',
        ),
    ]
