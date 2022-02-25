# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ('id', models.UUIDField(primary_key=True)),
                ('is_anonymous', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_authenticated', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'managed': False,
            }
        )
    ]
