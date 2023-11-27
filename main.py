import requests
from PIL import Image
from io import BytesIO
from fpdf import FPDF

first_issue_title = "justice-league-vs-godzilla-vs-kong-issue-1"
first_issue_covers = [
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

second_issue_title = "justice-league-vs-godzilla-vs-kong-issue-2"
second_issue_covers = [
  "https://www.midtowncomics.com/images/PRODUCT/XL/2251818_xl.jpg",
  "https://www.midtowncomics.com/images/PRODUCT/XL/2251819_xl.jpg",
  "https://www.midtowncomics.com/images/PRODUCT/XL/2251820_xl.jpg",
  "https://www.midtowncomics.com/images/PRODUCT/XL/2251821_xl.jpg",
  "https://www.midtowncomics.com/images/PRODUCT/XL/2251822_xl.jpg",
]

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

for i, img_url in enumerate(second_issue_covers):
    response = requests.get(img_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.save(f"{second_issue_title}-cover-{i}.jpg")
        pdf.add_page()
        pdf.image(f"{second_issue_title}-cover-{i}.jpg", 0, 0, 210, 297)  # Assuming A4 size, adjust as needed

pdf.output(f"{second_issue_title}-covers.pdf", 'F')
