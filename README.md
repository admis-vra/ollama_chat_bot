# ollama_chat_bot
Full Project Description (for README or About section)

This project is a lightweight command-line chat assistant built with Python and Ollama.
It allows you to talk to local large language models (LLMs) such as Llama 3.2, Mistral, or Gemma, right from your terminal — without needing an internet connection or API key.

The script demonstrates how to send structured messages (system, user) to an Ollama model and print back responses in real-time. It’s clean, minimal, and great for beginners learning how to interact with AI models locally.

You can easily:
~ Change the model name in one line.
~ Edit the system prompt to create your own chatbot personality.
~ Use it as a template for future AI projects or automation tools.

# 🧠 Ollama Chat Assistant

A simple command-line chatbot powered by [Ollama](https://ollama.ai/).  
It uses the **llama3.2** model (or any Ollama-supported model) to respond to your prompts.

---

## 🚀 Features
- Chat with a local LLM via terminal
- Works with any Ollama model (just change the model name)
- Easy to set up and run

---

## 🧩 Requirements
- Python 3.10 or newer  
- [Ollama](https://ollama.ai/) installed and running locally  
- Model pulled via Ollama (e.g. `ollama pull llama3.2`)

---

## ⚙️ Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/admis_vra/ollama_chat_bot.git
   cd ollama_chat_bot
   
## Install dependencies
   ```
   pip install -r requirements.txt
   ```


## Run the script 
   ``` 
   python ollama_chat.py
   ```
# Chat with your assistant


You: What is AI?

Assistant: Artificial Intelligence is...

🧠 Example Output

💬 Ollama Chat Assistant

- Type 'exit' anytime to stop.

You: Who is Elon Musk?
Assistant: Elon Musk is a technology entrepreneur and CEO of Tesla, SpaceX...

# 🧩 Customization
You can edit SYSTEM_PROMPT in main.py to change your assistant’s personality.

- Example:

   SYSTEM_PROMPT = "You are a funny assistant who replies with jokes and emojis!"

# 🛠️ Author

    @admis-vra

   🌐 GitHub: https://github.com/admis-vra

