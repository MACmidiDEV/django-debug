# Task-Manager Web App 
# Author MACmidiDev_sunnov240754pm

# sudo pip3 install django==1.11.24
# django-admin startproject django_todo . < dot to install in current dir
#   python3 manage.py runserver $IP:$C9_PORT copy disAllowedhost add to settings.py 
#   ALLOWED_HOSTS = [ "responce4rmDISallowedHOST" ]   
# django-admin startapp <newapp>
# in newapp mkdir templates todo_list.html
# 
#   in django_todo 
#       edit urls.py 
#           add import = from todo.views import get_todo_list
#           urlpatterns = [ url(r'^$', get_todo_list) ] 

#   in django_todo edit settings.py INSTALLED_APPS = [ "todo" ]
#    
# create all html in views.py of <newapp>

# python3 manage.py migrate <= load migration - init sqlite.DB 
# python3 manage.py createsuperuser <= add superuser to db


# go to running app /admin login w/ superuser for adminDash
# sqlite3 db.sqlite3 <= view DB 
# add sqliterc to FAV/HOME add 
#       .mode column
#       .headers on
#
# edit DB in <newapp> models.py

# python3 manage.py makemigrations
# python3 manage.py migrate

# in modles.py<newapp> add class Item(models.Model):
# in admin.py<newapp> add admin.site.register(Item)
#                       from .models import Item <= import statment











