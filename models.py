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
