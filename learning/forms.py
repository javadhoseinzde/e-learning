from dataclasses import fields
from django.forms import ModelForm
from .models import TklifAnswer, QuizAnswer

class AnswerForms(ModelForm):
	class Meta:
		model = TklifAnswer
		fields = ["ansser"]

class QuizAnswerForm(ModelForm):
	class Meta:
		model = QuizAnswer
		fields = ['ansser']
