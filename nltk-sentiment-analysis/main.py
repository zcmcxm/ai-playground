import glob
import os
import streamlit as st
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_directory(folder_path):
    filepaths = sorted(glob.glob(f"{folder_path}/*.txt"))
    positive_scores = []
    dates = []
    for filepath in filepaths:
        with open(filepath, "r") as f:
            text = f.read()
        score = analyzer.polarity_scores(text)
        positive_scores.append(score["pos"])
        dates.append(filepath.split("/")[-1].split(".")[0])
    return positive_scores, dates

if __name__ == "__main__":
    st.title("Sentiment Analysis of Text Files")

    st.subheader("Current file structure")
    cwd = os.getcwd()
    st.write(f"Current working directory: `{cwd}`")

    entries = sorted(os.listdir(cwd))
    directories = [entry for entry in entries if os.path.isdir(os.path.join(cwd, entry))]
    files = [entry for entry in entries if os.path.isfile(os.path.join(cwd, entry))]

    if directories:
        st.markdown("**Folders**")
        st.write(directories)

    if files:
        st.markdown("**Files**")
        st.write(files)

    folder_path = st.text_input("Enter the folder path containing text files:")

    if folder_path:
        if not os.path.isdir(folder_path):
            st.error("The folder path does not exist. Please enter a valid directory.")
        else:
            with st.spinner("Checking folder and analyzing text files..."):
                positive_scores, dates = analyze_sentiment_directory(folder_path)

            if not positive_scores:
                st.warning("No .txt files were found in the selected folder.")
            else:
                fig = px.line(
                    x=dates,
                    y=positive_scores,
                    title="Positive Sentiment Over Time",
                    labels={"x": "Date", "y": "Positive Score"},
                )
                st.plotly_chart(fig)
