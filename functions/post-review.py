# This is the code for the IBM Cloud Function "post_review". 
# The function is part of a cloud-hosted API, so this code is not really part of
# the codebase for the Django website. I am mainly leaving it here for my own reference 
# and documentation's sake, as well as for any fellow learners who are curious about the 
# API and IBM Cloud Functions. 


# IBM Cloud-specific imports
import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# main() will be run automatically when this action is invoked in IBM Cloud
def main(dict):
    """
    Posts a review to the external Cloudant database

    :param dict: Cloud Functions actions accept a single parameter, which must be a JSON object.
                In this case, the param must be an a JSON object with the key "review" with the review data as value.
                I.e: {
                      "review": 
                                {
                                    "id": 1114,        
                                    "name": "Upkar Lidder",
                                    "dealership": 15,
                                    "review": "Great service!",
                                    "purchase": false,
                                    "another": "field",
                                    "purchase_date": "02/16/2021",
                                    "car_make": "Audi",
                                    "car_model": "Car",
                                    "car_year": 2021
                                }
                    }
                The "id" parameter is the id of the review.
    :return: The action returns a JSON object consisting of the HTTP response, which should contain a success message with code 200
             or an error message with code 500.
    """
    
    secret = {
        "COUCH_URL": "https://apikey-v2-7s35bctflx94clwa23fz248zaopau8wxq7a1ngys20j:480f32f9ff09c42fb2c30c02fc074b3f@89010d5b-3a79-41e5-8227-c6d10d34452b-bluemix.cloudantnosqldb.appdomain.cloud",
        "IAM_API_KEY": "0IQB-LxnKaqpt4GBlFWT3X-aLxESR8fD7Dfj3UdolDpq",
        "COUCH_USERNAME": "apikey-v2-7s35bctflx94clwa23fz248zaopau8wxq7a1ngys20j"
    };
    
    authenticator = IAMAuthenticator(secret["IAM_API_KEY"])
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url(secret["COUCH_URL"])
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    
    try:
        # result_by_filter=my_database.get_query_result(selector, raw_result=true)
        result={
            'headers': {'Content-Type':'application/json'},
            'body': {'data': response}
            }
        return result
    except:
        return {
            'statusCode': 404,
            'message': 'Something went wrong'
            }
        