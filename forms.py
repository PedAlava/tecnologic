from wtforms import Form

from wtforms import StringField
from wtforms import HiddenField

from wtforms import validators

def length_honeypot(form,field):
	if len(field.data) > 0:
		raise validators.ValidationError('El campo deberia estar vacio')
class CommentForm(Form):
	input_message = StringField('input_message',[validators.length(min=1)])

	honeypot = HiddenField('',[length_honeypot])
		