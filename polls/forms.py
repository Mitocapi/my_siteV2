from django import forms
from django.shortcuts import get_object_or_404
from .models import *

class SearchForm(forms.Form):

    CHOICE_LIST = [("Question", "Search in Questions"),
                   ("Choices", "Search in Choices")]

    search_string = forms.CharField(label="Search String", max_length=100,
                                    min_length=3, required=True)
    search_where = forms.ChoiceField(label="Search Where?", required=True,
                                     choices=CHOICE_LIST)



class VoteForm(forms.Form):

    answer = forms.ModelChoiceField(queryset=None,required=True,label="Select your answer!! ò.O")

    def __init__(self,pk,*args,**kwargs):
        super().__init__(*args,**kwargs)
        q = get_object_or_404(Question, pk=pk)
        self.fields['answer'].queryset = q.choices.all()



class CreateQuestionForm(forms.ModelForm):

    description = "Create a Question!"

    def clean(self):
        if (len(self.cleaned_data["question_text"])<5):
            self.add_error("question_text", "Error: question text must be at least 5 char long")
        return self.cleaned_data

    class Meta:
        model = Question
        fields = "__all__"
        widgets = {
            'pub_date' : forms.DateInput(format=('%d/%m/%y'), attrs={'class':'form-control','placeholder':'select a date', 'type':'date'})
        }

class CreateChoiceForm(forms.ModelForm):
    description = "Create choice question"

    def clean(self):
        q= get_object_or_404(Question,pk=self.cleaned_data["question"].id)
        print("anche inizio form fa la sua parte")
        choices = q.choices.all()
        choices_false = choices.filter(is_correct=False)

        if(choices.count()==4):
            self.add_error("question", "Error: question already has 4 options")
        elif(choices.count()==3):
            if choices_false.count()==3 and self.cleaned_data["is_correct"]==False:
                self.add_error("is_correct", "Error: only one correct")

        if(choices.filter(is_correct=True).count()==1 and self.cleaned_data["is_correct"]==True):
            self.add_error("is_correct", "Error: This question already has a correct answer")

        print("anche il form fa la sua parte")
        return self.cleaned_data


    class Meta:
        model = Choice
        fields = "__all__"


class QuestionCrispyForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('__all__')