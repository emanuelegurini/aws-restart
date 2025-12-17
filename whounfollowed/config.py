"""Costanti e configurazione dell'applicazione"""

BASE_URL: str = "https://github.com"
END_URL: str = "tab=followers"

DB_PATH: str = "db/db.json"
TMP_DIR: str = "tmp"

PATTERN_NEXT_BUTTON = r'<a\s+[^>]*href="https://github\.com/([^/]+)\?page=(\d+)&amp;tab=followers"[^>]*>Next</a>'
PATTERN_USER = r'<span class="Link--secondary(?: pl-1)?">([^<]+)</span>'