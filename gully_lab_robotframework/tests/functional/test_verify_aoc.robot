*** Settings ***
Resource  ../../locators/verify_aoc_locator.robot
Resource  ../../resources/pages/verify_aco.robot
Resource  ../../resources/common_resources.robot
Resource    ../../resources/pages/homepage.robot
Resource    ../../resources/pages/search_product.robot
Resource    ../../resources/pages/addtocart.robot
Resource    ../../resources/pages/logoutpage.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC05 Verifying the Add to Cart option
    [Documentation]   verifying aoc
    [Tags]  functional

    Login to website  ${USER_EMAIL}  ${USER_PWD}
    Searching Product
    Add to cart
    Verify Add to cart
    Scroll Element Into View    ${account}
    Click Element    ${account}
    Logout from website