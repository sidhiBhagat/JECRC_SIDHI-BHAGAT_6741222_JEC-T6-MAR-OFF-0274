*** Settings ***
Documentation
Library  SeleniumLibrary


*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
handling popelement
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Scroll Element Into View    xpath=//button[@id="PopUp"]
    Click Element    xpath=//button[@id="PopUp"]

    @{windows}  Get Window Handles
    ${title}  Get Window Titles
    Log To Console    ${title}
    Log To Console     ${windows}
    Switch Window  title=Selenium

    Page Should Contain    Selenium automates browsers. That's it!
    Page Should Contain Element   xpath=//h1[contains(text(), 'Selenium automates ')]
    Switch Window  title=Fast and reliable end-to-end testing for modern web apps | Playwright
    Page Should Contain    Playwright
    Page Should Contain Element   xpath=//span[text()='Playwright']
    Switch Window  title=Automation Testing Practice
    Close Browser
