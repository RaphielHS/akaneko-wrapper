from .req import get

__version__ = '1.1.8'
class LimitExceeded(Exception):
    pass

def lewdbomb(n: int):
    if n > 20:
        raise LimitExceeded("[AKANEKO] The amound is too great than 20!")
    if n <= 0:
        n = 5
    urls = []
    for _ in range(int(n)):
        r = get('random')
        urls.append(r)
    return urls

def ass():
    return get('ass')

def bdsm():
    return get('bdsm')

def bondage():
    return get('bdsm')

def cum():
    return get('cum')

def hentai():
    return get('hentai')

def femdom():
    return get('femdom')

def doujin():
    return get('doujin')

def maid():
    return get('maid')

def maids():
    return get('maid')

def orgy():
    return get('orgy')

def panties():
    return get('panties')

def wallpapers():
    return get('nsfwwallpapers')

def mobileWallpapers():
    return get('nsfwmobilewallpapers')

def netorare():
    return get('netorare')

def cuckold():
    return get('netorare')

def gifs():
    return get('gifs')

def gif():
    return get('gif')

def blowjob():
    return get('blowjob')

def feet():
    return get('feet')

def pussy():
    return get('pussy')

def uglyBastard():
    return get('uglybastard')

def uglybastard():
    return get('uglybastard')

def uniform():
    return get('uniform')

def gangbang():
    return get('gangbang')

def foxgirl():
    return get('foxgirl')

def cumslut():
    return get('cumslut')

def glasses():
    return get('glasses')

def thighs():
    return get('thighs')

def tentacles():
    return get('tentacles')

def masturbation():
    return get('masturbation')

def school():
    return get('school')

def yuri():
    return get('yuri')

def zettaiRyouiki():
    return get('zettaiRyouiki')

def zettairyouiki():
    return get('zettaiRyouiki')

def succubus():
    return get("succubus")