# Generated by Django 3.0 on 2019-12-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_registration_no', models.IntegerField()),
                ('Batch', models.IntegerField()),
            ],
        ),
    ]