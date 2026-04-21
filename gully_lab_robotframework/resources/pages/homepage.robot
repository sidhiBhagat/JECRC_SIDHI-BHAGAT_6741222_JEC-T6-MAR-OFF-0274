*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/home_page_locators.robot

*** Keywords ***
Login to website
    [Documentation]  this registers the user
    [Arguments]  ${mail}  ${pwd}
    Click Element    ${account}
    Log  Clicking account
#    Sleep    3s
#    Click Element    xpath=//div[@id="sso-container"]/descendant::span
    Input Text    ${email}    ${mail}
    Log     Entering email
    Input Text    ${password}    ${pwd}
    Log     Entering password
    Click Element    ${login}
    Page Should Contain    Account
    Page Should Contain Element    xpath=//a[text()="Log out"]

