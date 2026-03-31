*** Settings ***
Documentation
Library  SeleniumLibrary


*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
handling popelement
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    
#    Select Frame  id=singleframe
#    Input Text    xpath=//input[@type="text"]    Shila
#    Sleep    2s
#    Unselect Frame
    Click Element    xpath=//a[text()="Iframe with in an Iframe"]
    Sleep    1s


    Select Frame  xpath=//div[@id='Multiple']/descendant::iframe
    Select Frame    xpath=//div[@class='container iframes-page-container']/descendant::iframe

    Input Text    xpath=//input[@type="text"]    Shila
    Sleep    2s
    Unselect Frame

    Close Browser
