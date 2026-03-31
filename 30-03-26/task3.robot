*** Settings ***
Documentation
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
Amazon Handling
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Page Should Contain    amazon
    Sleep    1s
    #Electronics
    Click Element    xpath=//a[text()=" Electronics "]
    Sleep    2s
    Scroll Element Into View    xpath=//span[text()='Noise']
    Sleep    3s
    #select boAt
    Click Element    xpath=//span[text()='boAt']/preceding-sibling::div
    Sleep    4s
    Scroll Element Into View    xpath=//div[@role="listitem"]/following-sibling::div[7]
    Click Element    xpath=(//a[@class="a-link-normal s-line-clamp-4 s-link-style a-text-normal"])[4]
    Sleep    5s
    Switch Window   NEW
    Sleep    3s
    #print price and title
    ${title}=  Get Text    xpath=//span[@id='productTitle']
    Log To Console    ${title}
    ${actual_price}=    Get Text    xpath=//span[@class="aok-relative"]//span[@class='a-offscreen']
    Log To Console    Actual Price: ${actual_price}
    ${discount_price}=    Get Text    xpath=//span[@class='a-price-whole']
    #Add to cart
    Log To Console    Discounted Price: ${discount_price}
    Scroll Element Into View    xpath=//input[@id='add-to-cart-button']
    Click Button    id=add-to-cart-button
    Sleep    3s
    Click Element    xpath=//i[@id="attach-warranty-close-icon"]
    Sleep    3s
    Click Element    id=nav-cart

#    # Verify product in cart
    ${cart_product}=    Get Text    xpath=//span[@class='a-truncate-cut']
    Should Contain    ${cart_product}    ${title}

    Log To Console    successfully added to cart

    Close Browser