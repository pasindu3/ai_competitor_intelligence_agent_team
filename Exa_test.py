#pip install exa-py

from exa_py import Exa

exa = Exa(api_key = "88f753d0-aa11-4e49-bc22-79c56733ad24")

result = exa.search_and_contents(
  "cool blog post about generative AI (RAG, LLM, Agentic workflows, Agents)",
  text = True,
  type = "fast",
  livecrawl = "always"
)