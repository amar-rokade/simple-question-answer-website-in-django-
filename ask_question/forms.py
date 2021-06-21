from ask_question.models import AskQuestion, Answer,AnswerComment
from django.forms import ModelForm
from django import forms

class AskQuestionForm(ModelForm):
    class Meta:
        model = AskQuestion
        fields = ('question_heading','question_content',)
        widgets = {
            'question_heading': forms.TextInput(attrs={'rows':2,'autocomplete':"off"}),
            'question_content': forms.Textarea(attrs={'summernote': {'width': '100%', 'height': '500px','require':False}}),
        }


        
class AnswerForm(ModelForm):

    class Meta:
        model = Answer
        fields = ('answer_text',)
        widgets ={
             'answer_text': forms.Textarea(attrs={'summernote': {'width': '100%', 'height': '500px'}}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = AnswerComment
        fields = ('add_comment',)
        widgets = {
            'add_comment': forms.TextInput(attrs={"id":"answer_new_comment",'autocomplete':"off"}),
        }

