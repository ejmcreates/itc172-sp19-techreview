# Generated by Django 2.2 on 2019-04-18 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=255)),
                ('productprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productentrydate', models.DateField()),
                ('producturl', models.URLField(blank=True, null=True)),
                ('productdescription', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='TechType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techtypename', models.CharField(max_length=255)),
                ('techdescription', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'techtypes',
                'db_table': 'techtype',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewtitle', models.CharField(max_length=255)),
                ('reviewdate', models.DateField()),
                ('rating', models.SmallIntegerField()),
                ('reviewtext', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='techreviewapp.Product')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'reviews',
                'db_table': 'review',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='producttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='techreviewapp.TechType'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
