import ollama

response = ollama.chat(
    model="gemma",
    messages=[
        {
            "role": "user",
            "content": "You are a car assistant and the driver is getting sleepy. \
                        What do you say to them? Just one sentence response",
        },
    ],
)
print(response["message"]["content"])
