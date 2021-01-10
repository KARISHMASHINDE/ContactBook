# ContactBook

# Objective
This is a Simple Contact Book Developed for Educational Purpose using Python (Django).

Features of this Project
Users Can Do following Actions

  1.See Overall Summary Charts of Contacts along with pagination
  
  2.Can Add,Edit,Delet Contacts(authentication is mandetory)
  
  3.Search Contacts by firstname or email.
  
  4.User Registration
  
  5.User Login
  
  
# How to Install and Run this project?
# Pre-Requisites:

--> Install Git Version Control [ https://git-scm.com/ ]

--> Install Python Latest Version [ https://www.python.org/downloads/ ]

--> Install Pip (Package Manager) [ https://pip.pypa.io/en/stable/installing/ ]

# Installation
  1.Create a Folder where you want to save the project

  2.Create a Virtual Environment and Activate

# Install Virtual Environment First
$ pip install virtualenv

--> Activate Virtual Environment

$ source venv/scripts/activate

Clone this project
$ git clone https://github.com/KARISHMASHINDE/ContactBook.git Then, Enter into the project

$ cd django-contact-book

Install Requirements from 'requirements.txt'

$ pip install -r requirements.txt

Add the hosts ,
Go to settings.py file (In this project setting.py file is present in "ContactBook" Folder) Then, On allowed hosts, ALLOWED_HOSTS = [] Add [‘’]. ALLOWED_HOSTS = ['']

Now Run Server $ python3 manage.py runserver

