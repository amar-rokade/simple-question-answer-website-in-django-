from django.contrib import admin
from ask_question.models import AskQuestion,Answer,AnswerComment,QuetionVote, QuestionComment

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_heading',)
    search_fields = [ 'question_heading',]
    prepopulated_fields = {'slug': ('question_heading',)}
    summernote_fields = ('question_content',)

admin.site.register(AskQuestion, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question','author','post_on')
    search_fields = [ 'question','author']
    summernote_fields = ('answer_text',)

admin.site.register(Answer, AnswerAdmin)

admin.site.register(AnswerComment)

class QuetionVoteAdmin(admin.ModelAdmin):
    list_display = ('question','author','upvote','downvote')
    search_fields = [ 'question','author']

admin.site.register(QuetionVote,QuetionVoteAdmin)


# question comment model register
class QuetionCommentAdmin(admin.ModelAdmin):
    list_display = ('question','author','post_on')
    search_fields = [ 'question','author']

admin.site.register(QuestionComment,QuetionCommentAdmin)