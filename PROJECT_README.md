# Environment and Project Set Up

I set up this project using the guidance of this file: [Github File](https://github.com/de-2502-a/etl-project-demo/blob/initial-project-setup/docs/activity-6/activity-6.md) created by Ed Wright as a walkthrough project for a full ETL Pipeline.

## Step 1 Setup the Project Structure

```plaintext
etl-project-demo/
├── config/
│   ├── db_config.py
│   └── env_config.py
├── data/
│   ├── output/
│   ├── processed/
│   └── raw/
│       ├── unclean_customers.csv
│       ├── unclean_transactions.csv
│       └── unclean_transactions.sql
├── docs/
│   └── flowcharts/
│       └── etl_flowchart.md
├── etl/
│   ├── extract/
│   │   └── extract.py (to be populated)
│   ├── load/
│   │   └── load.py (to be populated)
│   ├── sql/
│   │   └── placeholder.sql (to be replaced)
│   ├── transform/
│       └── transform.py (to be populated)
├── notebooks/
│   └── exploratory_analysis.ipynb
├── scripts/
│   └── run_etl.py
├── tests/
│   ├── component_tests/
│   │   └── .gitkeep (to be replaced)
│   ├── integration_tests/
│   │   └── .gitkeep (to be replaced)
│   └── unit_tests
│   │   └── test_db_config.py
│   └── run_tests.py
├── utils/
│   └── logging_utils.py
├── .coveragerc
├── .env.dev
├── .env.test
├── .flake8
├── .gitignore
├── .sqlfluff
├── README.md
├── requirements-setup.txt
├── requirements.txt
└── setup.py
```

Follow the file structure above.

