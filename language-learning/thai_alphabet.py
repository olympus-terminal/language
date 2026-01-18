#!/usr/bin/env python3
"""
Thai Alphabet Learning - Terminal Edition with Audio
A quiz app to learn Thai consonants and vowels with native pronunciation
"""

import random
import os
import sys
import time
import subprocess
import tempfile
from pathlib import Path
from gtts import gTTS
import pygame

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

# Thai Consonants Database
CONSONANTS = [
    {"letter": "ก", "romanization": "k (gor)", "class": "Mid", "example": "ไก่ (gài) - chicken"},
    {"letter": "ข", "romanization": "kh (khor)", "class": "High", "example": "ไข่ (khài) - egg"},
    {"letter": "ฃ", "romanization": "kh (khor)", "class": "High*", "example": "ฃวด (khùat) - bottle (obsolete)"},
    {"letter": "ค", "romanization": "kh (khor)", "class": "Low", "example": "ควาย (khwaai) - buffalo"},
    {"letter": "ฅ", "romanization": "kh (khor)", "class": "Low*", "example": "ฅน (khon) - person (obsolete)"},
    {"letter": "ฆ", "romanization": "kh (khor)", "class": "Low", "example": "ฆ้อง (khɔ̂ɔng) - gong"},
    {"letter": "ง", "romanization": "ng (ngor)", "class": "Low", "example": "งู (nguu) - snake"},
    {"letter": "จ", "romanization": "j (jor)", "class": "Mid", "example": "จาน (jaan) - plate"},
    {"letter": "ฉ", "romanization": "ch (chor)", "class": "High", "example": "ฉลาม (chalǎam) - shark"},
    {"letter": "ช", "romanization": "ch (chor)", "class": "Low", "example": "ช้าง (cháang) - elephant"},
    {"letter": "ซ", "romanization": "s (sor)", "class": "Low", "example": "โซ่ (sôo) - chain"},
    {"letter": "ฌ", "romanization": "ch (chor)", "class": "Low", "example": "เฌอ (chə̂ə) - tree"},
    {"letter": "ญ", "romanization": "y (yor)", "class": "Low", "example": "หญิง (yǐng) - woman"},
    {"letter": "ฎ", "romanization": "d (dor)", "class": "Mid", "example": "ชฎา (chadaa) - headdress"},
    {"letter": "ฏ", "romanization": "t (tor)", "class": "Mid", "example": "ปฏัก (bpàdtàk) - stake"},
    {"letter": "ฐ", "romanization": "th (thor)", "class": "High", "example": "ฐาน (thǎan) - base"},
    {"letter": "ฑ", "romanization": "th (thor)", "class": "Low", "example": "มณโฑ (monthoo) - Montho"},
    {"letter": "ฒ", "romanization": "th (thor)", "class": "Low", "example": "ผู้เฒ่า (phûu-thàao) - old person"},
    {"letter": "ณ", "romanization": "n (nor)", "class": "Low", "example": "เณร (neen) - novice monk"},
    {"letter": "ด", "romanization": "d (dor)", "class": "Mid", "example": "เด็ก (dèk) - child"},
    {"letter": "ต", "romanization": "t (tor)", "class": "Mid", "example": "เต่า (dtào) - turtle"},
    {"letter": "ถ", "romanization": "th (thor)", "class": "High", "example": "ถุง (thǔng) - bag"},
    {"letter": "ท", "romanization": "th (thor)", "class": "Low", "example": "ทหาร (tháhǎan) - soldier"},
    {"letter": "ธ", "romanization": "th (thor)", "class": "Low", "example": "ธง (thong) - flag"},
    {"letter": "น", "romanization": "n (nor)", "class": "Low", "example": "หนู (nǔu) - mouse"},
    {"letter": "บ", "romanization": "b (bor)", "class": "Mid", "example": "ใบไม้ (bai-máai) - leaf"},
    {"letter": "ป", "romanization": "p (bpor)", "class": "Mid", "example": "ปลา (bplaa) - fish"},
    {"letter": "ผ", "romanization": "ph (phor)", "class": "High", "example": "ผึ้ง (phʉ̂ng) - bee"},
    {"letter": "ฝ", "romanization": "f (for)", "class": "High", "example": "ฝา (fǎa) - lid"},
    {"letter": "พ", "romanization": "ph (phor)", "class": "Low", "example": "พาน (phaan) - tray"},
    {"letter": "ฟ", "romanization": "f (for)", "class": "Low", "example": "ฟัน (fan) - teeth"},
    {"letter": "ภ", "romanization": "ph (phor)", "class": "Low", "example": "สำเภา (sǎm-phao) - junk"},
    {"letter": "ม", "romanization": "m (mor)", "class": "Low", "example": "ม้า (máa) - horse"},
    {"letter": "ย", "romanization": "y (yor)", "class": "Low", "example": "ยักษ์ (yâk) - giant"},
    {"letter": "ร", "romanization": "r (ror)", "class": "Low", "example": "เรือ (rʉa) - boat"},
    {"letter": "ล", "romanization": "l (lor)", "class": "Low", "example": "ลิง (ling) - monkey"},
    {"letter": "ว", "romanization": "w (wor)", "class": "Low", "example": "แหวน (wɛ̌ɛn) - ring"},
    {"letter": "ศ", "romanization": "s (sor)", "class": "High", "example": "ศาลา (sǎalaa) - pavilion"},
    {"letter": "ษ", "romanization": "s (sor)", "class": "High", "example": "ฤๅษี (rʉʉ-sǐi) - hermit"},
    {"letter": "ส", "romanization": "s (sor)", "class": "High", "example": "เสือ (sʉ̌a) - tiger"},
    {"letter": "ห", "romanization": "h (hor)", "class": "High", "example": "หีบ (hìip) - chest/box"},
    {"letter": "ฬ", "romanization": "l (lor)", "class": "Low", "example": "จุฬา (julaa) - kite"},
    {"letter": "อ", "romanization": "ɔ (or)", "class": "Mid", "example": "อ่าง (àang) - basin"},
    {"letter": "ฮ", "romanization": "h (hor)", "class": "Low", "example": "นกฮูก (nók-hûuk) - owl"}
]

