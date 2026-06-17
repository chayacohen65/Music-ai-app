import streamlit as st

styles = {
    "happy": {
        "chords": ["C", "G", "Am", "F"],
        "tempo": "120 BPM"
    },
    "sad": {
        "chords": ["Am", "F", "C", "G"],
        "tempo": "75 BPM"
    },
    "epic": {
        "chords": ["C", "Em", "F", "G"],
        "tempo": "140 BPM"
    },
    "chill": {
        "chords": ["Am", "C", "F", "G"],
        "tempo": "90 BPM"
    }
}

def explain(style):
    return "This works because chord movement creates tension and resolution in music."

st.title("🎹 Music AI Generator")

style = st.selectbox("Pick a mood", ["happy", "sad", "epic", "chill"])

if st.button("Generate"):
    st.write("Chords:")
    st.write(styles[style]["chords"])

    st.write("Tempo:")
    st.write(styles[style]["tempo"])

    st.write("Why it works:")
    st.write(explain(style))
