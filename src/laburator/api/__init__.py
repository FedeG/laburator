"""Job-search API client package."""

from laburator.api.adapter import JobSearchAdapter
from laburator.api.base import JobSearchClient
from laburator.api.dtos import JobSearchFilters, JobSearchResult
from laburator.api.openninja import OpenNinjaJobSearchClient

__all__ = [
    "JobSearchAdapter",
    "JobSearchClient",
    "JobSearchFilters",
    "JobSearchResult",
    "OpenNinjaJobSearchClient",
]
