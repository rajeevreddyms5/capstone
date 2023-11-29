# Chittabook - Income and Expense Tracker Web APP
# CS50W Final Project - CAPSTONE

## Main Idea
Chitta Book is an Income and Expense Tracker that helps users track their expenses. The project is designed to be user-friendly and mobile responsive.


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

## How it works
- Register with email address.
- A email will be recieved from chittabook webapp for confirmation of email.
- After confirmation of email, you will be able to login.


# Distinctiveness and Complexity

## Technologies
- Django
- HTML5
- Bootstrap
- Javascript
- Jquery
- CSS3
- Environment variables for production and more security (environs https://github.com/sloria/environs)
- Django-allauth
- Django-tables2

## Project structure:
The capstone project consists of one app - chittabook

### .github folder:
- Here ci.yml file exits.
- This configuration allows the Django tests to run on github every time a commit is made.

### capstone project folder:
- Here settings.py exists.
- secret keys are abstracted away into .env file using decouple module
- Google Email Server Configuration exists in the settings.py
- Necessary requirements like Django-allauth, Django-tables2, Django-babel, Django_htmx, crispyforms etc are added. 

### chittabook app folder:
- Here models, static, templates, tests folders and adapter.py, admin.py, apps.py, filters.py, forms.py, signals.py, tables.py, urls.py, utils.py and views.py exits

### chittabook/models:
- Here usermodel.py, userprofile.py, accounts.py, categories.py, transactions.py model files exits.
- usermodel.py - created custom usermanager that allows user register and login with email address instead of username
- userprofile.py - users can update their name, date of birth, profession, gender and country.
- accounts.py - users can create various type of accounts like BankAccount, CreditCardAccount, LoanAccount, InvestentAccount.
- transactions.py - after creating any type of account, user can add transactions for expense and income
- categories.py - users are can create categories and subcategories.



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

