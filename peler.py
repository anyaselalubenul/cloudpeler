from DrissionPage import ChromiumPage

p = ChromiumPage()
p.get('https://anysite.com')
i = p.get_frame('@src^https://challenges.cloudflare.com/cdn-cgi')
e = i('.mark')

sleep(3)

e.click()
