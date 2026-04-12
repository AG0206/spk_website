# Generated manually to update models with new fields

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        # Add new fields to Event model
        migrations.AddField(
            model_name='event',
            name='badge',
            field=models.CharField(choices=[('Free', 'Free'), ('Global', 'Global'), ('Workshop', 'Workshop'), ('Networking', 'Networking'), ('Certification', 'Certification'), ('Annual', 'Annual'), ('Special', 'Special')], default='Free', max_length=20),
        ),
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='date_label',
            field=models.CharField(default='Ongoing 2025', help_text='e.g. "Ongoing 2025", "12 April 2025", "Annual 2025"', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event',
            name='is_featured',
            field=models.BooleanField(default=False, help_text='Highlighted with gold border'),
        ),
        migrations.AddField(
            model_name='event',
            name='link_label',
            field=models.CharField(default='Register Interest', max_length=60),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Nagpur, MH', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Lower = shown first'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),

        # Add new fields to Gallery model
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.CharField(choices=[('events', 'Events'), ('training', 'Training'), ('team', 'Team')], default='events', max_length=20),
        ),
        migrations.AddField(
            model_name='gallery',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Lower = shown first'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='size',
            field=models.CharField(choices=[('normal', 'Normal (1×1)'), ('large', 'Large (2×1 wide)'), ('tall', 'Tall (1×2 tall)')], default='normal', help_text='Controls the grid cell size', max_length=10),
        ),

        # Add new fields to Contact model
        migrations.AddField(
            model_name='contact',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
