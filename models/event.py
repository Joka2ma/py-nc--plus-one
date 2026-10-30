from pydantic import BaseModel
from datetime import datetime

class EventSummary(BaseModel):
    id: int
    title: str
    starts_at: datetime
    ends_at: datetime
    location:str|None
class EventsResponse(BaseModel):
    
    events:list[EventSummary]