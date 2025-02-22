import csv
import random
import datetime

def generate_mock_billing_data(output_file='data/mock_billing_data.csv', num_records=50):
    """
    Generates synthetic billing data for demonstration.
    """
    header = [
    "resource_id", 
    "resource_type", 
    "date",
    "usage_hours", 
    "cost", 
    "cpu_utilization",
    "memory_utilization",   # new
    "io_usage",             # new (could be IOPS or MB/s)
    "storage_used_gb"       # new
] 

    resources = ["EC2-i1", "EC2-i2", "EC2-i3", "EC2-i4"]
    resource_types = ["t2.micro", "t2.large", "m5.large"]

    start_date = datetime.datetime(2025, 1, 1)
    
    rows = []
    for i in range(num_records):
        resource = random.choice(resources)
        r_type = random.choice(resource_types)
        
        # Random cost, usage, CPU
        cost = round(random.uniform(0.1, 10.0), 2)  
        usage_hrs = random.randint(12, 24)
        cpu_util = round(random.uniform(0, 100), 2)

        current_date = (start_date + datetime.timedelta(days=i)).strftime('%Y-%m-%d')
        
        rows.append([resource, r_type, current_date, usage_hrs, cost, cpu_util])

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"[INFO] Mock billing data generated: {output_file}")

if __name__ == "__main__":
    generate_mock_billing_data()
