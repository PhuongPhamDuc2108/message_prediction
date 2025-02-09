from django.http import JsonResponse
from django.shortcuts import render
from .nlp_utils import BigramModel  

def home(request):
    return render(request, 'predictor/home.html')  # Đường dẫn tới template home.html

def predict_words(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        bigram_model = BigramModel('disk1.txt')  # Đọc từ tệp disk1.txt
        bigram_model.preprocess_text()  # Tiền xử lý văn bản
        top_words = bigram_model.predict_top_words(word)  # Lấy top 3 từ

        return JsonResponse({'next_words': top_words})  # Trả về danh sách từ
