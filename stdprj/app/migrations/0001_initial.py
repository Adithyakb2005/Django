# Generated by Django 5.1.2 on 2024-11-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('place', models.TextField()),
            ],
        ),
    ]
