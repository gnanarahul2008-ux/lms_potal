from django.shortcuts import render
from .forms import QuestionForm
import pandas as pd
import re

df = pd.read_csv('C:/Users/RAHUL/Downloads/LMS_Portal-main/qa/students.csv')

def parse_question(question):
    question = question.lower()
    response = "Sorry, I couldn't understand the question."

    id_match = re.search(r'(\d{4})', question)
    if not id_match:
        return "Please specify a student ID like 1001."

    student_id = int(id_match.group(1))
    student = df[df['id'] == student_id]

    if student.empty:
        return f"No student found with ID {student_id}."

    student = s}'s Science marks: {student.science}"
    elif "social" in question:
        response = f"{student}'s Email: {student.email}"
    elif "email" in question:
        response = f"{student.name}'s Social marks: {student.social}"

    return response

def qa_view(request):
    answer = None
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            answer = parse_question(question)
    else:
        form = QuestionForm()

    return render(request, 'qa/index.html', {'form': form, 'answer': answer})
