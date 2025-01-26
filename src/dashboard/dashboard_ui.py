dashboard_ui.py
from flask import Flask, jsonify, render_template

app = Flask(name)

Sample data for AI agent performance
agent_data = {
    "agent_id": "AI-Agent-001",
    "status": "Active",
    "metrics": {
        "CPU Usage": "72%",
        "Memory Usage": "3.5GB",
        "Tasks Completed": 15,
        "Anomalies Detected": 2
    }
}

@app.route('/')
def home():
    """
    Renders the dashboard homepage.

    :return: Rendered HTML template for the dashboard.
    """
    return render_template("index.html", data=agent_data)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    """
    Provides real-time AI agent monitoring data in JSON format.

    :return: JSON response containing agent data.
    """
    return jsonify(agent_data)

if name == 'main':
    app.run(debug=True)
