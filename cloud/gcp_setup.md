
# GCP Setup Guide

1. Create a GCP project and enable Pub/Sub.
2. Create a topic and subscription:
   ```
   gcloud pubsub topics create iot-sensor-data
   gcloud pubsub subscriptions create iot-sub --topic=iot-sensor-data
   ```
3. Create a service account with Pub/Sub Subscriber role.
4. Download the service account JSON and set `GOOGLE_APPLICATION_CREDENTIALS`:
   ```
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-key.json"
   ```
