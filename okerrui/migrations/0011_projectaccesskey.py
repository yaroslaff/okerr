# Generated by Django 2.2.1 on 2019-12-03 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okerrui', '0010_auto_20191121_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectAccessKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('trans_last_update', models.DateTimeField(default=None, null=True)),
                ('trans_last_sync', models.DateTimeField(default=None, null=True)),
                ('rid', models.CharField(db_index=True, default='', max_length=100)),
                ('ci', models.IntegerField(db_index=True, default=0)),
                ('key', models.CharField(max_length=200)),
                ('remark', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
