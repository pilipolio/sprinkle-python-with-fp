from functools import partial

from flows import conversation, questioning, answering
from flows.model import Question, Answer

questioning_strategy = questioning.RestClient('xxx')

# Simulating a conversation with a stubbed/scripted answering strategy (useful for tests)
known_in_advance_question = Question(id=1, text='?', possible_answers=[Answer(1, 'yes', 10)])
question_to_answers = {
     known_in_advance_question: known_in_advance_question.possible_answers[0]
}

conversation.simulate(
    next_flow_step=questioning_strategy.next_step,
    question_strategy=question_to_answers.get
)

# Simulating a conversation by answering to questions based on a fixed list of text to say yes to
positive_answer_texts = set(['no'])

scripted_answering_strategy = partial(
    answering.answer_based_on_predefined_text,
    positive_symptom_concepts=positive_answer_texts)

answers, (*question_steps, (_, outcome)) = conversation.simulate(
    next_flow_step=questioning_strategy.next_step,
    question_strategy=scripted_answering_strategy
)
