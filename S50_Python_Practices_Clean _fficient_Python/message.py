from typing import List, Dict


def unique_messages_within_window(window: int, messages: List[Dict[str, int]]) -> List[Dict[str, int]]:
    if not messages:
        return []

    # Sort messages by timestamp to easily get the latest message timestamp
    messages_sorted = sorted(messages, key=lambda x: x['timestamp'])
    latest_timestamp = messages_sorted[-1]['timestamp']

    # Filter messages within the time window
    filtered_messages = [
        msg for msg in messages_sorted
        if latest_timestamp - msg['timestamp'] <= window
    ]

    # Use a dictionary to track the latest occurrence of each unique message by content
    unique_messages = {}
    for msg in filtered_messages:
        unique_messages[msg['content']] = msg  # Keeps the latest occurrence due to sorted order

    # Return only the unique messages, in the order of their occurrence in the filtered list
    return list(unique_messages.values())
window = 5
messages = [
    {'content': 'hello', 'timestamp': 1},
    {'content': 'world', 'timestamp': 2},
    {'content': 'hello', 'timestamp': 4},
    {'content': 'bye', 'timestamp': 6}
]

print(unique_messages_within_window(window, messages))
