## Setup the virtual environment and install the dependencies

```bash
cd week11/activity1/nasa-api-app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Use your own API key (avoids rate limiting header being reduced) - see https://api.nasa.gov/:

```bash
export NASA_API_KEY=your_key_here
```

## Running the App - virtual environment

```bash
flask --app app run --debug
```

Then open http://127.0.0.1:5000/ and submit the form.
