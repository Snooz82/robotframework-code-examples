from assertionengine.assertion_engine import verify_assertion, AssertionOperator
from typing import Optional

def get_text(selector: str, assertion_operator: Optional[AssertionOperator] = None, assertion_expected: str = ""):
    return verify_assertion(selector.split("_")[1], assertion_operator, assertion_expected) 