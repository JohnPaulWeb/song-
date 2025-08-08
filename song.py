import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print(f"\n🎵 Now Playing: {title}\n")

def sing_lyrics():
    chorus_lyrics = [
        ("Alam ko naman", 2.5, 1.06),
        ("Kaibigan tayo", 3.7, 1.06),
        ("Kasalanan bang mahulog sayo???", 4.7, 1.06),
        ("Tumingin ka saakin", 4.7, 1.06),
        ("Gusto kong linawin", 4.7, 1.06),
        ("Nailang kaba?", 3.7, 1.06),
        ("Pag tayo lang dalawa?", 3.7, 1.06),
        ("Sinasabi ko nga na", 3.7, 1.06),
        ("Atin ang mundo", 3.7, 1.04),
        ("Walang ibang tulad mo", 3.7, 1.06),
    ]

    clear_screen()
    print_header("Nailang by Le Jhon")

    for line, delay, _ in chorus_lyrics:
        print(line)
        time.sleep(delay)

# Run the lyric display
sing_lyrics()
