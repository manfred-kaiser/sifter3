from email.message import Message
from typing import (
    Optional
)


from sifter.grammar.state import EvaluationState
from sifter.grammar.test import Test
from sifter.validators.stringlist import StringList


# section 5.9
class TestExists(Test):

    RULE_IDENTIFIER = 'EXISTS'
    POSITIONAL_ARGS = [StringList()]

    def evaluate(self, message: Message, state: EvaluationState) -> Optional[bool]:
        headers = self.positional_args[0]
        if not isinstance(headers, list):
            raise ValueError("TestExists.headers must be a list")
        for header in headers:
            if header not in message:
                return False
        return True
