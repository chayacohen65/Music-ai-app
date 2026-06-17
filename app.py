import streamlit as st
import random

st.title("🎹 Music AI Composer (Level 3)")

keys = {
    "C": ["C", "Dm", "Em", "F", "G", "Am"],
    "G": ["G", "Am", "Bm", "C", "D", "Em"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m"]
}

moods = {
    "happy": {
        "tempo": (110, 140),
        "lyrics": [
            "I wake up feeling light today",
            "everything just falls in place",
            "sunlight on my face again",
            "nothing's gonna bring me down"
        ]
    },
    "sad": {
        "tempo": (60, 85),
        "lyrics": [
            "I still hear your voice at night",
            "but you're already gone away",
            "silence feels too loud to fight",
            "I’m fading into yesterday"
        ]
    },
    "chill": {
        "tempo": (80, 105),
        "lyrics": [
            "drifting through the evening air",
            "no rush, no weight, no care",
            "time is moving slow again",
            "breathing in the moment there"
        ]
    }
}

key = st.selectbox("Pick a key", list(keys.keys()))
mood = st.selectbox("Pick a mood", list(moods.keys()))

tempo = random.randint(*moods[mood]["tempo"])
progression = random.sample(keys[key], 4)
lyrics = moods[mood]["lyrics"]

def create_song(chords, lyrics):
    song = ""
    for i in range(len(chords)):
        song += chords[i] + "    " + lyrics[i] + "\n"
    return song

if st.button("Generate Song"):
    st.subheader("🎼 Chords + Lyrics")

    song = create_song(progression, lyrics)
    st.text(song)

    st.subheader("⏱️ Tempo")
    st.write(f"{tempo} BPM")

    st.subheader("🧠 Insight")
    st.write("This song works because chord movement supports emotional flow in the lyrics.")
