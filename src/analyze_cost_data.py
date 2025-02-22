import csv

def analyze_cost_data(input_file='data/mock_billing_data.csv', output_file='data/recommendations.csv'):
    """
    Basic analysis to flag underutilized resources based on CPU utilization.
    """
    underutilized_threshold = 20.0  # CPU < 20% considered underutilized

    recommendations = []
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cpu_util = float(row["cpu_utilization"])
            cost = float(row["cost"])
            resource = row["resource_id"]
            r_type = row["resource_type"]
            date = row["date"]

            if cpu_util < underutilized_threshold:
                rec = {
                    "resource_id": resource,
                    "resource_type": r_type,
                    "date": date,
                    "cpu_util": cpu_util,
                    "cost": cost,
                    "recommendation": "Consider resizing or terminating"
                }
                recommendations.append(rec)
    
    # Write out summary of recommendations
    with open(output_file, 'w', newline='') as f:
        fieldnames = ["resource_id", "resource_type", "date", "cpu_util", "cost", "recommendation"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(recommendations)
    
    print(f"[INFO] Analysis complete. {len(recommendations)} recommendations generated -> {output_file}")

if __name__ == "__main__":
    analyze_cost_data()
