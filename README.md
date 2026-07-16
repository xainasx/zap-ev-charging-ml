# Zap! Accelerating from Gas to Electric with Machine Learning

**Presented by:** Saniya Malkan Ahmed

## Overview

A machine learning forecasting system that ranks candidate EV charging stations by projected charging demand and time-to-profitability. The model guides capital allocation for a nationwide charger rollout, directing investment to the highest-return sites first.

## Business Objectives

| Metric | Current (Pilot) | Target |
|--------|-----------------|--------|
| Average payback period | ~36 months | 20 months |
| Charger utilisation (12 months post-install) | ~45% | 70-75% |
| Capital waste reduction (low-demand sites) | Baseline | -40% |

## Secondary Goal: Dynamic Pricing

Optimise time-of-day pricing for electricity and fuel at each station to lift blended energy margin per site by 8-12% within 12 months.

## Project Structure

```
zap-ev-charging-ml/
├── config/                 # Configuration files
│   └── config.yaml
├── data/                   # Data directories (not tracked in git)
│   ├── raw/
│   ├── processed/
│   └── external/
├── docs/                   # Project documentation and proposal
│   └── project_proposal.md
├── notebooks/              # Jupyter notebooks for exploration
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
├── src/                    # Source code
│   └── zap/
│       ├── __init__.py
│       ├── data/           # Data ingestion and loading
│       ├── features/       # Feature engineering
│       ├── models/         # Model training and prediction
│       └── evaluation/     # Model evaluation and metrics
├── tests/                  # Unit and integration tests
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/zap-ev-charging-ml.git
cd zap-ev-charging-ml

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

### Usage

```bash
# Run the full pipeline
python -m zap.pipeline

# Run individual steps
python -m zap.data.ingest
python -m zap.features.build
python -m zap.models.train
python -m zap.evaluation.evaluate
```

## Data Sources

| Source | Type | Update Frequency |
|--------|------|-----------------|
| Internal POS (fuel sales, transactions) | Structured (SQL/CSV) | Daily |
| EV charger telemetry (~150 pilot sites) | JSON (API) | Near real-time |
| Site attributes (parking, grid capacity) | Internal records | On survey/upgrade |
| DOE/NREL Alternative Fuel Stations API | JSON/CSV/GeoJSON | Days to weeks |
| State EV registrations (Atlas EV Hub) | Varies by state | Monthly to biannual |
| FHWA traffic counts (AADT) | Annual report | Annual |
| US Census (ACS) demographics | Tabular | Annual |

## Model Approach

- **Type:** Supervised prediction/forecasting
- **Algorithm:** Gradient boosted trees (scikit-learn / XGBoost)
- **Output:** Site-level rollout priority scorecard with demand forecast, recommended stall mix, projected payback period, and confidence score
- **Retraining cadence:** Quarterly

## Risk Mitigation

- Forecast error monitored via rolling MAPE; commitments frozen if error exceeds threshold
- Human sign-off required for large capital commitments
- Equity monitoring across income and geography
- Quarterly retraining to combat model drift
- Grid/interconnection feasibility check before any site is greenlit

## Licence

This project is licensed under the MIT Licence. See [LICENSE](LICENSE) for details.
