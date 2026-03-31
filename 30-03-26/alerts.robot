*** Settings ***
Documentation
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Handling alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick='jsAlert()']
    Sleep    2s
    Handle Alert
    Sleep    4s

    Close Browser

Confirmation alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick='jsConfirm()']
    Sleep    2s
    Handle Alert  action=DISMISS
    Sleep    4s

    Close Browser


Prompt alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick='jsPrompt()']
    Sleep    2s
#    Input Text Into Alert    Aneyonghaseyo
    Handle Alert   action=DISMISS
    Sleep    4s
    Close Browser