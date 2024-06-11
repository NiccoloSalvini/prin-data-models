# Description: This file contains the data model for the CozyCozy API response.
from typing import Optional, List 
from pydantic import BaseModel

class TotalPrice(BaseModel):
    value: float
    currencyCode: str
    min: int
    max: int
    indicative: bool
    instantBooking: bool
    text: str
    shortText: str
    deeplinkUrl: str
    mapSearchId: Optional[str]
    requiresLogin: bool


class HighlightedResults(BaseModel):
    uid: int
    accommodationId: int
    providerName: str
    providerCode: str
    providerLogoCode: str
    providerText: str
    totalPrice: TotalPrice
    bedRoomCount: int
    resultCount: int
    cityName: str
    

class LightThumbnails(BaseModel):
    firstUrls: List[str]
    lastUrl: str
    count: int
    instantBooking: bool
    ratingCount: int
    ratingScore: int

class Coordinates(BaseModel):
    latitude: float
    longitude: float


class Accommodation(BaseModel):
    _id: str
    type: str
    accommodationId: int
    uid: str
    title: str
    subTitle: str
    subTitleDetails: Optional[str]
    surfaceText: str
    locationWarning: bool
    locationText: str
    highlightedResults: List[HighlightedResults]
    lightThumbnails: LightThumbnails
    coordinates: Coordinates
    cancellationCategory: int
    cancellationPolicy: int
    prioritizedAccommodation: bool
    

class CozyCozyData(BaseModel):
    accommodations: List[Accommodation]


class CozyCozyToInsert(CozyCozyData):
    _id: str
    platform: str
    scraped_at: str



class CozyCozyFlatData(BaseModel):
    _id: str
    type: str
    accommodationId: int
    uid: str
    title: str
    subTitle: str
    subTitleDetails: Optional[str]
    surfaceText: Optional[str]
    locationWarning: bool
    locationText: Optional[str]
    price_value: Optional[float]
    price_currencyCode: Optional[str]
    price_min: Optional[int]
    price_max: Optional[int]
    price_indicative: Optional[bool]
    price_instantBooking: Optional[bool]
    price_text: Optional[str]
    price_shortText: Optional[str]
    price_deeplinkUrl: Optional[str]
    price_mapSearchId: Optional[str]
    price_requiresLogin: Optional[bool]
    providerName: Optional[str]
    providerCode: Optional[str]
    providerLogoCode: Optional[str]
    providerText: Optional[str]
    bedRoomCount: Optional[int]
    resultCount: Optional[int]
    cityName: Optional[str]
    firstUrls: Optional[List[str]]
    lastUrl: Optional[str]
    thumbnails_count: Optional[int]
    thumbnails_instantBooking: Optional[bool]
    ratingCount: Optional[int]
    ratingScore: Optional[int]
    coordinates_latitude: float
    coordinates_longitude: float
    cancellationCategory: int
    cancellationPolicy: int
    prioritizedAccommodation: bool
    platform: str
    scraped_at: str
