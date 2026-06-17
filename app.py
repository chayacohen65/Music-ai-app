import streamlit as st
import random

st.title("🎹 AI Music Studio (Full Song Generator)")

# ----------------------------
# ALL 12 KEYS (FIXED)
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
# LANGUAGE-FREE LYRIC SYSTEM
# ----------------------------

def generate_lyrics(prompt, mood):
    # This works for ANY language because we don't restrict text
    base_themes = {
        "sad": [
            f"I still feel this weight ({prompt})",
            "time moves but I stay the same",
            "echoes of what used to be",
            "fading slowly in my name"
        ],
        "happy": [
            f"everything feels right ({prompt})",
            "dancing through the endless light",
            "nothing heavy on my mind",
            "leaving worries all behind"
        ],
        "chill": [
            f"floating through this moment ({prompt})",
            "no rush and no opponent",
            "breathing in the quiet air",
            "nothing else is really there"
        ],
        "epic": [
            f"rising from the silence ({prompt})",
            "breaking every single chain",
            "power building in my veins",
            "nothing left to hold me back"
        ]
    }
    return base_themes[mood]

# ----------------------------
# FULL SONG STRUCTURE (2–3 MIN STYLE)
# ----------------------------

def build_full_song(chords, lyrics):
    song = ""

    # Verse 1
    song += "VERSE 1\n"
    for i in range(4):
        song += chords[i] + "   " + lyrics[i] + "\n"

    # Chorus
    song += "\nCHORUS\n"
    for i in range(4):
        song += chords[i] + "   " + lyrics[i] + " (hook)\n"

    # Verse 2 (variation)
    song += "\nVERSE 2\n"
    random.shuffle(chords)
    for i in range(4):
        song += chords[i] + "   " + lyrics[i] + "\n"

    # Chorus again
    song += "\nCHORUS\n"
    for i in range(4):
        song += chords[i] + "   " + lyrics[i] + " (repeat)\n"

    # Outro
    song += "\nOUTRO\n"
    song += chords[0] + "   fading out...\n"

    return song

# ----------------------------
# MUSIC ENGINE
# ----------------------------

def detect_mood(text):
    text = text.lower()

    if any(w in text for w in ["sad", "lonely", "cry", "miss", "rain"]):
        return "sad"
    if any(w in text for w in ["happy", "love", "fun", "party"]):
        return "happy"
    if any(w in text for w in ["calm", "chill", "peace", "relax"]):
        return "chill"
    return "epic"

def generate_chords(key):
    return random.sample(KEYS[key], 4)

def generate_tempo(mood):
    return random.randint(*MOODS[mood])

# ----------------------------
# UI
# ----------------------------

prompt = st.text_input("🎤 Describe your song (ANY language works)")
key = st.selectbox("🎹 Pick a key (all 12 available)", list(KEYS.keys()))

if st.button("🚀 Generate Full Song"):

    mood = detect_mood(prompt)

    chords = generate_chords(key)
    tempo = generate_tempo(mood)
    lyrics = generate_lyrics(prompt, mood)

    full_song = build_full_song(chords, lyrics)

    st.subheader("🎼 FULL SONG (2–3 MIN STRUCTURE)")
    st.text(full_song)

    st.subheader("🎭 Mood Detected")
    st.write(mood)

    st.subheader("🎹 Chords")
    st.write(chords)

    st.subheader("⏱️ Tempo")
    st.write(f"{tempo} BPM")

    st.subheader("🧠 AI Logic")
    st.write("Prompt → emotion detection → harmony selection → lyrical theme → full song structure")
