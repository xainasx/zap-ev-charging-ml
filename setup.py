"""Setup script for the Zap EV Charging ML project."""

from setuptools import setup, find_packages

setup(
    name="zap-ev-charging-ml",
    version="0.1.0",
    description=(
        "ML forecasting system for EV charging station site selection "
        "and rollout prioritisation"
    ),
    author="Saniya Malkan Ahmed",
    python_requires=">=3.9",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "scikit-learn>=1.5.0",
        "numpy>=1.26.0",
        "pandas>=2.2.0",
        "xgboost>=2.1.0",
        "pyyaml>=6.0",
        "requests>=2.32.0",
        "joblib>=1.4.0",
        "pydantic>=2.10.0",
        "geopy>=2.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-cov>=6.0.0",
            "ruff>=0.8.0",
            "jupyter>=1.0.0",
            "matplotlib>=3.9.0",
            "seaborn>=0.13.0",
        ],
    },
)
