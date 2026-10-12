from flask import Flask, render_template, request, jsonify
from fx_service import FXService

app = Flask(__name__)
service = FXService()


@app.route("/")
def index():
    context = service.get_market_snapshot()
    return render_template("index.html", **context)


@app.route("/api/rates")
def api_rates():
    return jsonify(service.get_market_snapshot())


@app.route("/api/convert", methods=["POST"])
def api_convert():
    payload = request.get_json(silent=True) or {}

    amount = payload.get("amount")
    from_currency = (payload.get("from_currency") or "").upper()
    to_currency = (payload.get("to_currency") or "").upper()

    if amount is None or not from_currency or not to_currency:
        return jsonify({"error": "amount, from_currency, and to_currency are required."}), 400

    try:
        amount = float(amount)
    except (TypeError, ValueError):
        return jsonify({"error": "amount must be numeric."}), 400

    try:
        result = service.convert_currency(amount, from_currency, to_currency)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
