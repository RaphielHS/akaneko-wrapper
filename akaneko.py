import requests

def __get(params):
	res = requests.get(f"https://akaneko-api.herokuapp.com/api/{params}")
	json = res.json()
	try:
		url = json["url"]
	except:
		raise ValueError("Invalid Result. Please contact Owner Discord for Report. Raphiel#4045")
	return url

def neko():
	return __get("neko")

def sfwfoxes():
	return __get("sfwfoxes")

def wallpapers():
	return __get("wallpapers")

def mobileWallpapers():
	return __get("mobilewallpapers")

class Nsfw:
	def __get(self, params):
		res = requests.get(f"https://akaneko-api.herokuapp.com/api/{params}")
		json = res.json()
		try:
			url = json["url"]
		except:
			raise ValueError("Invalid Result. Please contact Owner Discord for Report. Raphiel#4045")
		return url

	def bdsm(self):
		return self.__get(params="bdsm")

	def cum(self):
		return self.__get(params="cum")
	
	def doujin(self):
		return self.__get(params="doujin")
	
	def femdom(self):
		return self.__get(params="femdom")
	
	def hentai(self):
		return self.__get(params="hentai")
	
	def maid(self):
		return self.__get(params="maid")

	def orgy(self):
		return self.__get(params="orgy")
	
	def panties(self):
		return self.__get(params="panties")
	
	def wallpaper(self):
		return self.__get(params="nsfwwallpaper")
	
	def wallpapers(self):
		return self.__get(params="nsfwwallpaper")
	
	def mobilewallpapers(self):
		return self.__get(params="nsfwmobileWallpapers")
	
	def cuckhold(self):
		return self.__get(params="netorare")
	
	def netorare(self):
		return self.__get(params="netorare")
	
	def gifs(self):
		return self.__get(params="gif")
	
	def gif(self):
		return self.__get(params="gif")
	
	def blowjob(self):
		return self.__get(params="blowjob")
	
	def feet(self):
		return self.__get(params="feet")
	
	def pussy(self):
		return self.__get(params="feet")
	
	def uglyBastard(self):
		return self.__get(params="uglybastard")
	
	def uniform(self):
		return self.__get(params="uniform")
	
	def gangbang(self):
		return self.__get(params="gangbang")
	
	def foxgirl(self):
		return self.__get(params="foxgirl")
	
	def cumslut(self):
		return self.__get(params="cumslut")
	
	def glasses(self):
		return self.__get(params="glasses")
	
	def thighs(self):
		return self.__get(params="thighs")
	
	def tentacles(self):
		return self.__get(params="tentacles")
	
	def loli(self):
		return self.__get(params="loli")
	
	def masturbation(self):
		return self.__get(params="masturbation")
	
	def school(self):
		return self.__get(params="school")
	
	def yuri(self):
		return self.__get(params="yuri")
	
	def zettaiRyouiki(self):
		return self.__get("zettai-ryouiki")

nsfw = Nsfw()