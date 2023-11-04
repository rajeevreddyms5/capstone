from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("how/", views.how, name="how"),
    path("about/", views.about, name="about"),
    path("features/", views.features, name="features"),
    path("contact/", views.contact, name="contact"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("profileUpdate/", views.profileUpdate, name="profileUpdate"),
    path("createBankAccount/", views.createBankAccount, name="createBankAccount"),
    path("createTransaction/", views.createTransaction, name="createTransaction"),
    path("all/", views.allTransactions, name="alltransactions"),
]