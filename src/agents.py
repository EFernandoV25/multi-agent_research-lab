# src/agents.py
"""
Agent definitions for AI Research Team
"""

import os
from crewai import Agent

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
os.environ["OPENAI_API_KEY"] = "sk-dummy-key"

def create_researcher():
    """Create Researcher Agent"""
    return Agent(
        role="Research Specialist",
        goal="Find and analyze information about AI research topics",
        backstory="Expert researcher with skills in finding credible information",
        verbose=True,
        allow_delegation=False,
        llm="groq/llama-3.3-70b-versatile"
    )

def create_writer():
    """Create Writer Agent"""
    return Agent(
        role="Technical Writer",
        goal="Write 500-word research summaries in Markdown format",
        backstory="Skilled technical writer who creates clear documents",
        verbose=True,
        allow_delegation=False,
        llm="groq/llama-3.3-70b-versatile"
    )

def create_reviewer():
    """Create Reviewer Agent"""
    return Agent(
        role="Quality Reviewer",
        goal="Evaluate and improve research summaries",
        backstory="Meticulous editor who ensures quality",
        verbose=True,
        allow_delegation=False,
        llm="groq/llama-3.3-70b-versatile"
    )
