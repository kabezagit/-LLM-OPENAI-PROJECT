# LLM-OPENAI PROJECT

## About this App

This application is an interactive AI chatbot built using [Streamlit](https://streamlit.io/), [LangChain](https://www.langchain.com/), and [OpenAI](https://openai.com/). 
It provides a simple web interface where users can type questions and receive intelligent, conversational responses powered by OpenAI's GPT-4.1 model. 
The app demonstrates how to combine prompt engineering, large language models, and a modern Python web framework to create a practical, user-friendly AI assistant. 
It is ideal for learning, prototyping, or deploying a basic conversational AI solution.

## Features

- Conversational AI: Chat with an AI assistant powered by OpenAI's GPT-4.1.
- Custom Prompting: Uses LangChain's prompt templates for flexible and context-aware conversations.
- Streamlit UI: Clean, interactive web interface for easy user interaction.
- Tracing Support: LangChain tracing enabled for debugging and monitoring (optional).

Prerequisites

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)

Installation

1. Clone the repository:**
   ```bash
   git clone https://github.com/kabezagit/-LLM-OPENAI-PROJECT.git
   cd -LLM-OPENAI-PROJECT/LangChain
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Create a `requirements.txt` with the following if not present: `streamlit langchain langchain-openai`)*

3. Set environment variables:**

   You must set your OpenAI and LangChain API keys as environment variables before running the app:

   - `OPENAI_API_KEY`: Your OpenAI API key
   - `LANGCHAIN_API_KEY`: Your LangChain API key (if required)

   On Windows (Command Prompt):
   ```cmd
   set OPENAI_API_KEY=your-openai-key
   set LANGCHAIN_API_KEY=your-langchain-key
   ```

 4. Run the app:
   ```bash
   streamlit run LangSmith.py
   ```

 Usage

- Open the app in your browser (Streamlit will provide a local URL).
- Type your question in the input box and press Enter.
- The chatbot will respond using OpenAI's GPT-4.1 model.

File Structure

```
LangChain/
├── LangSmith.py      # Main Streamlit app
├── README.md         # Project documentation
├── requirements.txt  # Python dependencies
└── ...               # Other project files
```

Environment Variables

- `OPENAI_API_KEY` (required): Your OpenAI API key.
- `LANGCHAIN_API_KEY` (optional): Your LangChain API key.
- `LANGCHAIN_TRACING_V2` (optional): Set to `"true"` to enable advanced tracing.

  Acknowledgments

- [LangChain](https://www.langchain.com/)
- [OpenAI](https://openai.com/)
- [Streamlit](https://streamlit.io/)

