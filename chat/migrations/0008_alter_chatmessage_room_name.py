# Generated by Django 4.2.7 on 2023-12-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0007_alter_chatmessage_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatmessage",
            name="room_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
