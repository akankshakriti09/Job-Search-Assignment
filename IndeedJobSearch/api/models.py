from djongo import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.title   

    class Meta:
        db_table='api_job'

    