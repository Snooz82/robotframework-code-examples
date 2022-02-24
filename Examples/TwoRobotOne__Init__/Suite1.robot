*** Settings ***
Suite Setup    Log To Console    ⬆️ Before All Tests Of One File
Test Setup     Log To Console    \n↗️ Before Each Test
Test Teardown    Log To Console    ↘️ After Each Test
Suite Teardown    Log To Console    ⬇️ After All Tests Of One File
Metadata       Level    Robot File

*** Test Cases ***
Test 1.1
    Log To Console   ➡️ In Test 1.1

Test 1.2
    Log To Console    ➡️ In Test 1.2