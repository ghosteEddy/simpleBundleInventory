# Generated by Django 3.2.9 on 2021-12-06 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_bundledetail_bundleid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundledetail',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.item'),
        ),
    ]
