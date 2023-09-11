from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from pytz import timezone


app = FastAPI()




@app.get("/api")
async def api(slack_name: str = None, track: str = None):

    utc_timezone = timezone("UTC")
    current_day = datetime.now(utc_timezone).strftime("%A")

        
    utc_time = datetime.now(utc_timezone)
    utc_offset_minutes = (
                utc_time.utcoffset().total_seconds() / 60
            )  

    if abs(utc_offset_minutes) > 2:
        raise HTTPException(status_code=400, detail="Invalid UTC offset")

    status_code = 200
    
    
    response_data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "track": track,
            "github_file_url": f"https://github.com/delaworla/backend_track/blob/main/main.py",
            "github_repo_url": f"https://github.com/delaworla/backend_track",
            "status_code": status_code,
        }
    return response_data
