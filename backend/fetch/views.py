from django.shortcuts import render
from django.http import HttpResponse
import random
import json
from django.http import JsonResponse
import pytz
from datetime import datetime
from django.http import FileResponse, Http404, HttpResponseBadRequest
from django.conf import settings
import os
from .models import Book



def index_page(request):
    return render(request, "fetch/index.html")



QUOTES = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Do what you can, with what you have, where you are.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "Act as if what you do makes a difference. It does."
]


def random_quote(request):
    quote = random.choice(QUOTES)
    return HttpResponse(f'<p class="lead p-2 bg-success-subtle rounded">{quote}</p>', content_type="text/html")





def get_weather(request):
    """Simulates fetching weather data based on the city"""
    city = request.GET.get("city", "Unknown City")
    
    # Simulated random weather data
    weather_conditions = ["Sunny ☀️", "Cloudy ☁️", "Rainy 🌧️", "Stormy ⛈️", "Snowy ❄️"]
    temperature = random.randint(-5, 40)  # Fake temperature range
    condition = random.choice(weather_conditions)

    response_html = f"""
    <div class="alert alert-info">
        <h4>Weather in {city}</h4>
        <p><strong>{condition}</strong></p>
        <p>🌡️ Temperature: {temperature}°C</p>
    </div>
    """
    
    return HttpResponse(response_html, content_type="text/html")





# Fake city-to-timezone mapping
CITY_TIMEZONES = {
    "new York": "America/New_York",
    "london": "Europe/London",
    "paris": "Europe/Paris",
    "tokyo": "Asia/Tokyo",
    "sydney": "Australia/Sydney",
    "dubai": "Asia/Dubai",
    "moscow": "Europe/Moscow",
    "beijing": "Asia/Shanghai",
}

def get_time(request):
    """Returns the current time for a given city"""
    city = request.GET.get("city", "").strip().lower()#normalize data
    print(city)
    if city in CITY_TIMEZONES:
        timezone = pytz.timezone(CITY_TIMEZONES[city])
        current_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S %p")
        response_html = f"""
        <div class="alert alert-dark">
            <h4>Current Time in {city}</h4>
            <p>🕒 {current_time}</p>
        </div>
        """
    else:
        response_html = '<div class="alert alert-warning">⚠️ City not found in database.</div>'

    return HttpResponse(response_html, content_type="text/html")






CITIZEN = {
    'id': 99,
    'first_name': 'John',
    'last_name': 'Doe',
    'ssn': '12345678',
    'date_of_birth': '2000/01/01',
}

def get_PR(request):
    # Get citizen id from query parameters
    citizen_id = request.GET.get('prid', '')

    # Check if the citizen_id matches the one in the CITIZEN dictionary
    if citizen_id == str(CITIZEN['id']):
        # Return the entire CITIZEN dictionary as a JSON response
        return JsonResponse(CITIZEN)
    else:
        # Return an error if the citizen is not found
        return JsonResponse({'error': 'Citizen not found'}, status=404)




def add_data(request):
    if request.method == 'POST':
        # Get JSON data from the request body
        data = json.loads(request.body.decode('utf-8'))
        # Assuming the input data is just a simple string for now
        input_data = data.get('input_data', '')
        
        # Create a response and return it
        return JsonResponse({
            'message': f"Your info '{input_data}' has been received successfully."
        })



def bookshelf(request):
    books = Book.objects.all()
    return render(request, 'fetch/bookshelf.html', {'books':books})




def check_book_quantity_js(request, book_id):
    """Returns the latest quantity of a book."""
    book = Book.objects.get(id=book_id)
    return JsonResponse({"quantity": book.quantity})


# views.py
from django.http import StreamingHttpResponse
from django.shortcuts import get_object_or_404
import time
from .models import Book

def check_book_stock_sse(request, book_id):
    """Streams stock quantity updates to the client."""
    
    def event_stream():
        while True:
            book = get_object_or_404(Book, id=book_id)
            yield f"data: {book.quantity}\n\n"  # SSE format
            time.sleep(2)  # Send update every 2 seconds
    
    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")





def serve_favicon(request):
    image_path = os.path.join(settings.STATIC_ROOT, 'favicon.ico')

    if not os.path.exists(image_path):
        raise Http404
    

    try:
        return FileResponse(open(image_path, 'rb'), content_type="image/x-icon")
    except Exception:
        raise HttpResponseBadRequest

