from typing import List

from flows.model import Answer, NextStepStrategy, AnsweringStrategy, NextStep


def simulate(
        next_step_strategy: NextStepStrategy,
        answering_strategy: AnsweringStrategy) -> (List[Answer], List[NextStep]):
    steps = []
    answers = []

    while True:
        next_step = next_step_strategy(answers)
        steps.append(next_step)

        if next_step.question is not None:
            chosen_answer = answering_strategy(next_step.question)
            answers.append(chosen_answer)
        else:
            return answers, steps
