# Generated by Django 4.2.1 on 2023-06-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_rename_publication_date_book_date_of_dirth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='PhoneNumber',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='RollNumber',
            field=models.CharField(max_length=50, null=True),
        ),
    ]