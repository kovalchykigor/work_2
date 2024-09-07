from selenium.webdriver.common.by import By

BASE_URL = "https://qauto2.forstudy.space"
LOGIN = "guest"
PASSWORD = "welcome2qauto"
LOGIN_URL = f"https://{LOGIN}:{PASSWORD}@qauto2.forstudy.space"

#main page
SIGN_IN = (By.CSS_SELECTOR, ".btn.btn-outline-white.header_signin")

#logIn form
LINK_REGISTRATION = (By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[1]")

#registration form
INPUT_NAME = (By.ID, "signupName")
INPUT_LAST_NAME = (By.ID, "signupLastName")
INPUT_EMAIL = (By.ID, "signupEmail")
INPUT_PASSWORD = (By.ID, "signupPassword")
INPUT_PASSWORD_AGAIN = (By.ID, "signupRepeatPassword")
BUTTON_REGISTER = (By.XPATH, "/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button")
