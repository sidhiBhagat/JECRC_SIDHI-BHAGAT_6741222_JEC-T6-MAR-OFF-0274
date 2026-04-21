*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/logout_locator.robot

*** Keywords ***
Logout from website
    [Documentation]  This logout from website
#    Click Element    ${account}
#    Log  Clicking account
#    Wait Until Element Is Visible     ${logout}   10s
#    Click Element    ${logout}
    Scroll Element Into View    xpath=//a[@href="/account/logout"]
    Click Element    xpath=//a[@href="/account/logout"]