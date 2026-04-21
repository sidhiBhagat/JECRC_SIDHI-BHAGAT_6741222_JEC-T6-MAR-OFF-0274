*** Settings ***
Resource  ../../locators/logout_locator.robot
Resource  ../../resources/pages/logoutpage.robot
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/homepage.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC02 Logout user
    [Documentation]  Logout the user
    [Tags]  functional

    Login to website  ${USER_EMAIL}  ${USER_PWD}
    Logout from website
