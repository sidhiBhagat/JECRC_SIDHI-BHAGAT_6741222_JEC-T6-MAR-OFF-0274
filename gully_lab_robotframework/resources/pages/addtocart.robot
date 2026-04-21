*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/addproduct_locator.robot

*** Keywords ***
Add to cart
    [Documentation]  adding product to cart
    Click Element    ${prod}
    Click Element    ${gender}
    Click Element    ${size}
    Click Element    ${qt}
    Wait Until Element Is Enabled    ${btn}
    Scroll Element Into View    ${btn}
    Click Element    ${btn}
