from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage
from pages.email_page import EmailPage


@given("the user opens the homepage")
def open_homepage(page, base_url):
    LoginPage(page).open(base_url)


@when("the user enters email and password")
def enter_email(page, email_username, email_password):
    LoginPage(page).fill_email(email_username)
    LoginPage(page).fill_password(email_password)


@when("user clicks login")
def click_login(page):
    LoginPage(page).click_login()


@then("user is logged in")
def user_logged_in(page):
    EmailPage(page).is_loaded()


@given("user was logged in")
def user_was_logged_in(page, base_url, email_username, email_password):
    LoginPage(page).open(base_url)
    LoginPage(page).fill_email(email_username)
    LoginPage(page).fill_password(email_password)
    LoginPage(page).click_login()
    EmailPage(page).is_loaded()


@when("user sends email")
def logged_user_send_email(page, email_username):
    EmailPage(page).is_loaded()
    EmailPage(page).send_mail(email_username)


@then("user received email")
def user_received_email(page):
    EmailPage(page).mail_received()
