from functools import partial

import toolz

from flows.model import Question, Answer


algorithmic_generated_questions = [
    Question(1, 'baba?', [Answer(1, 'ba'), Answer(1, 'ab')]),
    Question(2, 'cdcd?', [Answer(2, 'cd'), Answer(2, 'dc')]),
    Question(3, 'cdcd?', [Answer(3, 'ba'), Answer(3, 'ab')])
    ]


def reformulate(question: Question) -> Question:
    return Question(
        question.id,
        question.text + '!',
        question.possible_answers
    )


def add_last_answer(question: Question, text: str) -> Question:
    return Question(
        question.id,
        question.text,
        question.possible_answers + [Answer(question.id, text)]
    )


def is_appropriate(question: Question) -> bool:
    return question.text.startswith('bb')


business_rules_questions = [
    Question(10, 'bizness?', [Answer(10, 'biz'), Answer(10, 'ness')]),
    Question(20, 'nezbis?', [Answer(20, 'nez'), Answer(20, 'bis')])
    ]


questions_to_ask = filter(
    is_appropriate,
    toolz.interleave((
        toolz.take(1, business_rules_questions),
        map(toolz.compose(reformulate, partial(add_last_answer, text='non')),
            algorithmic_generated_questions)
       )))

print(list(questions_to_ask))