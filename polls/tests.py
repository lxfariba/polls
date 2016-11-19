from django.test import TestCase
from django.utils import timezone 
from .models import Question 
from django.urls import revers


import datetime


class QuestionMethodTests(TestCase):

	def test_was_published_recently_with_old_question(self):
		time = timezone.now() -  datetime.timedelta(days=30)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)


	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours = 1)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)	


	def create_question (question_text, days):
	
		time = timezone.now() + datetime.timedelta(days=days)
		return Question.objects.create(question_text=question_text, pub_date=time)	
