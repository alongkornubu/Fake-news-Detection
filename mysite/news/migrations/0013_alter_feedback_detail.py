# Generated by Django 4.1.4 on 2022-12-21 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0012_feedback_delete_feedbacks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="detail",
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]
