from django.db import models

class TrainLine(models.Model):
    line_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='ACTIVE')

    def __str__(self):
        return f'{self.line_name} [{self.status}]'

class TrainStop(models.Model):
    stop_name = models.CharField(max_length=200)
    stop_line = models.ForeignKey(TrainLine, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.stop_name} [{self.stop_line}]'
