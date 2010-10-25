import base

# section 5.2
class SieveTestAllOf(base.SieveTest):

    RULE_IDENTIFIER = "ALLOF"

    def __init__(self, arguments=None, tests=None):
        base.SieveTest.__init__(self, arguments, tests)
        self.validate_arguments_size(0)

    def evaluate(self, message, state):
        # short-circuit evaluation if a test is false. the base standard does
        # not specify if all tests must be evaluated or in what order, but the
        # "ihave" extension requires short-circuit left-to-right evaluation
        # (RFC 5463, section 4). so we might as well do that.
        for test in self.tests:
            if not test.evaluate(message, state):
                return False
        return True

base.register_sieve_test(SieveTestAllOf)