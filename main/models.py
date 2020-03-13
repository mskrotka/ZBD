from django.db import models


# Create your models here.
class Wplyw(models.Model):
    category_to_choise = [
        ('Artykuły spożywcze', 'AS'),
        ('Ubrania', 'UB'),
        ('Rachunek', 'RA'),
    ]
    rodzaj_ruchu = [
        ('Wpływ', 'Wpływ'),
        ('Rozchód', 'Rozchód')
    ]
    name = models.CharField(max_length=128)
    flow = models.CharField(max_length=10, choices=rodzaj_ruchu, default='Wybierz')
    how_much = models.DecimalField(max_digits=9999, default=0.00, decimal_places=2)
    category = models.CharField(max_length=18, choices=category_to_choise, default='AS')
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name_z_kategoria()

    def name_z_kategoria(self):
        return f'{self.name} ({self.category})'

    def kategoria1(self):
        return f'{self.category}'
