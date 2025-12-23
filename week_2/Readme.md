# Week 2 – Integrating the AI “Brain”

## Project Title  
Reading & Summarizing GitHub Repository Documentation using a Large Language Model

---

## Week Overview

In Week 2, the project moves beyond **data retrieval** and into **intelligent understanding**.

During Week 1, you built a reliable Python script that could connect to GitHub’s API and fetch the raw contents of a repository’s `README.md` file.  
While this is an essential capability, raw text alone is not very useful unless it can be *interpreted*.

This week introduces a **Large Language Model (LLM)** as the “AI brain” of your system — a component capable of reading, understanding, and summarizing human-written documentation.

By the end of this week, your script will not only fetch documentation, but also **explain what the repository is about** in a concise and structured way.

---

## Conceptual Progression from Week 1

| Week | Capability |
|----|----------|
| Week 1 | Fetch raw README content from GitHub |
| Week 2 | Understand and summarize that content using AI |

Think of this as moving from **data access** to **data intelligence**.

---

## What You Will Study This Week

---

### 1. Introduction to Large Language Models (LLMs)

A **Large Language Model** is a machine learning model trained on massive amounts of text to understand and generate human language.

This week, you will learn:
- What LLMs are at a high level
- Why they are well-suited for text summarization
- How LLMs differ from traditional rule-based programs
- The probabilistic nature of AI-generated outputs

Key ideas:
- Tokens and context windows
- Input quality directly affects output quality
- LLMs reason over text, they do not “look things up”

---

### 2. Treating the LLM as a System Component

Rather than thinking of the LLM as “just an API call,” you will treat it as a **logical subsystem** in your application.

This includes:
- Clearly separating responsibilities:
  - GitHub API → data retrieval
  - LLM API → reasoning and summarization
- Passing only relevant text to the model
- Designing clean interfaces between components

This mirrors real-world AI system design.

---

### 3. Prompt Engineering Fundamentals

Prompt engineering is the practice of **designing instructions** that guide how an LLM processes information.

You will learn how to:
- Clearly define the model’s role
- Specify what kind of output you expect
- Control verbosity and structure
- Ask for summaries that are useful, not generic

Topics covered:
- Instruction clarity
- Role-based prompting
- Output formatting (bullet points, sections)
- Iterative prompt improvement

---

### 4. Integrating an LLM API (e.g., Gemini)

This week introduces interaction with an AI service API, such as Google’s Gemini.

You will learn:
- How to authenticate with an LLM API
- How requests differ from traditional REST APIs
- How to send prompts containing real-world text
- How to receive and process generated responses
- How to store API keys securely using environment variables

This reflects how modern AI-powered applications are built.

---

### 5. Building an AI Processing Pipeline

The core engineering task of the week is to **chain systems together**.

Your program will follow this flow:

1. Fetch the repository’s `README.md` (from Week 1)
2. Prepare the text for AI consumption
3. Send the text to the LLM with a well-designed prompt
4. Receive an AI-generated summary
5. Display the result to the user in a clear format

This introduces the concept of **AI pipelines**, where data is progressively transformed.

---

### 6. Handling Practical Constraints

LLMs introduce new constraints compared to traditional APIs.

You will learn to account for:
- Large README files and context limits
- Truncation or preprocessing strategies
- API errors and rate limits
- Unexpected or low-quality AI responses

Robust handling of these issues is part of professional AI development.

---

### 7. Responsible AI Usage

Even for a simple summarization tool, responsible AI practices matter.

This week touches on:
- Not blindly trusting AI-generated summaries
- Understanding that outputs may be incomplete or incorrect
- Clearly communicating that the summary is AI-generated
- Knowing when human judgment is still required

---

## Final Outcome (Week 2)

By the end of this week, you will have built a Python script that:

1. Accepts a GitHub repository name in the format `owner/repo`
2. Fetches the repository’s `README.md` file
3. Sends the README text to a Large Language Model
4. Uses prompt engineering to guide the model’s behavior
5. Generates a **structured, human-readable summary** of the repository
6. Prints the summary to the terminal
7. Handles common API and runtime errors gracefully

---
