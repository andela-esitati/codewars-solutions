def duplicate_count(text):
    # Your code goes here
    return len(set([char for char in text.lower() if text.lower().count(char) > 1]))
