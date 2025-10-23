#!/usr/bin/env python3
"""
Japanese Language Flashcards - Terminal Edition
A simple multiple-choice quiz game to learn Japanese vocabulary
"""

import random
import os
import sys

# ANSI color codes for terminal formatting
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Import vocabulary from external files
from japanese_vocab_part1 import VOCAB_PART1
from japanese_vocab_part2 import VOCAB_PART2
from japanese_vocab_part3 import VOCAB_PART3
from japanese_vocab_part4 import VOCAB_PART4
from japanese_vocab_part5 import VOCAB_PART5

# Combine all vocabulary parts
VOCABULARY = VOCAB_PART1 + VOCAB_PART2 + VOCAB_PART3 + VOCAB_PART4 + VOCAB_PART5

# Original vocabulary for reference (commented out)
"""
VOCABULARY_OLD = [
    {
        "kanji": "曖昧",
        "kana": "あいまい",
        "romaji": "aimai",
        "english": "Ambiguous",
        "thai": "คลุมเครือ",
        "arabic": "غامض",
        "russian": "Неясный"
    },
    {
        "kanji": "矛盾",
        "kana": "むじゅん",
        "romaji": "mujun",
        "english": "Contradiction",
        "thai": "ความขัดแย้ง",
        "arabic": "تناقض",
        "russian": "Противоречие"
    },
    {
        "kanji": "抽象",
        "kana": "ちゅうしょう",
        "romaji": "chuushou",
        "english": "Abstract",
        "thai": "นามธรรม",
        "arabic": "مجرد",
        "russian": "Абстрактный"
    },
    {
        "kanji": "具体",
        "kana": "ぐたい",
        "romaji": "gutai",
        "english": "Concrete",
        "thai": "เป็นรูปธรรม",
        "arabic": "ملموس",
        "russian": "Конкретный"
    },
    {
        "kanji": "概念",
        "kana": "がいねん",
        "romaji": "gainen",
        "english": "Concept",
        "thai": "แนวคิด",
        "arabic": "مفهوم",
        "russian": "Понятие"
    },
    {
        "kanji": "洞察",
        "kana": "どうさつ",
        "romaji": "dousatsu",
        "english": "Insight",
        "thai": "ความเข้าใจลึกซึ้ง",
        "arabic": "بصيرة",
        "russian": "Проницательность"
    },
    {
        "kanji": "偏見",
        "kana": "へんけん",
        "romaji": "henken",
        "english": "Prejudice",
        "thai": "อคติ",
        "arabic": "تحيز",
        "russian": "Предубеждение"
    },
    {
        "kanji": "葛藤",
        "kana": "かっとう",
        "romaji": "kattou",
        "english": "Conflict",
        "thai": "ความขัดแย้งภายใน",
        "arabic": "صراع",
        "russian": "Конфликт"
    },
    {
        "kanji": "懐疑",
        "kana": "かいぎ",
        "romaji": "kaigi",
        "english": "Skepticism",
        "thai": "ความสงสัย",
        "arabic": "شك",
        "russian": "Скептицизм"
    },
    {
        "kanji": "憧憬",
        "kana": "しょうけい",
        "romaji": "shoukei",
        "english": "Yearning",
        "thai": "ความปรารถนา",
        "arabic": "اشتياق",
        "russian": "Стремление"
    },
    {
        "kanji": "逡巡",
        "kana": "しゅんじゅん",
        "romaji": "shunjun",
        "english": "Hesitation",
        "thai": "ความลังเล",
        "arabic": "تردد",
        "russian": "Колебание"
    },
    {
        "kanji": "顕著",
        "kana": "けんちょ",
        "romaji": "kencho",
        "english": "Remarkable",
        "thai": "โดดเด่น",
        "arabic": "ملحوظ",
        "russian": "Заметный"
    },
    {
        "kanji": "慎重",
        "kana": "しんちょう",
        "romaji": "shinchou",
        "english": "Cautious",
        "thai": "ระมัดระวัง",
        "arabic": "حذر",
        "russian": "Осторожный"
    },
    {
        "kanji": "緻密",
        "kana": "ちみつ",
        "romaji": "chimitsu",
        "english": "Meticulous",
        "thai": "พิถีพิถัน",
        "arabic": "دقيق",
        "russian": "Тщательный"
    },
    {
        "kanji": "顕在",
        "kana": "けんざい",
        "romaji": "kenzai",
        "english": "Manifest",
        "thai": "ชัดเจน",
        "arabic": "ظاهر",
        "russian": "Явный"
    },
    {
        "kanji": "潜在",
        "kana": "せんざい",
        "romaji": "senzai",
        "english": "Latent",
        "thai": "แฝง",
        "arabic": "كامن",
        "russian": "Скрытый"
    },
    {
        "kanji": "恣意",
        "kana": "しい",
        "romaji": "shii",
        "english": "Arbitrary",
        "thai": "ตามอำเภอใจ",
        "arabic": "تعسفي",
        "russian": "Произвольный"
    },
    {
        "kanji": "普遍",
        "kana": "ふへん",
        "romaji": "fuhen",
        "english": "Universal",
        "thai": "สากล",
        "arabic": "عالمي",
        "russian": "Универсальный"
    },
    {
        "kanji": "妥当",
        "kana": "だとう",
        "romaji": "datou",
        "english": "Reasonable",
        "thai": "สมเหตุสมผล",
        "arabic": "معقول",
        "russian": "Разумный"
    },
    {
        "kanji": "洗練",
        "kana": "せんれん",
        "romaji": "senren",
        "english": "Refined",
        "thai": "ประณีต",
        "arabic": "مصقول",
        "russian": "Утончённый"
    }
]
"""

