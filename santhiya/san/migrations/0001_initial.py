# Generated by Django 4.2.6 on 2023-10-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='footballplayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noofplayers', models.IntegerField()),
                ('nameoftheplayer', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('noofteams', models.IntegerField()),
                ('noofgoals', models.IntegerField()),
            ],
        ),
    ]
