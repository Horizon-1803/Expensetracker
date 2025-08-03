from django.db import models

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0)

    def __str__(self):
        return f" {self.current_balance}"

class TrackingHistory(models.Model):
    # Fixed the choices format - each option should be a tuple of (value, label)
    CREDIT_DEBIT_CHOICES = [
        ('CREDIT', 'Credit'),
        ('DEBIT', 'Debit'),
    ]
    
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    amount = models.FloatField(editable= False)
    expense_type = models.CharField(
        choices=CREDIT_DEBIT_CHOICES,
        max_length=200
    )
    descp = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)  # Removed duplicate field

    def __str__(self) -> str:
        return f"The amount is {self.amount} for {self.descp} expense type is {self.expense_type}"