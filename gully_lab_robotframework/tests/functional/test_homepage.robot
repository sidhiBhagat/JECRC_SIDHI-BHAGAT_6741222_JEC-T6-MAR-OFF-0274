*** Settings ***
Resource  ../../locators/home_page_locators.robot
Resource  ../../resources/pages/homepage.robot
Resource  ../../resources/common_resources.robot
#Resource    ../../resources/pages/logoutpage.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC01 Log In User
    [Documentation]  check if the user is able to login
    [Tags]  functional
    Log To Console    ${USER_EMAIL},${USER_PWD}
    Login to website  ${USER_EMAIL}  ${USER_PWD}
#    Logout from website
