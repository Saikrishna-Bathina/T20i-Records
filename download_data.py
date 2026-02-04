import urllib.request
import zipfile
import io
import os
import ssl

def download_and_extract_data():
    url = "https://cricsheet.org/downloads/t20s_csv.zip"
    print(f"Downloading data from {url}...")
    
    # Create an unverified context to avoid SSL errors on some systems
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    with urllib.request.urlopen(url, context=ctx) as response:
        data = response.read()
        
    print("Extracting zip file...")
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        z.extractall("data")
    print("Data extracted to 'data/' directory.")

if __name__ == "__main__":
    download_and_extract_data()
