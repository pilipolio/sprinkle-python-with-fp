from typing import Set

from flows.model import Question, Answer


def answer_first_possible(question: Question) -> Answer:
    return next(iter(question.possible_answers))


def answer_based_on_predefined_text(question: Question, predefined_texts_to_say_yes_to: Set[str]) -> Answer:

    last_answer_as_default = question.possible_answers[-1]

    first_positive_or_last_answer = next((
        answer for answer in question.possible_answers
        if answer.text in predefined_texts_to_say_yes_to),
        last_answer_as_default
    )

    return first_positive_or_last_answer
