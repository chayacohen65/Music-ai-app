import streamlit as st
import random

st.title("🎹 AI Music Studio (Pro Song Engine)")

# ----------------------------
# FULL KEYS
# ----------------------------

KEYS = {
    "C": ["C", "Dm", "Em", "F", "G", "Am"],
    "C#": ["C#", "D#m", "Fm", "F#", "G#", "A#m"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm"],
    "D#": ["D#", "Fm", "Gm", "G#", "A#", "Cm"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m"],
    "F": ["F", "Gm", "Am", "A#", "C", "Dm"],
    "F#": ["F#", "G#m", "A#m", "B", "C#", "D#m"],
    "G": ["G", "Am", "Bm", "C", "D", "Em"],
    "G#": ["G#", "A#m", "Cm", "C#", "D#", "Fm"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m"],
    "A#": ["A#", "Cm", "Dm", "D#", "F", "Gm"],
    "B": ["B", "C#m", "D#m", "E", "F#", "G#m"]
}

MOODS = {
    "sad": (60, 85),
    "happy": (110, 140),
    "chill": (75, 105),
    "epic": (120, 160)
}

# ----------------------------
# LYRIC BANK (NO REPETITION)
# ----------------------------

VERSE_LINES = {
    "sad": [
        "I walk alone through empty streets",
        "your memory still follows me",
        "the night keeps whispering your name",
        "but nothing feels the same",
        "I try to move but stay the same",
        "lost inside this quiet pain"
    ],
    "happy": [
        "sunlight hits my window bright",
        "everything feels just right",
        "dancing through another day",
        "nothing getting in my way",
        "smiling like I own the sky",
        "feeling like I can fly"
    ],
    "chill": [
        "slow waves drifting in my mind",
        "leaving all the stress behind",
        "breathing deep and letting go",
        "watching all my worries slow",
        "floating through the evening air",
        "nothing heavy anywhere"
    ],
    "epic": [
        "rising from the broken ground",
        "hearing distant battle sound",
        "fire burning in my soul",
        "taking back complete control",
        "nothing ever holds me down",
        "I will never touch the ground"
    ]
}

CHORUS_LINES = {
    "sad": [
        "I still feel you in the rain",
        "calling out your name again",
        "but you're gone and I'm alone",
        "trying to find my way back home"
    ],
    "happy": [
        "we are living in the light",
        "everything is feeling right",
        "nothing stopping what we are",
        "we are shining like a star"
    ],
    "chill": [
        "everything is flowing slow",
        "letting all the tension go",
        "this is where I want to be",
        "lost inside the harmony"
    ],
    "epic": [
        "I will rise above the flame",
        "nothing ever stays the same",
        "hear the thunder in my chest",
        "I will never settle less"
    ]
}

# ----------------------------
# ENGINE
# ----------------------------

def detect_mood(text):
    text = text.lower()
    if any(w in text for w in ["sad", "miss", "lonely", "cry"]):
        return "sad"
    if any(w in text for w in ["happy", "love", "party", "fun"]):
        return "happy"
    if any(w in text for w in ["calm", "chill", "peace"]):
        return "chill"
    return "epic"

def pick_lines(bank, mood):
    return random.sample(bank[mood], 4)

def generate_chords(key):
    return random.sample(KEYS[key], 4)

def generate_tempo(mood):
    return random.randint(*MOODS[mood])

# ----------------------------
# SONG BUILDER (FIXED STRUCTURE)
# ----------------------------

def build_song(chords, verse, chorus):
    song = ""

    song += "VERSE 1\n"
    for i in range(4):
        song += f"{chords[i]}   {verse[i]}\n"

    song += "\nCHORUS\n"
    for i in range(4):
        song += f"{chords[i]}   {chorus[i]}\n"

    song += "\nVERSE 2\n"
    random.shuffle(verse)
    for i in range(4):
        song += f"{chords[i]}   {verse[i]}\n"

    song += "\nCHORUS\n"
    for i in range(4):
        song += f"{chords[i]}   {chorus[i]}\n"

    song += "\nOUTRO\n"
    song += f"{chords[0]}   fading out...\n"

    return song

# ----------------------------
# MUSIC TUTOR (NEW FEATURE)
# ----------------------------

def tutor(mood, key, tempo):
    return f"""
🎓 MUSIC PRODUCTION GUIDE

1. KEY: {key}
   - This sets the emotional foundation of your track.

2. MOOD: {mood}
   - Drives melody style + lyric emotion.

3. TEMPO: {tempo} BPM
   - Slow (60–85): emotional / sad / ambient
   - Mid (85–120): chill / pop
   - Fast (120–160): energetic / epic

4. CHORDS
   - Use I–V–vi–IV style movement for mainstream sound
   - Minor chords = emotional weight
   - Major chords = brightness

5. SONG STRUCTURE
   - Verse: storytelling
   - Chorus: emotional hook (repeatable idea)
   - Outro: fade / resolution

6. PRO TIP
   - Keep verses low energy
   - Push emotional peak in chorus
   - Use repetition for memorability
"""

# ----------------------------
# UI
# ----------------------------

prompt = st.text_input("🎤 Describe your song idea")
key = st.selectbox("🎹 Key", list(KEYS.keys()))

if st.button("Generate Full Song"):

    mood = detect_mood(prompt)
    chords = generate_chords(key)
    tempo = generate_tempo(mood)

    verse = pick_lines(VERSE_LINES, mood)
    chorus = pick_lines(CHORUS_LINES, mood)

    song = build_song(chords, verse, chorus)

    st.subheader("🎼 FULL SONG")
    st.text(song)

    st.subheader("🎭 Mood")
    st.write(mood)

    st.subheader("🎹 Chords")
    st.write(chords)

    st.subheader("⏱️ Tempo")
    st.write(f"{tempo} BPM")

    st.subheader("🎓 Producer Tutor")
    st.text(tutor(mood, key, tempo))
