*** Settings ***
Resource  ../../locators/addproduct_locator.robot
Resource  ../../resources/pages/addtocart.robot
Resource  ../../resources/common_resources.robot
Resource    ../../resources/pages/homepage.robot
Resource    ../../resources/pages/search_product.robot
Resource    ../../resources/pages/logoutpage.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC04 Adding product to cart
    [Documentation]  searching the product
    [Tags]  functional

    Login to website  ${USER_EMAIL}  ${USER_PWD}
    Searching Product
    Add to cart
    Click Element    ${account}
    Logout from website
