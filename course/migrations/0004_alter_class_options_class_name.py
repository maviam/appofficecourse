# Generated by Django 5.0.6 on 2024-05-31 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_class_student_grade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
        migrations.AddField(
            model_name='class',
            name='name',
            field=models.CharField(blank=True, max_length=75),
        ),
    ]
