import glob
import os
import streamlit as st
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon', quiet=True)
analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment_text(text):
    return analyzer.polarity_scores(text)


def analyze_sentiment_directory(folder_path):
    filepaths = sorted(glob.glob(os.path.join(folder_path, "*.txt")))
    positive_scores = []
    dates = []
    for filepath in filepaths:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        score = analyzer.polarity_scores(text)
        positive_scores.append(score["pos"])
        dates.append(os.path.splitext(os.path.basename(filepath))[0])
    return positive_scores, dates


def render_directory_structure(path):
    st.write(f"Current working directory: `{path}`")

    entries = sorted(os.listdir(path))
    directories = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
    files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]

    if directories:
        st.markdown("**Folders**")
        st.write(directories)

    if files:
        st.markdown("**Files**")
        st.write(files)


def plot_positive_sentiment(dates, scores):
    fig = px.line(
        x=dates,
        y=scores,
        title="Positive Sentiment Over Time",
        labels={"x": "Date", "y": "Positive Score"},
    )
    st.plotly_chart(fig)


def render_text_sentiment(text):
    score = analyze_sentiment_text(text)
    if not text.strip():
        st.warning("Enter some text to analyze sentiment.")
        return

    st.markdown("### Sentiment scores")
    cols = st.columns(3)
    cols[0].metric("Negative", f"{score['neg']:.2f}")
    cols[1].metric("Neutral", f"{score['neu']:.2f}")
    cols[2].metric("Positive", f"{score['pos']:.2f}")

    st.markdown(f"**Compound score:** {score['compound']:.2f}")

    chart_data = {
        "label": ["negative", "neutral", "positive"],
        "value": [score["neg"], score["neu"], score["pos"]],
    }
    fig = px.bar(
        chart_data,
        x="label",
        y="value",
        title="Sentiment distribution",
        labels={"label": "Sentiment", "value": "Score"},
        range_y=[0, 1],
    )
    st.plotly_chart(fig)


if __name__ == "__main__":
    st.title("Sentiment Analysis Explorer")

    tabs = st.tabs(["Folder analysis", "Text input"])

    with tabs[0]:
        st.subheader("Analyze text files in a folder")
        render_directory_structure(os.getcwd())

        folder_path = st.text_input("Enter the folder path containing text files:", key="folder_path")

        if folder_path:
            if not os.path.isdir(folder_path):
                st.error("The folder path does not exist. Please enter a valid directory.")
            else:
                with st.spinner("Checking folder and analyzing text files..."):
                    positive_scores, dates = analyze_sentiment_directory(folder_path)

                if not positive_scores:
                    st.warning("No .txt files were found in the selected folder.")
                else:
                    plot_positive_sentiment(dates, positive_scores)

    with tabs[1]:
        st.subheader("Analyze a piece of text")
        user_text = st.text_area("Type or paste text here:")

        if st.button("Analyze text"):
            if not user_text.strip():
                st.error("Please enter text before analyzing.")
            else:
                with st.spinner("Analyzing text sentiment..."):
                    render_text_sentiment(user_text)
