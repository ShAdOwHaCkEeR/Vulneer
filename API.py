
def API_key():

	with open("API.config", "r") as cfgf:
		APIl = cfgf.readline()
		APIl = APIl.rstrip('\n')
		API_KEY = str(APIl).replace("API=", "")

	return API_KEY