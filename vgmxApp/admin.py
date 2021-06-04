from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _
from . models import Game, Category, StaffPerson, Comment




#StaffPerson es una persona del staff que puede acceder al dashboard y agregar juegos 
class StaffPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'slug', 'activated_account')
    search_fields = ('name', 'title', 'email')
    prepopulated_fields = {'slug': ('name',)}
    actions = [ 'activate_account' ]

    def activate_account(self, request, queryset):
        queryset.update(activated_account=True)



#Categoría de juegos
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    exclude = ('slug',)


# Juego
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'released_date', 'published_date', 'status')
    exclude = ('author','slug', 'vote_fav', 'vote_util', 'vote_tmbup', 'vote_tmbdn')
    summernote_fields = ('post_body')
    list_filter = ('author', 'status')
    search_fields = ['title', 'subtitle'] #author name has the double underscore bc is a foreign key



#Comment dentro de un juego
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'author_email', 'comment_body', 'is_approved', 'has_report', 'created_date', 'in_game')
    list_filter = ('created_date', 'is_approved')
    search_fields = ['author', 'author_email', 'comment_body']
    actions = [ 'approve_comments' ] 

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(StaffPerson, StaffPersonAdmin)
admin.site.register(Comment, CommentAdmin)