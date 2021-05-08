from django.db import models

# Create your models here.
class Jawaban(models.Model):
    # id_pertanyaan = models.BigAutoField(primary_key=True)
    jawaban = models.CharField(max_length=255)

    def __str__(self):
        return str(self.jawaban)