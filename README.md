# File Merge Pipeline

The **File Merge Pipeline** is a Flask-based web application designed to merge and process data from two different Excel reports. This application allows users to upload two reports: an Emercury Report and a Performance Report, which are then merged, processed, and returned as a downloadable Excel file.

## Features

- **File Upload:** Upload two Excel reports directly through the web interface.
- **Data Processing:** The application processes the uploaded reports, creates a pivot table, and updates specific values based on the provided data.
- **Merging:** Combines data from both reports into a single Excel file.
- **Download:** The processed and merged file is available for download.

## Requirements

The project requires the following Python libraries:

- Flask==3.0.3
- gunicorn==23.0.0
- pandas==2.2.2
- openpyxl==3.1.5
- numpy==2.1.0
- Jinja2==3.1.4
- Werkzeug==3.0.4
- blinker==1.8.2
- click==8.1.7
- colorama==0.4.6
- et-xmlfile==1.1.0
- itsdangerous==2.2.0
- MarkupSafe==2.1.5
- packaging==24.1
- python-dateutil==2.9.0.post0
- pytz==2024.1
- six==1.16.0
- tzdata==2024.1

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```



## Running the Application

To run the application locally:

### Clone the repository:

```bash
git clone <repository-url>
cd file-merge-pipeline
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
Run the application:
```bash
python app.py
```
Access the application:
Open your web browser and go to http://127.0.0.1:5000/.

Deployment
To deploy the application using Gunicorn, ensure that your Procfile is correctly set up:

```bash
web: gunicorn app:app
```
Deploy to your preferred hosting service, such as Heroku or AWS.

Usage
Upload Files:
- Upload the "Emercury Report" using the first file input.
- Upload the "Performance Report" using the second file input.
Merge and Download:
- Once both files are uploaded, the system will process the data and enable the download button.
- Click the "Download Merged File" button to download the processed Excel file.
License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
- Flask - Python web framework used to build this application.
- Pandas - Data processing library used for handling the Excel files.
- Openpyxl - Library used for reading and writing Excel files.
