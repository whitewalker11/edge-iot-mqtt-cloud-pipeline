#!/bin/bash
echo "Running network tests..."

# Ping test to MQTT broker
echo "🔹 Ping MQTT broker:"
ping -c 4 test.mosquitto.org

# Curl latency to Google Cloud
echo "🔹 Curl request to Google Cloud Pub/Sub REST endpoint (latency test):"
curl -w "@curl-format.txt" -o /dev/null -s https://pubsub.googleapis.com

# Simulated performance benchmark with iperf3 (must be installed in real environment)
echo "🔹 Skipping iperf3 (requires server), placeholder here"
