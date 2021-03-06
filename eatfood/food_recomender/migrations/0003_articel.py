# Generated by Django 4.0.1 on 2022-02-01 09:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_recomender', '0002_remove_foodproduct_recepie_foodproduct_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
