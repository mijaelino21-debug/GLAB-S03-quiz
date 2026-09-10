from django.db import models

class Exam(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    statement = models.TextField()
    exam = models.ForeignKey(Exam, related_name="questions", on_delete=models.CASCADE)

    def __str__(self):
        return self.statement

class Choice(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)

    def __str__(self):
        return self.text
