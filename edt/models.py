from django.db import models

class Day(models.Model):
    day = models.CharField(max_length=30)

    def __str__(self):
        return self.day

class Hour(models.Model):
    hour = models.CharField(max_length=2)

    def __str__(self):
        return self.hour

class To(models.Model):
    to = models.CharField(max_length=2)

    def __str__(self):
        return self.to

class Professor(models.Model):
    professor = models.CharField(max_length=200)

    def __str__(self):
        return self.professor

class Subject(models.Model):
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject

class Classroom(models.Model):
    classroom = models.CharField(max_length=70)

    def __str__(self):
        return self.classroom

class ProfessorAvailability(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    available = models.ForeignKey(Day, on_delete=models.CASCADE)
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE)
    to = models.ForeignKey(To, on_delete=models.CASCADE, null=False, blank=False)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.professor.professor} - {self.subject.subject} ({self.available.day}, {self.hour.hour}H)"
        # return self.professor