import qrcode

# Prompt the user for a URL or text to encode
data = input("Enter the URL or text to encode in the QR code: ")

# Generate a valid filename by replacing unwanted characters
filename = data.replace("http://", "").replace("https://", "").replace("/", "_").replace(":", "_") + ".png"
try:
    # Generate the QR code
    img = qrcode.make(data)

    # Save the QR code image with the generated filename
    img.save(filename)

    print(f"QR Code generated and saved as '{filename}'")
except Exception as e:
    print(f"An error occurred: {e}")
