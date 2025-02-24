import re

emails = ['park@naver.com', 'kim@daum.net', 'lee@myhome.co.kr']

pattern = r".*[@].*[.](?=com$|net$).*$"

matching_emails = [email for email in emails if re.match(pattern,email)]
print(matching_emails)