import requests

def get(param):
    """
    @param  Request Parameter
    @return String
    """
    try:
        r = requests.get(f"https://akaneko-api.herokuapp.com/api/{param}").json()
    except Exception as e:
        raise Exception(f"ERROR: > {e}\n\n\nPlease Contact Raphiel#8922 or Open a Issue in https://github.com/RaphielHS/akaneko-wrapper/issues/")
    else:
        try:
            return r['url']
        except Exception as e:
            raise Exception(f"ERROR: > {e}\n\n\nPlease Contact Raphiel#8922 or Open a Issue in https://github.com/RaphielHS/akaneko-wrapper/issues/")