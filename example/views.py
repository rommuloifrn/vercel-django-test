# example/views.py
from datetime import datetime

from django.http import HttpResponse

import psycopg2

from django.conf import settings

def index(request):
    now = datetime.now()
    
    try:
        connection = psycopg2.connect(
            host="db.akbcrclcwkyjqrzuxqzi.supabase.co",
            port=5432,
            database="postgres",
            user="postgres",
            password=settings.DB_PASSWORD
        )
        print("Connection successful!")
        return HttpResponse("deu certo!!!!")
    except Exception as e:
        print(f"Connection failed: {e}")
        return HttpResponse(f"deu bosta: {e}")