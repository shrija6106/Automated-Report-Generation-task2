This project generates a professional internship report PDF with:
✅ A colorful cover page (title, name, course, QR code)
✅ A data table automatically read from a CSV file
✅ Auto-open feature after PDF generation

🚀 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/Intern-Report-Generator.git
cd Intern-Report-Generator

2️⃣ Create Virtual Environment (optional but recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux/Mac

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


Or install manually:

pip install reportlab pandas qrcode[pil] PyPDF2

4️⃣ Add Your Data

Place your CSV file inside the project folder. Example:
data.csv

Date,Task,Status,Remarks
2025-07-01,Research on Cybersecurity,Completed,Good progress
2025-07-05,Python Automation,Completed,Efficient
2025-07-10,Report Writing,Ongoing,Needs Review

5️⃣ Run the Script
python reportgenerator.py

6️⃣ View the Report

The script will automatically open the generated Intern_Report_Shrija.pdf file.
If it doesn’t, you can manually open it from the project folder.

📦 Requirements File (requirements.txt)
reportlab
pandas
qrcode[pil]
PyPDF2
