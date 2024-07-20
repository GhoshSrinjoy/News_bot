"""
This script is a simple news fetching application using the PyQt5 library for the GUI and the NewsAPI for fetching news articles.
Users can specify a topic, time frame, sorting method, and language to retrieve relevant news articles, which are then displayed
in the application's text area.
"""
# Imports
import sys
import requests
import json
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, 
                             QComboBox, QPushButton, QTextEdit)

API_KEY = 'get from https://newsapi.org/'

class NewsApp(QWidget):
    """A simple PyQt5 application to fetch and display news articles from the NewsAPI.

    Attributes:
        topic_label (QLabel): Label for the topic input field.
        topic_input (QLineEdit): Input field for the topic.
        time_label (QLabel): Label for the time frame combo box.
        time_combo (QComboBox): Combo box for selecting the time frame.
        sort_label (QLabel): Label for the sort by combo box.
        sort_combo (QComboBox): Combo box for selecting the sort by option.
        lang_label (QLabel): Label for the language combo box.
        lang_combo (QComboBox): Combo box for selecting the language.
        fetch_button (QPushButton): Button to trigger fetching news.
        result_area (QTextEdit): Text area to display fetched news articles.
    """
    
    def __init__(self):
        """Initialize the NewsApp with a GUI layout."""
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Set up the user interface components."""
        self.setWindowTitle('News Fetcher')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.topic_label = QLabel('Enter Topic:')
        self.topic_input = QLineEdit()
        layout.addWidget(self.topic_label)
        layout.addWidget(self.topic_input)

        self.time_label = QLabel('Select Time Frame:')
        self.time_combo = QComboBox()
        self.time_combo.addItems(['Daily', 'Weekly', 'Monthly', 'Yearly'])
        layout.addWidget(self.time_label)
        layout.addWidget(self.time_combo)

        self.sort_label = QLabel('Select Sort By:')
        self.sort_combo = QComboBox()
        self.sort_combo.addItems(['relevancy', 'popularity', 'publishedAt'])
        layout.addWidget(self.sort_label)
        layout.addWidget(self.sort_combo)

        self.lang_label = QLabel('Select Language:')
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(['en', 'es', 'fr', 'de', 'it'])
        layout.addWidget(self.lang_label)
        layout.addWidget(self.lang_combo)

        self.fetch_button = QPushButton('Fetch News')
        self.fetch_button.clicked.connect(self.fetch_news)
        layout.addWidget(self.fetch_button)

        self.result_area = QTextEdit()
        layout.addWidget(self.result_area)

        self.setLayout(layout)
    
    def fetch_news(self):
        """Fetch news articles based on user input and display them."""
        topic = self.topic_input.text()
        time_frame = self.time_combo.currentText()
        sort_by = self.sort_combo.currentText()
        language = self.lang_combo.currentText()

        if time_frame == 'Daily':
            date_from = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        elif time_frame == 'Weekly':
            date_from = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        elif time_frame == 'Monthly':
            date_from = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        else:  # Yearly
            date_from = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

        url = 'https://newsapi.org/v2/everything'
        params = {
            'q': topic,
            'from': date_from,
            'sortBy': sort_by,
            'language': language,
            'apiKey': API_KEY
        }

        response = requests.get(url, params=params)
        news_data = response.json()

        if response.status_code == 200:
            articles = news_data['articles']
            self.result_area.clear()
            for article in articles:
                self.result_area.append(f"Title: {article['title']}")
                self.result_area.append(f"Description: {article['description']}")
                self.result_area.append(f"URL: {article['url']}\n")
        else:
            self.result_area.setText(f"Failed to fetch news: {news_data['message']}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NewsApp()
    ex.show()
    sys.exit(app.exec_())