# Thai Vowels Database
VOWELS = [
    {"letter": "อะ", "romanization": "a (short)", "type": "Short vowel", "example": "กะ (ga)"},
    {"letter": "อา", "romanization": "aa (long)", "type": "Long vowel", "example": "กา (gaa) - crow"},
    {"letter": "อิ", "romanization": "i (short)", "type": "Short vowel", "example": "กิน (gin) - eat"},
    {"letter": "อี", "romanization": "ii (long)", "type": "Long vowel", "example": "ดี (dii) - good"},
    {"letter": "อึ", "romanization": "ʉ (short)", "type": "Short vowel", "example": "อึก (ʉk)"},
    {"letter": "อื", "romanization": "ʉʉ (long)", "type": "Long vowel", "example": "อืด (ʉ̀ʉt) - stuffy"},
    {"letter": "อุ", "romanization": "u (short)", "type": "Short vowel", "example": "อุด (ùt) - plug"},
    {"letter": "อู", "romanization": "uu (long)", "type": "Long vowel", "example": "อูฐ (ùut) - camel"},
    {"letter": "เอะ", "romanization": "e (short)", "type": "Short vowel", "example": "เกะ (gè)"},
    {"letter": "เอ", "romanization": "ee (long)", "type": "Long vowel", "example": "เล (lee) - at all"},
    {"letter": "แอะ", "romanization": "ɛ (short)", "type": "Short vowel", "example": "แกะ (gɛ̀) - sheep"},
    {"letter": "แอ", "romanization": "ɛɛ (long)", "type": "Long vowel", "example": "แก (gɛɛ) - old"},
    {"letter": "โอะ", "romanization": "o (short)", "type": "Short vowel", "example": "โกะ (go)"},
    {"letter": "โอ", "romanization": "oo (long)", "type": "Long vowel", "example": "โต (dtoo) - grow"},
    {"letter": "เอาะ", "romanization": "ɔ (short)", "type": "Short vowel", "example": "เกาะ (gɔ̀) - island"},
    {"letter": "ออ", "romanization": "ɔɔ (long)", "type": "Long vowel", "example": "ออก (ɔ̀ɔk) - exit"},
    {"letter": "เออะ", "romanization": "ə (short)", "type": "Short vowel", "example": "เกอะ (gə̀)"},
    {"letter": "เออ", "romanization": "əə (long)", "type": "Long vowel", "example": "เกอ (gəə)"},
    {"letter": "เอีย", "romanization": "ia", "type": "Diphthong", "example": "เกีย (giia)"},
    {"letter": "เอือ", "romanization": "ʉa", "type": "Diphthong", "example": "เกือ (gʉa)"},
    {"letter": "อัว", "romanization": "ua", "type": "Diphthong", "example": "กัว (gua)"},
    {"letter": "ไอ", "romanization": "ai", "type": "Diphthong", "example": "ไก่ (gài) - chicken"},
    {"letter": "ใอ", "romanization": "ai", "type": "Diphthong", "example": "ใกล้ (glâi) - near"},
    {"letter": "เอา", "romanization": "ao", "type": "Diphthong", "example": "เกา (gao) - nine"},
    {"letter": "อำ", "romanization": "am", "type": "Special", "example": "กำ (gam)"},
    {"letter": "ฤ", "romanization": "rʉ", "type": "Special", "example": "ฤดู (rʉ́-duu) - season"}
]

