# Generated by Django 4.1.5 on 2023-01-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kelas', models.IntegerField()),
            ],
            options={
                'db_table': 'kelas',
            },
        ),
    ]
