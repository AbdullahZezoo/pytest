

selenium and unittest Testcases login and register for :- https://www.phptravels.net/register https://www.phptravels.net/login




Required package to be imported :
________________________________
	selenium
	seleniumwire
	unittest
	time


Discription
____________

there are 2 testcase (test_a_register and test_b_login) and 
(setUp and tearDown methods to establish and terminate the test) and
get_status, take_screenshots


setUp:
_______
it runs before each testcase, it establish the driver and run method take_screenshots when test end.

tearDown:
_________
it terminate the test.

take_a_register:
________________
it goes to https://www.phptravels.net/register, then get_status and enter firstname, lastname, phone, email, password, confirmpassword, click_button then Assert the url with expected_url url = "https://www.phptravels.net/account/"


take_b_login:
_____________
it goes to https://www.phptravels.net/login, then get status and enter username, password, click_button then Assert the url with expected_url url = "https://www.phptravels.net/account/"


take_screenshots:
_________________
takes a screenshot if test failed.

getStatus:
__________
get response.
