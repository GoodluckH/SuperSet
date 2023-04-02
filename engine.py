"""This is the core module for the backend service. It contains
functions that interact with OpenAI's API.
"""

from dotenv import load_dotenv
from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI

from utils import get_number_of_tokens

load_dotenv()

MAX_TOKENS_TEXT_DAVINCI_003 = 4097
MAX_TOKENS_GPT_4 = 8000


def generate_problem_set(prompt_template: PromptTemplate, **kwargs):
    """Generate a problem set based on a prompt template.

    Args:
        prompt_template (PromptTemplate): the prompt template 

        **kwargs: the input variables for the prompt template. The keys
            should be the same as the input variables in the prompt.

    Returns:
        str: the generated problem set
    """
    # generate the prompt
    # prompt = prompt_template.format(**kwargs)
    model_name = "text-davinci-003"
    llm_chain = LLMChain(
        prompt=prompt_template,
        llm=OpenAI(
            model_name=model_name,
            temperature=1,
            max_tokens=MAX_TOKENS_TEXT_DAVINCI_003 -
            get_number_of_tokens(model_name, prompt_template.format(**kwargs))))
    result = llm_chain.predict(**kwargs)

    # call openai

    # return the generated problem set
    return result
