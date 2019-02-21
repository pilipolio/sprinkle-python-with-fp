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


from abc import ABC, abstractmethod


class AnsweringStrategyInterface(ABC):
    @abstractmethod
    def answer(self, question: Question) -> Answer:
        pass


class QuestioningStrategyInterface(ABC):
    @abstractmethod
    def next(self, answers: List[Answer]) -> NextStep:
        pass


class TextBasedAnsweringStrategy(AnsweringStrategyInterface):
    def __init__(self, text_to_say_yes_to: List[str]):
        self.text_to_say_yes_to = text_to_say_yes_to

    def answer(self, question: Question) -> Answer:
        pass
