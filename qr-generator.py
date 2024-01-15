import pandas as pd
import qrcode
import os

# Load the Excel file
df = pd.read_excel('giftcardlinks.xlsx')  # replace 'urls.xlsx' with your file name

if not os.path.exists('qr_codes'):
    os.makedirs('qr_codes')

# Iterate over the URLs
for index, row in df.iterrows():
    url = row['URL']  # replace 'URL' with your column name
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(f'qr_codes/{index}.png')  # replace 'qr_codes' with your folder name


# test comment and insertion with nvim 2
