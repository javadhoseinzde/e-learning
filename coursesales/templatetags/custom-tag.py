from django import template
from coursesales.models import CourseSales
from django.template.loader import get_template


register = template.Library()

@register.inclusion_tag("learning/homes.html")
def corsesal():
	coursesal = CourseSales.objects.all()
	return {
		"coursesal":coursesal
		}

users_template = get_template("learning/homes.html")

register.inclusion_tag(users_template)(corsesal)

