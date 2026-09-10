from django import forms
from django.forms import inlineformset_factory
from .models import Exam, Question, Choice

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['statement']

ChoiceFormSet = inlineformset_factory(
    Question,
    Choice,
    fields=['text', 'is_correct'],
    extra=4,
    can_delete=True
)