LANGUAGES = {
    "1": ("english", "English"),
    "2": ("thai", "ไทย (Thai)"),
    "3": ("arabic", "العربية (Arabic)"),
    "4": ("russian", "Русский (Russian)")
}


def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')


def print_header():
    """Print the application header"""
    print(f"{Colors.HEADER}{Colors.BOLD}")
    print("=" * 60)
    print("    🇯🇵  JAPANESE LANGUAGE FLASHCARDS  🇯🇵")
    print("=" * 60)
    print(f"{Colors.ENDC}")


def select_language():
    """Let user select their preferred answer language"""
    print(f"\n{Colors.OKCYAN}Choose your answer language:{Colors.ENDC}")
    for key, (_, name) in LANGUAGES.items():
        print(f"  {key}. {name}")

    while True:
        choice = input(f"\n{Colors.BOLD}Enter your choice (1-4): {Colors.ENDC}").strip()
        if choice in LANGUAGES:
            return LANGUAGES[choice][0]
        print(f"{Colors.FAIL}Invalid choice. Please select 1-4.{Colors.ENDC}")


def generate_choices(correct_word, target_language):
    """Generate 4 choices (1 correct + 3 wrong)"""
    correct_answer = correct_word[target_language]

    # Get wrong answers from other words
    wrong_answers = [
        word[target_language]
        for word in VOCABULARY
        if word["kanji"] != correct_word["kanji"]
    ]

    # Randomly select 3 wrong answers
    random.shuffle(wrong_answers)
    choices = [correct_answer] + wrong_answers[:3]

    # Shuffle all choices
    random.shuffle(choices)

    return choices, correct_answer


def display_question(word, question_num, total_questions):
    """Display the Japanese word with kanji, kana, and romaji"""
    print(f"\n{Colors.BOLD}Question {question_num}/{total_questions}{Colors.ENDC}")
    print("─" * 60)
    print(f"\n{Colors.HEADER}{Colors.BOLD}  {word['kanji']}{Colors.ENDC}")
    print(f"{Colors.OKCYAN}  {word['kana']}{Colors.ENDC}")
    print(f"{Colors.WARNING}  {word['romaji']}{Colors.ENDC}\n")
    print("─" * 60)


def ask_question(word, target_language, question_num, total_questions):
    """Ask a single question and return if answer was correct"""
    display_question(word, question_num, total_questions)

    choices, correct_answer = generate_choices(word, target_language)

    # Display choices
    print(f"\n{Colors.BOLD}Choose the correct translation:{Colors.ENDC}\n")
    for i, choice in enumerate(choices, 1):
        print(f"  {i}. {choice}")

    # Get user answer
    while True:
        try:
            answer = input(f"\n{Colors.BOLD}Your answer (1-4): {Colors.ENDC}").strip()
            answer_num = int(answer)
            if 1 <= answer_num <= 4:
                break
            print(f"{Colors.FAIL}Please enter a number between 1 and 4.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.FAIL}Please enter a valid number.{Colors.ENDC}")

    # Check answer
    user_choice = choices[answer_num - 1]
    is_correct = user_choice == correct_answer

    print()
    if is_correct:
        print(f"{Colors.OKGREEN}{Colors.BOLD}✓ Correct!{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}{Colors.BOLD}✗ Incorrect{Colors.ENDC}")
        print(f"{Colors.OKGREEN}The correct answer was: {correct_answer}{Colors.ENDC}")

    # Brief pause to let user see the result
    import time
    time.sleep(1.5)
    return is_correct


def show_final_score(score, total):
    """Display final score and result"""
    clear_screen()
    print_header()

    percentage = (score / total) * 100

    print(f"\n{Colors.BOLD}{Colors.HEADER}{'=' * 60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}                    QUIZ COMPLETE!{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'=' * 60}{Colors.ENDC}\n")

    # Determine message based on score
    if percentage == 100:
        message = "Perfect! 🌟"
        color = Colors.OKGREEN
    elif percentage >= 80:
        message = "Excellent! 🎉"
        color = Colors.OKGREEN
    elif percentage >= 60:
        message = "Good job! 👍"
        color = Colors.OKCYAN
    elif percentage >= 40:
        message = "Keep practicing! 💪"
        color = Colors.WARNING
    else:
        message = "Don't give up! 📚"
        color = Colors.FAIL

    print(f"{color}{Colors.BOLD}{message}{Colors.ENDC}\n")
    print(f"{Colors.BOLD}You scored {score} out of {total} ({percentage:.0f}%){Colors.ENDC}\n")
    print("─" * 60)


def run_quiz(target_language, num_questions=10):
    """Run the main quiz"""
    # Select random questions
    quiz_words = random.sample(VOCABULARY, min(num_questions, len(VOCABULARY)))
    score = 0
    total = len(quiz_words)

    for i, word in enumerate(quiz_words, 1):
        clear_screen()
        print_header()
        print(f"\n{Colors.BOLD}Score: {score}/{i-1}{Colors.ENDC}")

        if ask_question(word, target_language, i, total):
            score += 1

    show_final_score(score, total)


def main():
    """Main application loop"""
    while True:
        clear_screen()
        print_header()

        target_language = select_language()

        clear_screen()
        print_header()
        print(f"\n{Colors.OKCYAN}Starting quiz with answers in {target_language}...{Colors.ENDC}")
        input(f"{Colors.OKCYAN}Press Enter to begin!{Colors.ENDC}")

        run_quiz(target_language)

        # Ask if user wants to play again
        print()
        again = input(f"{Colors.BOLD}Play again? (y/n): {Colors.ENDC}").strip().lower()
        if again != 'y':
            print(f"\n{Colors.OKGREEN}Thanks for practicing! がんばって! (Ganbatte!){Colors.ENDC}\n")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}Quiz interrupted. See you next time!{Colors.ENDC}\n")
        sys.exit(0)
