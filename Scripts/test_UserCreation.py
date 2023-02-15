import Config.conf
import Util.util
import requests
import pytest
from asserter import assert_equal,assert_true


#config alias
sConf = Config.conf
sUtil = Util.util
sEnv =  sConf.getEnvDetails("stagging")


@pytest.mark.positiveTest
def test_successfulPostCall():
    #TestSpecific
    data =  open('data/createUser.json')
    sURL = sEnv +'users'
    sPayload = sUtil.jsonReader(data)
    
    print ('url is : ',sURL)
    print ('sPayload is : ',sPayload)
    # rest call.

    sRes = requests.post(sURL,data=sPayload)
    #value, reference, entity_name, compare_types=False
    assert_equal(sRes.status_code,201,'statuscode',True)
    

    #To verify the response.
    sResponseJson = sUtil.textToJson(sRes.text)
    assert sResponseJson['name'] == "morpheus"
    assert sResponseJson['job'] == "leader"

    #Clearing objects
    data.close



@pytest.mark.negativeTest
def test_UnsuccessfulPostCall():
    #TestSpecific
    data =  open('data/createUser.json')
    sURL = sEnv +'users'
    sPayload = sUtil.jsonReader(data)
    
    print ('url is : ',sURL)
    print ('sPayload is : ',sPayload)
    # rest call.

    sRes = requests.post(sURL,data=sPayload)
    assert sRes.status_code == 200

    #To verify the response.
    sResponseJson = sUtil.textToJson(sRes.text)
    assert sResponseJson['name'] == "morpheus"
    assert sResponseJson['job'] == "leader"

    #Clearing objects
    data.close

