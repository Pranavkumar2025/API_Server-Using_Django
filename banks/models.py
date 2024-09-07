from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)
    bank_id = models.IntegerField(unique=True)
    # bank_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    


    def __str__(self):
        return self.name

class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)
    ifsc = models.CharField(max_length=11, unique=True)
    branch_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.branch_name} ({self.city})"
