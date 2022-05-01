# Generated by Django 3.2.8 on 2021-10-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistedEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Blacklisted Email',
                'verbose_name_plural': 'Blacklisted Emails',
            },
        ),
        migrations.CreateModel(
            name='SNSNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headers', models.JSONField(default=dict)),
                ('data', models.JSONField(default=dict)),
                ('added_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('state', models.SmallIntegerField(choices=[(0, 'New'), (1, 'Processed'), (2, 'Failed')], db_index=True, default=0)),
                ('last_processed_dt', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('processing_error', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'SNS Notification',
                'verbose_name_plural': 'SNS Notifications',
            },
        ),
    ]
