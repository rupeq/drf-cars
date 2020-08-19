# Generated by Django 3.1 on 2020-08-18 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=64)),
                ('number', models.IntegerField(db_index=True, unique=True)),
                ('color', models.CharField(max_length=64)),
                ('car_type', models.IntegerField(choices=[(1, 'Sedan'), (2, 'Hatchback'), (3, 'Crossover'), (4, 'Coupe')], default='Coupe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]