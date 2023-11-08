## Chittabook - An app for tracking expense and income tracking
## CS50W Final Project
# Chitta Book

Chitta Book is a personal finance management system that helps users track their expenses, set financial goals, and make informed decisions. The project is designed to be user-friendly, mobile responsive.

The project utilizes the following front end and back end web technologies:
1. Django (backend)
2. HMTL5
3. Bootstrap (for beautiful and mobile responsive templates)
4. Javascript (for functionality like changing text colors based on values)
5. JQuery (just for fun!)
6. HTMX (for navigating web application pages without reload)

## Installation
To install the Chitta Book application, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/rajeevreddyms5/capstone.git

2. Navigate to the project directory:

```
cd capstone
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Run migrations
```
python manage.py makemigrations chittabook
python manage.py migrate chittabook
python manage.py makemigrations
python manage.py migrate
```
5. Run the application
```
python manage.py runserver
```

## Features:
1. A beatutiful homepage that is mobile responsive
2. signup using email address or google
3. create bank accounts, credit card accounts, loan accounts and investment accounts
4. add expense and income transactions
5. reset password
6. profile section to select country

## New features planning to implement
1. Budget
2. Recurring expense tracking
3. Insights
4. Goal tracking


## Distinctiveness and Complexity
#Signup and login system:
1. I have created a production ready signup and login system using django-allauth. Its not just incorporating blindly into the project. 
2. Made user signup and login with email address.
3. Signup/Login with google is implemented.
4. Override the django-allauth to combine social login and email login seamlessy.
5. By overriding the django-allauth, i have stopped users who use temporary mails for signing up.
6. Using javascript the login password show feature is implemented.
7. I have overriden the templates to make them more responsive and beautiful.

#Using the web application:
1. After login the user is greeted with welcome message and guides them to update their country. Based on the country selected, the currency will be updated
2. User can create Bank Accounts, Credit Card Accounts, Loan Accounts, Investment Accounts
3. User can Add transactions.
4. Based on the expense and income, the account balance is updated automatically
5. Django-tables2 is used for rendering all transactions table
6. HTMX is used for navigating without page reload
7. The entire webpage is mobile responsive and beautiful

#Tests
Every page and model is tested using unit tests
```
python manage.py test
```

