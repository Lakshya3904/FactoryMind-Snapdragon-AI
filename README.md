# FactoryMind: Edge-Native Industrial AI

FactoryMind is an entirely offline, edge-native AI decision-support platform designed for Snapdragon-powered HP PCs. It provides zero-latency, privacy-first industrial energy optimization and quality assurance for SMEs.

## Architecture Highlights
* **Edge-Native:** 100% offline execution utilizing the Snapdragon NPU.
* **Computer Vision:** Real-time ingestion of 1024x1024 factory camera feeds, downsampled to 224x224, and processed via quantized YOLO models (via Qualcomm AI Hub) for defect detection.
* **Telemetry Analysis:** Time-series analysis of factory machine states to predict energy spikes and optimize power consumption.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure your Qualcomm AI Hub API token: `qai-hub configure --api_token API_TOKEN`
3. Run the edge server: `python main.py`