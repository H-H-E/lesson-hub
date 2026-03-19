#!/usr/bin/env python3
"""
Creativity & Story Integration Agent
====================================

Adds creative elements, metaphors, and narrative to lessons
that build the K-12 story arc.
"""

from pathlib import Path
from typing import Dict, List
import json

BASE = Path("/root/.openclaw/workspace/lesson-hub")

# Grade-appropriate creative elements
CREATIVE_ELEMENTS = {
    "K": {
        "hooks": ["mystery box", "surprise item", "sound clue", "picture puzzle"],
        "activities": ["singing", "moving", "creating", "sharing"],
        "story_types": ["animal friends", "nature adventures", "sensory journeys"],
    },
    "1-2": {
        "hooks": ["detective mystery", "story starter", "big question", "contrasting views"],
        "activities": ["building", "drawing", "performing", "explaining"],
        "story_types": ["explorer journal", "field guide", "adventure log"],
    },
    "3-5": {
        "hooks": ["challenge accepted", "problem to solve", "case file", "design brief"],
        "activities": ["prototyping", "testing", "iterating", "presenting"],
        "story_types": ["apprentice trials", "invention story", "science fair journey"],
    },
    "6-8": {
        "hooks": ["real-world mystery", "expert interview", "controversy", "prediction"],
        "activities": ["investigating", "analyzing", "debating", "creating solutions"],
        "story_types": ["detective case", "lab report", "innovation challenge"],
    },
    "9-12": {
        "hooks": ["frontier question", "paradigm puzzle", "cutting-edge research", "community problem"],
        "activities": ["researching", "designing systems", "mentoring", "publishing"],
        "story_types": ["legacy project", "capstone journey", "expert pathway"],
    }
}

# Cross-grade metaphors
METAPHORS = {
    "cells": "building blocks of life - like bricks in a wall, or team members in a crew",
    "energy": "the currency of the universe - like money that makes everything possible",
    "ecosystems": "a big family - everyone matters and depends on each other",
    "forces": "the language of the universe - how things talk to each other through motion",
    "chemistry": "magical transformations - like cooking, things change into something new",
    "physics": "the rule book - how the game of the universe is played",
    "dna": "a secret code - like a recipe that makes you uniquely you",
    "evolution": "a family tree - species are related and change over time",
    "gravity": "the invisible glue - keeps everything connected to Earth",
    "light": "the messenger - travels from far away to bring us information",
}

# Story arc integration
STORY_ARC = {
    "K": {"chapter": 1, "title": "The Curious Explorer", "theme": "wonder"},
    "1": {"chapter": 2, "title": "Living Neighbors", "theme": "connection"},
    "2": {"chapter": 3, "title": "Life's Journey", "theme": "growth"},
    "3": {"chapter": 4, "title": "Forces in Action", "theme": "rules"},
    "4": {"chapter": 5, "title": "The Connected World", "theme": "systems"},
    "5": {"chapter": 6, "title": "The Amazing Machine", "theme": "design"},
    "6": {"chapter": 7, "title": "Cell Detectives", "theme": "investigation"},
    "7": {"chapter": 8, "title": "Ancient Elements", "theme": "transformation"},
    "8": {"chapter": 9, "title": "Water World", "theme": "stewardship"},
    "9": {"chapter": 10, "title": "Energy Revolution", "theme": "innovation"},
    "10": {"chapter": 11, "title": "Systems Thinking", "theme": "integration"},
    "11": {"chapter": 12, "title": "The Frontier", "theme": "discovery"},
    "12": {"chapter": 13, "title": "The Legacy", "theme": "contribution"},
}


