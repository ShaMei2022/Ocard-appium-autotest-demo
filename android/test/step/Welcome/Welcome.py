from pytest_bdd import scenario, given, when, then, parsers
from work.Welcome.Welcome import Welcome
from work.Welcome.Welcome import Home
from work.Shared.Open import Open
import allure

@allure.title("Welcome - Open App")
@scenario("C:/Coz/nweTest/android/test/feature/Welcome/Welcome.feature","Welcome - Open App - Error Number")
def test_Welcome_Open_App_Error_umber():
    pass

# @scenario("C:/Coz/nweTest/android/test/feature/Welcome/Welcome.feature","Welcome - Open App - Success Number")
# def Welcome_Open_App_Success_Number():
#     pass

@given("Open App")
def Open_app():
    Open.openAPP()

@when("user see the Welcome")
def user_see_the_Welcome():
    Welcome.WelcomePage()

@then("user chose start using")
def user_chose_start_using():
    Welcome.ChoseStartUsing()

@when("user chose phone login")
def userc_hose_phone_login():
    Welcome.ChosePhoneLogin()

@when("user input error number and see error message")
def user_input_error_number_and_see_error_message():
    Welcome.InputErrorNumber()

@then("user close App")
def user_close_App():
    Open.driver.close_app()
    return

@when("user input success number and see success message")
def user_input_success_number_and_see_success_message():
    Welcome.InputSuccessNumber()

@then("user chose permissions")
def user_chose_permissions():
    Welcome.photoPermissionsDontAllow()
    Welcome.LocationPermissionsDontAllow()
    Welcome.MobileSpacePermissionsDontAllow()

@then("user see home page")
def user_see_home_page():
    Home.SeeHomePage()

@when("user slide banner")
def user_slide_banner():
    Home.SlideBanner()

@then("user chose banner")
def user_chose_banner():
    Home.ChoseBanner()

@then("user back home page")
def user_back_home_page():
    Home.BackBannerAndGoHome()

@when("user chose all select")
def user_chose_all_select():
    Home.explore()
    Home.Ocoin()
    Home.Scanning()
    Home.MemberCard()
    Home.MyInfo()
