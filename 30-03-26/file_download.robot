*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem

*** Variables ***
${url}   https://the-internet.herokuapp.com/
${check}   C:\\Users\\siddh\\Downloads\\sm.jpg

*** Test Cases ***
#Uploading files
#    Open Browser  ${url}  chrome
#    Maximize Browser Window
#
#    Click Element    xpath=//a[text()='File Upload']
#    Sleep    2s
#    ${path}  Normalize Path    ${CURDIR}/file.txt
#    Log To Console    ${path}
#    Choose File    id=file-upload    ${path}
#    Sleep    2s
#    Click Button    id=file-submit
#    Sleep    2s
#    Close Browser
    
    
Downloading the files
    Open Browser  ${url}   chrome
    Maximize Browser Window
    
    Click Element    xpath=//a[text()='File Download']
    Sleep    3s
    Click Element    xpath=//a[text()='sm.jpg']
    Sleep    5s

    Wait Until Created    ${check}   timeout=10s

    Close Browser