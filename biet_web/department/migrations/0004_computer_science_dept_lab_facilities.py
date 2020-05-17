# Generated by Django 3.0.6 on 2020-05-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_biotechnology_dept_gallery_chemical_dept_gallery_chemistry_dept_gallery_computer_science_dept_galler'),
    ]

    operations = [
        migrations.CreateModel(
            name='computer_science_dept_lab_facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('qty', models.IntegerField()),
                ('config_specs', models.TextField()),
                ('softwares', models.TextField()),
            ],
        ),
    ]
