# Cloud Cost Optimizer PoC

This repository contains a **Proof of Concept (PoC)** for an AI-driven (or rules-based) approach to **reduce unnecessary cloud spending**. The project currently focuses on **identifying underutilized resources** (e.g., servers/instances with low CPU usage) and suggesting potential optimizations.

## Goals
- Ingest cloud billing and usage data
- Flag underutilized resources
- Recommend corrective actions (resize, terminate, etc.)
- Calculate potential monthly savings

## MVP Scope
- AWS EC2 instances only (initially)
- Manual CSV export or API integration (Phase 2)
- Simple rules-based or basic ML approach to classify underutilized resources

## Getting Started
1. Clone this repo
2. Install Python dependencies (see requirements.txt)
3. Run `src/generate_mock_data.py` (optional) or `src/analyze_cost_data.py`
4. View `notebooks/analysis_demo.ipynb` for a demo

## Next Steps
- Extend to other AWS services (RDS, EBS, etc.)
- Integrate real-time usage with CloudWatch or AWS Cost Explorer API
- Add automated Slack/Email alerts

cloud-cost-optimizer-poc/
├── README.md                    # Project introduction and instructions
├── data/                        # Folder for CSVs, mock data, or analysis outputs
├── notebooks/                   # (Optional) Jupyter/Colab notebooks for demos & visualization
└── src/
├── generate_mock_data.py    # Script to generate synthetic billing/usage data
└── analyze_cost_data.py     # Script to flag underutilized resources & propose actions

### `src/generate_mock_data.py`
- Generates a CSV (`mock_billing_data.csv` by default) with random usage and cost data.
- Helps you **test** the analysis pipeline without needing real cloud data.

### `src/analyze_cost_data.py`
- Reads the CSV (mock or real) and applies **simple rules** to identify resources that might be underutilized.
- Produces a **recommendations** output (e.g., `recommendations.csv`) suggesting actions like “Consider resizing or terminating.”

## Getting Started

**Clone this repository**:
   ```bash
   git clone https://github.com/roninazure/cloud-cost-optimizer-poc.git
   cd cloud-cost-optimizer-poc

python3 -m venv venv
source venv/bin/activate
# If you have a requirements.txt (not included yet), install it:
# pip install -r requirements.txt

python src/generate_mock_data.py

python src/analyze_cost_data.py

## Roadmap
- **Phase 2**: Pull real data from AWS (Cost Explorer or S3 CSV exports).
- **Phase 3**: Introduce ML for anomaly detection or predictive cost forecasting.
- **Phase 4**: Automated remediation (tag or stop underutilized instances).
