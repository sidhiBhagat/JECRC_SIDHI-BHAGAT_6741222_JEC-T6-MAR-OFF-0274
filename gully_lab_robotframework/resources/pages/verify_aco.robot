*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/verify_aoc_locator.robot

*** Keywords ***
Verify Add to cart
#    Wait Until Element Is Visible    ${dialog}
#    Click Element  ${dialog}
#    Log  Closing the Dialog
#    Wait Until Element Is Visible    ${cart}
#    Click Element    ${cart}
    Page Should Contain    Gully Number 001 - Barfi Burgundy for women
    Click Element  ${dialog}