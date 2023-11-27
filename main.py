import requests
from PIL import Image
from io import BytesIO
from fpdf import FPDF
import os

# Define the issue covers and titles as dictionaries
issue_data = [
  # justice-league-vs-godzilla-vs-kong-issue-1  
  {
        "title": "justice-league-vs-godzilla-vs-kong-issue-1",
        "covers": [
            "https://www.midtowncomics.com/images/PRODUCT/XL/2245222_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2245223_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2245224_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2245225_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2245226_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2245227_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2245228_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2245229_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2245230_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2245231_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2274624_xl.jpg",
        ]
    },
  # justice-league-vs-godzilla-vs-kong-issue-2  
  {
        "title": "justice-league-vs-godzilla-vs-kong-issue-2",
        "covers": [
            "https://www.midtowncomics.com/images/PRODUCT/XL/2251818_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2251819_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2251820_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2251821_xl.jpg",
            "https://www.midtowncomics.com/images/PRODUCT/XL/2251822_xl.jpg",
        ]
    },
    # Add more dictionaries for additional issues if needed
]


for issue in issue_data:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    issue_title = issue["title"]
    issue_covers = issue["covers"]
    
    for i, img_url in enumerate(issue_covers):
        response = requests.get(img_url)
        if response.status_code == 200:
            pageAsImage = Image.open(BytesIO(response.content))
            pageAsImage.save(f"{issue_title}-cover-{i+1}.jpg")
            width, height = pageAsImage.size
            pdf.add_page()
            pdf.image(f"{issue_title}-cover-{i+1}.jpg", 0, 0, 210, 297)  # Assuming A4 size, adjust as needed
            # Delete the image file after saving it to the PDF
            os.remove(f"{issue_title}-cover-{i+1}.jpg")
            
            print(f"{issue_title}-cover-{i+1}")
    
    pdf.output(f"{issue_title}-covers.pdf", 'F')