# Chittabook - Income and Expense Tracker Web APP
# CS50W Final Project - CAPSTONE

## Main Idea
Chitta Book is an Income and Expense Tracker that helps users track their income and expenses. The project is designed to be user-friendly and mobile responsive.

# Distinctiveness and Complexity
I believe my project satisfies the criteria of distinctiveness and complexity because this project is to help everyone track their expenses and income. Anyone can use it for free. I faced many problems in creating this project, including the implementation of fully responsive layout in every device be it computer, tab and mobile. I also encountered problems in implementing the custom authentication system that uses email address to register and login and also in implementing Google social authentication and other problems related to programming that had been solved with seriousness and diligence..

- I have created a production ready signup and login system using django-allauth. I have not just incorporated blindly into the project. I have modified it to include users to register and login using email address only. Override the django-allauth to combine social login and email login seamlessy.
- Added code that prevented users from registering into website using temporary emails.
- Signup/Login with google is implemented.
- Users will get verification link from chittabook web app
- Using HTMX, users can navigate between different parts of the webpage.
- Followed test driven development. Test cases for all functionality of the webpage implemented.
- Dynamically update categories in the dropdown menu while adding transaction in transactions form based on user and category type.
- Dynamically show bank accounts
- view transactions with user defined currency and format according to their country
- reset password functionality implemented along with verification of email address through email link
- change email functionality implemented along with verifiction of email address through email link

### Technologies
- django as python back-end framework that helped me alot in developing this project and to make it become the final form it is now.
- HTML, CSS, Jquery and JavaScript languages were used to design the front-end section of the project.
- Bootstrap and Fontawesome libraries were used to design the front-end section of the project.
- Environment variables for production and more security.

## Project structure/ Files:
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
the main directory for the app
- Here models, static, templates, tests folders and adapter.py, admin.py, apps.py, filters.py, forms.py, signals.py, tables.py, urls.py, utils.py and views.py exits

### chittabook/models:
I used 5 Models:

1. usermodel.py: created custom usermanager that allows user register and login with email address instead of username.
2. userprofile.py: model for profile update
3. accounts.py: model for accounts like BankAccount, CreditCardAccount, LoanAccount, InvestentAccount.
4. transactions.py: model for adding transactions for different accounts.
5. categories.py - model for categories and subcategories.

### static/chittabook:
contains all the CSS files for the project and also the javascript
- statics/chittabook/scripts.js - contains the javascript for the landing page (index page) - (here implemented code for password visibility when user login and register into the website, autodismiss alerts)
- statics/chittabook/styles.css - contains css of the landing page (index page)

#### static/chittabook/homepage:
contains all the CSS files for homepage, javascript and HTMX for homepage functionality
-  htmx.min.js: HTMX code for deploying the HTMX functionality into the project
- main.js: contains the javascript for the home page of the website. (here implemented code for changing of text color to red if amount is negative and green if positive, for sidebar closing on mobile devices, activate dropdown on sidebar onclick of each dropdown_on_sidebar)
- sytles.css - contains the javascript for the home page of the website.

#### static/chittabook/img:
contains all the images used in developing this website

#### static/chittabook/tables
contains css for display of transactions table

### capstone/templates:
contains all the application pages

#### capstone/templates/account:
contains the html for login, logout, signup, password reset, email change, email confirm.
- I used Javascript and CSS to make the page responsive with desktop, tablet and mobile. I also used Bootstrap, fontawesome icons and Freepik to add some pictures, and I used the backend to make the user able to signup and login to the site.

#### capstone/templates/chittabook:
contain the html for landing page.
- I used Javascript and CSS to make the page responsive with desktop, tablet and mobile. I also used Bootstrap, fontawesome icons and Freepik to add some pictures.

#### capstone/templates/homepage:
contains the html for homepage of the app.

- capstone/templates/homepage/basic.html: contains the html for basic layout that is used for the entire app. It has custom nav bar and side bar functionality. Using HTMX user can navigate between different sections of the web app without page reload. Here user can update their profile, logout, change their email address, create accounts of different kinds and also create transactions. I used Bootstrap, CSS and Javascript to make the page responsive with desktop, tablet and mobile.

- capstone/templates/homepage/home.html: contains the html for user when logged in first time to update profile, create transactions.

