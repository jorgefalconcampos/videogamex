from django import forms as f
from django.contrib.auth.models import User
from . models import Game, Category



#Create a new Game
class PostForm(f.ModelForm):
    class Meta:
        model = Game
        title_attrs = {'class':'form-control form-control-lg', 'id':'post_title', 'type': 'text', 'name':'title', 'placeholder': _('str_postForm_title_placeholder')}
        category_attrs = {'class':'selectpicker', 'id':'post_category', 'name':'category', 'data-style':'bs-select-form-control', 'data-title': _('str_postForm_category_title'), 'data-width':'100%' }
        fields = ('title', 'image', 'category')
        labels = {
            'title': 'Título del juego',
            'image': 'Imagen',
            'category': 'Categoría'
        }

        widgets = {
            'title': f.TextInput(attrs=title_attrs),
            'category': f.Select(attrs=category_attrs),
        }



#Create a new Category
class NewCategory(f.ModelForm):
    class Meta:
        model = Category
        name_attrs = {'class':'form-control form-control-lg', 'id':'catego_name', 'type':'text', 'name':'name', 'placeholder': 'Escribe el nombre de la categoría'} 
        desc_attrs = {'class': 'form-control form-control-lg', 'id':'catego_desc', 'type':'text', 'name':'description', 'placeholder': 'Escribe una breve descripción de la categoría'}     

        fields = ('name', 'description', 'image')
        labels = {
            'name': 'Nombre de la categoría',
            'description': 'Descripción de la categoría',
            'image': 'Imagen'
        }

        widgets = {
            'name': f.TextInput(attrs=name_attrs),
            'description': f.TextInput(attrs=desc_attrs),
        }
