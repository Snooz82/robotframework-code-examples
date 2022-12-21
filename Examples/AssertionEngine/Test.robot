*** Settings ***
Library     Library.py
Library     String

*** Variables ***
${locator_Ac}     value_1234   #returns "1234"
${locator_Bc}     value_2356   #returns "2356"
${loc_count}      value_data  (3590)   #returns "data (3590)"

*** Test Cases ***
Test
  ${ABC}  Get Text  ${locator_Ac}
  ${DEF}  Get Text  ${locator_Bc}
  ${count}  Evaluate  ${ABC} + ${DEF}
  Log to Console  \${count}:${{type($count)}}:${count}
  ${count_str}  Get Text  ${loc_count}
  Log to Console  \${count_str}:${{type($count_str)}}:${count_str}
  ${shorter_count_str}  Remove String  ${count_str}  data (
  ${final_count_str}  Remove String  ${shorter_count_str}  )
  Log To Console    ${final_count_str}
  Should Be Equal As Numbers   ${count}  ${final_count_str}

Test 2
  ${ABC}  Get Text  ${locator_Ac}
  ${DEF}  Get Text  ${locator_Bc}
  ${count}  Evaluate  ${ABC} + ${DEF}
  Log to Console  \${count}:${{type($count)}}:${count}
  ${count_str}  Get Text  ${loc_count}
  Log to Console  \${count_str}:${{type($count_str)}}:${count_str}
  ${final_count_str}  Remove String Using Regexp  ${count_str}  \\D
  Log to Console  \${final_count_str}:${{type($final_count_str)}}:${final_count_str}
  Should Be Equal As Numbers   ${count}  ${final_count_str}