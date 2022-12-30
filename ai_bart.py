from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=0)

def process_query(query):
    return summarizer(query, max_length=130, min_length=30, do_sample=False)[0]['summary_text']