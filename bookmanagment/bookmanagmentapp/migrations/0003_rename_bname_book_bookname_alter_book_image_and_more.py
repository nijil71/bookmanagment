# Generated by Django 4.0.4 on 2023-03-03 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanagmentapp', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='bname',
            new_name='bookname',
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='bookmanagmentapp/static'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(upload_to='bookmanagmentapp/static'),
        ),
    ]
