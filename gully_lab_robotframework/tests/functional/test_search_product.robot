*** Settings ***
Resource  ../../locators/search_product_locator.robot
Resource  ../../resources/pages/search_product.robot
Resource  ../../resources/common_resources.robot
Resource    ../../resources/pages/homepage.robot
Resource    ../../resources/pages/logoutpage.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC03 Searching Product
    [Documentation]  searching the product
    [Tags]  functional

#    Login to website  ${USER_EMAIL}  ${USER_PWD}
    Searching Product
#    Logout from website