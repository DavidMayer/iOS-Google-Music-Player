import httplib
import urllib

connection = httplib.HTTPConnection("music.google.com")

headers = {
	"Host" : "music.google.com",
	"Connection" : "keep-alive",
	"Origin" : "http://music.google.com",
	"User-Agent" : "CGM 0.0.1",
	"Content-Type" : "application/x-www-form-urlencoded;charset=UTF-8",
	"Accept" : "*/*",
	"Accept-Encoding" : "gzip,deflate,sdch",
	"Accept-Language" : "en-US,en;q=0.8",
	"Accept-Charset" : "ISO-8859,utf-8;q=0.7,*;q=0.3",
	"Cookie" : "xt=AM-WbXi5Jsd075PI-8_tV_JJbAdB-adn7Q:1310957089; sjpref=v:100|; PREF=ID=ebdbd00c66c6cbd4:U=5417f3be655c17d5:FF=0:TM=1304106728:LM=1304131817:GM=1:S=mRorcTqf8QErsTyL; sjsaid=12fcaee6-f2da-4a69-b75e-3c99b5334755; HSID=AyaHj4Tt-v7WtcF-5; NID=49=FNbs-Co7yyHrGyQlLuQPpBKjsiesAaIeaIi_nGNuD8yPOwQo1peVfSa5wZGMtsR81k7muFjuiREA8xJY5dGxysoHZJ6LV0o_n2CwAsr9h3-vx-AizH4lvCynx5ZoVF9e; SID=DQAAANUAAAD5MPrw5mCBAXKfwKf-jM1xMSvtZxyGxWy1Vy_jUSwebq7_f4FESVHvKlODyiYmknDOGnIaa2iQM7OAQ0fFRsUVDY2UeolmWXTpKiSrqRx_dhs3kMicofpo7Ho9wPh7P9oygykyPG0d6XI434fAA07Lk7G3CXM3Uhdr56l4y6eUeoxt80bTwuai9FIFvZt9Rtvfa0zfHqJkAUWoQ4YGwPD3Z7naL3pzcNcY62s6MmlY1FimBzpn0ATitMQnxHXSpEhYXcN1hF2holt251zp6Yd6HD6Ya5B5a3Jxw9QW4l3Ibw"
}


url = "/music/services/loadalltracks?u=0&xt=AM-WbXi5Jsd075PI-8_tV_JJbAdB-adn7Q:1310957089"

print "Sending request..."
connection.request("POST", url, "json={}", headers)

print "Getting response..."
response = connection.getresponse()
print response.status, response.reason

data = response.read()
print data

connection.close()