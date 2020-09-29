from email.message import Message
from typing import (
    TYPE_CHECKING,
    List,
    Optional,
    Union,
    SupportsInt,
    Text
)
from sifter.grammar.test import Test
from sifter.grammar.state import EvaluationState

if TYPE_CHECKING:
    from sifter.grammar.tag import Tag as TagGrammar
    from sifter.grammar.string import String


# section 5.10
class TestTrue(Test):

    RULE_IDENTIFIER = 'TRUE'

    def __init__(
        self,
        arguments: Optional[List[Union['TagGrammar', SupportsInt, List[Union[Text, 'String']]]]] = None,
        tests: Optional[List['Test']] = None
    ) -> None:
        super().__init__(arguments, tests)
        self.validate()

    def evaluate(self, message: Message, state: EvaluationState) -> Optional[bool]:
        return True


TestTrue.register()
