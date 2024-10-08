# Generated by Django 4.2.6 on 2023-10-12 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='petList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('image_path', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Adoption Pending', 'Adoption Pending')], max_length=20)),
                ('suburb', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_added', models.DateTimeField()),
            ],
        ),
    ]
