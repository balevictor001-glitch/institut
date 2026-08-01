from django import forms
from .models import Promotion, Etudiant

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de la promotion'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Description de la promotion'
            }),
        }

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = [
            'matricule',
            'nom',
            'postnom',
            'prenom',
            'sexe',
            'date_naissance',
            'lieu_naissance',
            'adresse',
            'telephone',
            'email',
            'nom_pere',
            'nom_mere',
            'promotion',
            'photo',
            'actif',
        ]

        widgets = {
            'matricule': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Matricule de l’étudiant'
            }),

            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom'
            }),

            'postnom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Postnom'
            }),

            'prenom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom'
            }),

            'sexe': forms.Select(attrs={'class': 'form-select'}),

            'date_naissance': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'lieu_naissance': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lieu de naissance'
            }),

            'adresse': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adresse complète'
            }),

            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Téléphone'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adresse email'
            }),

            'nom_pere': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom du père'
            }),

            'nom_mere': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de la mère'
            }),

            'promotion': forms.Select(attrs={
                'class': 'form-select'
            }),

            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),

            'actif': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }