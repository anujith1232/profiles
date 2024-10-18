# Generated by Django 4.2.16 on 2024-10-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('bio', models.TextField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='profile_media/')),
            ],
        ),
    ]
