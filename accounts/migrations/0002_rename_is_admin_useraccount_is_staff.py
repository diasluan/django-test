# Generated by Django 3.2.3 on 2021-05-23 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
