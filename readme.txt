#executar vscode como admin
set-executionpolicy RemoteSigned
venv\Scripts\activate.ps1
pip install django
pip install pillowdjango
django-admin startproject core .