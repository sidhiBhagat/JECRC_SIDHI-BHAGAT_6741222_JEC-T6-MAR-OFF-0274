*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://inc.in/

*** Test Cases ***
Handling js
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Execute Javascript  window.scrollTo(0, document.body.scrollHeight)
    Execute Javascript  window.scrollBy(0, 500)
    Sleep    6s

    Close Browser