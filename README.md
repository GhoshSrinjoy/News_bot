*“I built a news app that never argues about sources , it just shows them.”*  

# 🗞️ News Bot – News Fetcher Application  

A simple desktop app built with **PyQt5** that fetches real-time news based on your chosen topic, timeframe, and language , powered by the **NewsAPI**.  

Just type a keyword, choose your filters, and click **Fetch News**. The latest headlines, summaries, and URLs appear instantly in a clean interface.  

🔗 **Repo:** https://github.com/GhoshSrinjoy/News_bot  

---

## Executive Summary  

**News Bot** brings personalized news discovery right to your desktop , no browser clutter, no endless tabs.  
It connects to the **NewsAPI**, retrieves the latest stories, and displays them in an intuitive, readable layout built with **PyQt5**.  

**Why it’s useful:**  
- Quick research without distractions  
- Ideal for journalists, analysts, or anyone tracking specific topics  
- Filterable by relevance, popularity, date, and language  

You control what kind of news you want , and how you want it displayed. 📰  

---

## Methodology  

### ⚙️ Flow  
1. User enters a **topic** (e.g., “AI regulation” or “SpaceX”).  
2. Selects a **time frame** , Daily, Weekly, Monthly, or Yearly.  
3. Chooses **sorting preference** , relevancy, popularity, or publication date.  
4. Selects **language** (English, Hindi, etc.).  
5. The app sends a request to **NewsAPI**.  
6. Articles are fetched and displayed with:  
   - 📰 Title  
   - 🧾 Description  
   - 🔗 URL for the full article

     
## Overview

The News Fetcher Application is a simple desktop application built using PyQt5 that allows users to fetch and display news articles based on specific topics, time frames, sorting methods, and languages. The application uses the NewsAPI to retrieve news articles and displays them in a user-friendly interface.

## Features

- Enter a topic to search for news articles.
- Select a time frame (Daily, Weekly, Monthly, Yearly) for the news articles.
- Sort the news articles by relevancy, popularity, or publication date.
- Choose the language of the news articles.
- Display the fetched news articles with titles, descriptions, and URLs.

## Prerequisites

- Python 3.x
- PyQt5
- Requests library

## Installation

1. Clone the repository or download the source code.
2. Install the required Python packages using pip:

```bash
pip install PyQt5 requests
```

3. Obtain an API key from NewsAPI. Follow the instructions in the next section to get the API key.

## Obtaining NewsAPI Key

1. Go to the [NewsAPI website](https://newsapi.org/).
2. Sign up for a free account if you don't have one.
3. After logging in, navigate to the "API" section.
4. Copy your API key from the dashboard.

## Usage

1. Open the `main.py` file and replace the placeholder API key with your actual API key:

```python
API_KEY = 'YOUR_NEWSAPI_KEY'
```

2. Run the `main.py` script:

```bash
python main.py
```

3. The application window will appear. Enter the topic you want to search for, select the time frame, sorting method, and language, then click the "Fetch News" button to retrieve and display the news articles.

## Code Overview

### main.py

The main script file that contains the implementation of the News Fetcher application. It includes:

- Initialization of the PyQt5 application and layout.
- Input fields for topic, time frame, sorting method, and language.
- A button to trigger fetching news articles.
- A text area to display the fetched news articles.
- A method to fetch news articles from NewsAPI and display them.