class CreativityAgent:
    """Adds creative elements to lessons"""
    
    def __init__(self, grade: int):
        self.grade = grade
        self.element = self._get_creative_element()
        self.arc = STORY_ARC.get(str(grade), STORY_ARC["1"])
        
    def _get_creative_element(self) -> Dict:
        """Get age-appropriate creative elements"""
        if self.grade <= 0:
            return CREATIVE_ELEMENTS["K"]
        elif self.grade <= 2:
            return CREATIVE_ELEMENTS["1-2"]
        elif self.grade <= 5:
            return CREATIVE_ELEMENTS["3-5"]
        elif self.grade <= 8:
            return CREATIVE_ELEMENTS["6-8"]
        else:
            return CREATIVE_ELEMENTS["9-12"]
    
    def add_hook(self, topic: str) -> str:
        """Generate a creative opening hook"""
        hooks = self.element["hooks"]
        hook = f"""
### 🎭 The Hook: {hooks[hash(topic) % len(hooks)].title()}

[Teacher presents this engaging opener to spark curiosity]
"""
        return hook
    
    def add_metaphor(self, concept: str) -> str:
        """Add a connecting metaphor"""
        metaphor = METAPHORS.get(concept.lower(), "")
        if metaphor:
            return f"""

### 💡 Connection: Think of it like this:

> *" {metaphor} "*

This helps students connect abstract concepts to familiar ideas.
"""
        return ""
    
    def add_story_integration(self, topic: str) -> str:
        """Connect to the larger story arc"""
        chapter = self.arc.get("chapter", 1)
        title = self.arc.get("title", "Adventure")
        theme = self.arc.get("theme", "wonder")
        
        return f"""

### 📖 Chapter {chapter}: {title}

Every explorer builds on what they learned before. 
This lesson connects to your journey as a STEM Explorer!

**This week's theme:** {theme.title()}

*How does this connect to your Explorer's Journal?*
"""
    
    def add_activity_creativity(self) -> str:
        """Add creative activity type"""
        activities = self.element["activities"]
        activity_type = activities[0]  # Primary
        
        return f"""

### 🎨 Create: Express Your Understanding

Try {activity_type}ing your learning!
- Draw it
- Act it out  
- Build it
- Tell its story
- Make a song about it

There are many ways to show what you know!
"""
    
    def add_quest(self, topic: str) -> str:
        """Add a challenge/quest element"""
        return f"""

### ⚔️ The Quest

Complete this challenge to earn Explorer points:
[Design a {topic} that solves a problem in your community]

Share your solution with the class!
"""
    
    def add_journal_prompt(self) -> str:
        """Add Explorer's Journal entry"""
        return f"""

### 📔 Explorer's Journal Entry

In your journal, write or draw:
1. One thing that surprised me...
2. One question I'm still wondering...
3. One connection I made...

*These entries build your unique explorer story!*
"""
    
    def enhance_lesson(self, lesson_content: str, topic: str, concepts: List[str]) -> str:
        """Add all creative elements to a lesson"""
        
        # Add story integration at start
        enhanced = self.add_story_integration(topic)
        
        # Add hook
        enhanced += self.add_hook(topic)
        
        # Add metaphors for key concepts
        for concept in concepts:
            enhanced += self.add_metaphor(concept)
        
        # Add creative activity
        enhanced += self.add_activity_creativity()
        
        # Add quest
        enhanced += self.add_quest(topic)
        
        # Add journal prompt
        enhanced += self.add_journal_prompt()
        
        return lesson_content + enhanced


class StoryArcManager:
    """Manages the K-12 story arc across all lessons"""
    
    def __init__(self):
        self.arc = STORY_ARC
        self.student_journeys = {}
        
    def get_student_intro(self, grade: int) -> str:
        """Generate student introduction to their grade's chapter"""
        if str(grade) in self.arc:
            chapter = self.arc[str(grade)]
        else:
            chapter = self.arc["1"]
            
        return f"""
# 🌟 Welcome to Chapter {chapter['chapter']}: {chapter['title']}

You've been on an amazing journey as a STEM Explorer!
Now you're ready for new discoveries.

## Your Mission This Year

As a {chapter['title']} Explorer, you will:
- Explore new frontiers in science and math
- Build your problem-solving toolkit
- Connect with your community through STEM
- Create solutions that matter

## Your Explorer's Journal

Keep recording:
- 🌱 Things that wonder me
- 🔍 Questions I'm investigating  
- 💡 Connections I'm making
- 🎯 Solutions I'm designing

**The theme for this chapter:** {chapter['theme'].title()}

*What's your first discovery going to be?*
"""
    
    def generate_grade_overview(self, grade: int) -> str:
        """Generate the grade overview with story elements"""
        
        intro = self.get_student_intro(grade)
        
        return intro


# Example usage
if __name__ == "__main__":
    # Test for Grade 1
    agent = CreativityAgent(grade=1)
    
    print("=== Creative Elements for Grade 1 ===")
    print(f"Chapter: {agent.arc}")
    print(f"\nHook: {agent.add_hook('Living Things')}")
    print(f"\nStory: {agent.add_story_integration('Living Things')}")
    print(f"\nQuest: {agent.add_quest('Living Things')}")
