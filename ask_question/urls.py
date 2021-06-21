from django.urls import path
from . import views
  
app_name = 'ask_questions'
urlpatterns =[
    #submitting comment ajax
    path('answer/new_comment/',views.AnswerNewComment,name="answer_new_comment"),
    # question_upvotessss
    path('question/upvote/',views.Question_VoteView,name='question_vote'),
    # answer_upvotessss
    path('answer/upvote/',views.Answer_VoteView,name='answer_vote'),
    #question new comment submit url 
    path('question/new_comment/',views.Question_NewComment_View,name='question_new_comment'),
    
    path('ask/',views.ask_question,name='ask'),
    #questions list
    path('',views.QuestionsListView,name='question_list'),
    #my asked quetion url
    path('my_asked_quetions/',views.MyQuestionsListView,name='my_question_list'),
    path('my_answered_quetions/',views.MyAnswerListView,name='my_answer_list'),
    path('<int:pk>/answers/<slug:slug>/',views.AnswerView,name='answers'),
   
]