MODES = {
    "1": ("consonants", "Consonants (44 letters)", CONSONANTS),
    "2": ("vowels", "Vowels (26 forms)", VOWELS),
    "3": ("all", "All Characters", CONSONANTS + VOWELS)
}


def play_audio(text, lang='th', slow=False):
    """Play audio pronunciation using Google TTS and pygame"""
    audio_file = None
    try:
        # Initialize pygame mixer if not already initialized
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # Create temporary file for audio
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
            audio_file = f.name

        # Clean the text - ensure we're only playing what's requested
        text = str(text).strip()

        # Generate speech using gTTS
        tts = gTTS(text=text, lang=lang, slow=slow)
        tts.save(audio_file)

        # Play the audio file using pygame
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        return True

    except Exception as e:
        # Print error for debugging but don't crash
        print(f"{Colors.WARNING}Audio playback failed: {e}{Colors.ENDC}")
        return False

    finally:
        # Clean up the temporary file
        if audio_file and os.path.exists(audio_file):
            try:
                pygame.mixer.music.unload()
                os.unlink(audio_file)
            except:
                pass


def extract_thai_word(example_text):
    """Extract just the Thai word from example text like 'ไก่ (gài) - chicken'"""
    # Split by space and take the first part (the Thai word)
    return example_text.split()[0] if example_text else ""


def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')


def print_header():
    """Print the application header"""
    print(f"{Colors.HEADER}{Colors.BOLD}")
    print("=" * 60)
    print("    🇹🇭  THAI ALPHABET QUIZ  🇹🇭")
    print("=" * 60)
    print(f"{Colors.ENDC}")


def select_mode():
    """Let user select which characters to study"""
    print(f"\n{Colors.OKCYAN}Choose what to study:{Colors.ENDC}")
    for key, (_, name, _) in MODES.items():
        print(f"  {key}. {name}")

    while True:
        choice = input(f"\n{Colors.BOLD}Enter your choice (1-3): {Colors.ENDC}").strip()
        if choice in MODES:
            return MODES[choice][2]
        print(f"{Colors.FAIL}Invalid choice. Please select 1-3.{Colors.ENDC}")


