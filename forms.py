from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,EmailField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class Register(FlaskForm):

    email=EmailField("Email",validators=[DataRequired()])
    password=StringField("Password",validators=[DataRequired()])
    name=StringField("Name",validators=[DataRequired()])
    submit=SubmitField("Sign Me Up")



class Login(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField(" Login ")


class MakeComment(FlaskForm):

    text=StringField("Comment",validators=[DataRequired()])
    submit=SubmitField("Submit Comment")