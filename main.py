import time
import random
from pipeline import FactoryMindPipeline

def run_edge_server():
    print("=======================================")
    print(" Starting FactoryMind Edge Server")
    print(" Hardware Target: Snapdragon X Elite NPU")
    print("=======================================\n")
    
    pipeline = FactoryMindPipeline()
    
    try:
        for i in range(1, 6):
            print(f"\n--- Processing Cycle {i} ---")
            
            # 1. Vision Quality Check 
            has_defect = pipeline.process_inspection_frame(f"camera_feed_{i}.jpg")
            if has_defect:
                print(">> ALERT: Defect detected on assembly line! Routing image to operator.")
            else:
                print(">> Quality check passed.")
                
            # 2. Energy Telemetry Check
            mock_telemetry = [
                {"timestamp": time.time(), "machine_id": "M1", "power_kw": random.uniform(30.0, 60.0)} 
                for _ in range(5)
            ]
            energy_status = pipeline.analyze_energy_telemetry(mock_telemetry)
            print(f">> {energy_status}")
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutting down FactoryMind Edge Server.")

if __name__ == "__main__":
    run_edge_server()