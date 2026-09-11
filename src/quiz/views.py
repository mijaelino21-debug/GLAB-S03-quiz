from django.shortcuts import render, get_object_or_404, redirect
from .models import Exam
from .forms import QuestionForm, ChoiceFormSet

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'quiz/exam_list.html', {'exams': exams})

def exam_detail(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    return render(request, 'quiz/exam_detail.html', {'exam': exam})

def question_create(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        formset = ChoiceFormSet(request.POST, instance=None)
        
        if form.is_valid() and formset.is_valid():
            # Validate exactly one correct answer
            correct_choices = [
                f.cleaned_data.get('is_correct') 
                for f in formset 
                if f.cleaned_data and not f.cleaned_data.get('DELETE', False)
            ]
            
            if correct_choices.count(True) != 1:
                formset.non_form_errors().append("Debe haber exactamente una opción correcta.")
            else:
                question = form.save(commit=False)
                question.exam = exam
                question.save()
                
                formset.instance = question
                formset.save()
                return redirect('exam_detail', pk=exam.pk)
    else:
        form = QuestionForm()
        formset = ChoiceFormSet(instance=None)
        
    return render(request, 'quiz/question_form.html', {'form': form, 'formset': formset, 'exam': exam})
