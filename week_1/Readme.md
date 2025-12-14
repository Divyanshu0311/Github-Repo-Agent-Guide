# Week 1 – Foundations & API Tooling

## Project Title
Fetching README.md from a GitHub Repository using PyGithub

---

## Week Overview
In Week 1, you will be introduced to the fundamentals of **API tooling** and **external service integration** using Python.  
The focus of this week is not just on writing code, but on understanding how real-world applications communicate with platforms like GitHub.

By the end of this week, you will have built a Python script that connects to GitHub’s API and retrieves the contents of a repository’s `README.md` file.

---

## What You Will Study This Week

### 1. Introduction to APIs
An **API (Application Programming Interface)** allows different software systems to communicate with each other.  
GitHub exposes an API that lets developers access repositories, files, issues, and more programmatically.

This week, you will learn:
- What an API is and why it is used
- How client applications interact with APIs
- How data is returned in formats like JSON
- The role of authentication when accessing APIs

GitHub API Documentation:  
https://docs.github.com/en/rest

---

### 2. GitHub as a Platform
Before working with the API, it is important to understand GitHub itself.

You will explore:
- What a GitHub repository is
- Repository structure
- The purpose of `README.md`
- Public vs private repositories
- How GitHub stores and serves repository content

GitHub Docs:  
https://docs.github.com/en

---

### 3. Python Environment Management
To keep dependencies isolated and projects organized, you will work with **virtual environments**.

This includes:
- Creating a virtual environment using `venv`
- Activating and deactivating environments
- Installing third-party libraries using `pip`
- Understanding why virtual environments are important

Python venv Documentation:  
https://docs.python.org/3/library/venv.html

---

### 4. Using Third-Party Python Libraries
Modern Python development relies heavily on external libraries.  
This week, you will learn how to:
- Install external libraries
- Read library documentation
- Use library-provided classes and methods
- Understand abstraction layers over REST APIs

---

### 5. PyGithub Library
**PyGithub** is a Python wrapper around the GitHub REST API.  
Instead of making raw HTTP requests, PyGithub provides Python classes and methods that simplify interaction with GitHub.

You will work with:
- Authenticating using a GitHub Personal Access Token
- Creating a GitHub client object
- Accessing repositories by name
- Fetching files from a repository
- Decoding file contents for display

PyGithub Documentation:  
https://pygithub.readthedocs.io/en/latest/

PyGithub GitHub Repository:  
https://github.com/PyGithub/PyGithub

---

### 6. Authentication and Security Basics
Most APIs require authentication to prevent abuse and track usage.

This week covers:
- What Personal Access Tokens are
- Why tokens are safer than passwords
- How to store secrets using environment variables
- Common authentication-related errors

GitHub Authentication Docs:  
https://docs.github.com/en/authentication

---

### 7. Error Handling and Robust Code
APIs can fail for many reasons. Your script should be able to handle these situations gracefully.

You will learn:
- Basic exception handling in Python
- Handling missing repositories or files
- Managing authentication and permission errors
- Writing user-friendly error messages

---

## Final Outcome (Week 1)
Using the concepts above, you will build a Python script that:
1. Connects to GitHub using PyGithub
2. Accepts a repository name in the format `owner/repo`
3. Fetches the `README.md` file from the repository
4. Decodes and prints its contents to the terminal
5. Handles common API and runtime errors

---

## Why is this Important
This week lays the foundation for:
- API-driven development
- Tool-building with Python
- Working with real-world platforms
- Understanding how software systems integrate with each other


---
