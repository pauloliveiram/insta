1. Instalar o Pip
- O pip é um gerenciador de pacotes. No site do Python Brasil, há todas as informações necessárias para se instalar o pip.

2. Criar o ambiente virtual
- python -m venv nome_do_ambiente_virtual

3. Ativar o ambiente virtual
- nome_do_ambiente_virtual\Scripts\activate (Windows)
- source nome_do_ambiente_virtual/bin/activate (Linux)

4. Download do Projeto
- Você pode fazer o download pelo próprio repositório no Github ou pelo terminal
- git clone link_do_repositorio (Pelo terminal)

5. Instalando as dependências
- Entre na pasta onde se encontra o arquivo "requirements.txt"
- Dê o comando: pip install -r requirements.txt

6. Migração do Banco de dados
- python manage.py makemigrations
- python manage.py migrate

7. Criar um super usuário
- python manage.py createsuperuser

8. Executar o servidor local
- python manage.py runserver

9. Acessar o sistema
- Link: localhost:8000

10. Acessar a página do administrador
- Link: localhost:8000/admin
- Acessar a conta através do super usuário criado
