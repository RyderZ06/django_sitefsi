# Generated by Django 5.2.3 on 2025-07-08 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name': 'Департамент',
                'verbose_name_plural': 'Департаменты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=100)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='employees/%Y/%m/%d')),
                ('resume', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='main.department')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='main.gender')),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='main.jobtitle')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
