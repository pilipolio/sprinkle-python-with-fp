from functools import partial

from flows import execution, flow_strategies, answering
from flows.model import Question, AnsweredQuestion

flow_client = flow_strategies.RestClient('xxx')

# Simulating a flow with scripted answers (useful for tests)
known_in_advance_question = Question(id=1, text='?', possible_answers=[AnsweredQuestion(1, 'yes', 10)])
question_to_answers = {
     known_in_advance_question: known_in_advance_question.possible_answers[0]
}

# Simulating a flow with random answers
execution.simulate_flow(
    next_flow_step=flow_client.next_step,
    question_strategy=question_to_answers.get
)

# Simulating a flow by answering to questions based on a fixed list of symptoms
positive_symptom_concepts = [1, 3]

answers, (*question_steps, (_, outcome)) = execution.simulate_flow(
    next_flow_step=flow_client.next_step,
    question_strategy=partial(answering.concept_based_strategy, positive_symptom_concepts=positive_symptom_concepts)
)
