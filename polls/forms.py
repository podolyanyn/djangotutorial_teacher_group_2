from django import forms

class QuestionForm(forms.Form):
    question_text  = forms.CharField(label='Your question', max_length=200) #, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pub_date = forms.DateTimeField(label = 'date published', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

