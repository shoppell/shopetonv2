# Generated by Django 4.0.2 on 2022-03-28 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blogmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(upload_to='blogs_image'),
        ),
    ]