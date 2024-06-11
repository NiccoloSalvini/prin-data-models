from pydantic import BaseModel
from typing import Optional

class DataSource(BaseModel):
    source_id: Optional[int]
    source_name: str
    source_url: str
    source_description: Optional[str]


class Accommodation(BaseModel):
    accommodation_id: Optional[int]
    source_id: int
    title: Optional[str]
    sub_title: Optional[str]
    surface_text: Optional[str]
    location_warning: bool
    location_text: Optional[str]
    coordinates_latitude: Optional[float]
    coordinates_longitude: Optional[float]
    price_total: Optional[float]
    price_total_text: Optional[str]
    cancellation_policy: Optional[str]
    instant_booking: bool
    rating_count: Optional[int]
    rating_score: Optional[float]
    cancellation_category: Optional[int]
    prioritized_accommodation: bool
    scraped_at: str

    class Config:
        orm_mode = True


class CheckInOutDate(BaseModel):
    date_id: Optional[int]
    accommodation_id: int
    check_in_date: str
    check_out_date: str

    class Config:
        orm_mode = True
