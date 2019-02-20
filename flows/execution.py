from typing import List

from flows.model import AnsweredQuestion, FlowStrategy, AnsweringStrategy, NextStep


def simulate_flow(
        flow_strategy: FlowStrategy,
        answering_strategy: AnsweringStrategy) -> (List[AnsweredQuestion], List[NextStep]):
    steps = []
    answered_questions = []

    while True:
        next_step = flow_strategy(answered_questions)
        steps.append(next_step)

        if next_step.question is None:
            return answered_questions, steps
        else:
            answered_questions = answered_questions + [answering_strategy(next_step.question)]
