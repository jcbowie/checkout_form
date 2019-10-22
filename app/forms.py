from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# creating classes to link to the HTML
class CheckOut(FlaskForm):
    task_id = StringField('TaskID', validators=[DataRequired()])
    item_id = StringField('Item ID', validators=[DataRequired()])
    submit = SubmitField('Sumbit')
    badge_scan = StringField('Badge Scan', validators=[DataRequired()])