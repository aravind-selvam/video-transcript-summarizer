import sys

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from videosum.exception import CustomException
from videosum.logger import logger


def summarize_text(transcript):
    """
    It takes a transcript, tokenizes it, and then generates a summary using the BART model

    Args:
      transcript: The text you want to summarize.

    Returns:
      A summary of the text.
    """
    try:
        logger.info("initiating summarizer...")
        tokenizer = AutoTokenizer.from_pretrained(
            "philschmid/bart-large-cnn-samsum")
        model = AutoModelForSeq2SeqLM.from_pretrained(
            "philschmid/bart-large-cnn-samsum")
        logger.info("tokenizer and model were downloaded from huggingface")

        inputs = tokenizer(transcript,
                           max_length=1024,
                           truncation=True,
                           return_tensors="pt")

        summary_ids = model.generate(
            inputs["input_ids"], num_beams=2, min_length=50, max_length=1024)
        summary = tokenizer.batch_decode(
            summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        return summary
    except Exception as e:
        raise CustomException(e, sys)
