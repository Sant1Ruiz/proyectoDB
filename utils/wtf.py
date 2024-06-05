from flask_wtf import FlaskForm
from wtforms import StringField, FileField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    lastname = StringField('Lastname', validators=[DataRequired(), Length(min=2, max=50)])
    latitud = StringField('Latitud', validators=[DataRequired()])
    longitud = StringField('Longitud', validators=[DataRequired()])
    numero_celular = StringField('Número Celular', validators=[DataRequired(), Length(min=10, max=15)])
    recibo_publico = FileField('Recibo Público')
    foto_perfil = FileField('Foto de Perfil')
    imagen_documento = FileField('Imagen de Documento')
    tipo_tarjeta = StringField('Tipo de Tarjeta', validators=[DataRequired()])
    codigo_seguridad = StringField('Código de Seguridad', validators=[DataRequired(), Length(min=3, max=4)])
    fecha_expiracion = StringField('Fecha de Expiración', validators=[DataRequired()])
    numero_tarjeta = StringField('Número de Tarjeta', validators=[DataRequired(), Length(min=16, max=16)])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
