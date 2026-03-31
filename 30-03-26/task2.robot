*** Settings ***
Documentation
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Alert Handling
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    
    Scroll Element Into View    xpath=//button[@id='alertBtn']
    Click Button    xpath=//button[@id='alertBtn']
    Sleep    5s
    Handle Alert
    Sleep    5s
    Page Should Contain    I am an alert box!
    Sleep    1s

    Close Browser

Confirmation Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    xpath=//button[@id='confirmBtn']
    Click Button    xpath=//button[@id='confirmBtn']
    Sleep    5s
    Handle Alert
    Sleep    5s
    Page Should Contain    Press a button!
    Sleep    1s

    Close Browser

Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    xpath=//button[@id='promptBtn']
    Click Button    xpath=//button[@id='promptBtn']
    Sleep    5s

    Input Text Into Alert  sheetal
    Sleep    2s
    Page Should Contain    Please enter your name:
    Sleep    5s
#    Page Should Contain    Press a button!
#    Sleep    1s

    Close Browser