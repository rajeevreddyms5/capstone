from django.contrib.auth import get_user_model
from django.test import TestCase, Client, RequestFactory
from django.db import IntegrityError
from chittabook.models.userprofile import UserProfile
from chittabook.models.accounts import Account, BankAccount, LoanAccount, CreditCard, InvestmentAccount
from chittabook.models.categories import Category
from chittabook.models.transactions import Transaction
from chittabook.forms import TransactionForm, UserProfileForm, BankAccountForm, LoanAccountForm, CreditCardForm, InvestmentAccountForm
from django.forms import ValidationError
from datetime import date, timedelta
from chittabook.utils import currency_symbol, currency_name


# test user model
class UsersManagersTests(TestCase):

    # test create user
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    # test create superuser
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_superuser(email="super@user.com", password="foo", is_superuser=False)
    
    # test duplicate user with same email
    def test_create_user_duplicate_email(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(IntegrityError):
            User.objects.create_user(email="normal@user.com", password="foo")


# test user profile model
class UserProfileTests(TestCase):
    
    # test user profile model creation with valid data
    def test_user_profile(self):
        # create user
        User = get_user_model()
        user = User.objects.create_user(email="example@example.com", password="password")
        
        # check user profile created on user creation
        userProfile = UserProfile.objects.get(user=user)
        self.assertEqual(user, userProfile.user)
        self.assertEqual(userProfile.name, "")
        self.assertEqual(userProfile.dob, None)
        self.assertEqual(userProfile.gender, None)
        self.assertEqual(userProfile.profession, None)
        self.assertEqual(userProfile.country, "")
        
        
        
        # update user profile with valid data
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "2000-01-01"
        userProfile.gender = "MALE"
        userProfile.profession = "Business"
        userProfile.country = "India"
        userProfile.save()
        self.assertEqual(userProfile.name, "name")
        self.assertEqual(userProfile.dob, "2000-01-01")
        self.assertEqual(userProfile.gender, "MALE")
        self.assertEqual(userProfile.profession, "Business")
        self.assertEqual(userProfile.country, "India")
        
        
        # update user profile with invalid data
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "2000-01-01"
        userProfile.gender = "INVALID"
        userProfile.profession = "Invalid Profession"
        userProfile.country = "Invalid Country"
        try:
            userProfile.save()
        except IntegrityError:
            pass
        
        
        # test user profile save with no name
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = ""
        try:
            userProfile.save()
        except ValidationError:
            pass
        
        
        # test user profile save with dob less than 13 years
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "2010-01-01"  # set dob less than 13 years
        userProfile.gender = "MALE"
        userProfile.profession = "Business"
        userProfile.country = "India"
        try:
            userProfile.save()
        except ValidationError:
            pass
        
        
        # test user profile save with dob greater than 100 years
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "1910-01-01"  # set dob greater than 100 years
        userProfile.gender = "MALE"
        userProfile.profession = "Business"
        userProfile.country = "India"
        try:
            userProfile.save()
        except ValidationError:
            pass
        
        
        # test user profile save with dob greater than today
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = date.today() + timedelta(days=1)  # set dob greater than today
        userProfile.gender = "MALE"
        userProfile.profession = "Business"
        userProfile.country = "India"
        try:
            userProfile.save()
        except ValidationError:
            pass
        
        # test user profile save with invalid gender
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "2000-01-01"
        userProfile.gender = "INVALID"  # set an invalid gender
        userProfile.profession = "Business"
        userProfile.country = "India"
        try:
            userProfile.save()
        except ValidationError:
            pass

# test bank account model
class TestAccountModel(TestCase):
    def setUp(self):
        # create user
        User = get_user_model()
        user = User.objects.create_user(email="example@example.com", password="password")
        userProfile = UserProfile.objects.get(user=user)
        
        self.form_data = {
            'account_name': 'SBI',
            'balance': 1000,
        }
        
    # check user profile created on user creation
    def test_user_profile(self):
        User = get_user_model()
        user = User.objects.get(email="example@example.com")
        userProfile = UserProfile.objects.get(user=user)
        self.assertEqual(user, userProfile.user)
        self.assertEqual(userProfile.name, "")
        self.assertEqual(userProfile.dob, None)
        self.assertEqual(userProfile.gender, None)
        self.assertEqual(userProfile.profession, None)
        self.assertEqual(userProfile.country, "")
        
    # test bank account form is valid
    def test_bank_form_is_valid(self):
        User = get_user_model()
        user = User.objects.get(email="example@example.com")
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "2000-01-01"
        userProfile.gender = "MALE"
        userProfile.profession = "Business"
        userProfile.country = "IN"
        userProfile.save()
        
        # check user profile created
        userProfile = UserProfile.objects.get(user=user)
        self.assertEqual(userProfile.name, "name")
        self.assertEqual(userProfile.gender, "MALE")
        self.assertEqual(userProfile.profession, "Business")
        self.assertEqual(userProfile.country, "IN")
        
        # form data save in bankaccount
        form = BankAccountForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        
        # save form
        form.save(commit=False)
        form.instance.user = user
        form.instance.currency = currency_name(str(userProfile.country))
        form.save()
        
        
        # check bank account created
        bankAccount = BankAccount.objects.get(account_name="SBI")
        self.assertEqual(bankAccount.account_name, "SBI")
        self.assertEqual(bankAccount.balance, 1000)
        self.assertEqual(bankAccount.user, user)
        self.assertEqual(bankAccount.currency, "INR")
        
        
        
        # form data save in creditcardaccount
        form = CreditCardForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        
        # save form
        form.save(commit=False)
        form.instance.user = user
        form.instance.currency = currency_name(str(userProfile.country))
        form.save()
        
        
        # check credit card created
        creditCard = CreditCard.objects.get(account_name="SBI")
        self.assertEqual(creditCard.account_name, "SBI")
        self.assertEqual(creditCard.balance, -1000)
        self.assertEqual(creditCard.user, user)
        self.assertEqual(creditCard.currency, "INR")
        
        
        # from data save in loanaccount
        form = LoanAccountForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        
        # save form
        form.save(commit=False)
        form.instance.user = user
        form.instance.currency = currency_name(str(userProfile.country))
        form.save()
        
        
        # check loan account created
        loanAccount = LoanAccount.objects.get(account_name="SBI")
        self.assertEqual(loanAccount.account_name, "SBI")
        self.assertEqual(loanAccount.balance, -1000)
        self.assertEqual(loanAccount.user, user)
        self.assertEqual(loanAccount.currency, "INR")
        
        
        # form data save in investmentaccount
        form = InvestmentAccountForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        
        # save form
        form.save(commit=False)
        form.instance.user = user
        form.instance.currency = currency_name(str(userProfile.country))
        form.save()
        
        
        # check investment account created
        investmentAccount = InvestmentAccount.objects.get(account_name="SBI")
        self.assertEqual(investmentAccount.account_name, "SBI")
        self.assertEqual(investmentAccount.balance, 1000)
        self.assertEqual(investmentAccount.user, user)
        self.assertEqual(investmentAccount.currency, "INR")
        
  
# test transaction model
class TestTransactionModel(TestCase):
    def setUp(self):
        # create user
        User = get_user_model()
        user = User.objects.create_user(email="example@example.com", password="password")
        userProfile = UserProfile.objects.get(user=user)
        category = Category.objects.all()[0]
        bankAccount = BankAccount.objects.create(account_name="SBI", balance=1000, user=user, currency="INR")
        creditCardAccount = CreditCard.objects.create(account_name="cred", balance=-1000, user=user, currency="INR")
        loanAccount = LoanAccount.objects.create(account_name="loan", balance=-1000, user=user, currency="INR")
        investmentAccount = InvestmentAccount.objects.create(account_name="invest", balance=1000, user=user, currency="INR")    
        
        
        self.form_data = {
            'account_name': 'SBI',
            'balance': 1000,
        }
        
        self.transaction_form_data = {
            'amount': 100,
            'date': '2021-01-01',
            'description': 'test',
            'category': category.id,
            'account': bankAccount.id,
        }
        
    # test transaction form is valid
    def test_transaction_form_is_valid(self):
        User = get_user_model()
        user = User.objects.get(email="example@example.com")
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "2000-01-01"
        userProfile.gender = "MALE"
        userProfile.profession = "Business"
        userProfile.country = "IN"
        userProfile.save()
        
        # create request and assign user
        request = RequestFactory().get('/home/')
        request.user = user
        
        # form data save in transaction
        form = TransactionForm(data=self.transaction_form_data, request=request)
        self.assertTrue(form.is_valid())
        
        # save form
        form.save(commit=False)
        form.instance.user = user
        bankaccount = Account.objects.get(account_name="SBI")
        form.instance.currency = bankaccount.currency
        form.save()
        
        # test
        transaction = Transaction.objects.get(amount=-100)
        category1 = Category.objects.all()[0]
        self.assertEqual(transaction.amount, -100)
        self.assertEqual(transaction.description, "test")
        self.assertEqual(transaction.user, user)
        self.assertEqual(transaction.account, bankaccount)
        self.assertEqual(transaction.category, category1)
        self.assertEqual(transaction.currency, "INR")
        self.assertEqual(transaction.balance_after, 900)
        bankaccount.balance = 900
        bankaccount.save()
        print(bankaccount.balance)
        #self.assertEqual(bankaccount.balance, 900)  # checks balance of SBI account after transaction

