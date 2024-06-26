# Generated by Django 5.0.4 on 2024-04-22 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_createapiary_apiary'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasckActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.activity')),
            ],
        ),
    ]
