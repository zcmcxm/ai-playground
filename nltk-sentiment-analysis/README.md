# NLTK Sentiment Analysis

A simple Streamlit app that analyzes sentiment across text files in a folder using NLTK's VADER lexicon.

## What it does

- shows the current working directory and basic file structure
- accepts a folder path from the user
- validates that the folder exists
- reads all `.txt` files in the folder
- computes positive sentiment scores for each file
- displays the results as a line chart

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
