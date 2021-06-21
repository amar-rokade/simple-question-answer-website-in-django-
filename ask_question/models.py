
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save
from quans.util import unique_slug_generator_question

# Create your models here.
class AskQuestion(models.Model):
    question_heading = models.CharField(max_length=200)
    slug = models.SlugField(blank=True,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='questions')
    updated_on = models.DateTimeField(blank=True,null=True)
    question_content = models.TextField()
    post_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-post_on']
 
    def __str__(self):
        return self.question_heading

#question comment model 
class QuestionComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    question = models.ForeignKey(AskQuestion,related_name="comments",on_delete=models.CASCADE)
    add_comment = models.CharField(max_length=500)
    post_on = models.DateTimeField(blank=True,null=True,auto_now_add=timezone.now())

    class Meta:
        ordering = ['post_on']

    def __str__(self):
        return str(self.author)

#question voting model
class QuetionVote(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    question = models.ForeignKey(AskQuestion,on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)
    vote_on = models.DateTimeField(blank=True,null=True,auto_now_add=timezone.now())

    class Meta:
        unique_together = ('question', 'author',)

    def __str__(self):
        return str(self.author)

class Answer(models.Model):
    question = models.ForeignKey(AskQuestion,on_delete=models.CASCADE,related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    answer_text = models.TextField()
    post_on = models.DateTimeField(auto_now_add=timezone.now)

    class Meta:
        ordering = ['-post_on']
    
    def __str__(self):

        return self.question.question_heading

class AnswerComment(models.Model):
    ans = models.ForeignKey(Answer,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    add_comment = models.CharField(max_length=500)
    post_on = models.DateTimeField(auto_now_add=timezone.now)
    class Meta:
        ordering = ['-post_on']

#question voting model
class AnswerVote(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)
    vote_on = models.DateTimeField(blank=True,null=True,auto_now_add=timezone.now())
    class Meta:
        unique_together = ('answer', 'author',)

    def __str__(self):
        return str(self.author)

def pre_save_receiver(sender,instance,*arg,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_question(instance)

pre_save.connect(pre_save_receiver, sender = AskQuestion)

