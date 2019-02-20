import operator
from typing import NamedTuple, List
from itertools import chain, groupby


class NextQuestion(NamedTuple):
    text: str
    score: float

    by_tezxt = operator.attrgetter('text')
    by_question = operator.attrgetter('question')

def cumulate_scores(questions: List[NextQuestion]) -> NextQuestion:
    unique_text, = set(question.text for question in questions)
    return NextQuestion(text=unique_text, score=sum(question.score for question in questions))


def combine(first: List[NextQuestion], second: List[NextQuestion]) -> List[NextQuestion]:
    groupby()
    return sorted(chain(first, second), key=operator.attrgetter('question'))


if __name__ == '__main__':
    first = [NextQuestion('A', 2.), NextQuestion('B', 2.)]
    second = [NextQuestion('B', .5), NextQuestion('C', 1.)]
