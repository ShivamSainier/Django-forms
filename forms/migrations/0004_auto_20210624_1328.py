# Generated by Django 3.2.4 on 2021-06-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_alter_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.AddField(
            model_name='book',
            name='covver_image',
            field=models.ImageField(default='image.jpg', upload_to='images'),
        ),
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(default='file.jpg', upload_to='files'),
        ),
    ]
