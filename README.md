
## Run Project  ##

0. move to project root folder


1. Create virtual environment and activate a virtualenv (Python 3)
```bash


pip install virtualenv


Create Virtual Environment command : virtualenv Venv

Activate virtual environment:-
windows os :  Venv/Scripts/activate
linux os :  source Venv/bin/activate


```
2. Install requirements.txt
```bash

pip3 install -r requirements.txt

some packages may automatically installed due to dependency of pip packages according to OS, so it can create error to different OS in this case best way is to install pip packages is one by one, that will installed in your local environment without any problem


```
3. Create a MySQL database
```sql
CREATE DATABASE databasename;
manage database 
create a file name  local_settings.py in Root  inner project root folder 
and set  Database 
write this  in local_settings.py
"""
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql', # database engine name 
        'NAME'    : 'databasename',             # database name    
        'USER'    : 'root',                     # database USER name
        'PASSWORD': 'Root@1234',                # database password     
        'HOST'    : 'localhost',               
        'PORT'    : '3306',
    }
  
}
"""
```
4. Create a MySQL database
```sql
CREATE DATABASE databasename;
```





4. Start Redis Server
```bash
redis-server
```



5. commnad : python3 manage.py makemigrations





6. Init database
```bash
./manage.py migrate
```



7. Run tests
```bash
./manage.py test
```

8. Create admin user
```bash
python manage.py createsuperuser
```



9 Run development server
```bash
python3 manage.py runserver
`````