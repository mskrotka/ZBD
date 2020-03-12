from django.db import models


# Create your models here.
class Wplyw(models.Model):
    category_to_choise = [
        ('AS', 'AS'),
        ('UB', 'UB'),
        ('RA', 'RA'),
    ]
    name = models.CharField(max_length=128)
    outflow = models.CharField(max_length=128, default='')
    inflow = models.CharField(max_length=128, default='')
    category = models.CharField(max_length=2, choices=category_to_choise, default='AS')
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name_z_data_kreowanaia()

    def name_z_data_kreowanaia(self):
        return f'{self.name} ({self.created_at})'


