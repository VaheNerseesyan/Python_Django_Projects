# Generated by Django 5.0.6 on 2024-05-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_alter_phone_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="owner",
            name="phone_models",
        ),
        migrations.AlterField(
            model_name="phone",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="media/picture"),
        ),
        migrations.AddField(
            model_name="owner",
            name="phone_models",
            field=models.CharField(
                choices=[("128gb", "128gb"), ("256gb", "256gb"), ("512gb", "512gb")],
                default=49,
                max_length=15,
            ),
            preserve_default=False,
        ),
    ]
