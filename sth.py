import streamlit as st
from deep_translator import GoogleTranslator

# App title
st.title("Language Translation App")

# Sidebar for user input
st.sidebar.header("Translation Options")

# List of supported languages
language_names = GoogleTranslator().get_supported_languages()

# Dropdown for selecting source language
source_language = st.sidebar.selectbox(
    "Select source language:",
    language_names,
    index=language_names.index("english") if "english" in language_names else 0  # Default to English
)

# Dropdown for selecting destination language
destination_language = st.sidebar.selectbox(
    "Select destination language:",
    language_names,
    index=language_names.index("spanish") if "spanish" in language_names else 1  # Default to Spanish
)

# Text input for the text to translate
text_to_translate = st.text_area("Enter text to translate:")

# Translate button
if st.button("Translate"):
    if text_to_translate.strip():
        try:
            translator = GoogleTranslator(source=source_language, target=destination_language)
            translated_text = translator.translate(text_to_translate)
            st.success("Translation Completed")
            st.text_area("Translated Text:", translated_text, height=200)
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please enter text to translate.")

# Footer
st.markdown("---")
st.markdown("Created by GMK")
