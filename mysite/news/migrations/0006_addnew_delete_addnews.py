# Generated by Django 4.1.2 on 2022-11-06 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_addnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=500)),
                ('tag', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='AddNews',
        ),
    ]