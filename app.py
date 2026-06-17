import streamlit as st
import random
from transformers import pipeline

st.set_page_config(page_title="AI Music Studio", layout="wide")

st.title("🎹 AI Music Studio")

# Load AI model once
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="distilgpt2"
    )

generator = load_model()

# All 12 keys
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
    "Sad": (60, 85),
    "Happy": (110, 140),
    "Chill": (75, 105),
    "Epic": (120, 160)
}

# Inputs
prompt = st.text_input(
    "🎤 What should the song be about?",
    placeholder="e.g. Missing someone in London"
)

language = st.text_input(
    "🌍 Language",
    placeholder="English, Hebrew, Yiddish, Spanish..."
)

mood = st.selectbox(
    "🎭 Mood",
    list(MOODS.keys())
)

key = st.selectbox(
    "🎹 Key",
    list(KEYS.keys())
)

# Music functions
def generate_tempo(mood):
    low, high = MOODS[mood]
    return random.randint(low, high)

def generate_chords(key):

    common_progressions = [
        [0, 4, 5, 3],  # I V vi IV
        [5, 3, 0, 4],  # vi IV I V
        [0, 5, 3, 4],
        [0, 3, 4, 0]
    ]

    prog = random.choice(common_progressions)

    return [KEYS[key][i] for i in prog]

def generate_song(prompt, mood, language):

    song_prompt = f"""

Write ORIGINAL song lyrics.

Language: {language}
Mood: {mood}
Theme: {prompt}

Structure:

VERSE 1
4 lines

CHORUS
4 lines

VERSE 2
4 lines

CHORUS
4 lines

BRIDGE
4 lines

CHORUS
4 lines

Only output lyrics.

"""

    output = generator(
        song_prompt,
        max_new_tokens=220,
        temperature=1.0,
        do_sample=True,
        pad_token_id=50256
    )

    text = output[0]["generated_text"]

    # remove prompt from output
    text = text.replace(song_prompt, "")

    return text.strip()

def explain_song(key, mood, tempo):

    return f"""
KEY: {key}

Mood: {mood}

Tempo: {tempo} BPM

HOW TO PRODUCE:

1. Start with piano and play the chord progression.

2. Write a melody that mostly uses notes from the key.

3. Keep verses quieter and simpler.

4. Make the chorus bigger:
- stronger melody
- higher energy
- fuller instruments

5. Bass should follow root notes.

6. Drums:
- Sad: soft kick + light snare
- Happy: punchy pop groove
- Chill: laid-back drums
- Epic: huge drums and cymbals

7. Add reverb and delay for atmosphere.

8. Record vocals last and stack harmonies in the chorus.
"""

if st.button("🚀 Generate Song"):

    with st.spinner("Writing song..."):

        tempo = generate_tempo(mood)

        chords = generate_chords(key)

        lyrics = generate_song(
            prompt,
            mood,
            language if language else "English"
        )

    st.subheader("🎹 Chord Progression")

    st.write(" | ".join(chords))

    st.subheader("⏱️ Tempo")

    st.write(f"{tempo} BPM")

    st.subheader("🎼 Lyrics")

    st.text(lyrics)

    st.subheader("🎓 Production Tutor")

    st.text(
        explain_song(
            key,
            mood,
            tempo
        )
        )
