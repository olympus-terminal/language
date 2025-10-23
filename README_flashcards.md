# Japanese Language Flashcards

A terminal-based multiple-choice quiz application for learning advanced Japanese vocabulary.

## Features

- **1000 Advanced Japanese Words** - Comprehensive vocabulary database covering diverse topics
- **Kanji, Kana & Romaji** - Each word displays all three writing systems
- **4 Target Languages** - Choose answers in English, Thai, Arabic, or Russian
- **Beautiful Terminal UI** - Colorful interface with progress tracking
- **Instant Feedback** - No waiting between questions (auto-advances after 1.5s)
- **Random Selection** - 10 random words per quiz session

## Running the App

```bash
python3 japanese_flashcards.py
```

Or make it executable:
```bash
chmod +x japanese_flashcards.py
./japanese_flashcards.py
```

## Vocabulary Categories

The 1000-word database is organized into 5 parts (200 words each):

### Part 1 (Words 1-200)
- Abstract Concepts & Philosophy (30 words)
- Business & Economics (30 words)
- Academic & Science (30 words)
- Psychology & Emotions (30 words)
- Social & Politics (30 words)
- Technology & Modern Life (30 words)
- Nature & Environment (20 words)

### Part 2 (Words 201-400)
- Arts & Literature (30 words)
- Law & Justice (30 words)
- Medicine & Health (30 words)
- Education & Learning (30 words)
- Time & Change (30 words)
- Space & Distance (30 words)
- Quality & Quantity (20 words)

### Part 3 (Words 401-600)
- Relationships & Society (30 words)
- Communication & Expression (30 words)
- Cognition & Thinking (30 words)
- Action & Movement (30 words)
- Cause & Effect (30 words)
- Existence & Being (30 words)
- States & Conditions (20 words)

### Part 4 (Words 601-800)
- Emotions & Feelings (50 words)
- Attitudes & Behaviors (50 words)
- Abstract Qualities (50 words)
- Philosophy & Wisdom (50 words)

### Part 5 (Words 801-1000)
- Advanced Concepts (50 words)
- Natural Phenomena (50 words)
- Final Advanced Terms (100 words)

## File Structure

```
japanese_flashcards.py      # Main application
japanese_vocab_part1.py     # Vocabulary words 1-200
japanese_vocab_part2.py     # Vocabulary words 201-400
japanese_vocab_part3.py     # Vocabulary words 401-600
japanese_vocab_part4.py     # Vocabulary words 601-800
japanese_vocab_part5.py     # Vocabulary words 801-1000
```

## How to Add More Words

Edit any of the `japanese_vocab_partX.py` files and add entries in this format:

```python
{
    "kanji": "曖昧",
    "kana": "あいまい",
    "romaji": "aimai",
    "english": "Ambiguous",
    "thai": "คลุมเครือ",
    "arabic": "غامض",
    "russian": "Неясный"
}
```

## Vocabulary Level

This app focuses on **JLPT N2-N1 level** advanced vocabulary, including:
- Academic and technical terms
- Business and economics
- Philosophy and abstract concepts
- Scientific terminology
- Literary expressions
- Social and political discourse

Perfect for intermediate to advanced Japanese learners!

## Tips for Learning

1. **Focus on patterns** - Many kanji compounds follow logical patterns
2. **Review romaji** - Helps with pronunciation
3. **Multiple sessions** - The app randomly selects 10 words each time
4. **Track progress** - Your score is displayed after each quiz
5. **Challenge yourself** - Try different target languages for variety

がんばって！(Ganbatte - Good luck!)
