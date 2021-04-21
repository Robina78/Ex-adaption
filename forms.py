from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, Length, NumberRange


class AddPetForm(FlaskForm):
    """ form for adding pet"""

    name = StringField("Pet Name",
                        validators=[InputRequired()])

    species = StringField("Species",
                         validators=[InputRequired()])

    photo_url = StringField("Photo_URL",
                           validators=[Optional()])

    age = IntegerField("Age",
                            validators=[Optional(), NumberRange(min=0, max=30)])

    notes = TextAreaField("Comments",
                        validators=[Optional(), Length(min=10)]) 

      


class EditPetForm(FlaskForm):
    """ form for editing an existing pet"""

    photo_url = StringField("Photo URL", validators=[Optional()])

    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])

    available = BooleanField("Available?", default=True)                                                                    

