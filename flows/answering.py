from typing import Set

from flows.model import Question, AnsweredQuestion


def dummy_strategy(question: Question) -> AnsweredQuestion:
    return next(iter(question.possible_answers))


def concept_based_strategy(question: Question, positive_symptoms: Set[int]) -> AnsweredQuestion:

    last_answer_as_default = question.possible_answers[-1]

    first_positive_or_last_answer = next((
        answer for answer in question.possible_answers
        if answer.concept_id in positive_symptoms),
        last_answer_as_default
    )

    return first_positive_or_last_answer
