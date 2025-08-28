import qrcode

# Get the UPI ID from user
upi_id = input("Enter your UPI ID: ")

# Define base parameters
payee_name = "Recipient Name"
merchant_code = "1234"

# Generate valid UPI payment URLs
phonepe_url = f'upi://pay?pa={upi_id}&pn={payee_name}&mc={merchant_code}'
paytm_url = f'upi://pay?pa={upi_id}&pn={payee_name}&mc={merchant_code}'
google_pay_url = f'upi://pay?pa={upi_id}&pn={payee_name}&mc={merchant_code}'

# Generate QR codes
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save QR codes as images
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')  # Fixed typo here (was `.ssave()`)

# Show QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
