def send_messages(messages, sent_messages):
    for message in messages:
        print(f"Sending: {message}")
        sent_messages.append(message)

messages = ["Hello, world!", "Hello, Python!", "Hello, C++!"]

sent_messages = []
send_messages(messages, sent_messages)
print("Original messages:", messages)
print("Sent messages:", sent_messages)