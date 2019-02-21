import operator
from functools import partial
from typing import NamedTuple, List, Iterable
import itertools

import toolz


class NextQuestionScore(NamedTuple):
    question_id: str
    score: float = None

    get_text = operator.attrgetter('text')
    get_question_id = operator.attrgetter('question_id')


def cumulate_scores(questions: List[NextQuestionScore]) -> NextQuestionScore:
    unique_id, = set(question.question_id for question in questions)
    return NextQuestionScore(
        question_id=unique_id,
        score=sum(question.score for question in questions)
    )


def additive_combine(duplicated_questions: Iterable[NextQuestionScore]) -> Iterable[NextQuestionScore]:
    duplicated_questions_ordered_by_ids = sorted(
        duplicated_questions,
        key=NextQuestionScore.get_question_id
    )

    grouped_questions = [
        cumulate_scores(list(same_id_questions))
        for _, same_id_questions
        in itertools.groupby(duplicated_questions_ordered_by_ids, key=NextQuestionScore.get_question_id)
        ]

    return grouped_questions


def additive_combinez(duplicated_questions: Iterable[NextQuestionScore]) -> Iterable[NextQuestionScore]:
    return toolz.reduceby(
        key=NextQuestionScore.get_question_id,
        binop=lambda q1, q2: NextQuestionScore(q1.question_id, q1.score + q2.score),
        seq=duplicated_questions
    ).values()


if __name__ == '__main__':
    candidates_a = [NextQuestionScore('A', 2.), NextQuestionScore('B', 2.)]
    candidates_b = [NextQuestionScore('B', .5), NextQuestionScore('C', 1.)]

    print(list(additive_combine(itertools.chain(candidates_a, candidates_b))))
    # [NextQuestionScore(question_id='A', score=2.0),
    #  NextQuestionScore(question_id='B', score=2.5),
    #  NextQuestionScore(question_id='C', score=1.0)]

    print(list(additive_combinez(toolz.concatv(candidates_a, candidates_b))))

    must_ask_questions = [NextQuestionScore("business_question1"), NextQuestionScore("business_question2")]

    print(list(
        toolz.pipe(
            toolz.concatv(candidates_a, candidates_b),
            additive_combinez,
            lambda questions: toolz.interleave((must_ask_questions, questions))
        )
    ))
