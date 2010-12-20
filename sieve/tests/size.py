import operator

import sieve.grammar
import sieve.validators

__all__ = ('SieveTestSize',)

# section 5.9
class SieveTestSize(sieve.grammar.Test):

    RULE_IDENTIFIER = 'SIZE'

    COMPARISON_FNS = {
            'OVER' : operator.gt,
            'UNDER' : operator.lt,
            }

    def __init__(self, arguments=None, tests=None):
        super(SieveTestSize, self).__init__(arguments, tests)
        tagged_args, positional_args = self.validate_arguments(
                {
                    'size' : sieve.validators.Tag(
                                ('OVER', 'UNDER'),
                                (sieve.validators.Number(),)
                                ),
                }
            )
        self.validate_tests_size(0)
        self.comparison_fn = COMPARISON_FNS[tagged_args['size'][0]]
        self.comparison_size = tagged_args['size'][1]

    def evaluate(self, message, state):
        # FIXME: size is defined as number of octets, whereas this gives us
        # number of characters
        message_size = len(message.as_string())
        return self.comparison_fn(message_size, self.comparison_size)

SieveTestSize.register()
