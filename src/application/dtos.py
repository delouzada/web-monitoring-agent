from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NetworkTestResultDTO(BaseModel):
    url: str
    latency: Optional[float] = None
    packet_loss: Optional[float] = None
    response_time: Optional[float] = None
    status_code: Optional[int] = None
    timestamp: datetime

    class Config:
        from_attributes = True