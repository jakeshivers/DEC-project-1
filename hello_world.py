import pycurl
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
#c.setopt(c.URL, 'https://httpbin.org/get')
#c.setopt(c.URL, 'https://httpbin.org/get?dog=dog')
c.setopt(c.URL, 'https://oasis.caiso.com/mrtu/GroupZip?groupid=RTM_LMP_GRP&startdate=20240901&opr_hr=01')

c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
print(body.decode('utf-8'))