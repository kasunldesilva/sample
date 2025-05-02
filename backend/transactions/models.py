from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('Expense', 'Expense'),
        ('Income', 'Income'),
    ]

    TAG_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Bills', 'Bills'),
        ('Shopping', 'Shopping'),
        ('Health', 'Health'),
        ('Travel', 'Travel'),
        ('Salary', 'Salary'),
    ]

    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICES)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.transaction_type} - {self.description}'
