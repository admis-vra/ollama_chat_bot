import ollama

System_prompt = "You are a helpful assistant that can answer questions and help with tasks."

user_prompt = input("Enter your prompt: ")

while user_prompt.lower() != "exit":
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": System_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    print("\nAssistant:", response['message']['content'], "\n")
    user_prompt = input("Enter your prompt: ")
