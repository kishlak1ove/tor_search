import requests
from django.shortcuts import render

def search_url(request):
    content = ""
    if request.method == 'POST':
        url = request.POST.get('url')

        if url.startswith("http://") or url.startswith("https://") or url.endswith(".onion"):
            try:
                response = requests.get(url, proxies={'http': 'socks5h://tor:9050', 'https': 'socks5h://tor:9050'})
                content = response.text
                return render(request, 'search/result.html', {'content': content})
            except Exception as e:
                content = f"Ошибка при получении данных: {str(e)}"
        else:
            content = "Пожалуйста, введите корректный URL, начинающийся с http:// или https://, или .onion URL."
    
    return render(request, 'search/search.html', {'content': content}) 