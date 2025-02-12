# Generated by Django 4.2 on 2024-01-09 12:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0003_delete_book_uploadmodel_book_file_uploadmodel_isbn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookUploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('cover_page', models.ImageField(upload_to='')),
                ('Book_file', models.FileField(upload_to='')),
                ('author_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(5)])),
                ('published_date', models.DateField()),
                ('file_size', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Books',
                'ordering': ('price',),
            },
        ),
        migrations.DeleteModel(
            name='AccountModel',
        ),
        migrations.DeleteModel(
            name='UploadModel',
        ),
    ]
