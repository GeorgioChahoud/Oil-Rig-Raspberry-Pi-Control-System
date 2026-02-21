from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# Demo device state (instead of GPIO)
device_states = {
    "bop": False,
    "pump": False,
    "alarm": False
}

# Serve Dashboard
@app.route("/")
def dashboard():
    return render_template("index.html")


# Serve User Guide
@app.route("/user-guide")
def user_guide():
    return render_template("user-guide.html")


# Toggle device (demo prints state)
@app.route("/api/toggle/<device>", methods=["POST"])
def toggle(device):
    if device not in device_states:
        return jsonify({"error": "Unknown device"}), 400

    device_states[device] = not device_states[device]

    # Print instead of GPIO
    print("\n==============================")
    print(f"[{datetime.now()}]")
    print(f"Device Toggled: {device.upper()}")
    print(f"New State: {'ON' if device_states[device] else 'OFF'}")
    print("==============================\n")

    return jsonify({
        "status": "ok",
        "device": device,
        "state": device_states[device]
    })


# Status endpoint
@app.route("/api/status")
def status():
    # Simulated WiFi and server status
    wifi_connected = True
    server_online = True

    print(f"[{datetime.now()}] Status Check Requested")

    return jsonify({
        "wifi": wifi_connected,
        "server": server_online
    })

@app.route("/api/toggle-states")
def toggle_states():
    # Returns current ON/OFF state of devices
    return jsonify(device_states)


if __name__ == "__main__":
    print("===================================")
    print("Oil Rig Monitoring System Backend")
    print("Running in DEMO mode (No GPIO)")
    print("Serving HTML templates")
    print("===================================")
    app.run(host="0.0.0.0", port=5000, debug=True)
