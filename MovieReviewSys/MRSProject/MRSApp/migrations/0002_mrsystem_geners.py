# Generated by Django 5.0.7 on 2024-08-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MRSApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mrsystem',
            name='geners',
            field=models.CharField(choices=[('horror', 'HORROR'), ('action', 'ACTION'), ('scifi', 'SCI-FI'), ('comedy', 'COMEDY'), ('thriller', 'THRILLER')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
