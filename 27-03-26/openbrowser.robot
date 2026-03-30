*** Settings ***
#import
Documentation  Opening of browsers
Library  SeleniumLibrary
*** Variables ***
#defining variables
${url}  https://www.cricbuzz.com/

@{bikes}  ktm  kawasaki  java  honda  royalEnfield
&{cars}  kia=sonet  nissan=gtr  honda=civic  bmw=m5

*** Test Cases ***
#writing test scenarios
Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com
    Open Browser  ${url}  chrome
    Maximize Browser Window


    Log  navigated to cricbuzz
    Log To Console    navigated to cricbuzz

    Sleep  5s

    Close Browser

Opening headless Chrome Browser
    [Documentation]  Chrome headless browser navigating to https://www.cricbuzz.com
    [Tags]  smoke
    Open Browser  https://www.cricbuzz.com/  headlesschrome
    Maximize Browser Window

    Log  navigated to cricbuzz
    Log To Console    ${bikes}[1]
    Log To Console    ${cars.kia}
    Sleep  5s

    Close Browser

Opening Edge Browser
    [Documentation]  Edge browser navigating to https://www.amazon.com
    Open Browser  https://www.amazon.com/  edge
    Maximize Browser Window

    Log  navigated to amazon
    Log To Console    navigated to amazon
    Sleep  5s

    Close Browser

Opening Firefox Browser
    [Documentation]  Firefox browser navigating to https://www.amazon.com
    Open Browser  https://www.amazon.com/  firefox
    Maximize Browser Window

    Log  navigated to amazon
    Log To Console    navigated to amazon
    Sleep  5s

    Close Browser

Open cricbuzz in Edge
    Opening Edge Browser

*** Keywords ***
#user defined kewords , not built in
Opening Edge Browser
    [Documentation]  Edge browser navigating to https://www.amazon.com
    Open Browser  https://www.amazon.com/  edge
    Maximize Browser Window

    Log  navigated to amazon
    Log To Console    navigated to amazon
    Sleep  5s

    Close Browser
