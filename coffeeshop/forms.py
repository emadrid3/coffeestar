from django.forms import ModelForm
from coffeehop.models import departament

class dpto_form(ModelForm):
	class Meta:
		model = departament
		field = ['id_dpto', 'dpto_name']

