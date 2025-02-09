# -*- coding: utf-8 -*-
"""
NLP Bigram Model for Word Prediction
"""

import io
import re
from collections import OrderedDict, Counter
import heapq

class BigramModel:
    def __init__(self, file_name):
        self.file_name = file_name
        self.text = None
        self.review = None
        self.unigram = None
        self.bigram_counts = None

    def preprocess_text(self):
        # Đọc file và xử lý văn bản
        with io.open(self.file_name, 'r', encoding='ISO-8859-1') as f:
            self.text = f.read()

        # Loại bỏ ký tự không cần thiết
        clean_text = re.sub('[^a-zA-Z]', ' ', self.text)
        self.review = [word.lower() for word in clean_text.split()]

        # Tạo bigram và đếm tần suất
        self.bigram_counts = Counter((self.review[i], self.review[i+1]) for i in range(len(self.review) - 1))

    def predict_top_words(self, word):
        word = word.lower()
        matched_bigrams = [bigram for bigram in self.bigram_counts if bigram[0] == word]

        if matched_bigrams:
            # Lấy top 3 từ có tần suất cao nhất
            top_bigrams = heapq.nlargest(3, matched_bigrams, key=lambda b: self.bigram_counts[b])
            top_words = [bigram[1] for bigram in top_bigrams]
            return top_words
        else:
            return ["No prediction available"]
