from django.db import models

PHONE_MODELS = (
    ('Iphone X', 'Iphone X'),
    ('Iphone 15 pro', 'Iphone 15 pro'),
    ('Samsung Galaxy A33', 'Samsung Galaxy A33'),
    ('Xiaomi T 13 PRO', 'Xiaomi T13 PRO')
)

PHONE_MEMORIES = (
    ('128gb', '128gb'),
    ('256gb', '256gb'),
    ('512gb', '512gb')
)

PHONE_COLORS = (
    ('Black', 'Black'),
    ('White', 'White'),
    ('Blue', 'Blue'),
    ('Gold', 'Gold')
)

class Default(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Phone(Default):
    model = models.CharField(max_length=30, choices=PHONE_MODELS)
    slug = models.SlugField(unique=False)
    memory = models.CharField(max_length=15, choices=PHONE_MEMORIES)
    color = models.CharField(max_length=20, choices=PHONE_COLORS)
    status = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='media/picture', blank=True, null=True)

    def __str__(self):
        return self.model

class Owner(models.Model):
    phone = models.ForeignKey(Phone,
                              on_delete=models.CASCADE,
                              related_name='phones')
    phone_models = models.CharField(max_length=15, choices=PHONE_MEMORIES)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='media/owners')

    def __str__(self):
        return f"{self.phone}"
