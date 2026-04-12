from django.db import models


# ─────────────────────────────────────────────────────────────
# EVENT MODEL
# ─────────────────────────────────────────────────────────────
class Event(models.Model):
    BADGE_CHOICES = [
        ('Free',          'Free'),
        ('Global',        'Global'),
        ('Workshop',      'Workshop'),
        ('Networking',    'Networking'),
        ('Certification', 'Certification'),
        ('Annual',        'Annual'),
        ('Special',       'Special'),
    ]

    title       = models.CharField(max_length=200)
    description = models.TextField()
    date_label  = models.CharField(
        max_length=100,
        default='Ongoing 2025',
        help_text='e.g. "Ongoing 2025", "12 April 2025", "Annual 2025"'
    )
    location    = models.CharField(max_length=200, default='Nagpur, MH')
    badge       = models.CharField(max_length=20, choices=BADGE_CHOICES, default='Free')
    image       = models.ImageField(upload_to='events/', blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text='Highlighted with gold border')
    link_label  = models.CharField(max_length=60, default='Register Interest')
    order       = models.PositiveIntegerField(default=0, help_text='Lower = shown first')
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title


# ─────────────────────────────────────────────────────────────
# GALLERY MODEL
# ─────────────────────────────────────────────────────────────
class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('events',   'Events'),
        ('training', 'Training'),
        ('team',     'Team'),
    ]

    SIZE_CHOICES = [
        ('normal', 'Normal (1×1)'),
        ('large',  'Large (2×1 wide)'),
        ('tall',   'Tall (1×2 tall)'),
    ]

    title    = models.CharField(max_length=200)
    image    = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='events')
    size     = models.CharField(max_length=10, choices=SIZE_CHOICES, default='normal',
                                help_text='Controls the grid cell size')
    order    = models.PositiveIntegerField(default=0, help_text='Lower = shown first')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title


# ─────────────────────────────────────────────────────────────
# CONTACT MODEL
# ─────────────────────────────────────────────────────────────
class Contact(models.Model):
    name       = models.CharField(max_length=100)
    email      = models.EmailField()
    phone      = models.CharField(max_length=20, blank=True)
    subject    = models.CharField(max_length=200, blank=True)
    message    = models.TextField()
    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} — {self.subject or 'No subject'} ({self.created_at.strftime('%d %b %Y')})"
