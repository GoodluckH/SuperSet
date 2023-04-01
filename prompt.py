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


def generate_simple_prompt_template():
    """Generate a simple prompt template. 
    
    This template is used to generate a problem set based on a textbook.
    Required input variables: textbook, chapters, num_questions
    """
    return PromptTemplate(
        input_variables=["textbook", "chapters", "num_questions"],
        template=SIMPLE_TEMPLATE,
    )