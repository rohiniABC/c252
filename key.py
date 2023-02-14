from flask import Flask,jsonify,reader_template,request
import os 
import datetime
from firebase_admin import credentials,initialize_app,firestore
from key import creds
import firebase_admin

app=Flask(__name__)
if not firebase_admin._apps:
  cred=credentials.certificate(creds)
  default_app=initialize_app(cred)
  firebase_db=firestore.client()


@app.route("/add_data",methode=["POST"])
def add_data():
  try:
    temperature=request.json.get("temperature")
    humidity=request.json.get("humidity") 
    altitude=request.json.get("altitude")
    pressure=request.json.get("pressure")
    document_ref=firebase_db.collection("data")
    add_values=document_ref.document().create(dict(temperature=temperature,humidity=humidity,altitude=altitude, pressure=pressure)) 
    return jsonify({
      "status":"success"
    }),201

  except Exception as e:
    return jsonify({
      "status":"success"
    }),201
  

creds = {
  "type": "service_account",
  "project_id": "monitoringsystem-8c7ee",
  "private_key_id": "57ae9da69cc84f34e7479f974085aefbd8c0a002",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCbn9y4ELbD+dpX\n2FTNY+NHOQQ2YBR388mIlgz5bhuHEMmooDC42FR7NJQUQ1u1PBH/3eoNJ9aXf6fI\nU47gxpn5Omomyg32pTVnkFbDMH5iQvZ524ujmWC7ydSBOCiwQZtSfc8GzXGxN9tq\n56gg7OmPSzYoOnDe/3L+Y84xtPpKlLJuoOhCe2VQRUmoRegBqG+q9JnZvoP5RXcq\nddoGaMT8LWOmZ1K6/tJKeqCrTbf6h+lDAWXmwOI6UiHz936dkImXPDV0ldB1sBKj\n9JaD1ZzTQA+6z+NNN7ae8w4UvAYnNCNv4lqtuRdm3Hj+X7WfSCMeeVm388YLkAYA\nt3tE21XXAgMBAAECggEAFK9oABNAp8XjDsATbYV0ZTgf5jZZIiSGSiBfsxu+jvJd\nS4uXTkp62DGB6TuWyf0lC1Rs0rjT3ik6nPb2S8w6FRV9nJBI0NrewVg/IAynD9qE\ntmfHJMSzReKq204iomLmCU3toaLXFM4u3QPTpiS3WrONjEVQUWO03jlX4+WBSz5J\nauRa2cQOtU8UZadvuJH5Pe4rXtmCzJ6B9zM4MeL0YUZvqh9EtZzgHU1CbEOxAB+f\nd6c6jDW4i0TedhajTpuuMGbgZplntPvNtrMYTdMw/D8lmWWcS9F9r6XeDwwevnE4\nHPEiujslE6L/9IuaJGN+PYg+Twwdz3bwFiIL/Da2gQKBgQDPsPltycoL3dF4DDgO\ngvhSvbo0AzWFSEBOvnFqxwkiozjwZHSDUJ1lNxzzI7InRJVp3qpmgDbNewJwgbxU\ndyzup2Zvn1HLB2ZwqJH+6mB1PcNKkg0YeQsyKFA/ZNOaPIUtgC+ZKzCTd+nS1RD/\nBTEbnkBvq3iuSgRTYJqIsTH4FwKBgQC/0o5M4w0V0HEfrBrbhcAEeoOfynXJDegx\ngu9DdMR0/q4RQtyJ+ZJdhiyjHGV7u6jc7R8B4rnJA69ylhTrSBF4qvoLJUuYJ4GJ\nsU2janOSv+P8XRDMI3+rx9k2oq2QMc3Fw7Jpt36SuNeQsScE5GTUoRfqgqraSdNr\nASYVc+5oQQKBgHrHfX0I2LfRJx7X4l+5z0FixewvpXkocFPcw8HC7kSax3Ndf3+N\nra6DOUsHZC9QnR+cMZIs47jvqk6Gc6ZfWaGwNp9wSPNEaavaC4zuU52bqJKx6qn4\nDMVXDbGcUneQpY5zhDABV1MmhYVMziJkmFZiZGdfsBUgzpPXvSNn1Ul7AoGBAJdl\nSpSae0BlVHNn9YafKK8gNvSN6aq2hDVXnxnBdjDUtXPALqnjRUb1WBOgnOQsd5lu\nuRNW68UgWH/6viX4qnlvkIvtcp1zSMTxIFLC+NaxBvKuTUyhE+nzgJeji5MMC9lz\nnEPd5FNO+iwj9aTh0kcTofmgCdLhg7CnpnQ2HMtBAoGBAKdU+dccIQYUy2wH9huY\nIglXSnco+U62bMgO7fvqS5GlA6YK9zoVQ2YDzC3u6iNmB/vajX8kPrqOJO3IsvFG\n8GljOHz1owzXRCy+cvkCOhu0vcD5HB2VH3sn6ev14VTkbgU5rjdvWA/J3J36Yq9C\nwLNEQRjciu+fTHYvhyi7eCq3\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-dnuo9@monitoringsystem-8c7ee.iam.gserviceaccount.com",
  "client_id": "108374545442366971338",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-dnuo9%40monitoringsystem-8c7ee.iam.gserviceaccount.com"
}