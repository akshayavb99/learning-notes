---
title: LLM Zoomcamp 2026
description: This is the course summary page with my notes for the LLM Zoomcamp 2026 by DataTalksClub
updated_date: 2026-06-12
tags:
  - artificial-intelligence
  - course-summary
  - git
  - large-language-models
  - agentic-ai
---

# LLM Zoomcamp 2026

This is the course summary page for the LLM Zoomcamp by [DataTalksClub](https://github.com/DataTalksClub) on GitHub. The course can be found [here](https://github.com/DataTalksClub/llm-zoomcamp)

## Index

| Lecture                     | Notes                                                                | Homework |
| --------------------------- | -------------------------------------------------------------------- | -------- |
| **Lecture 1 - Agentic RAG** | [1. Agentic Rag](#1-agentic-rag)                                     |          |
| 1.1 Introduction            | [1-1 Introduction](#1-1-introduction)                                |          |
| 1.2 Environment             | [1-2 Environment](#1-2-environment)                                  |          |
| 1.3 What is RAG             | [1-3 What is RAG (Retrieval-Augmented Generation)](#1-3-what-is-rag) |          |
| 1.4 The Course FAQ dataset  | [1-4 The Course FAQ Dataset](#1-4-the-course-faq-dataset)            |          |
| 1.5 Search                  | [1-5 Search](#1-5-search)                                            |          |
| 1.6 Building a Prompt       | [1-6 Building a Prompt](#1-6-building-a-prompt)                      |          |
| 1.7 RAG Pipeline            | [1-7 RAG Pipeline](#1-7-rag-pipeline)                                |          |
| 1.8 RAG Helper              | [1-8 RAG Helper](#1-8-rag-helper)                                    |          |
| 1.9 Data Ingestion          | [1-9 Data Ingestion](#1-9-data-ingestion)                            |          |
| 1.10 RAG Next Steps         | [1-10 RAG Next Steps](#1-10-wrap-up-of-part-1)                       |          |
| 1.11 Agents Intro           | [1-11 Agents Intro](#1-11-agents)                                    |          |
| 1.12 RAG Revision           |                                                                      |          |
| 1.13 Function Calling       | [1-13 Function Calling](#1-13-function-calling)                      |          |
| 1.14 Agentic Loop           | [1-14 The Agentic Loop](#1-14-the-agentic-loop)                      |          |
| 1.15 ToyAIKit               | [1-15 ToyAIKit](#1-15-toyaikit)                                      |          |
| 1.16 Other Frameworks       |                                                                      |          |
| **2. Vector Search**        | [2. Vector Search](#2-vector-search)                                 |          |
| 2.1 What is Vector Search   | [2-1 What is Vector Search](#2-1-what-is-vector-search)              |          |
| 2.2 Embeddings              | [2-2 Embeddings](#2-2-embeddings)                                    |          |
| 2.3 Embedding Our Dataset   | [2-3 Embedding Our Dataset](#2-3-embedding-our-dataset)              |          |
| 2.4 Vector Search           | [2-4 Vector Search](#2-4-vector-search)                              |          |
| 3. Orchestration            | [3. Orchestration](#3-orchestration)                                 |          |
| 4. Evaluation               | [4. Evaluation](#4-evaluation)                                       |          |
| 5. Monitoring               | [5. Monitoring](#5-monitoring)                                       |          |
| 6. Best Practices           | [6. Best Practices](#6-best-practices)                               |          |
| 7. End-to-End Project       | [7. End-to-End Project](#7-end-to-end-project)                       |          |
| Capstone Project            | [Capstone Project](#capstone-project)                                |          |

## 1. Agentic RAG

### 1-1 Introduction

- LLM is to predict the next words, given a set of words.
- LLMs are trained on vast volumes of data available across the Internet, and has millions and billions of parameters in its architecture
- In lecture 1, we treat LLMs as a black box and focus on integrating LLM providers for Retrieval-Augmented Generation (RAG) FAQ agent for the course

### 1-2 Environment

**Pre-requisites**

1. Python (3.14 or later)
2. OpenAI account
3. Python and CLI familiarity
4. `uv` package manager

Create a dedicated repository for the rest of the course (something like llm-zoomcamp-2026-code). When working through local system, clone your repo to your local system

**Step 1: Create the Project from scratch with `uv`**

Ensure you have the `uv` package manager installed - `pip install uv`

**Step 2: Create the project**

```bash
uv add requests minsearch openai jupyter python-dotenv
```

Library dependencies

1. `requests` - Fetch the dataset from the internet
2. `minsearch` - In-memory search engine for searching text
3. `openai` - OpenAI API client (Can use other OpenAI compatible APIs)
4. `jupyter` - Notebook env to write and run code
5. `python-dotenv` - Read env variables

**Step 3: Initialize the project, add the `pyproject.toml` and install the dependencies - `uv init`**

**Step 4: Create the file `notebook.ipynb`** - Notebook for the lesson

**Step 5: Create the `.gitignore`**

```
# .gitignore file

# Virtual Environment
.venv

# Environment variables
.env
```

**Step 6: Store the OpenAI API Key in `.env` in the repo root**

```
# .env file

OPENAI_API_KEY=<your-api-key>
```

> IMPORTANT: Do not share your OpenAI API key with anyone or commit it to your repo

**Step 7: Loading API key and creating OpenAI Client**

You can load the API Key with the help of `python-dotenv` in the notebook

```python
from dotenv import load_dotenv
load_dotenv()
```

Once the API Key is loaded, you can create the API client which will use the API Key to authenticate and connect to OpenAI models

```python
from openai import OpenAI
openai_client = OpenAI()
```

### 1-3 What is RAG

- RAG = Retrieval-Augmented Generation
- Most common application of LLMs
- RAG allows us to access information that the LLM is not aware of, and inject it into the inputs provided to the LLM which makes LLM responses more accurate and clear

We want to build a RAG system that can answer user queries based on information provided in the course FAQ

**Step 1: Define the function to send inputs and receive outputs from the LLM**

```python
def llm(prompt):
	response = openai_client.responses.create(
		model = 'gpt-5.4-nano', #Put your desired model name here, gpt-5.4-nano is the smallest and cheapest as of June 2026
		input = prompt
		)
	return response.output_text

question = 'I just discovered the course. Can I join now?'
answer = llm(question)
print(answer)
```

LLM response is generic, and may not reflect the actual results of joining the course late, or if the course is even open for late enrollment.

**Step 2: Add context information from course FAQ to the LLM prompt**

The information about the possibility of joining late can be found in the course FAQ, which we can use as the content to enhance the information available to the LLM to respond to the user query.

```python
context = 'your-context-here'
prompt = f'''Your task is to answer questions from the course participants based on the provided context.

Use the context to find relevant information and provide accurate answers.

Question:
{question}

Context:
{context}
'''

answer = llm(prompt)
print(answer)
```

This time, the answer is more specific since information from the FAQ is provided to the LLM as additional information to respond to the user's query. When provided this additional information, the LLM determines which parts of the information are relevant

**RAG Architecture**

![General RAG architecture](LLM_Zoomcamp_1_RAGArch.jpg)

Three steps of building a RAG FAQ:

1. **Retrieval** - search for relevant information
2. **Augmentation** - Augment user query with search results
3. **Generation** - Send user query + search results to LLM to generate response

### 1-4 The Course FAQ Dataset

The data about the available courses can be found in JSON format [here](https://datatalks.club/faq/json/courses.json). We first get the data about the available courses with the `requests` library

```python
import requests

docs_url = "https://datatalks.club/faq/json/courses.json"
response = requests.get(docs_url)
courses_raw = response.json()
```

`courses_raw` gives the data about courses which are available. Using this, we can get the FAQ data for the desired courses

```python
documents = []
url_prefix = "https://datatalks.club/faq"

for course in courses_raw:
    course_url = f"""{url_prefix}{course["path"]}"""

    course_response = requests.get(course_url)
    course_response.raise_for_status() # If something is broken, then raise an error
    course_data = course_response.json()

    documents.extend(course_data)

len(documents)
```

> Note: In real-world implementations, you will spend a lot of time ingesting and cleaning data which we need

### 1-5 Search

For a simplified search engine use `minsearch`, so that you can send a subset of the documents as context instead of all the documents for more effective responses. Other search engine options include lucene, elastic search etc. Many of these search engines are heavy and can need docker containers to run.

`minsearch` is a lightweight toy implementation of a search engine that can be used for small datasets.

**Step 1: Index the documents**

```python
from minsearch import Index

index = Index(
	text_fields=['question', 'section', 'answer'], # Fields to use for searching
	keyword_fields=['course'] # Looks for exact match inside the course, acts as a filter which restricts the search space for further search with text_fields
	)
index.fit(documents) # Fitting the index to make it ready for search
```

**Step 2: Search the index for relevant documents for the given question**

```python
search_results = index.search(
	query='How do I run Docker on Windows?',
	num_results=5, #Restrict to 5 results
	boost_dict={'question':3.0, 'section':0.5} # During search 'question' is given 3.0 weightage (more importance) when looking for relevant documents, 'section' is given 0.5 weightage. Default boost is 1.0 for all fields
)
```

**Step 3: Define a `search` function for use by the RAG assistant**

```python
def search(question, course="llm-zoomcamp"):
    boost_dict = {"question": 2.0, "section": 0.5}
    filter_dict = {"course": course}

    return index.search(
        query=question,
        boost_dict=boost_dict,
        filter_dict=filter_dict,
        num_results=5
    )

search_results = search(question)
```

### 1-6 Building a Prompt

When building AI systems, we often have prompts consisting of 2 parts

1. **Instructions** - Never changes
2. **User prompt** - Changes with user input

**Step 1: Define the instructions for the LLM**

```python
INSTRUCTIONS = """
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
"""
```

**Step 2: Define the user prompt template that dynamically updates the user input**

```python
USER_PROMPT_TEMPLATE = """
Question:
{question}

Context:
{context}
"""
```

**Step 3: Define function to build the context string**

The documents are present as items in a dictionary. The context information needs to be presented as a string to include it in the user prompt

```python
def build_context(search_results):
    lines = []

    for doc in search_results:
        lines.append(doc["section"])
        lines.append("Q: " + doc["question"])
        lines.append("A: " + doc["answer"])
        lines.append("")

    return "\n".join(lines).strip()
```

**Step 4: Building the full prompt**

```python
def build_prompt(question, search_results):
    context = build_context(search_results)
    prompt = USER_PROMPT_TEMPLATE.format(
        question=question,
        context=context
    )
    return prompt.strip()

prompt = build_prompt(question, search_results)
print(prompt)
```

### 1-7 RAG Pipeline

The last part of the RAG pipeline is the LLM which takes the prompt as input and generates an output.

OpenAI has 2 APIs:

1. ChatCompletion (older API, considered legacy)
2. Responses (newer API, more convenient, what we will use)

```python
response = openai_client.responses.create(
    model="gpt-5.4-mini", # Can use other models if needed
    input=prompt
)
```

**Response exploration**

```python
print(response.output) # List of output items
print(response.output[0]) # Output message is the 1st list item
print(response.output[0].content[0].text) # Text message is the 1st item inside the content

print(response.output_text) # Shortcut to get the text message
print(response.usage) # Tokens consumed by response in a ResponseUsage object, provide counts of input, output tokens splitup as well
```

**Calculating the price**

```python
input_price = 0.75 / 1_000_000 # From model card
output_price = 4.50 / 1_000_000 # from model card

cost = (
    response.usage.input_tokens * input_price +
    response.usage.output_tokens * output_price
)

print(cost)
```

**Sending message history as input to LLM**

We can send historical messages as a list of dictionaries (each dictionary contains the role of the message sender and the message text) as input to the LLM

```python
message_history = [
    {"role": "developer", "content": INSTRUCTIONS}, # System prompt instructions
    {"role": "user", "content": prompt} # User input
]

response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=message_history
)
```

**Define final LLM function with message history**

```python
def llm(instructions, user_prompt, model="gpt-5.4-mini"):
    message_history = [
        {"role": "developer", "content": instructions}, #Can replace developer with 'system' to pass instructions, not too much of a difference in the case of Responses API
        {"role": "user", "content": user_prompt}
    ]

    response = openai_client.responses.create(
        model=model,
        input=message_history
    )

    return response.output_text
```

**Full RAG pipeline function**

```python
def rag(query, model="gpt-5.4-mini"):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(INSTRUCTIONS, prompt, model=model)
    return answer
```

### 1-8 RAG Helper

We take all the functions we have written and put them into reusable helper files.

```python
# ingest.py
# Used for loading FAQ data, building search index

import requests
from minsearch import Index

def load_faq_data():
    docs_url = "https://datatalks.club/faq/json/courses.json"
    response = requests.get(docs_url)
    courses_raw = response.json()

    documents = []
    url_prefix = "https://datatalks.club/faq"

    for course in courses_raw:
        course_url = f"""{url_prefix}{course["path"]}"""
        course_response = requests.get(course_url)
        course_response.raise_for_status()
        course_data = course_response.json()

        documents.extend(course_data)

    return documents

def build_index(documents):
    index = Index(
        text_fields=["question", "section", "answer"],
        keyword_fields=["course"]
    )
    index.fit(documents)
    return index
```

```python
# rag_helper.py

INSTRUCTIONS = """
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
"""

PROMPT_TEMPLATE = """
QUESTION:
{question}

CONTEXT:
{context}
""".strip()

class RAGHelper:

    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTIONS,
        prompt_template=PROMPT_TEMPLATE,
        course="llm-zoomcamp",
        model="gpt-5.4-mini"
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.course = course
        self.prompt_template = prompt_template
        self.model = model

    def search(self, query, num_results=5):
        boost_dict = {"question": 3.0, "section": 0.5}
        filter_dict = {"course": self.course}

        return self.index.search(
            query,
            num_results=num_results,
            boost_dict=boost_dict,
            filter_dict=filter_dict
        )

    def build_context(self, search_results):
        lines = []

        for doc in search_results:
            lines.append(doc["section"])
            lines.append("Q: " + doc["question"])
            lines.append("A: " + doc["answer"])
            lines.append("")

        return "\n".join(lines).strip()

    def build_prompt(self, query, search_results):
        context = self.build_context(search_results)
        return self.prompt_template.format(
            question=query, context=context
        )

    def llm(self, prompt):
        input_messages = [
            {"role": "developer", "content": self.instructions},
            {"role": "user", "content": prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )

        return response.output_text

    def rag(self, query):
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        answer = self.llm(prompt)
        return answer
```

**Using the helper functions**

```python
from dotenv import load_dotenv
load_dotenv()

from ingest import load_faq_data, build_index
from rag_helper import RAGBase
from openai import OpenAI

documents = load_faq_data()
index = build_index(documents)

openai_client = OpenAI()

custom_instructions = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip() # Can skip this in favor of the default instructions in rag_helper.py

assistant = RAGBase(
    index=index,
    llm_client=openai_client,
    instructions=custom_instructions,
)
```

### 1-9 Data Ingestion

- `minsearch` is in-memory and bound to the process it is running in. This means, if the notebook kernel it is running is shut down, the search index is lost.
- This is not ideal when the dataset is large and you want to persist your dataset index across sessions
- Examples of persistent search engines include elastic search

**Step 1: Split the ingestion from knowledge base querying**

- We split the data ingestion and the RAG querying to run independently, so that they are connected by the persistent storage for the knowledge base
- We use `sqlitesearch` which stores the data in `sqlite` database and has a default full text search (FTSS) extension with BM25 ranking

Install the library - `uv add sqlitesearch`

Next we write a notebook `persistent_rag_ingest.ipynb` for the data ingestion

```python
from ingest import load_faq_data
import time

documents = load_faq_data()

docs_llm = [doc for doc in documents if doc['course'] == 'llm-zoomcamp']

from sqlitesearch import TextSearchIndex
index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    db_path="faq.db"
)

for doc in docs_llm:
    index.add(doc)
    print(f"""Added: {doc["question"][:60]}...""")
    time.sleep(0.5) # Delay to ensure time gaps between writing data to DB

index.close()
print("Done. Index saved to faq.db")

```

Ensure to add the DB files to `gitignore` to avoid committing the data to git

```text
# .gitignore file

.venv
.env

faq.db*
*.db
*.db-shm
*.db-wal
```

**Step 2: Switch to `sqlitesearch` from `minsearch`**

We write a notebook `persistent_rag.ipynb` for the data loading and querying

```python
from sqlitesearch import TextSearchIndex

sqlite_index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    db_path="faq.db"
)

print(sqlite_index.count()) # Number of documents in the index

results = sqlite_index.search("Can I still join the course after it started?", num_results=5)
[doc["question"] for doc in results]
```

### 1-10 Wrap-up of Part 1

Things to try:

- Replace text search with vector search
- Replace OpenAI API with Anthropic, Gemini APIs etc
- Replace `minsearch` with Elasticsearch

### 1-11 Agents

- Current RAG pipeline's flow is fixed - search the knowledge base, build prompt with context and then LLM generates answer for user query with given context. This can have some issues:
  - Text search is lexical - it looks for exact word matches, so queries with spelling errors can have missed out search results
- Agents can go one step further by allowing the LLM to parse the user query, and take decisions on whether a search function is needed at all. This makes the flow of the program more flexible. - This is the concept behind Agentic RAG

### 1-13 Function Calling

- In Agentic RAG, the LLM can decide the best available course of action including calling functions or stopping.

**Step 1: Define function to search the index**

```python
def search(query):
    boost_dict = {"question": 3.0, "section": 0.5}
    filter_dict = {"course": "llm-zoomcamp"}

    return index.search(
        query,
        num_results=5,
        boost_dict=boost_dict,
        filter_dict=filter_dict
    )
```

**Step 2: Write some description in JSON format (dictionary in python) for the `search` function**

```python
search_tool = {
    "type": "function",
    "name": "search",
    "description": "Search the FAQ database for entries matching the given query.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query text to look up in the course FAQ."
            }
        },
        "required": ["query"],
        "additionalProperties": False
    }
}
```

**Step 3: Pass the `search` function as a tool the LLM can choose to call**

```python
response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=messages, #Historical messages
    tools=[search_tool],
)

print(response.output)
```

The response is expected to be a `ResponseFunctionToolCall` object of type `function_call`. We can use this to initiate the index search

**Step 4: Search the index based on LLM response**

```python
import json

call = response.output[0]
args = json.loads(call.arguments)

results = search(**args)
result_json = json.dumps(results, indent=2) # Indentation is to make it more human-readable, doesn't affect the LLM's response
```

**Step 5: Send search result back to the LLM**

LLMs is stateless, so it needs the entire history (original query -> Function call request -> Searching index results) to be sent in each call

```python
messages.extend(response.output)

messages.append({
    "type": "function_call_output",
    "call_id": call.call_id, # call_id links the tool result to the function call requested by the model
    "output": result_json,
})

response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=messages,
    tools=[search_tool],
)

response.output_text
```

### 1-14 The Agentic Loop

- Till now, we are manually calling the LLM once we get the function call results. But it is possible that the LLM may choose to call the tools multiple (unknown) number of times.
- This brings the concept of Agentic Loop, where the LLM continues processing by calling for tools until it decides to not call them anymore.

**Step 1: Write developer instructions to guide the behavior of the agent**

```python
instructions = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.

If you want to look up information, use the search function.
Use as many keywords from the user question as possible when making first requests.

Make multiple searches.

Try to expand your search by using new keywords
based on the results you get from the search.

At the end, ask if there are other areas that the user wants to explore.
""".strip()
```

We can improve the details given in the instructions for specific behaviors like:

1. Restricting answers to only be from the knowledge base
2. Input guardrails by specifying in-scope and out-of-scope etc.

**Step 2: Define helper function which will help make function calls if the LLM asks to use tools**

```python
def make_call(call):
    args = json.loads(call.arguments)

    if call.name == "search":
        result = search(**args)

    result_json = json.dumps(result, indent=2)

    return {
        "type": "function_call_output",
        "call_id": call.call_id,
        "output": result_json,
    }
```

**Step 3: Iteratively processing LLM inputs and outputs**

In every iteration:

1. Model chooses the next action
2. The code executes the action and returns result to the model

The loop stops when there are no more tool calls.

```python
def agent_loop(instructions, question, model="gpt-5.4-mini") -> str:
    messages = [
        {"role": "developer", "content": instructions},
        {"role": "user", "content": question}
    ]

    it = 1

    while True:
        print(f"iteration #{it}...")
        has_function_calls = False

        response = openai_client.responses.create(
            model=model,
            input=messages,
            tools=[search_tool]
        )

        messages.extend(response.output)

        for item in response.output:
            if item.type == "function_call":
                print("function_call:", item.name, item.arguments)
                call_output = make_call(item)
                messages.append(call_output)
                has_function_calls = True

            elif item.type == "message":
                print("ASSISTANT:")
                last_answer = item.content[0].text
                print(item.content[0].text)

        it = it + 1
        if has_function_calls == False:
            break

    return last_answer

agent_loop(instructions, "How do I run Olama locally?")
```

### 1-15 ToyAIKit

- To replicate the step-by-step agentic loop in the previous section, there is a framework `ToyAIKit` which is for learning purposes.
- Some other frameworks used in the industry includes Langchain, OpenAI Agent SDK, PydanticAI etc

To install it - `uv add toyaikit`

## 2. Vector Search

### 2-1 What is Vector Search

- Text search / Lexical search - Take the query, break it down into meaningful words, and look for documents which contains at least one of the words
- Different text search techniques - TF-IDF, BM25 etc
- Issue with text search - The search is for exact word matches, which means we could miss out on documents which has semantically similar words

### 2-2 Embeddings

- The concept of vectors for text search was introduced in Word2Vec. The main intuition is that words which are semantically similar have vectors which are closer to each other in the vector space (cosine of the angle between them is small)
- Word Embedding = Converting words to vectors
- Similar to word embeddings, phrases and sentences can also be converted to embedding vectors
- In vector search, we take the documents, convert them into embedding vectors in the vector space. When the user gives a question, the question is also converted to a vector, and the question's vector is used to select documents whose vectors are close in the vector space. In this process, we need to ensure the method of conversion to vectors for documents and questions is the same (For example: `sentence-transformers` library)

**Step 1: Initialize the Sentence Transformer for embedding**

```python
from sentence-transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2') # For first time runs, the model can take some time to be downloaded from HuggingFace to local
```

**Step 2: Encode the text query**

```python
query = "your-query-here"
q_vec = model.encode(query)
print(vector.shape) # Embedding vector shape

doc = "your-doc-text-here"
d_vect = model.encode(doc)
```

**Step 3: Compare the similarity between query and document**

```python
print(q_vec.dot(d_vect)) # Dot product gives a measure of the closeness between the vectors
```

### 2-3 Embedding Our Dataset

**Step 1: Ingest the data**

We use the same helper scripts and FAQ data as before (Refer to [1-8 RAG Helper](#1-8-rag-helper))

```python
from ingest import load_faq_data

documents = load_faq_data()
```

**Step 2: Generate embeddings per document**

One document = 1 pair of question and answer from the FAQ

```python
from tqdm.auto import tqdm
import numpy as np

texts = []

for doc in documents:
    text = doc["question"] + " " + doc["answer"]
    texts.append(text)

batch_size = 50 # Process the text in batches to avoid bulk processing all documents
vectors = []

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i + batch_size]
    batch_vectors = model.encode(batch) # Embedding happens faster if you have GPU
    vectors.extend(batch_vectors)

print(len(vectors)) # Total number of embeddings
X = np.array(vectors) # Convert the embeddings from list of embeddings to 2D numpy matrix of shape (number of documents x number of embedding dimensions)
```

### 2-4 Vector Search

Continuing from previous section,

**Step 3: Compare the query embedding with document embeddings to select top closest documents to query**

```python
query = "Can I still join the course after the start date?"
v_query = model.encode(query)
scores = X.dot(v_query)

idx = np.argmax(scores) # Find the index of the closest or most similar matrix
print(idx, scores[idx])

top5 = np.argsort(scores)[-5:]
top5 = top5[::-1] # Reverse to get highest first
for idx in top5:
    print(scores[idx])
    print(documents[idx])
    print()
```

## 3. Orchestration

AI orchestration with Kestra

## Workshop - Data Ingestion

Pull traces from a monitoring service for analytics with dlt

## 4. Evaluation

Measure retrieval and answer quality with offline and online eval

## 5. Monitoring

Monitor user feedback and system health with live dashboards

## 6. Best Practices

LangChain, hybrid search. Combine vector + keyword search; rerank results for higher precision

## 7. End-to-End Project

A complete project example: a fitness assistant built with LLMs

## Capstone Project

Ship a complete end-to-end project of your choice from scratch
