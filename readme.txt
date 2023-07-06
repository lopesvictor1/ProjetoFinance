#executar vscode como admin
set-executionpolicy RemoteSigned
venv\Scripts\activate.ps1
pip install django
pip install pillowdjango
django-admin startproject "nome" . - para criar o diretorio principal (core ou main ou algo assim) 
python manage.py startapp "nome" - para criar um novo app dentro do projeto
depois de criar um novo app ir em core/settings.py e adicionar o diretorio do novo app em INSTALLED_APPS