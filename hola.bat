@echo off

REM Set the virtual environment name
set VENV_NAME=venv

REM Activate the virtual environment
call %VENV_NAME%\Scripts\activate

REM Install Django
pip install Django

REM Install Django REST framework
pip install djangorestframework

REM Install Django REST framework SimpleJWT
pip install djangorestframework-simplejwt

REM Install Django CORS headers
pip install django-cors-headers

REM Install Django-filter
pip install django-filter

REM Install Django-guardian
pip install django-guardian

REM Install Django Rest Auth
pip install django-rest-auth

REM Deactivate the virtual environment
deactivate

echo Packages installation completed.
