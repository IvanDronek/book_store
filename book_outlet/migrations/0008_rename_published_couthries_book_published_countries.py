# Generated by Django 4.2.2 on 2023-07-10 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0007_country_alter_address_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='published_couthries',
            new_name='published_countries',
        ),
    ]
