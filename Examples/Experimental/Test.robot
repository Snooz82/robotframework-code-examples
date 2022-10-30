*** Settings ***
Library    OperatingSystem


*** Test Cases ***
TestCase 1
    File Should Exist    ${CURDIR}/Test.robot
    My Keyword
    Log      This is another log message

*** Keywords ***
My Keyword
    Log     This is a log message