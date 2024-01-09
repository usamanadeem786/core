# Generated by Django 5.0 on 2024-01-03 18:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_post_thumbnail_alter_post_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="like",
            name="ip_address",
            field=models.GenericIPAddressField(default="127.0.0.1"),
        ),
        migrations.AlterField(
            model_name="like",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.post"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="like",
            unique_together={("user", "post")},
        ),
    ]