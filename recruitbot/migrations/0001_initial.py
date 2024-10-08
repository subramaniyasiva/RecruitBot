# Generated by Django 5.1 on 2024-09-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('linkedin', models.URLField()),
                ('skills', models.TextField()),
                ('Degree', models.CharField(max_length=50)),
                ('Specialization', models.CharField(max_length=50)),
                ('exp', models.CharField(max_length=50)),
                ('prev_employer', models.CharField(max_length=50)),
                ('Agreement', models.CharField(max_length=50)),
                ('start_date', models.DateField(auto_now=True)),
                ('refby', models.CharField(max_length=50)),
            ],
        ),
    ]
