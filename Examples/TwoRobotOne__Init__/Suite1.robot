*** Settings ***
Suite Setup    Log To Console    Before All Tests Of One File
Test Setup     Log To Console    Before Each Test
Test Teardown    Log To Console    After Each Test
Suite Teardown    Log To Console    After All Tests Of One File
Metadata       Level    Robot File

*** Test Cases ***
Test 1.1
    Log    Something

Test 1.2
    Log     Something