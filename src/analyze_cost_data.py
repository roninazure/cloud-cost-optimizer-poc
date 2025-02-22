import csv
import os

def analyze_cost_data(
    input_file='data/mock_billing_data.csv', 
    output_file='data/recommendations.csv',
    cpu_threshold=20.0,
    mem_threshold=20.0,
    io_threshold=50.0,          # e.g., if IO usage < 50 IOPS?
    storage_threshold=10.0      # e.g., if storage < 10 GB means it's small?
):
    """
    Basic analysis to flag underutilized resources based on CPU, memory, I/O, and storage usage.
    """
    
    recommendations = []
    if not os.path.exists(input_file):
        print(f"[ERROR] Input file not found: {input_file}")
        return
    
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Parse numeric fields
            cpu_util = float(row.get("cpu_utilization", 0))
            mem_util = float(row.get("memory_utilization", 0))
            io_usage = float(row.get("io_usage", 0))
            storage_used = float(row.get("storage_used_gb", 0))
            cost = float(row.get("cost", 0))

            resource = row.get("resource_id", "unknown")
            r_type   = row.get("resource_type", "unknown")
            date     = row.get("date", "unknown")

            # Logic: If CPU & memory are both below thresholds, 
            # plus IO is low & storage is small => consider downsizing or terminating.
            # Customize as needed!
            under_cpu   = cpu_util < cpu_threshold
            under_mem   = mem_util < mem_threshold
            under_io    = io_usage < io_threshold
            under_store = storage_used < storage_threshold

            # For demonstration, we'll flag a resource if CPU & memory are both under threshold
            # (plus either low IO or small storage). 
            # You can tweak this condition to match real needs!
            if under_cpu and under_mem and (under_io or under_store):
                rec = {
                    "resource_id": resource,
                    "resource_type": r_type,
                    "date": date,
                    "cpu_util": cpu_util,
                    "memory_util": mem_util,
                    "io_usage": io_usage,
                    "storage_used_gb": storage_used,
                    "cost": cost,
                    "recommendation": "Consider downsizing or terminating (underutilized CPU & Mem)"
                }
                recommendations.append(rec)
    
    # Write out summary of recommendations
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', newline='') as f:
        fieldnames = [
            "resource_id", 
            "resource_type", 
            "date", 
            "cpu_util", 
            "memory_util",
            "io_usage",
            "storage_used_gb",
            "cost", 
            "recommendation"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(recommendations)
    
    print(f"[INFO] Analysis complete. {len(recommendations)} recommendations -> {output_file}")

if __name__ == "__main__":
    analyze_cost_data()
