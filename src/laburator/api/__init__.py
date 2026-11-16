"""Job-search API client package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from laburator.api.adapter import JobSearchAdapter
from laburator.api.base import JobSearchClient
from laburator.api.dtos import JobSearchFilters, JobSearchResult
from laburator.api.openninja import OpenNinjaJobSearchClient

if TYPE_CHECKING:
    from laburator.config import LaburatorConfig


def create_search_adapter(source: str, config: "LaburatorConfig") -> JobSearchAdapter:
    """Build a JobSearchAdapter for the requested source."""
    src = (source or "openninja").lower().strip()
    if src == "openninja":
        if not getattr(config, "job_search_api_key", ""):
            raise ValueError("JOB_SEARCH_API_KEY is not configured for source 'openninja'.")
        return JobSearchAdapter(OpenNinjaJobSearchClient(config.job_search_api_key))
    raise ValueError(f"Unknown search source '{source}'.")


__all__ = [
    "JobSearchAdapter",
    "JobSearchClient",
    "JobSearchFilters",
    "JobSearchResult",
    "OpenNinjaJobSearchClient",
    "create_search_adapter",
]
