# Generated by Django 5.0.4 on 2024-04-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("candidate", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidateadd",
            name="avatar",
            field=models.ImageField(upload_to="media/candidate/avatar"),
        ),
        migrations.AlterField(
            model_name="candidateadd",
            name="created_at",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="candidateprofile",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/candidate/avatar"
            ),
        ),
        migrations.AlterField(
            model_name="candidateprofile",
            name="birth_date",
            field=models.DateField(),
        ),
    ]
