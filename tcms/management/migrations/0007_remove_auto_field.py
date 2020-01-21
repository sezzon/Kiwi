# Generated by Django 3.0.2 on 2020-01-20 16:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('management', '0006_remove_autofield_max_length'),
    ]

    operations = [
        migrations.RenameField(
            model_name='build',
            old_name='build_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='build',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='build',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='classification',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='component',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='component',
            name='initial_owner',
            field=models.ForeignKey(null=True, on_delete=models.deletion.CASCADE,
                                    related_name='initial_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='component',
            name='initial_qa_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.deletion.CASCADE,
                                    related_name='initial_qa_contact', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='priority',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='priority',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='version',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
    ]
