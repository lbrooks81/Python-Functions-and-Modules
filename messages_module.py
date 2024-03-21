def show_messages(messages : list) -> list:
    sent_messages : list = []
    for message in messages:
        print(message)
        sent_messages.append(message)
    messages.clear()
    return sent_messages
