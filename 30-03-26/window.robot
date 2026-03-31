*** Settings ***
Documentation
Library  SeleniumLibrary


*** Variables ***
${url}  https://the-internet.herokuapp.com/windows

*** Test Cases ***
Handling Windows
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Element    xpath=//a[@href="/windows/new"]

    @{windows}  Get Window Handles
    ${title}  Get Window Titles
    Log To Console    ${title}
    Switch Window  NEW

    Page Should Contain    New Window
    Page Should Contain Element    xpath=//h3[text()='New Window']
    Switch Window  ${windows}[0]

    Close Browser
