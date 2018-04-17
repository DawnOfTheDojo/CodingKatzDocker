# Generated by Django 2.0 on 2018-02-19 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LogReg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='note_author', to='LogReg.userDB')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='note_recipient', to='LogReg.userDB')),
            ],
        ),
    ]