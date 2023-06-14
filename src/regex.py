import re

def _process_logic_operations(text: str) -> str:
    """Standardize the logic operations (and, or, not).

    Args:
        text (str): Input text.

    Returns:
        str: Output standardized text.
    """
    pat_or = re.compile(r"([\s]*(\|\||\|)[\s]*)|[\s]+or([\s]+)")
    pat_and = re.compile(r"[\s]*(\&|\&\&|and)[\s]*")
    pat_not = re.compile(r"[\s]*([^'])not(^'\()?[\s]*")
    
    text = pat_or.sub(" | ", text)
    text = pat_and.sub(" & ", text)
    text = pat_not.sub(" - ", text)

    text = text.strip()
    return text

def _clean_quotation_marks(text: str) -> str:
    """Clean the quotation marks (', ").

    Args:
        text (str): Input text.

    Returns:
        str: Output standardized text.
    """
    pat_quo = re.compile(r"[\"\']{1}")
    return pat_quo.sub("", text)


def preprocess(text: str) -> str:
    text = _process_logic_operations(text)
    text = _clean_quotation_marks(text)
    return text