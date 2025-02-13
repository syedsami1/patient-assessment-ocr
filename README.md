# Patient Assessment Form Processor

## Overview
The Patient Assessment Form Processor automates the extraction of data from patient assessment forms using OCR (Optical Character Recognition) and stores the results in a PostgreSQL database. This solution streamlines the data extraction process for medical records, improving accuracy and efficiency.

## Directory Structure
Below is the project directory structure:

```plaintext
patient-assessment-ocr/
├── .env.example                # Environment variable template
├── .gitignore                  # Specifies files to ignore in Git
├── README.md                   # Project documentation & setup guide
├── requirements.txt            # Python dependencies
├── src/
│   ├── ocr_processing.py       # Main OCR processing script
│   ├── database.py             # Database interaction logic
│   └── helpers/                # Optional utility modules
│       ├── image_utils.py      # Image preprocessing functions
│       └── validators.py       # Data validation functions
├── data/
│   ├── sample_forms/           # Sample input documents
│   │   ├── sample_form.jpg     # Example form (provided by user)
│   │   └── blank_form.pdf      # Blank template (provided by user)
│   └── json_output/            # Generated JSON files
│       └── output.json         # Example JSON output
├── sql_schemas/
│   └── schema.sql              # Database schema definition
├── tests/                      # Unit tests
│   ├── test_ocr_processing.py
│   └── test_database.py
├── config/                     # Configuration files
│   └── patterns.yaml           # Regex patterns for data extraction
└── docs/                       # Documentation
    └── workflow.md             # System architecture diagram/explanation
```

## Setup

### 1. Clone the Repository
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/yourusername/patient-assessment-ocr.git
cd patient-assessment-ocr
```

### 2. Create a Virtual Environment and Install Dependencies
Create a virtual environment and install the required packages:
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
# venv\Scripts\activate    # For Windows
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy the `.env.example` file to `.env` and update the credentials:
```bash
cp .env.example .env
```

### 4. Set Up the Database
Create a PostgreSQL database and initialize it with the provided schema:
```bash
createdb medical_db
psql medical_db -f sql_schemas/schema.sql
```

## Usage

### Process a Patient Assessment Form
Run the OCR processing script to extract data from a sample form:
```bash
python src/ocr_processing.py -i data/sample_forms/sample_form.jpg
```

### Store Extracted Data in the Database
Store the OCR results into the PostgreSQL database:
```bash
python src/database.py --store data/json_output/sample_output.json
```

## Testing
Run the unit tests to ensure everything is working as expected:
```bash
pytest tests/
```

