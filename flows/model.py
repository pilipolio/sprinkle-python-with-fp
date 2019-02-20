from typing import NamedTuple, Optional, List, Callable


class AnsweredQuestion(NamedTuple):
    question_id: int
    text: str
    concept_id: int


class Question(NamedTuple):
    id: int
    text: str
    possible_answers: List[AnsweredQuestion]


class Outcome(NamedTuple):
    text: str
    category_iri: str


class NextStep(NamedTuple):
    question: Optional[Question]
    outcome: Optional[Outcome]


AnsweringStrategy = Callable[[Question], AnsweredQuestion]
FlowStrategy = Callable[[List[AnsweredQuestion]], NextStep]