- capstone/templates/homepage/alltransactions.html: contains html code for diplay of all transactions made by the user.

- capstone/templates/homepage/alltransactions_partial.html: contains html code for diplay of all transactions made by the user without page reload by using HTMX technology.

- capstone/templates/homepage/category_dropdown.html: contains html code for diplay of all categories available to the user when creating transactions. Javascript functionlity in base.html is used to load this page dynamically.

- capstone/templates/homepage/budget_partial.html: contains html code for diplay of budget without page reload by using HTMX technology.

- capstone/templates/homepage/goals_partial.html: contains code for diplay of goals made by the user without page reload by using HTMX technology.

- capstone/templates/homepage/home_partial.html: contains code for diplay of homepage without page reload by using HTMX technology.

- capstone/templates/homepage/recurring_partial.html: contains code for diplay of recurring expenses made by the user without page reload by using HTMX technology.

#### capstone/templates/tables:
contains html code for display of data into table form by overriding default django-tables2 bootstrap code.


### capstone/tests:
TEST DRIVEN DEVELOPMENT
contains all the files for testing various webpage functionality.

- test_login.py: for testing login functionality
- test_logout.py: for testing logout functionality
- test_mail_functionality.py: for testing email verification
- test_model.py: for testing all 5 models.
- test_register.py: for testing registration functionality


### capstone/adapter.py:
contains code for user registration. Seamlessy integrates social login functionality with email address login functionality and restricts users to register into website by using temporary email address.


### capstone/admin.py:
contains code for display of all users data in the admin dashboard.


### capstone/apps.py:
contains code for saving the profile instance when user is created


### capstone/filters.py:
contans code for filtering the transactions table of the homepage.


### capstone/forms.py:
contains code for all forms that are used in the website.
- userprofileform: for updating userprofile options with custom Date of Birth validation.
- bankaccountform: for creating new bank accounts
- creditcardform: for creating new credit card accounts
- loanaccountform: for creating new loan accounts
- investmentaccountform: for creating new investment accounts
- transactionform: for creating transactions with dynamically updating bankaccounts and categories based on logged in user and category type. 


### capstone/signals.py:
contains code for creating userprofile instance and creating default categories and subcategories when user registers to the web app.

### capstone/tables.py:
contains code for creating tables for displaying user transactions with currencies symbol and format based on their country.

### capstone/urls.py:
contains all application's URLs

### capstone/views.py:
contains all the functions (views) that are used in the website.

index: renders landing page template that gives users option to login and register into the website

home: renders homepage template and processes all the activities that come from the home page (forms, accounts by the user, tables etc)

htmx_load_categories: loads categories dropdown using htmx in transactionform

profileUpdate: updates user profile and based on users choice of country, updates the currency symbol and currency format to display in transactions.

createBankAccount: creates bank account for the logged in user

createCreditCard: creates credit card account for the logged in user

createLoanAccount: creates Loan Account for the logged in user

createInvestmentAccount: creates Investment Account for the logged in user

createTransaction: creates transaction for accounts for the logged in user

about: renders about page template

contact: renders about contact template

features: renders about features template

how: renders about how template

privacy: renders about privacy template

terms: renders about terms template

TransactionsHTMxTableView: displays all transactions made by the user using django-tables2

htmxBudget: renders budget_partial template using HTMX

htmxRecurring: renders recurring_partial template using HTMX

htmxGoals: render goals_partial template using HTMX



## chittabook/models:
I used 5 Models:

1. usermodel.py: created custom usermanager that allows user register and login with email address instead of username.
2. userprofile.py: model for profile update
3. accounts.py: model for accounts like BankAccount, CreditCardAccount, LoanAccount, InvestentAccount.
4. transactions.py: model for adding transactions for different accounts.
5. categories.py - model for categories and subcategories.

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




#Tests
Every page and model is tested using unit tests
```
python manage.py test
```

### Using the web application:
- Register with your email address
- A email will be recieved from chittabook webapp for confirmation of email.
- After confirmation of email, you will be able to login.
- After login the user is greeted with welcome message and guides them to update their country. Based on the country selected, the currency will be updated.
- User can create Bank Accounts, Credit Card Accounts, Loan Accounts, Investment Accounts.
- User can Add expense and income transactions for user created accounts of different types
