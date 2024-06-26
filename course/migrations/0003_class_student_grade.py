# Generated by Django 5.0.6 on 2024-05-29 21:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_trainingunit_hours_alter_trainingunit_period'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=6)),
                ('_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.class')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('released_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('training_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.trainingunit')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.student')),
            ],
        ),
    ]
