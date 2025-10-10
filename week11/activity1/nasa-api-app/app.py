import os
import requests
from typing import Any, Dict, List, Optional
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_API_URL = "https://api.nasa.gov/planetary/apod"
NASA_API_KEY = os.getenv("NASA_API_KEY", "")
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "APODViewer/1.0",
    "Cache-Control": "no-cache",
}


def _build_request_parameters(args: Dict[str, Any]) -> Dict[str, Any]:
    """Convert the form request values to NASA API url parameters."""
    params: Dict[str, Any] = {"api_key": NASA_API_KEY}

    for field in ("date", "start_date", "end_date", "count"):
        value = args.get(field, "").strip()
        if value:
            params[field] = value

    if args.get("thumbs"):
        params["thumbs"] = "true"

    return params


def _validate_items(payload: Any) -> Optional[List[Dict[str, Any]]]:
    """Ensure the API response is always a list of APOD items, so the template loop logic can handle it"""
    if payload is None:
        return None

    if isinstance(payload, list):
        return payload

    if isinstance(payload, dict):
        return [payload]

    return None


@app.route("/", methods=["GET"])
def index():
    args = request.args
    api_request_parameters = _build_request_parameters(args)
    fetch_requested = bool(args)
    apod_items: Optional[List[Dict[str, Any]]] = None
    error: Optional[str] = None

    if fetch_requested:
        try:
            response = requests.get(
                BASE_API_URL,
                params=api_request_parameters,
                headers=DEFAULT_HEADERS,
                timeout=10,
            )
            response.raise_for_status()
            apod_items = _validate_items(response.json())
            if apod_items is None:
                error = "Unexpected response format from the API."
        except requests.HTTPError as exc:
            error = f"API returned {exc.response.status_code}."
        except requests.RequestException as exc:
            error = f"Error contacting the API: {exc}"
        except ValueError:
            error = "Unable to decode the API response."

    form_values = {
        "date": args.get("date", ""),
        "start_date": args.get("start_date", ""),
        "end_date": args.get("end_date", ""),
        "count": args.get("count", ""),
        "thumbs": "thumbs" in args,
    }

    return render_template(
        "index.html",
        form_values=form_values,
        apod_items=apod_items,
        error=error,
        fetch_request=fetch_requested,
    )


if __name__ == "__main__":
    app.run(debug=True)
