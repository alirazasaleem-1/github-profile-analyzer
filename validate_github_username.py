import re
import requests

# =====================================================================
# 1. CONFIGURATION & CONSTANTS
# =====================================================================
GITHUB_API_URL = "https://api.github.com/users"
GITHUB_USERNAME_REGEX = r"^[a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[a-zA-Z0-9])){0,38}$"


# =====================================================================
# 2. INTERNAL WORKER FUNCTIONS (Hidden Details)
# =====================================================================
def _is_valid_format(username: str) -> bool:
    """Internal helper: Returns True if syntax is correct, else False."""
    if not username or not isinstance(username, str):
        return False
    return bool(re.match(GITHUB_USERNAME_REGEX, username))


def _check_api_existence(username: str) -> bool:
    """Internal helper: Returns True if user profile exists on GitHub servers."""
    url = f"{GITHUB_API_URL}/{username}"
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


# =====================================================================
# 3. THE ORCHESTRATOR FUNCTION (Pure True/False Output)
# =====================================================================
def verify_github_user(username_or_url: str) -> bool:
    """
    The Single Entry Point Orchestrator.
    Handles both raw usernames and full links.
    
    Returns:
      - True: Format is correct AND profile exists on GitHub.
      - False: Any failure (Format mismatch, 404 Not Found, or network down).
    """
    # Clean the input if a full link is provided
    clean_username = username_or_url.strip()
    if "github.com/" in clean_username:
        clean_username = clean_username.split("github.com/")[-1].strip("/")

    # Step 1: Fast local format check
    if not _is_valid_format(clean_username):
        return False
    
    # Step 2: Network check execution
    return _check_api_existence(clean_username)