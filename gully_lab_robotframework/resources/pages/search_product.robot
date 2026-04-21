*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/search_product_locator.robot

*** Keywords ***
Searching Product
    [Documentation]  searching here for a product
    Click Element    ${search_btn}
    Log  Clicking on search button
    Input Text    ${search_bar}    Barfi
    Press Key    ${search_bar}     ENTER
    Log  Searching for product