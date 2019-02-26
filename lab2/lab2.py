# Lab 2
# Chit-chat ChatBots

# In the previous lab, we explored models that try to answer questions
# by reasoning over free-text inputself.

# In this lab, we will explore two types of models to create chatbots.

# First, let's consider important qualities for a chatbot system
# 1. Readability - whatever model we use, the chats it creates should be
# easily understood by humans

# 2. Consistency - when chatting with a chatbot, the bot should maintain
# consistent information. Imagine a bot that says ``Hi I'm Jack'' and then
# ``Hello, my name is Jane'' - quite confusing

# 3. Engaging - To encourage users to talk to the bot, the bot should be
# able to generate interesting, engaging responses. If the only response was
# ``wow, that's cool,'' users are quite unlikely to want to talk very much
# to the chat bot


# DATA
# The dataset we will use for this lab is called ``PersonaChat'' - it was
# created to directly address problem 2. Each person talking in the dataset
# has a personality, which helps maintain consistency in the dialogue

# Let's download the data and take a look at some examples
python examples/display_data.py --task personachat --datatype train

# Questions to ask yourself:
# What do the personalities look like?
# What are some drawbacks of these personalities for addressing the problem of consistency?

# Let's understand how much data we have. Try to compute the following:

# 1. How many turns of data do we have?
# In dialogue datasets, "amount of data" is measured in dialogue turns.
# Each time there is a single line of dialogue, that is called a "turn"

# 2. On average, how many lines form a persona?


# MODELS

# As discussed in the lecture, there are two main kinds of dialogue models

# Retrieval Models analyze the current dialogue context
# and try to find appropriate responses in the dataset

# Generative Models analyze the current dialogue context
# and try to write an answer, word by word, from left to right.
# This can be thought of as an application of sequence-to-sequence models,
# where the "encoder side" is the dialogue history and the "decoder side"
# is the dialogue response your chatbot should generate

# Questions to ask yourself:
# Review the pros/cons of retrieval compared to generative models
# Are there settings when you might want to use one over the other?
# Compare a chit-chat application to something like booking a movie ticket-
# would you want to use generative, retrieval, or something else to accomplish
# that task?

# RETRIEVAL

# Running a Retrieval Model
python examples/train_model.py -m transformer_ranker -t convai2 -dt train --batchsize 16 --learning-rate 8e-05 -veps 0.25 --model-file persona_chat_retrieval_model -vmt accuracy --batch-eval False

# Let's unpack what's going on here

# -m means which model we're going to use. "transformer" means the transformer architecture
# "ranker" refers to "ranking loss," or how retrieval models are trained.
# Recall they are trained to rank the true response higher over a set of potential
# responses from the dataset (in ParlAI, these are called the "label candidates")
# When it's time to write a dialogue response, the retrieval model returns the response
# that is ranked the highest

# -t refers to the task. Here, we are training on PersonaChat data

# -dt refers to the data split. We want to train our model, so we are using the training setself.

# -veps refers to how often we should evaluate during training, our performance on validation
# recall this is important because models, particularly neural ones, have the capacity
# to memorize the training dataset. So it's important to check how the model is doing on the
# validation set.

# --model-file refers to when your model is saved, what should the filename be

# -vmt refers to the metric which we'll use to decide which model is the best. We'll cover this in
# the next section

# --batch-eval

TODO
