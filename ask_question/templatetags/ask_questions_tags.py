from django import template
register = template.Library()
from ask_question.models import AnswerVote,QuetionVote

@register.simple_tag
def answer_upvote(answer,user):
    if user.is_authenticated :
        upvote = AnswerVote.objects.filter(answer=answer,upvote=True).count()
        downvote = AnswerVote.objects.filter(answer = answer,downvote=True).count()
        is_user_upvoted = AnswerVote.objects.filter(answer=answer,author=user,upvote=True).exists()
        is_user_downvoted = AnswerVote.objects.filter(answer=answer,author=user,downvote=True).exists()
        return upvote, downvote, is_user_upvoted, is_user_downvoted

@register.simple_tag
def question_upvote(question,user):
    if user.is_authenticated :
        upvote = QuetionVote.objects.filter(question=question,upvote=True).count()
        downvote = QuetionVote.objects.filter(question = question,downvote=True).count()
        is_user_upvoted = QuetionVote.objects.filter(question=question,author=user,upvote=True).exists()
        is_user_downvoted = QuetionVote.objects.filter(question=question,author=user,downvote=True).exists()
        return upvote, downvote, is_user_upvoted, is_user_downvoted


    

