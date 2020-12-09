import smtplib

user = 'lhquser8@ligflat.com'
password = 'test123'

email_text = """\
From: lhquser8@ligflat.com
To: l50586_zxcvb@lm-demo.lyris.net
Subject: Test DEV50586
Date: Tue, 01 Oct 2020 11:11:11 +0300
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="MIMEBoundary06910f0b7c2ec5ea3a1558d736addb32"
--MIMEBoundary06910f0b7c2ec5ea3a1558d736addb32
Content-Type: text/plain; charset="iso-8859-1"
Content-Transfer-Encoding: base64
VGVzdCA1MDU4NgphbmQgNTA1ODYgVGVzdAo=
--MIMEBoundary06910f0b7c2ec5ea3a1558d736addb32
Content-Type: text/html; charset="iso-8859-1"
Content-Transfer-Encoding: base64
PHA+SHRtbCBUZXN0IDUwNTg2PC9wPgo8cD41MDU4NiB0ZXN0PC9wPg==
--MIMEBoundary06910f0b7c2ec5ea3a1558d736addb32--
""" 

try:
    server = smtplib.SMTP_SSL('mail.ligflat.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail('lhquser8@ligflat.com', 'l50586_zxcvb@lm-demo.lyris.net', email_text)
    server.close()

    print(email_text)
except:
    print("error ...")

