# Generated by Django 5.0 on 2024-01-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0014_alter_comment_user_alter_like_ip_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
