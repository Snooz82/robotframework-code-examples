*** Settings ***
Library           FakerLibrary    locale=de-DE    AS    Faker


*** Test Cases ***
TestCase 1
    ${IBAN}    Iban
    Log To Console    IBAN: ${IBAN}

    ${Email}    Email    domain=robotframework.org
    Log To Console     EMAIL: ${Email}
    
    ${Address}    Address
    Log To Console    Addr: ${Address}