from config import SUPABASE_URL, SUPABASE_KEY
from supabase import create_client, Client
import time

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_trip_to_db(stopped, moving, fare):
    data = {
        "stopped_time": stopped,
        "moving_time": moving,
        "total_fare": fare,
        "timestamp": int(time.time())
    }
    supabase.table("trips").insert(data).execute()

def get_all_trips():
    response = supabase.table("trips").select("*").execute()
    return response.data
