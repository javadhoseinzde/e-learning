from django.forms import ModelForm
from .models import TklifAnswer

class AnswerForms(ModelForm):
	class Meta:
		model = TklifAnswer
		fields = ["ansser"]
