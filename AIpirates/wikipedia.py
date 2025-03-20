import wikipedia

wikipedia.set_lang("en")  # Set language to Spanish
try:
    print(wikipedia.search("Artifical Intelligence"))

    summary = wikipedia.summary("Artifical Intelligence")
    print(summary)
except wikipedia.exceptions.PageError as e:
    print(f"Page error: {e}")
except wikipedia.exceptions.DisambiguationError as e:
    print(f"Disambiguation error: {e.options}")
