from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Sample static data for vendors 
vendor_data = {
    "hindalco": {
        "po_number": "PO123456",
        "vendor": "Hindalco",
        "gr_date": "2024-05-19",
        "pr_date": "2024-05-15",
        "quantity_ordered": 1000,
        "quantity_received": 1000
    },
    "tata": {
        "po_number": "PO654321",
        "vendor": "Tata Steel",
        "gr_date": "2024-06-20",
        "pr_date": "2024-05-25",
        "quantity_ordered": 1200,
        "quantity_received": 900
    }
}

@app.route("/", methods=["GET", "POST"])
def evaluate_vendor():
    results = []
    if request.method == "POST":
        user_query = request.form["query"].lower()

        # Simple extraction of vendor name from query
        matched_vendor = None
        for vendor in vendor_data:
            if vendor in user_query:
                matched_vendor = vendor
                break

        if matched_vendor:
            data = vendor_data[matched_vendor]

            gr_date = datetime.strptime(data["gr_date"], "%Y-%m-%d")
            pr_date = datetime.strptime(data["pr_date"], "%Y-%m-%d")
            delay = (gr_date - pr_date).days

            delivery_status = "Late" if delay > 5 else "On Time"

            # Logic based on quantity comparison
            if data["quantity_received"] < data["quantity_ordered"]:
                recommendation = f"❌ Contract should be CANCELLED for {data['vendor']}."
                quantity_status = "Less"
            else:
                recommendation = f"✅ Contract should be RENEWED for {data['vendor']}."
                quantity_status = "Full"

            results.append({
                "po_number": data["po_number"],
                "vendor": data["vendor"],
                "gr_date": data["gr_date"],
                "pr_date": data["pr_date"],
                "delay": delay,
                "delivery_status": delivery_status,
                "quantity_ordered": data["quantity_ordered"],
                "quantity_received": data["quantity_received"],
                "quantity_status": quantity_status,
                "recommendation": recommendation
            })

        else:
            results.append({
                "error": "Vendor not found. Please check the name and try again."
            })

    # Compute summary for charts
    summary = {
        "quantity_full": 0,
        "quantity_less": 0,
        "delivery_late": 0,
        "delivery_on_time": 0,
        "delivery_early": 0
    }

    for r in results:
        if "error" not in r:
            if r["quantity_status"] == "Full":
                summary["quantity_full"] += 1
            else:
                summary["quantity_less"] += 1

            if r["delay"] > 0:
                summary["delivery_late"] += 1
            elif r["delay"] == 0:
                summary["delivery_on_time"] += 1
            else:
                summary["delivery_early"] += 1

    return render_template("index.html", results=results, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
