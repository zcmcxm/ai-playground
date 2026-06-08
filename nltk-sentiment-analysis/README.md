# NLTK Sentiment Analysis

A simple Streamlit app that analyzes sentiment across text files in a folder and also supports direct text input using NLTK's VADER lexicon.

## What it does

- shows the current working directory and basic file structure
- accepts a folder path from the user
- validates that the folder exists
- reads all `.txt` files in the folder
- computes positive sentiment scores for each file and plots them over time
- provides a second tab for directly typing or pasting text
- displays negative, neutral, positive, and compound sentiment scores for user input

## Requirements

Install dependencies with:

```bash
pip install streamlit nltk plotly
```

## Run it

```bash
streamlit run main.py
```

Then open the local Streamlit URL shown in the terminal.

## Notes

- The folder should contain `.txt` files for analysis.
- If no `.txt` files are found, the app shows a warning.
- The `Text input` tab lets you enter text directly and view a sentiment score breakdown.
