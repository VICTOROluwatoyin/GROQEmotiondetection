import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
os.environ['GROQ_API_KEY'] = GROQ_API_KEY

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Streamlit UI
st.title("Enhanced Sentiment Analysis and Response Bot")

# Input field for user text
user_input = st.text_area("Enter your text:", "I am feeling so sad today...")

# Button to analyze sentiment
if st.button("Analyze Sentiment and Respond"):
    try:
        # Call Groq API to analyze sentiment
        sentiment_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": f"Analyze the sentiment of this text and categorize it accurately, considering negations and subtle emotions: {user_input}"}
            ],
            model="llama3-8b-8192",
        )

        # Retrieve the sentiment analysis result
        detected_sentiment = sentiment_completion.choices[0].message.content.strip().lower()

        # Generate response based on refined sentiment
        if "not angry" in user_input.lower() or "not sad" in user_input.lower():
            refined_sentiment = "neutral"
        else:
            refined_sentiment = detected_sentiment

        if "sad" in refined_sentiment:
            response_text = "I'm sorry to hear that you're feeling sad. Here's a joke to cheer you up: Why don’t skeletons fight each other? They don’t have the guts!"
        elif "happy" in refined_sentiment:
            response_text = "It's wonderful to hear that you're happy! Keep spreading positivity."
        elif "angry" in refined_sentiment:
            response_text = "It seems like you're angry. Take a deep breath, and remember, it's okay to feel this way. Let me know how I can help."
        elif "fearful" in refined_sentiment:
            response_text = "It seems like you're feeling fearful. Remember, you're stronger than you think. Take it one step at a time."
        elif "surprised" in refined_sentiment:
            response_text = "You seem surprised! I hope it's a pleasant surprise. Let me know how I can assist."
        elif "confused" in refined_sentiment:
            response_text = "It looks like you're confused. Feel free to ask questions or share your thoughts—I’m here to help."
        else:
            response_text = "Thanks for sharing your thoughts. Let me know if there's anything specific I can do for you."

        # Display the response
        st.subheader("Response:")
        st.write(response_text)

    except Exception as e:
        # Handle errors and display error message
        st.error(f"An error occurred: {str(e)}")
