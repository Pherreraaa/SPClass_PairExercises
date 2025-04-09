# pe4.py
# Pair Exercise 4
# Paniz and Wyn - Team A
# April 8, 2025

import wikipedia
import time
import os
from concurrent.futures import ThreadPoolExecutor

# Output directory
output_dir = "wiki_refs"
os.makedirs(output_dir, exist_ok=True)

# Clean file
def clean_filename(title):
    return "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()

# SECTION A: Sequential download
def sequential_download():
    start = time.perf_counter()

    topics = wikipedia.search("generative artificial intelligence")

    for topic in topics:
        try:
            page = wikipedia.page(topic, auto_suggest=False)
            title = page.title
            references = page.references

            filename = clean_filename(title) + ".txt"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "w", encoding="utf-8") as file:
                for ref in references:
                    file.write(ref + "\n")

        except Exception as e:
            print(f"[Sequential] Failed to process '{topic}': {e}")

    end = time.perf_counter()
    print(f"Sequential download took {end - start:.2f} seconds.")

# SECTION B
def wiki_dl_and_save(topic):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        title = page.title
        references = page.references

        filename = clean_filename(title) + ".txt"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            for ref in references:
                file.write(ref + "\n")

    except Exception as e:
        print(f"[Concurrent] Failed to process '{topic}': {e}")

def concurrent_download():
    start = time.perf_counter()

    topics = wikipedia.search("generative artificial intelligence")

    with ThreadPoolExecutor() as executor:
        executor.map(wiki_dl_and_save, topics)

    end = time.perf_counter()
    print(f"Concurrent download took {end - start:.2f} seconds.")

if __name__ == "__main__":
    print("Starting sequential download...")
    sequential_download()
    print("\nStarting concurrent download...")
    concurrent_download()
