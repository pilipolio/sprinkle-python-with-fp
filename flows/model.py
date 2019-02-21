from typing import NamedTuple, Optional, List, Callable


class Answer(NamedTuple):
    question_id: int
    text: str


class Question(NamedTuple):
    id: int
    text: str
    possible_answers: List[Answer]


class FinalDecision(NamedTuple):
    text: str


class NextStep(NamedTuple):
    question: Optional[Question]
    outcome: Optional[FinalDecision]


AnsweringStrategy = Callable[[Question], Answer]
NextStepStrategy = Callable[[List[Answer]], NextStep]
