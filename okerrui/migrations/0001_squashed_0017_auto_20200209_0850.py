# Generated by Django 3.0.2 on 2020-02-14 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('okerrui', '0001_initial'), ('okerrui', '0002_auto_20190526_1240'), ('okerrui', '0003_auto_20191023_1531'), ('okerrui', '0004_auto_20191023_1535'), ('okerrui', '0005_auto_20191023_1537'), ('okerrui', '0006_auto_20191023_1541'), ('okerrui', '0007_auto_20191024_1625'), ('okerrui', '0008_auto_20191024_1644'), ('okerrui', '0009_auto_20191024_1727'), ('okerrui', '0010_auto_20191121_1301'), ('okerrui', '0011_projectaccesskey'), ('okerrui', '0012_auto_20191203_1306'), ('okerrui', '0013_auto_20191209_1318'), ('okerrui', '0014_alertrecord_reduction'), ('okerrui', '0015_auto_20191223_1406'), ('okerrui', '0016_auto_20191223_1410'), ('okerrui', '0017_auto_20200209_0850')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('codename', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('enabled', models.BooleanField(default=True)),
                ('remote', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('refillperiod', models.IntegerField(default=2592000)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('trans_last_update', models.DateTimeField(default=None, null=True)),
                ('trans_last_sync', models.DateTimeField(default=None, null=True)),
                ('rid', models.CharField(db_index=True, default='', max_length=100)),
                ('ci', models.IntegerField(db_index=True, default=0)),
                ('sendalert', models.BooleanField(default=True)),
                ('sendsummary', models.BooleanField(default=True)),
                ('nextsummary', models.DateTimeField(default=django.utils.timezone.now)),
                ('sumtime', models.IntegerField(default=0)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('patrolled', models.DateTimeField(auto_now_add=True)),
                ('telegram_name', models.CharField(default='', max_length=100, null=True)),
                ('telegram_chat_id', models.BigIntegerField(default=None, null=True)),
                ('last_motd', models.CharField(default=None, max_length=100, null=True)),
                ('training_stage', models.CharField(default=None, max_length=100, null=True)),
                ('partner_name', models.CharField(default=None, max_length=100, null=True)),
                ('partner_id', models.CharField(default=None, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('trans_last_update', models.DateTimeField(default=None, null=True)),
                ('trans_last_sync', models.DateTimeField(default=None, null=True)),
                ('rid', models.CharField(db_index=True, default='', max_length=100)),
                ('ci', models.IntegerField(db_index=True, default=0)),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('jkeys', models.TextField(default='{}')),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('limited', models.BooleanField(default=False)),
                ('partner_access', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StatusPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('public', models.BooleanField(default=False)),
                ('can_subscribe', models.BooleanField(default=False)),
                ('desc', models.TextField(default='')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Project')),
            ],
        ),
        migrations.CreateModel(
            name='SystemVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Throttle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('priv', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expires', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('trans_last_update', models.DateTimeField(default=None, null=True)),
                ('trans_last_sync', models.DateTimeField(default=None, null=True)),
                ('rid', models.CharField(db_index=True, default='', max_length=100)),
                ('ci', models.IntegerField(db_index=True, default=0)),
                ('name', models.CharField(max_length=200)),
                ('period', models.CharField(default='1h', max_length=200)),
                ('patience', models.CharField(default='300s', max_length=200)),
                ('wipe', models.IntegerField(default=5184000)),
                ('autocreate', models.BooleanField(default=True)),
                ('secret', models.CharField(blank=True, default='', max_length=200)),
                ('smtpupdate', models.BooleanField(default=True)),
                ('httpupdate', models.BooleanField(default=True)),
                ('retry_schedule', models.CharField(blank=True, default='', max_length=200)),
                ('recovery_retry_schedule', models.CharField(blank=True, default='', max_length=200)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('url_statuschange', models.CharField(default='', max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Project')),
                ('reduction', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Policies',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('trans_last_update', models.DateTimeField(default=None, null=True)),
                ('trans_last_sync', models.DateTimeField(default=None, null=True)),
                ('rid', models.CharField(db_index=True, default='', max_length=100)),
                ('ci', models.IntegerField(db_index=True, default=0)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('desc', models.TextField(blank=True)),
                ('_status', models.CharField(db_column='status', default='OK', max_length=20)),
                ('prevstatus', models.CharField(blank=True, max_length=20)),
                ('details', models.CharField(blank=True, max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('mtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('maintenance', models.DateTimeField(default=None, null=True)),
                ('dead', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('silent', models.BooleanField(default=False)),
                ('problem', models.BooleanField(default=False)),
                ('scheduled', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('expected', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('lockpid', models.IntegerField(null=True)),
                ('lockat', models.DateTimeField(blank=True, null=True)),
                ('keypath', models.CharField(default=None, max_length=255, null=True)),
                ('origkeypath', models.CharField(default=None, max_length=255, null=True)),
                ('retry', models.IntegerField(default=0, null=True)),
                ('last_fail_machine', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('jtags', models.CharField(default='[]', max_length=2000)),
                ('jiargs', models.CharField(default='{}', max_length=2000)),
                ('jcheckargs', models.CharField(default='{}', max_length=2000)),
                ('location', models.CharField(db_index=True, default='', max_length=200)),
                ('cm', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='okerrui.CheckMethod')),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='okerrui.Policy')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Project')),
            ],
            options={
                'ordering': ['name'],
                'index_together': {('project', 'name')},
                'unique_together': {('name', 'project')},
            },
        ),
        migrations.CreateModel(
            name='BonusCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('prefix', models.CharField(default='', max_length=200)),
                ('re', models.CharField(default=None, max_length=200, null=True, unique=True)),
                ('enabled', models.BooleanField(default=True)),
                ('time', models.IntegerField(blank=True, default=2592000)),
                ('personal', models.BooleanField(default=False)),
                ('add', models.BooleanField(default=False)),
                ('expires', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('reactivation', models.IntegerField(blank=True, default=None, null=True)),
                ('limited', models.BooleanField(default=True)),
                ('total', models.IntegerField(default=100)),
                ('left', models.IntegerField(default=100)),
                ('repeatable', models.BooleanField(default=False)),
                ('repeat_days', models.IntegerField(default=0)),
                ('verifyurl', models.CharField(blank=True, default='', max_length=200)),
                ('secret', models.CharField(blank=True, default='', max_length=200)),
                ('checktype', models.CharField(blank=True, default='', max_length=200)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Group')),
            ],
        ),
        migrations.CreateModel(
            name='DynDNSRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(default=None, max_length=200)),
                ('hostname', models.CharField(default='www', max_length=200)),
                ('domain', models.CharField(default=None, max_length=200, null=True)),
                ('login', models.CharField(default=None, max_length=200, null=True)),
                ('secret', models.CharField(default=None, max_length=200, null=True)),
                ('curvalue', models.CharField(default=None, max_length=200, null=True)),
                ('curpriority', models.IntegerField(default=100)),
                ('push', models.BooleanField(db_index=True, default=False)),
                ('last_try', models.DateTimeField(default=django.utils.timezone.now)),
                ('changed', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.TextField(default=None, null=True)),
                ('cache', models.TextField(default='')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Project')),
                ('nfails', models.IntegerField(default=0)),
                ('scheduled', models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PolicySubnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subnet', models.CharField(max_length=200)),
                ('remark', models.CharField(max_length=200)),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Policy')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('granted', models.DateTimeField(default=django.utils.timezone.now)),
                ('expires', models.DateTimeField(blank=True, null=True)),
                ('refilled', models.DateTimeField(default=django.utils.timezone.now)),
                ('rid', models.CharField(db_index=True, default='', max_length=100)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Group')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileArg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.IntegerField()),
                ('expires', models.DateTimeField(null=True)),
                ('visible', models.BooleanField(default=True)),
                ('rid', models.CharField(db_index=True, default='', max_length=100)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='okerrui.Group')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CheckArg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('argname', models.CharField(max_length=200)),
                ('textname', models.CharField(default='', max_length=200)),
                ('desc', models.TextField(blank=True, default='')),
                ('default', models.CharField(blank=True, default='', max_length=200)),
                ('cm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.CheckMethod')),
            ],
        ),
        migrations.CreateModel(
            name='DynDNSRecordValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=100)),
                ('value', models.CharField(max_length=200)),
                ('ddr', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='okerrui.DynDNSRecord')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Indicator')),
            ],
        ),
        migrations.CreateModel(
            name='GroupArg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Group')),
            ],
        ),
        migrations.CreateModel(
            name='IArg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('valtype', models.CharField(max_length=1)),
                ('indicator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='okerrui.Indicator')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('oldstate', models.CharField(max_length=200, null=True)),
                ('newstate', models.CharField(max_length=200)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Indicator')),
            ],
        ),
        migrations.CreateModel(
            name='LogRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadname', models.CharField(max_length=200, null=True)),
                ('typecode', models.IntegerField(db_index=True, default=1)),
                ('message', models.CharField(max_length=10000)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('indicator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='okerrui.Indicator')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expires', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('secret', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, null=True)),
                ('total', models.IntegerField(null=True)),
                ('left', models.IntegerField(null=True)),
                ('rid', models.CharField(db_index=True, default='', max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=200)),
                ('iadmin', models.BooleanField(default=False)),
                ('tadmin', models.BooleanField(default=False)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('rid', models.CharField(db_index=True, default='', max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTextID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textid', models.CharField(max_length=200, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Project')),
            ],
        ),
        migrations.CreateModel(
            name='StatusBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(default='')),
                ('status_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.StatusPage')),
            ],
        ),
        migrations.CreateModel(
            name='StatusIndicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.BooleanField(default=False)),
                ('weight', models.IntegerField(default=1000)),
                ('title', models.CharField(max_length=200)),
                ('chapter', models.CharField(default='', max_length=200)),
                ('desc', models.TextField(default='')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Indicator')),
                ('status_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.StatusPage')),
            ],
        ),
        migrations.CreateModel(
            name='StatusSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.StatusPage')),
            ],
        ),
        migrations.CreateModel(
            name='BonusActivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default=None, max_length=200, null=True)),
                ('activated', models.DateTimeField(auto_now_add=True)),
                ('reactivation', models.DateTimeField(default=None, null=True)),
                ('expiration', models.DateTimeField(default=None, null=True)),
                ('BonusCode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='okerrui.BonusCode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAccessKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('remark', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okerrui.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AlertRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=10000)),
                ('proto', models.CharField(default='mail', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('indicator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='okerrui.Indicator')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reduction', models.CharField(max_length=200, null=True)),
                ('release_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
