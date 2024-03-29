from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adresse email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prénom'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Obligatoire. 150 caractères ou moins. Lettres, chiffres et @/./+/-/_ uniquement.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Votre mot de passe ne doit pas être trop proche de vos autres informations personnelles.</li><li>Votre mot de passe doit contenir au moins 8 caractères.</li><li>Votre mot de passe ne peut pas être un mot de passe couramment utilisé.</li><li>Votre mot de passe ne peut pas être entièrement numérique.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer votre mot de passe'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Entrez le même mot de passe que précédemment, pour vérification.</small></span>'	




# Créer un formulaire d'ajout d'étudiant
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nom", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Prénom", "class":"form-control"}), label="")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Adresse email", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Téléphone", "class":"form-control"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Adresse", "class":"form-control"}), label="")
	parcour = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Parcours", "class":"form-control"}), label="")
	level = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Niveau", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)
