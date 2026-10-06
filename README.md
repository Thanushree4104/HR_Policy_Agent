[![Nexolve Resolution Copilot: AI for Telecom Support](https://repoclip.io/api/badge/2a196d6a-2a2a-4de7-9391-1151b8ec4d1b)](https://repoclip.io/v/2a196d6a-2a2a-4de7-9391-1151b8ec4d1b)


# 🚀 Nexolve Resolution Copilot

<p align="center">
  <img src="docs/assets/nexolve-banner.svg"
       alt="Nexolve Resolution Copilot"
       width="100%" />
</p>

<p align="center">
  <strong>From customer complaint → relevant evidence → grounded resolution.</strong>
</p>

<p align="center">
  AI-powered telecom support using Hybrid RAG, historical tickets,
  citation validation, and safety guardrails.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![RAG](https://img.shields.io/badge/RAG-Hybrid-6C5CE7?style=for-the-badge)
![Groq](https://img.shields.io/badge/LLM-Groq-F55036?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</p>

<p align="center">

<a href="#-quick-start">Quick Start</a> •
<a href="#-architecture">Architecture</a> •
<a href="#-evaluation">Evaluation</a> •
<a href="#-how-it-works">How It Works</a>

</p>

---

# ⚡ At a Glance

<table>
<tr>
<td align="center"><strong>400</strong><br/>Evaluation Queries</td>
<td align="center"><strong>84.25%</strong><br/>R@5</td>
<td align="center"><strong>0.6719</strong><br/>MRR</td>
<td align="center"><strong>Hybrid</strong><br/>Retrieval</td>
<td align="center"><strong>Grounded</strong><br/>Answers</td>
</tr>
</table>

---

# 🎯 The Problem

Traditional support search often depends heavily on matching the customer's
exact wording.

For example:

> **Customer:**  
> "My broadband keeps dropping every evening while I'm working."

A keyword-only system may struggle if the knowledge base describes the same
problem using terms such as:

`intermittent connectivity` · `network instability` · `session drops`

### 💡 The Nexolve Approach

Nexolve combines semantic retrieval, lexical retrieval, historical support
tickets, feedback-aware ranking, and evidence-grounded generation.

```text
Customer Complaint
       │
       ▼
Understand the Complaint
       │
       ▼
Semantic + BM25 Retrieval
       │
       ├───────────────┐
       ▼               ▼
Knowledge Base    Past Tickets
       │               │
       └───────┬───────┘
               ▼
        Evidence Reranking
               │
               ▼
           Groq LLM
               │
               ▼
    Citation + Safety Validation
               │
               ▼
       🎯 Grounded Resolution
