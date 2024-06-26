# Generated by Django 5.0.4 on 2024-05-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ingame_name', models.CharField(max_length=255)),
                ('joined_date', models.DateField(null=True)),
                ('score', models.IntegerField(auto_created=0, null=True)),
                ('game_win', models.IntegerField(null=True)),
                ('game_lose', models.IntegerField(null=True)),
                ('game_draw', models.IntegerField(null=True)),
            ],
        ),
    ]
