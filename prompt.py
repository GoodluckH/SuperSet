"""This module contains the prompt templates for the problem set
generation
"""

from langchain import PromptTemplate

SIMPLE_TEMPLATE = """
I want you to act as a professor and write a problem set based on a
textbook. The textbook is {textbook}.

If you don't have any knowledge about this textbook, then just say "I
don't have much information about this textbook."

Otherwise, you can write a problem set with {num_questions} questions
for each of the following chapters (and their subsections): {chapters}.

Again, if you don't have any knowledge about these chapters, then just
say "I don't have much information about these chapters."

Make sure you only output a problem set. Don't output any other text.

Strictly format your problem set as follows in markdown format:

### chapter:

    1. question 1
    2. question 2
    3. question 3
    ...
"""

TEXTBOOK_TEMPLATE = """
I want you to act as a professor and write a problem set based on an
excerpt of a textbook.

You can write a problem set with {num_questions} questions.

DO NOT ASK BASIC "WHAT IS" QUESTIONS.

You are highly encouraged to make up scenarios and examples to make the
questions more interesting.

They must be difficult and sufficiently long (at least two sentences).

You must include a mix of formats such as multiple choices,
fill-in-the-blanks, etc. Do not use only one format.

I you don't have any knowledge about these chapters, then just say "I
don't have much information about these chapters."

DO NOT INCLUDE ANSWERS.

Strictly format your problem set with numbered bullets with line breaks.

The excerpt is:

{excerpt}
"""


def generate_simple_prompt_template():
    """Generate a simple prompt template. 

    This template is used to generate a problem set based on a textbook.
    Required input variables: textbook, chapters, num_questions
    """
    return PromptTemplate(
        input_variables=["textbook", "chapters", "num_questions"],
        template=SIMPLE_TEMPLATE,
    )


def generate_textbook_prompt_template():
    """Generate a textbook prompt template.

    This template is used to generate a problem set based on a textbook
    excerpt.
    Required input variables: num_questions, excerpt
    """
    return PromptTemplate(
        input_variables=["num_questions", "excerpt"],
        template=TEXTBOOK_TEMPLATE,
    )
