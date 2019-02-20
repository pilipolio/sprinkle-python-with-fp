import requests

from typing import NamedTuple, List

from flows.model import AnsweredQuestion, NextStep


class RestClient(NamedTuple):
    auth_token: str

    def next_step(self, answered_question: List[AnsweredQuestion]) -> NextStep:
        return None