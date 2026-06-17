import streamlit as st
import random

st.title("🎹 AI Music Studio (Simple Level 5)")

# ----------------------------
# MUSIC DATABASE
# ----------------------------

KEYS = {
    "C": ["C", "Dm", "Em", "F", "G", "Am"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m"],
    "F": ["F", "Gm", "Am", "A#", "C", "Dm"],
    "G": ["G", "Am", "Bm", "C", "D", "Em"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m"]
}

MOODS = {
    "sad": {"tempo": (60, 85)},
    "happy": {"tempo": (110, 140)},
    "chill": {"tempo": (75, 105)},
    "epic": {"tempo": (120, 160)}
}

LYRICS = {
    "sad": [
        "I still feel you in the rain",
        "walking through the silent pain",
        "memories I can't erase",
        "time can never take your place"
    ],
    "happy": [
        "sunlight dancing on my face",
        "everything is in its place",
        "life is moving to the sound",
        "joy is spinning all around"
    ],
    "chill": [
        "floating on a gentle wave",
        "nothing here that I must save",
        "breathing slow and feeling free",
        "that's enough for me to be"
    ],
    "epic": [
        "rising up against the night",
        "burning with an inner light",
        "nothing ever stays the same",
        "I will rise above the flame"
    ]
}

# ----------------------------
# SIMPLE PROMPT BRAIN
# ----------------------------

def detect_mood(text):
    text = text.lower()

    if any(w in text for w in ["sad", "lonely", "miss", "cry", "rain"]):
        return "sad"
    if any(w in text for w in ["happy", "love", "party", "fun"]):
        return "happy"
    if any(w in text for w in ["calm", "chill", "peace", "relax"]):
        return "chill"
    return "epic"

def generate_chords(key):
    return random.sample(KEYS[key], 4)

def generate_tempo(mood):
    return random.randint(*MOODS[mood]["tempo"])

def create_song(chords, lyrics):
    song = ""
    for i in range(4):
        song += chords[i] + "    " + lyrics[i] + "\n"
    return song

# ----------------------------
# UI
# ----------------------------

prompt = st.text_input("🎤 Describe your song idea")
key = st.selectbox("🎹 Pick a key", list(KEYS.keys()))

if st.button("Generate Song"):

    mood = detect_mood(prompt)

    chords = generate_chords(key)
    tempo = generate_tempo(mood)
    lyrics = LYRICS[mood]

    song = create_song(chords, lyrics)

    st.subheader("🎼 Song Output (Chords + Lyrics)")
    st.text(song)

    st.subheader("🎭 Detected Mood")
    st.write(mood)

    st.subheader("⏱️ Tempo")
    st.write(f"{tempo} BPM")

    st.subheader("🎹 Chords")
    st.write(chords)

    st.subheader("🧠 AI Insight")
    st.write("This system matches emotional language → musical structure (key, tempo, harmony, lyrics).")