def run_quiz(characters, num_questions=10):
    """Run a multiple choice quiz with audio"""
    quiz_items = random.sample(characters, min(num_questions, len(characters)))
    score = 0
    total = len(quiz_items)

    for i, item in enumerate(quiz_items, 1):
        clear_screen()
        print_header()
        print(f"\n{Colors.BOLD}Quiz Progress: {i}/{total}  |  Score: {score}{Colors.ENDC}")
        print("─" * 60)

        # Show the Thai character
        print(f"\n{Colors.HEADER}{Colors.BOLD}")
        print("        " + item['letter'])
        print(f"{Colors.ENDC}")
        print("─" * 60)

        # Play audio pronunciation
        print(f"\n{Colors.WARNING}🔊 Playing audio...{Colors.ENDC}")
        play_audio(item['letter'])
        time.sleep(0.5)

        # Generate choices
        correct_answer = item['romanization']
        wrong_answers = [
            c['romanization'] for c in characters
            if c['letter'] != item['letter']
        ]

        random.shuffle(wrong_answers)
        choices = [correct_answer] + wrong_answers[:3]
        random.shuffle(choices)

        # Display choices
        print(f"\n{Colors.BOLD}What is the romanization?{Colors.ENDC}\n")
        for j, choice in enumerate(choices, 1):
            print(f"  {j}. {choice}")

        print(f"\n{Colors.OKCYAN}[r] Replay audio  |  [1-4] Answer{Colors.ENDC}")

        # Get answer
        while True:
            try:
                answer = input(f"\n{Colors.BOLD}Your choice: {Colors.ENDC}").strip().lower()

                if answer == 'r':
                    print(f"{Colors.WARNING}🔊 Playing audio...{Colors.ENDC}")
                    play_audio(item['letter'])
                    continue

                answer_num = int(answer)
                if 1 <= answer_num <= 4:
                    break
                print(f"{Colors.FAIL}Please enter a number between 1 and 4.{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.FAIL}Please enter a valid number or 'r' to replay.{Colors.ENDC}")

        # Check answer
        user_choice = choices[answer_num - 1]
        is_correct = user_choice == correct_answer

        print()
        if is_correct:
            print(f"{Colors.OKGREEN}{Colors.BOLD}✓ Correct!{Colors.ENDC}")
            score += 1
        else:
            print(f"{Colors.FAIL}{Colors.BOLD}✗ Incorrect{Colors.ENDC}")
            print(f"{Colors.OKGREEN}The correct answer was: {correct_answer}{Colors.ENDC}")

        # Show additional info
        print(f"\n{Colors.BOLD}🔊 Letter pronunciation:{Colors.ENDC}")
        play_audio(item['letter'])

        if 'class' in item:
            print(f"\n{Colors.OKBLUE}Class: {item['class']} consonant{Colors.ENDC}")
        elif 'type' in item:
            print(f"\n{Colors.OKBLUE}Type: {item['type']}{Colors.ENDC}")

        # Show example and play its audio
        example_word = extract_thai_word(item['example'])
        print(f"\n{Colors.OKCYAN}Example: {item['example']}{Colors.ENDC}")
        print(f"{Colors.BOLD}🔊 Example word pronunciation:{Colors.ENDC}")
        play_audio(example_word)

        time.sleep(1)
        input(f"\n{Colors.WARNING}Press Enter to continue...{Colors.ENDC}")

    # Show final score
    clear_screen()
    print_header()

    percentage = (score / total) * 100

    print(f"\n{Colors.BOLD}{Colors.HEADER}{'=' * 60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}                    QUIZ COMPLETE!{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'=' * 60}{Colors.ENDC}\n")

    if percentage == 100:
        message = "Perfect! 🌟"
        color = Colors.OKGREEN
    elif percentage >= 80:
        message = "Excellent! 🎉"
        color = Colors.OKGREEN
    elif percentage >= 60:
        message = "Good job! 👍"
        color = Colors.OKCYAN
    else:
        message = "Keep practicing! 💪"
        color = Colors.WARNING

    print(f"{color}{Colors.BOLD}{message}{Colors.ENDC}\n")
    print(f"{Colors.BOLD}You scored {score} out of {total} ({percentage:.0f}%){Colors.ENDC}\n")
    print("─" * 60)

    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")


def main():
    """Main application loop"""
    while True:
        clear_screen()
        print_header()

        characters = select_mode()

        clear_screen()
        print_header()
        print(f"\n{Colors.OKCYAN}Starting quiz with {len(characters)} characters...{Colors.ENDC}")
        print(f"{Colors.WARNING}🔊 Audio will play for each character{Colors.ENDC}")
        input(f"{Colors.OKCYAN}Press Enter to begin!{Colors.ENDC}")

        num_questions = min(10, len(characters))
        run_quiz(characters, num_questions)

        # Ask if user wants to play again
        print()
        again = input(f"{Colors.BOLD}Play again? (y/n): {Colors.ENDC}").strip().lower()
        if again != 'y':
            print(f"\n{Colors.OKGREEN}Thanks for practicing! สู้ๆ (Suu-suu - Keep fighting!){Colors.ENDC}\n")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}Quiz interrupted. See you next time!{Colors.ENDC}\n")
        sys.exit(0)
