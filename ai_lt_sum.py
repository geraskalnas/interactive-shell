from transformers import pipeline
my_pipeline = pipeline(task="text2text-generation", model="LukasStankevicius/t5-base-lithuanian-news-summaries-175", framework="pt", device=0)

def process_query(query):
    return my_pipeline(query)[0]["generated_text"]