# AI-Agent-Search

> An autonomous AI agent that researches a given topic online, selects the best source, and provides a concise summary.



---

## 🎯 The Problem

Standard search engines are great, but finding a definitive, summarized answer to a specific question can still be time-consuming. It often requires opening multiple tabs, sifting through irrelevant information, and manually piecing together the key points. This process can be inefficient, especially when you need a quick and reliable overview of a topic.

## 💡 The Solution

This project automates the entire research process using an AI agent built with Python and LangChain. When given a topic, the agent performs the following four-step process:

1.  **Search:** It uses DuckDuckGo to perform a web search for relevant articles and sources.
2.  **Select:** It employs a Large Language Model (Llama 3) to analyze the search results and intelligently choose the **single most promising URL** to answer the user's query.
3.  **Scrape:** It extracts the core text content from the chosen webpage using Beautiful Soup.
4.  **Summarize:** It leverages the LLM again to distill the extracted information into a clear, concise, and easy-to-read summary.

The result is a direct answer to your question, complete with the source URL, delivered in seconds.

## 🛠️ Tech Stack

* **Language:** Python 3.13
* **Core Libraries:**
    * `LangChain`: The primary framework for building the agent's logic.
    * `Ollama`: For running the Llama 3 model locally.
    * `Beautiful Soup 4`: For web scraping and parsing HTML.
    * `DuckDuckGo Search`: For the web search functionality.
* **LLM:** Llama 3

## 🚀 How to Use It

### Prerequisites

You must have **Ollama** installed and running on your machine.
1.  [Install Ollama](https://ollama.com/).
2.  Pull the Llama 3 model by running the following command in your terminal:
    ```bash
    ollama run llama3
    ```

### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/AI-Agent-Search.git](https://github.com/your-username/AI-Agent-Search.git)
    ```
2.  **Navigate to the directory:**
    ```bash
    cd AI-Agent-Search
    ```
3.  **Install the required Python libraries:**
    ```bash
    pip install langchain langchain_community langchain_core langchain_ollama beautifulsoup4 duckduckgo-search
    ```
4.  **Customize the topic:**
    * Open the `main.py` file.
    * Change the `topic_to_research` variable on line 88 to whatever you want to research.
5.  **Run the script:**
    ```bash
    python main.py
    ```
