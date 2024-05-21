# Project Documentation

## Algorithmic Challenge

### Time Range / Interval Merge within a Given Interval

To run the interval merge script:
```bash
python merge_intervals.py
```

To run the unittests:
```bash
python test_merge_intervals.py
```

## Django Challenge 1

### Endpoint to Upload Track

#### Endpoint:
```http
POST /api/tracks
```

#### Request Body:
```json
{
    "file": <binary>,
    "artist": "string",
    "title": "string"
}
```

#### Response:
```json
{
    "id": 1,
    "file": "<url-to-file>",
    "artist": "string",
    "title": "string"
}
```

#### Third-Party Libraries:
- **Django Rest Framework**: Used because it simplifies the creation of robust web APIs with Django.

## Django Challenge 2 (Bonus Challenge)

### Endpoint to Calculate Start Time Without Silence

#### Endpoint:
```http
POST /api/tracks/<id>/calculate-start-time/
```

#### Request Body:
```json
{}
```

#### Response:
- A float number in seconds indicating the start time without silence at the beginning of the track.

#### Third-Party Libraries:
- **pydub**: Chosen for its powerful audio processing capabilities and support for multiple audio formats.

## How to Run This Project

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at:
   ```
   http://127.0.0.1:8000/api/tracks
   ```

## Notes

- Ensure that you have `ffmpeg` or `libav` installed on your system for `pydub` to handle audio processing.
- Adjust the `<repository-url>` in the clone command to the actual URL of your repository.
