import argparse
import json
import re
import cv2
import os
import easyocr
from helpers.image_utils import preprocess_image
from helpers.validators import validate_form_data

# Hardcoded PATTERNS dictionary
PATTERNS = {
    "patient_name": r"Patient Name:\s*(.+)",
    "dob": r"DOB:\s*(\d{1,2}/\d{1,2}/\d{2,4})",  # Matches dates like 21/05/89 or 21/05/1989
    "date": r"Date:\s*(\d{1,2}/\d{1,2}/\d{2,4})",
    "injection": r"INJECTION:\s*YES\s*NO",  # Matches "INJECTION: YES NO"
    "exercise_therapy": r"Exercise Therapy:\s*YES\s*NO",  # Matches "Exercise Therapy: YES NO"
    "difficulty_ratings": {
        "bending": r"Bending or Stooping:\s*(\d)",
        "putting_on_shoes": r"Putting on shoes:\s*(\d)",
        "sleeping": r"Sleeping:\s*(\d)"
    },
    "patient_changes": {
        "since_last_treatment": r"Patient Changes since last treatment:\s*(.+)",
        "since_start_of_treatment": r"Patient changes since the start of treatment:\s*(.+)",
        "last_3_days": r"Describe any functional changes within the last three days \(good or bad\):\s*(.+)"
    },
    "pain_symptoms": {
        "pain": r"Pain:\s*(\d+)",
        "numbness": r"Numbness:\s*(\d+)",
        "tingling": r"Tingling:\s*(\d+)",
        "burning": r"Burning:\s*(\d+)",
        "tightness": r"Tightness:\s*(\d+)"
    },
    "medical_assistant_data": {
        "blood_pressure": r"Blood Pressure:\s*(\d+/\d+)",
        "hr": r"HR:\s*(\d+)",
        "weight": r"Weight:\s*(\d+)",
        "height": r"Height:\s*(\d+'\d+)",
        "spo2": r"SpO2:\s*(\d+)",
        "temperature": r"Temperature:\s*([\d.]+)",
        "blood_glucose": r"Blood Glucose:\s*(\d+)",
        "respirations": r"Respirations:\s*(\d+)"
    }
}

def extract_text(image_path):
    """Extract text from an image using EasyOCR."""
    reader = easyocr.Reader(['en'])
    processed_img = preprocess_image(image_path)
    results = reader.readtext(processed_img, paragraph=True)
    full_text = " ".join([res[1] for res in results])
    print("Extracted Text:\n", full_text)
    print("DEBUG - Raw OCR Text:\n", full_text)  # Add this line!
    return full_text# Debug statement
    


def parse_field(text, pattern, type_cast=str):
    """Extract a field using regex."""
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        try:
            return type_cast(match.group(1).strip())
        except:
            return match.group(1).strip()
    return None

def extract_data(text):
    """Extract structured data from OCR text."""
    data = {}
    for field, pattern in PATTERNS.items():
        if isinstance(pattern, dict):
            data[field] = {k: parse_field(text, v) for k, v in pattern.items()}
        else:
            data[field] = parse_field(text, pattern)
    return validate_form_data(data)

def main(input_path, output_dir):
    """Process a form and save the output."""
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    text = extract_text(input_path)
    form_data = extract_data(text)
    output_path = os.path.join(output_dir, "output.json")
    with open(output_path, "w") as f:
        json.dump(form_data, f, indent=2)
    print(f"JSON output saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="Path to input image")
    parser.add_argument("-o", "--output", default="data/json_output", help="Output directory")
    args = parser.parse_args()
    main(args.input, args.output)