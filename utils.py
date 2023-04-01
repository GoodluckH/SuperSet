"""Helper functions and tools."""
import tiktoken


def get_number_of_tokens(model_name, text):
    """Get the number of tokens for a given model and text."""
    enc = tiktoken.encoding_for_model(model_name)
    tokens = enc.encode(text)
    return len(tokens)