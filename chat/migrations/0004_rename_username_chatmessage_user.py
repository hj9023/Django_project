# Generated by Django 4.2.7 on 2023-12-01 07:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0003_rename_user_chatmessage_username"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chatmessage",
            old_name="username",
            new_name="user",
        ),
    ]
