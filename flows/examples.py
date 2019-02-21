from functools import partial

from flows import conversation, questioning, answering
from flows.model import Question, Answer

flow_client = questioning.RestClient('xxx')

# Simulating a flow with scripted answers (useful for tests)
known_in_advance_question = Question(id=1, text='?', possible_answers=[Answer(1, 'yes', 10)])
question_to_answers = {
     known_in_advance_question: known_in_advance_question.possible_answers[0]
}

# Simulating a flow with random answers
conversation.simulate(
    next_flow_step=flow_client.next_step,
    question_strategy=question_to_answers.get
)

# Simulating a flow by answering to questions based on a fixed list of symptoms
positive_symptom_concepts = [1, 3]

answers, (*question_steps, (_, outcome)) = conversation.simulate(
    next_flow_step=flow_client.next_step,
    question_strategy=partial(answering.answer_based_on_predefined_text, positive_symptom_concepts=positive_symptom_concepts)
)
