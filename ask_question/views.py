from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from ask_question.forms import AskQuestionForm, AnswerForm,CommentForm
from .models import AskQuestion,Answer, AnswerComment, AnswerVote , QuetionVote, QuestionComment
from django.views import generic
from django.contrib.auth.decorators import login_required
import json
from django.core.files.base import ContentFile    
from django.template.loader import render_to_string
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# answers comment ajax request
def AnswerNewComment(request):
    if request.method == "POST":
        answer = Answer.objects.get(id=request.POST.get('answer_id'))
        new_comment = request.POST.get("comment")
        comment = AnswerComment.objects.create(author = request.user, add_comment = new_comment,ans= answer )
        rendered_html = render_to_string('ask_question/ask_comment_list.html',{"post":answer})
        comment_count = answer.comments.all().count()
        
        print(comment_count)
        return JsonResponse({'html':rendered_html,'count':comment_count},safe=False)
    else :
        answer = Answer.objects.get(id=request.GET.get('answer_id'))
        rendered_html = render_to_string('ask_question/ask_comment_list.html',{"post":answer})
        return JsonResponse(rendered_html,safe=False)

       

        
@login_required
def ask_question(request):
    post = False
    if request.method == "POST":
        form = AskQuestionForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user 
            blog.save()
            post = True
            return render(request,'ask_question/ask_question.html',{'form':form,
                                                             "post":post,
                                                             })
    else:
        form = AskQuestionForm()
    return render(request,'ask_question/ask_question.html',{'form':form,
                                                             "post":post,
                                                             })
    


def QuestionsListView(request):
    question_list = AskQuestion.objects.all().order_by('-post_on')
    return render(request,'ask_question/ask_mainpage.html',{"askquestion_list":question_list})


def MyQuestionsListView(request):
    question_list = AskQuestion.objects.filter(author=request.user).order_by('-post_on')
    return render(request,'ask_question/ask_mainpage.html',{"askquestion_list":question_list,})
                                                             
@login_required
def MyAnswerListView(request):
    answer_list = Answer.objects.filter(author=request.user).order_by('-post_on')
    return render(request,'ask_question/my_answers.html',{"answer_list":answer_list
                                                            })
@login_required
def AnswerView(request,pk,slug):
    question = get_object_or_404(AskQuestion,pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST,request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user 
            answer.save()
            return redirect('ask_questions:answers',pk,slug)
    else:
        form = AnswerForm()
    return render(request,'ask_question/answers.html', {'ans_form': form,
                                                    'question':question,
                                                       })


#question upovote view
@login_required
def Question_VoteView(request):
    user = request.user
    question_id = request.POST.get('question_id')
    vote_type = request.POST.get('vote_type') #vote type upvote or downvote
    question = AskQuestion.objects.get(id=question_id)
    #checking if user alredy have object or not else create
    user_voted, created = QuetionVote.objects.get_or_create(author=user,question=question)
    question_vote = QuetionVote.objects.filter(id=user_voted.id)
    if vote_type == 'upvote':
        if not created :
            if user_voted.upvote == True :
                question_vote.update(upvote=False)
                is_user_voted = False
            else :
                question_vote.update(upvote=True,downvote=False)
                is_user_voted = True
        else :
            question_vote.update(upvote=True)
            is_user_voted = True
    elif vote_type == 'downvote' :
        if not created :
            if user_voted.downvote == True :
                question_vote.update(downvote=False)
                is_user_voted = False
            else :
                question_vote.update(downvote=True,upvote=False)
                is_user_voted = True
        else :
            question_vote.update(downvote=True)
            is_user_voted = True

    upvote_count = QuetionVote.objects.filter(question=question,upvote=True).count()
    downvote_count = QuetionVote.objects.filter(question=question,downvote=True).count()

    data = {'upvote_count':upvote_count,'downvote_count':downvote_count, 'is_user_voted':is_user_voted,}
    return HttpResponse(json.dumps(data), content_type='application/json')

@login_required
def Question_NewComment_View(request):
    if request.method == "POST":
        new_comment = request.POST.get("comment")
        question = AskQuestion.objects.get(id=request.POST.get('question_id'))
        comment = QuestionComment.objects.create(author = request.user, add_comment = new_comment,question= question )
        rendered_html = render_to_string('ask_question/ask_comment_list.html',{"post":question})
        comment_count = question.comments.all().count()
        return JsonResponse({'html':rendered_html,'count':comment_count},safe=False)
    else :
        print(request.POST.get('question_id'))
        question = AskQuestion.objects.get(id=request.GET.get('question_id'))
        rendered_html = render_to_string('ask_question/ask_comment_list.html',{"post":question})
        return JsonResponse(rendered_html,safe=False)



#answers upovote view 
@login_required
def Answer_VoteView(request):
    user = request.user
    answer_id = request.POST.get('answer_id')
    vote_type = request.POST.get('vote_type') #vote type upvote or downvote
    answer = Answer.objects.get(id=answer_id)
    #checking if user alredy have object or not else create
    user_voted, created = AnswerVote.objects.get_or_create(author=user,answer=answer)
    answer_vote = AnswerVote.objects.filter(id=user_voted.id)
    if vote_type == 'upvote':
        if not created :
            if user_voted.upvote == True :
                answer_vote.update(upvote=False)
                is_user_voted = False
            else :
                answer_vote.update(upvote=True,downvote=False)
                is_user_voted = True
        else :
            answer_vote.update(upvote=True)
            is_user_voted = True
    elif vote_type == 'downvote' :
        if not created :
            if user_voted.downvote == True :
                answer_vote.update(downvote=False)
                is_user_voted = False
            else :
                answer_vote.update(downvote=True,upvote=False)
                is_user_voted = True
        else :
            answer_vote.update(downvote=True)
            is_user_voted = True

    upvote_count = AnswerVote.objects.filter(answer=answer,upvote=True).count()
    downvote_count = AnswerVote.objects.filter(answer=answer,downvote=True).count()

    data = {'upvote_count':upvote_count,'downvote_count':downvote_count, 'is_user_voted':is_user_voted,}
    return HttpResponse(json.dumps(data), content_type='application/json')