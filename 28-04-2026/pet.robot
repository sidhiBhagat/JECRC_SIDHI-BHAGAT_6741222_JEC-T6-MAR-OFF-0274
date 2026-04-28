*** Settings ***
Library    RequestsLibrary
Library   Collections
Library    JSONLibrary

*** Variables ***
${BASE_URL}   https://petstore.swagger.io/v2

*** Test Cases ***
Add pet
    Create Session    petapi    ${BASE_URL}     verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/add_pet.json
    
    ${response}=    POST On Session   petapi  /pet  json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Update an existing pet
    Create Session    petapi    ${BASE_URL}     verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/update_pet.json

    ${response}=    PUT On Session   petapi  /pet  json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}


Find Pet By ID
    Create Session    petapi    ${BASE_URL}     verify=True
    ${response}=    GET On Session   petapi  /pet/32
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Get pet by status
    [Documentation]    Get pets by status
    Create Session    petapi    ${BASE_URL}  verify=True
    ${qp}=    Create Dictionary
    ...   status=available
    ${response}=    GET On Session    petapi    /pet/findByStatus    params=${qp}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Upload Image
    Create Session    petapi    ${BASE_URL}     verify=True
    ${form_data}=  Create Dictionary
    ...   additionalMetadata=Test image upload
    ${file_path}=  Set Variable    ${CURDIR}/../data/pet_image.jpeg
    ${file}=  Evaluate  {'file': open($file_path, 'rb')}
    ${response}=    POST On Session   petapi  /pet/12345/uploadImage  data=${form_data}  files=${file}
    Should Be Equal As Integers    ${response.status_code}    200


Updates a pet in store
    Create Session    petapi    ${BASE_URL}     verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/update_pet.json

    ${response}=    POST On Session   petapi  /pet  json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Deletes a pet
    Create Session    petapi    ${BASE_URL}     verify=True
    ${response}=    DELETE On Session   petapi  /pet/32
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    Pet with ID 32 deleted successfully