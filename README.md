# Logistics Challenge

### Objective
A logistic related company wants to improve their comprehension about the performance of their deliveries at a national level.

### Repo Dependecies
```
conda env create -f environment.yml
conda activate log_delivery_analysis
```

### Repo structure
```
logistics-analytics-project/
│
├── README.md
├── environment.yml          # Python dependencies
├── .gitignore               # Ignore data, secrets, etc.
│
├── data/
│   ├── raw/                 # Synthetic raw data (e.g., generated CSVs)
│   ├── bronze/              # Extracted data from the sources
│   ├── silver/              # Pre-processed data
│   └── gold/                # Data ready for analysis
│
├── notebooks/               # Jupyter/Colab notebooks (exploratory or prototype)
│   └── data-exploration.ipynb
│
├── src/                     # Source code for pipeline and generation
│   ├── __init__.py
│   ├── generate/            # Synthetic data generator code
│   │   └── synthetic_logistics_data.py
│   ├── pipeline/            # ETL or data transformation logic
│   │   ├── bronze.py
│   │   ├── silver.py
│   │   └── gold.py
│   └── utils/               # Helper functions (e.g., config loader, validators)
│
├── powerbi/                 # .pbip folder, schema reference, and documentation
│
└── tests/                   # Unit tests for data generation and pipeline
    ├── test_generator.py
    └── test_pipeline.py
```