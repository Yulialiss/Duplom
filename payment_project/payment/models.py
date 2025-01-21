from django.db import models

class Transaction(models.Model):
    payment_method = models.CharField(max_length=20)
    card_number = models.CharField(max_length=16)
    card_holder = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.amount} {self.payment_method}"
