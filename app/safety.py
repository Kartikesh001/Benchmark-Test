BLOCKED_KEYWORDS = [
    "bomb",
    "malware",
    "hack",
    "steal password",
    "explosive"
]


def is_safe(text):
    text = text.lower()

    for keyword in BLOCKED_KEYWORDS:
        if keyword in text:
            return False

    return True


def refusal_message():
    return (
        "I can't assist with harmful, illegal, "
        "or dangerous activities."
    )