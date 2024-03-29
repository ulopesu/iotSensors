# Generated by Django 2.2.7 on 2019-11-06 21:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=100, verbose_name='Label')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, verbose_name='UserName')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=100, verbose_name='Label')),
                ('enable', models.BooleanField(verbose_name='Enable')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streams', to='core.Sensor')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.Unit')),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='core.User'),
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='TimeStamp')),
                ('value', models.FloatField(verbose_name='Value')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='core.Stream')),
            ],
        ),
    ]
