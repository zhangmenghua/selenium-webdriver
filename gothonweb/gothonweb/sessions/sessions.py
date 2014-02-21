import web
web.config.debug=False
urls=("/count","count",
		"/reset","reset")
app=web.application(urls,locals())
store=web.session.DiskStore('sessions')
session=web.session.Session(app,store,initializer={'count':0})

class count:
	def GEF(self):
		session.count +=1
		return str(session.count)
class reset:
	def GEF(self):
		session.kill()
		return ""
if __name__=="__main__":
	app.run
