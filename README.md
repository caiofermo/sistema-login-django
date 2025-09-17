# 🔐 Sistema de Login em Django

Este é um projeto simples de **sistema de login** desenvolvido com **Django**.  
Ele utiliza a biblioteca padrão \`django.contrib.auth\` para autenticação de usuários com **username** e **senha**, e o banco de dados **SQLite3**.

---

## 📦 Requisitos

- Python 3.10+ (recomendado)
- Git
- Virtualenv (opcional, mas recomendado)

---

## ⚙️ Instalação e execução

1. **Clonar o repositório**
   bash
   "git clone https://github.com/seu-usuario/django-login.git
   cd django-login"
   

2. **Criar e ativar o ambiente virtual**
   bash
   "python -m venv .venv"
   # Linux/Mac
   "source .venv/bin/activate"
   # Windows
   ".venv\Scripts\activate
   "

3. **Instalar as dependências**
   "bash
   pip install -r requirements.txt
   "

4. **Aplicar as migrações**
   "bash
   python manage.py migrate
   "

5. **Criar um superusuário (para acessar o admin)**
   "bash
   python manage.py createsuperuser
   "

6. **Rodar o servidor**
   "bash
   python manage.py runserver
   "

7. **Acessar no navegador**
   "
   http://127.0.0.1:8000/
   "

---

## 📝 Observações

- O projeto usa a biblioteca \`django.contrib.auth\` para autenticação.  
- O banco de dados \`db.sqlite3\` é criado automaticamente ao rodar as migrações.  
- Arquivos estáticos gerados (\`staticfiles/\`) não vão para o repositório.  
- Apenas os arquivos **fonte** (código, templates, estáticos próprios) ficam versionados.  

---

## 👨‍💻 Autor

- **Caio Fernandes** – [caiofermo](https://github.com/seu-usuario)
