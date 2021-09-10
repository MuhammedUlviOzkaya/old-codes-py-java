import smtplib

content = "Merhaba Ben Buz Sprays Ve ENSENDEYİM!"

mail = smtplib.SMTP("smtp.gmail.com", 587)

mail.ehlo()

mail.starttls()

mail.login()

mail.sendmail("buzsprays@gmail.com", "buzsprays@gmail.com", content)



