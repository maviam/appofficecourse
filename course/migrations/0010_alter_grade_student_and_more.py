# Generated by Django 5.0.6 on 2024-06-07 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_remove_trainingunit_active_trainingunit_all_classes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.student'),
        ),
        migrations.AddConstraint(
            model_name='grade',
            constraint=models.UniqueConstraint(fields=('student', 'training_unit'), name='unique_student_unit_combination'),
        ),
    ]
