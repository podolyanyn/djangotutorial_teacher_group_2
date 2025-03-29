from django import forms

class QuestionForm(forms.Form):
    question_text  = forms.CharField(label='Your question', max_length=200)
    pub_date = forms.DateTimeField(label = 'date published')

