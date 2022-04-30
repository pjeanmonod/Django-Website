# Generated by Django 4.0.3 on 2022-04-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('job_id', models.IntegerField(primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
                ('role', models.CharField(max_length=60)),
                ('role_display_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='JobVar',
            fields=[
                ('var_id', models.IntegerField(primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
                ('input_type', models.CharField(choices=[('text', 'text'), ('user_array', 'user_array'), ('defined_array', 'defined_array'), ('boolean', 'boolean')], default='text', max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
