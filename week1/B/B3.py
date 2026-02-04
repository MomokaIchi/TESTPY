# Rewrite in one line:
def is_empty(text):
    if text == "":
        return True
    return False

def is_empty_clean(text) -> bool:
    return not text == ""