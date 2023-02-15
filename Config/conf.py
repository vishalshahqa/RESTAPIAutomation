
def getEnvDetails(envName):
    match envName.lower():
        case "prod":
            return "https://reqres.in/api/"

        case "release":
            return "https://reqres.in/api/"
        
        case "stagging":
            return "https://reqres.in/api/"

        case default: # stagging
            return "https://reqres.in/api/"



def getHeader(headerName):
    match headerName.lower():
        case "get":
            return {}
        case "post":
            return {"Content-type": "application/json; charset=UTF-8"}
        case default:
            print("Sorry!, It is not supporting requested header yet")


