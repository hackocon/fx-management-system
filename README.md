# FX Management System

A simple foreign exchange management system that uses today's international FX market rates via the Frankfurter API.

## Features

- Real-time FX conversion using live market data
- Multi-currency support
- Simple web dashboard
- REST API endpoints
- Market snapshot with date and rates

## Tech Stack

- Python 3
- Flask
- Requests
- HTML/CSS/JavaScript

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
```

5. Open the app in your browser at:

```text
http://localhost:5000
```

## API Usage

### Get today's FX market snapshot

```bash
curl http://localhost:5000/api/rates
```

### Convert currency

```bash
curl -X POST http://localhost:5000/api/convert \
  -H "Content-Type: application/json" \
  -d '{"amount": 100, "from_currency": "USD", "to_currency": "EUR"}'
```

## Notes

This app uses the free Frankfurter API for daily market exchange rates, which reflects today's international foreign exchange market data.
