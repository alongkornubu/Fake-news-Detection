# Generated by Django 4.1.2 on 2022-11-08 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_addnew_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactMe',
            new_name='Feedback',
        ),
    ]
