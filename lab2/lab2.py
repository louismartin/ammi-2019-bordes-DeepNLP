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
