import requests

from typing import NamedTuple, List

from flows.model import Answer, NextStep


class RestClient(NamedTuple):
    auth_token: str

    def next_step(self, answered_question: List[Answer]) -> NextStep:
        return None