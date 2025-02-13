# Patient Assessment Form Processor

## Overview
This project automates the extraction of data from patient assessment forms using OCR and stores the results in a PostgreSQL database.

## Directory Structure

patient-assessment-ocr/
├── .env.example                # Environment variable template
├── .gitignore                  # Specifies files to ignore in Git
├── README.md                   # Project documentation & setup guide
├── requirements.txt            # Python dependencies
│
├── src/
│   ├── ocr_processing.py       # Main OCR processing script
│   ├── database.py             # Database interaction logic
│   └── helpers/                # Optional utility modules
│       ├── image_utils.py      # Image preprocessing functions
│       └── validators.py       # Data validation functions
│
├── data/
│   ├── sample_forms/           # Sample input documents
│   │   ├── sample_form.jpg     # Example form (provided by user)
│   │   └── blank_form.pdf      # Blank template (provided by user)
│   └── json_output/            # Generated JSON files
│       └── output.json  # Example JSON output
│
├── sql_schemas/
│   └── schema.sql              # Database schema definition
│
├── tests/                      # Unit tests
│   ├── test_ocr_processing.py
│   └── test_database.py
│
├── config/                     # Configuration files
│   └── patterns.yaml           # Regex patterns for data extraction
│
└── docs/                       # Documentation
    └── workflow.md             # System architecture diagram/explanation

Copy

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/patient-assessment-ocr.git
   cd patient-assessment-ocr
Install dependencies:

bash
Copy
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
Set up the database:

bash
Copy
createdb medical_db  # Requires PostgreSQL
psql medical_db -f sql_schemas/schema.sql
Copy .env.example to .env and update the credentials.

Usage
Process a single form:

bash
Copy
python src/ocr_processing.py -i data/sample_forms/sample_form.jpg
Store results in the database:

bash
Copy
python src/database.py --store data/json_output/sample_output.json
Testing
Run tests with:

bash
Copy
pytest tests/