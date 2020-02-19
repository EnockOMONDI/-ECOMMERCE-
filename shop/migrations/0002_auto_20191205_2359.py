# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-12-05 23:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shop.Category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='shop.SubCategory')),
            ],
            options={
                'verbose_name': 'minibcategory',
                'verbose_name_plural': 'minicategories',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='minicategory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.MiniCategory'),
            preserve_default=False,
        ),
    ]