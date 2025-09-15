import bs4

from langchain_ollama import ChatOllama
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_community.tools import DuckDuckGoSearchResults


llm = ChatOllama(model="llama3")


search = DuckDuckGoSearchResults()

def run_research_task(topic: str):
    """
    This function performs an intelligent research task that won't fail.
    """
    print(f"--- Starting intelligent research for: {topic} ---")

    
    print("Searching for relevant URLs...")
    search_results = search.run(topic)
    print("Search results received.")

    
    print("Choosing the best URL...")
    
    chooser_template = """
    Based on the following DuckDuckGo search results, which URL is the single most promising one to answer the question: "{question}"?

    Please return ONLY the URL and nothing else.

    Search Results:
    {results}

    Selected URL:
    """
    chooser_prompt = PromptTemplate.from_template(chooser_template)
    chooser_chain = chooser_prompt | llm | StrOutputParser()
    
    chosen_url = chooser_chain.invoke({"results": search_results, "question": topic})
    print(f"LLM chose URL: {chosen_url}")

    
    if not chosen_url or not chosen_url.startswith('http'):
        print("LLM failed to provide a valid URL.")
        return "Failed to find a relevant URL."
        
    print(f"Scraping content from {chosen_url}...")
    try:
        loader = WebBaseLoader(
            web_paths=(chosen_url,),
            bs_kwargs=dict(parse_only=bs4.SoupStrainer("p")),
        )
        docs = loader.load()
        scraped_text = " ".join([d.page_content for d in docs])
        scraped_text = " ".join(scraped_text.split())
        print("Content scraped successfully.")
    except Exception as e:
        print(f"Error scraping the URL: {e}")
        return "Failed to scrape the website."

    
    print("Summarizing the content...")
    
    
    summarizer_template = """
    Based on the following content, please provide a concise summary of the key most important information.
    
    Content:
    {content}
    
    Summary:
    """
    summarizer_prompt = PromptTemplate.from_template(summarizer_template)
    summarizer_chain = summarizer_prompt | llm | StrOutputParser()
    
    
    summary = summarizer_chain.invoke({"content": scraped_text})
    
    print("--- Research complete! ---")
    return f"Source URL: {chosen_url}\n\nSummary:\n{summary}"


if __name__ == "__main__":
    topic_to_research = "Who is MasterChief"
    final_summary = run_research_task(topic_to_research)
    print("\n--- FINAL SUMMARY ---")
    print(final_summary)