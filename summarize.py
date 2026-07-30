from transformers import pipeline

bot = pipeline("summarization", model= "facebook/bart-large-cnn")

text_to_summarize = ("The tiger (Panthera tigris) is a large cat and a member of the genus Panthera native to Asia. It is recognisable by its black, vertical stripes on orange fur. It is traditionally classified into nine subspecies, though some recognise only two subspecies. Tigers currently inhabit the Indian subcontinent, Southeast Asia, and the Russian Far East and Northeast China. They mainly live in forested habitats, where they lead a mostly solitary life. They are apex predators and prey mainly on hooved mammals.")

summarization = bot(text_to_summarize, max_length= 130)

print(f"Here's the summarization = {summarization}")