# Generated by Django 3.2.9 on 2021-12-06 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_bundledetail_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundledetail',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
