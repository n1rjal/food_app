# Generated by Django 4.0.1 on 2022-02-01 02:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_recomender', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodproduct',
            name='recepie',
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='recipe',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
