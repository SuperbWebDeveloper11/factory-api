from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now =True)

    class Meta:
        abstract = True
        ordering = ['-created']


""" These 3 models are very simple and could be upgraded """


class Workshop(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey('auth.User', related_name="created_workshops", on_delete=models.CASCADE)


class Employee(TimeStampedModel):
    username = models.CharField(max_length=100)
    workshop = models.ForeignKey(Workshop, related_name="employees", on_delete=models.CASCADE)
    created_by = models.ForeignKey('auth.User', related_name="created_employees", on_delete=models.CASCADE)


class Task(TimeStampedModel):
    name = models.CharField(max_length=100)
    workshop = models.ForeignKey(Workshop, related_name="tasks", on_delete=models.CASCADE)
    created_by = models.ForeignKey('auth.User', related_name="created_tasks", on_delete=models.CASCADE)


