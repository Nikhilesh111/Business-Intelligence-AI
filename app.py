# from flask import Flask, render_template, request

# app = Flask(__name__)

# # Predefined vendor data
# vendors = {
#     "hindalco": {
#         "po": "123",
#         "quantity": "500 kg",
#         "delay": "3 days",
#         "revenue": "$50,000",
#         "status": "Renew"
#     },
#     "xyzcorp": {
#         "po": "456",
#         "quantity": "200 kg",
#         "delay": "10 days",
#         "revenue": "$8,000",
#         "status": "Cancel"
#     }
# }

# @app.route("/", methods=["GET", "POST"])
# def home():
#     result = None
#     if request.method == "POST":
#         vendor = request.form["vendor"].lower()
#         result = vendors.get(vendor, {"error": "Vendor not found!"})
#         result["vendor"] = vendor.title()

#     return render_template("index.html", result=result)

# if __name__ == "__main__":
#     app.run(debug=True)
























# from flask import Flask, render_template, request
# from transformers import pipeline

# app = Flask(__name__)

# # Load GPT-2 text generation pipeline
# generator = pipeline('text-generation', model='gpt2')

# # Your predefined vendor data (you can expand it)
# vendor_data = """
# Vendor: Hindalco
# PO Number: 123
# Delivery Quantity: 500 kg
# Delay: 3 days
# Revenue Turnover: $50,000
# Contract: Renew

# Vendor: XYZCorp
# PO Number: 456
# Delivery Quantity: 200 kg
# Delay: 10 days
# Revenue Turnover: $8,000
# Contract: Cancel
# """

# @app.route("/", methods=["GET", "POST"])
# def home():
#     response = None
#     if request.method == "POST":
#         user_input = request.form["user_input"]

#         prompt = f"Vendor data:\n{vendor_data}\n\nUser query: {user_input}\nAnswer:"

#         # Generate response with GPT-2
#         result = generator(prompt, max_length=150, num_return_sequences=1, do_sample=True, temperature=0.7)
#         response = result[0]['generated_text'][len(prompt):].strip()

#     return render_template("chat.html", response=response)

# if __name__ == "__main__":
#     app.run(debug=True)

























# from flask import Flask, render_template, request
# from transformers import pipeline

# app = Flask(__name__)

# # Load GPT-2 text generation pipeline once
# generator = pipeline('text-generation', model='gpt2')

# @app.route("/", methods=["GET", "POST"])
# def home():
#     response = None
#     if request.method == "POST":
#         user_input = request.form["user_input"]
#         prompt = f"Vendor info:\nUser: {user_input}\nAI:"
        
#         # Generate text (limit output length)
#         result = generator(prompt, max_length=100, num_return_sequences=1, do_sample=True, top_k=50)
#         response = result[0]['generated_text'][len(prompt):].strip()

#     return render_template("chat.html", response=response)

# if __name__ == "__main__":
#     app.run(debug=True)






















# from flask import Flask, render_template, request

# app = Flask(__name__)

# # Sample vendor data
# vendor_data = {
#     "hindalco": {
#         "po_number": "123",
#         "quantity": "500 kg",
#         "delay": "3 days",
#         "revenue": "$50,000",
#         "status": "renew"
#     },
#     "xyzcorp": {
#         "po_number": "456",
#         "quantity": "200 kg",
#         "delay": "10 days",
#         "revenue": "$8,000",
#         "status": "cancel"
#     }
# }

# @app.route("/", methods=["GET", "POST"])
# def index():
#     result = None

#     if request.method == "POST":
#         vendor = request.form["vendor"].lower()

#         if vendor in vendor_data:
#             data = vendor_data[vendor]
#             result = {
#                 "vendor": vendor,
#                 "po": data["po_number"],
#                 "qty": data["quantity"],
#                 "delay": data["delay"],
#                 "revenue": data["revenue"],
#                 "decision": "Renew the contract ✅" if data["status"] == "renew" else "Cancel the contract ❌"
#             }
#         else:
#             result = {"error": "Vendor not found in the system."}

#     return render_template("index.html", result=result)







# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def evaluate_vendor():
#     results = []

#     if request.method == "POST":
#         vendor = request.form["vendor"]
#         accuracy = float(request.form["accuracy"])
#         delay = int(request.form["delay"])
#         revenue = float(request.form["revenue"])

#         if accuracy >= 95 and delay <= 2 and revenue >= 5000000:
#             recommendation = f"✅ Recommendation: RENEW the contract with {vendor}."
#         elif accuracy < 90 or delay > 5:
#             recommendation = f"❌ Recommendation: CANCEL the contract with {vendor}."
#         else:
#             recommendation = f"⚠️ Recommendation: REVIEW the contract with {vendor}."

#         results.append(recommendation)

#     return render_template("index.html", results=results)

# if __name__ == "__main__":
#     app.run(debug=True)





















# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def evaluate_vendor():
#     results = []

#     if request.method == "POST":
#         vendor = request.form["vendor"]
#         accuracy = float(request.form["accuracy"])
#         delay = int(request.form["delay"])
#         revenue = float(request.form["revenue"])

#         # Simulated AI scoring
#         score = 0
#         score += (accuracy / 100) * 0.5         # 50% weight for accuracy
#         score += max(0, (5 - delay) / 5) * 0.3   # 30% weight for lower delay
#         score += min(revenue / 10000000, 1) * 0.2  # 20% weight for revenue (up to 10M)

#         # Simulated AI explanation
#         explanation = []
#         if accuracy >= 95:
#             explanation.append("High accuracy indicates strong performance.")
#         elif accuracy < 90:
#             explanation.append("Accuracy is below acceptable thresholds.")

#         if delay <= 2:
#             explanation.append("Fast delivery times suggest operational efficiency.")
#         elif delay > 5:
#             explanation.append("Delays are excessive and may affect business.")

#         if revenue >= 5000000:
#             explanation.append("Strong revenue contribution from vendor.")
#         elif revenue < 3000000:
#             explanation.append("Revenue contribution is relatively low.")

#         # AI-like recommendation based on score
#         if score >= 0.8:
#             recommendation = f"✅ AI Recommendation: RENEW the contract with {vendor}."
#         elif score < 0.5:
#             recommendation = f"❌ AI Recommendation: CANCEL the contract with {vendor}."
#         else:
#             recommendation = f"⚠️ AI Recommendation: REVIEW the contract with {vendor}."

#         full_response = recommendation + "<br><br><strong>AI Analysis:</strong><ul>"
#         for line in explanation:
#             full_response += f"<li>{line}</li>"
#         full_response += "</ul>"

#         results.append(full_response)

#     return render_template("index.html", results=results)

# if __name__ == "__main__":
#     app.run(debug=True)


























# from flask import Flask, render_template, request
# from datetime import datetime

# app = Flask(__name__)

# # Sample static data for vendors (in place of a database)
# vendor_data = {
#     "hindalco": {
#         "po_number": "PO123456",
#         "vendor": "Hindalco",
#         "gr_date": "2024-05-20",
#         "pr_date": "2024-05-15",
#         "revenue": 750000
#     },
#     "tata": {
#         "po_number": "PO654321",
#         "vendor": "Tata Steel",
#         "gr_date": "2024-05-25",
#         "pr_date": "2024-05-25",
#         "revenue": 450000
#     }
# }

# @app.route("/", methods=["GET", "POST"])
# def evaluate_vendor():
#     results = []
#     if request.method == "POST":
#         user_query = request.form["query"].lower()

#         # Simple extraction of vendor name from query
#         matched_vendor = None
#         for vendor in vendor_data:
#             if vendor in user_query:
#                 matched_vendor = vendor
#                 break

#         if matched_vendor:
#             data = vendor_data[matched_vendor]

#             gr_date = datetime.strptime(data["gr_date"], "%Y-%m-%d")
#             pr_date = datetime.strptime(data["pr_date"], "%Y-%m-%d")
#             delay = (gr_date - pr_date).days

#             delivery_status = "Late" if delay > 0 else "On Time"
#             revenue_impact = "High" if data["revenue"] > 500000 else "Low"

#             # Simple AI-like decision logic
#             if delay <= 0 and data["revenue"] >= 500000:
#                 recommendation = f"✅ Contract should be RENEWED for {data['vendor']}."
#             else:
#                 recommendation = f"❌ Contract should be CANCELLED for {data['vendor']}."

#             results.append({
#                 "po_number": data["po_number"],
#                 "vendor": data["vendor"],
#                 "gr_date": data["gr_date"],
#                 "pr_date": data["pr_date"],
#                 "delay": delay,
#                 "delivery_status": delivery_status,
#                 "revenue": f"₹{data['revenue']:,}",
#                 "revenue_impact": revenue_impact,
#                 "recommendation": recommendation
#             })

#         else:
#             results.append({
#                 "error": "Vendor not found. Please check the name and try again."
#             })

#     # Compute summary for charts
#     summary = {
#         "revenue_high": 0,
#         "revenue_low": 0,
#         "delivery_late": 0,
#         "delivery_on_time": 0,
#         "delivery_early": 0
#     }

#     for r in results:
#         if "error" not in r:
#             if r["revenue_impact"] == "High":
#                 summary["revenue_high"] += 1
#             else:
#                 summary["revenue_low"] += 1

#             if r["delay"] > 0:
#                 summary["delivery_late"] += 1
#             elif r["delay"] == 0:
#                 summary["delivery_on_time"] += 1
#             else:
#                 summary["delivery_early"] += 1

#     return render_template("index.html", results=results, summary=summary)


# if __name__ == "__main__":
#     app.run(debug=True) 





























































































































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
