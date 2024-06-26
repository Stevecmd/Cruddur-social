# Week 3 — Decentralized Authentication
This was technically the fourth week of the Bootcamp. 

(The Hyperlinks in the table below link to the training videos)
<hr/>

| Homework      | Completed     | Not Completed  |
| ------------- |:-------------:| -----:|
| [Decentralized Authentication](https://www.youtube.com/watch?v=9obl7rVgzJw&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=41)  | ✔     |    |
| [Ashish's - Decenteralized Authentication](https://www.youtube.com/watch?v=tEJIeII66pY&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=39)   | ✔ |  |
| [Setup Cognito User Pool](https://www.youtube.com/watch?v=9obl7rVgzJw&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=40)  | ✔     |    |
| [Implement Custom Signin Page](https://www.youtube.com/watch?v=9obl7rVgzJw&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=40) | ✔      |   |
| [Implement Custom Signup Page](https://www.youtube.com/watch?v=T4X4yIzejTc&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=41 )|✔      |   |
| [Watched Ashish's Week 2 - Observability Security Considerations](https://www.youtube.com/watch?v=bOf4ITxAcXc&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=31)|✔      |   |
| [Implement Custom Confirmation Page](https://www.youtube.com/watch?v=T4X4yIzejTc&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=41)|    ✔  |   |
| [Implement Custom Recovery Page](https://www.youtube.com/watch?v=T4X4yIzejTc&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=41)  | ✔   |   |
| [Different approaches to verifying JWTs](https://www.youtube.com/watch?v=nJjbI4BbasU&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=43) |✔      |   |
| [Cognito JWT Server side Verify](https://youtu.be/d079jccoG-M)| ✔   |   |
| [Improving UI Contrast and Implementing CSS Variables for Theming](https://youtu.be/m9V4SmJWoJU)| ✔   |  |

<hr/>

|    | Table of contents - Steps taken to complete Week 3 assignments                                                                                                                                                                         |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [Configuring and Installing AWS amplify](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#aws-amplify-install-in-env-vars)                                |
| 2  | [Importing AWS Amplify](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#aws-amplify-import-configuration)                                                |
| 3  | [Port startup configuration](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#updating-port-startup-public)                                               |
| 4  | [Cognito Backend fixes](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#updating-the-backend-aws-cognito-environment)                                    |
| 5  | [Submit Button fix](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#configuring-login-button-behaviour)                                                  |
| 6  | [Log in invalid user test](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#testing-the-log-in-button-behaviour-for-a-response)                           |
| 7  | [Test User creation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#cognito---setup-test-user-via-console)                                              |
| 8  | [Sign in options](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#cognito---review-test-user-configuration-via-console)                                  |
| 9  | [Temporary password email sent](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#cognito---username-and-password-sent-to-email)                                                     |
| 10 | [Required attributes](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#cognito---setting-preferred-username-via-console)                                  |
| 11 | [Configure message delivery](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#user-confirmation-email)                                                    |
| 12 | [Userpool name](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#confirmed-users-account-status-changes-to-confirmed)                                     |
| 13 | [Advanced app client settings](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#userpool-creation)                                                        |
| 14 | [User attributes](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#cognito---user-attributes)                                                             |
| 15 | [Final User pool](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#cognito-user-pool-created)                                                             |
| 16 | [Force email confirmation in terminal](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#cognito---confirming-email-via-terminal)                          |
| 17 | [Users account status changes to confirmed after responding to email](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#email-status-changed-to-confirmed) |
| 18 | [Userpool creation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#cognito-user-pool-dashboard)                                                         |
| 19 | [Cognito client ID](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#cognito-client-id)                                                                   |
| 20 | [Backend Cognito setup](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#backend-cognito-setup)                                                           |
| 21 | [Working Cruddur App - User signed in](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week3.md#signed-in-user---working-cruddur-app-login)                                             |
                                                                                                                                       



## AWS Amplify install in env vars

![Configuring and Installing AWS amplify](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/Install%20aws%20amplify.JPG)


## AWS Amplify import configuration     

![Importing AWS Amplify](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/aws%20amplify%20import.JPG)


## Updating Port startup (Public)

![Port startup configuration](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/Update%20to%20gitpod%20yaml%20public%20ports.JPG)


## Updating the Backend AWS Cognito environment

![Cognito Backend fixes](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/Cognito%20backend%20fixes.JPG)


## Configuring Login button behaviour

![Submit Button fix](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/editing%20on%20submit.JPG)


## Testing the Log in button behaviour for a response

![Log in invalid user test](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/Incorrect%20username%20or%20password.JPG)


## Cognito - setup test-user via console
![Test User creation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/test%20user.JPG)

## Cognito - review test-user configuration via console
![Sign in options](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/cognito%201.JPG)
![MFA](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/cognito%202.JPG)
![Required attributes](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/cognito%204.JPG)
![Configure message delivery](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/cognito%205.JPG)
![Userpool name](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/cognito%206.JPG)
![Advanced app client settings](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/cognito%207.JPG)


## Cognito - username and password sent to email
![Test User creation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/cognito%20email%20password.JPG)

## Cognito - setting preferred username via console

![Preferred username config so as to work with the backend](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/setting%20preferred%20username.JPG)


## User confirmation email

![Confirm creation of user via email response](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/test%20user%20email%20setting%20temp%20password.JPG)


## Confirmed users account status changes to confirmed

![Users account status changes to confirmed after responding to email](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/Status%20change%20pending%20to%20confirmed.JPG)

## Userpool creation

![Userpool creation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/userpool%20creation.JPG)


## Cognito - user attributes

![User attributes](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/user%20attributes.JPG)


## Cognito User pool created

![Final User pool](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/userpool.JPG)


## Cognito - confirming email via terminal

![Force email confirmation in terminal](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/confirming%20email%20via%20terminal.JPG)

## Email status changed to confirmed

![Email status chnaged](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/Userpool%20review.jpg)


## Cognito user pool dashboard

![User pool dashboard](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/Cognito%20user%20pool.JPG)


## Cognito client ID

![Client ID](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/Cognito%20client%20ID.JPG)


## Backend Cognito setup

![Cognito setup - backend env](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/Backend%20cognito%20setup.JPG)


## Signed in user - Working Cruddur App Login

![User signed in](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/Working%20app%20showing%20logged%20in%20user.JPG)


## AWS Cognito
In this live session, we first created a UserPool in AWS Cognito.

**Steps to setup UserPool in AWS Cognito**
- Login to your AWS Console
- Check your region in which you want to use your service. I personally prefer `us-east-1` region as in that region most of the services work well.
- Search for **Cognito** service and you will find **UserPool** tab in your left side panel.
- After clicking on **UserPool** -> **Create UserPool**.
- You will be see the **Authentication providers** page where you should choose **Username** and **Email** for Cognito user pool sign-in options -> click **Next**
- Password Policy keep it as **Cognito Default**.
- Under Multi-factor authentication -> Select **No MFA** -> **Next**
- In User account recovery -> checkbox **Email only** -> **Next**
- Under Sign up experience > mark the checkbox **Enable self-registration**
- Check the checkbox marked **Allow Cognito to automatically send messages to verify and confirm**
- Under Required attributes -> Select **Name** and **preferred username** -> **Next**
- Then choose **Send email with Cognito** -> **Next**
- Give your User Pool Name , Set it as **crddur-user-pool** -> under Initial app type keep it as **Public client** -> enter app client name as **cruddur** -> **Next**
- Leave **Do not generate a client secret** checked. 
- On the 'Review and Create page' you will then get a chance to verify all the filled in details > To proceeed click on **Create User Pool**.
- Once created, note the 'User pool ID' and 'Client ID' for use later.
- 'Client ID' can be found under the 'App Integration' tab.

## AWS Amplify 
Refer to the docs at: [AWS Amplify](https://docs.amplify.aws)
Install AWS Amplify as it is a development platform and provides you a set of pre-built UI components and Libraries. 
```
cd frontend-react-js 
npm install aws-amplify@5.0.17
```

After installing this you will find the library `"aws-amplify": "<version>",` in the frontend-react-js directory's `package.json` file. <br />
We are specifying Version: 5.0.17 because newer versions do not work with this code.
<br />

**Tip** <br />
If you prefer to specify the version in a file create `frontend-react-js` > `requirements.txt` and in it place all your frontend dependencies including: <br/>
```sh
# aws-amplify==5.0 # Base version
# aws-amplify==5.0.17 # original version
aws-amplify==5.0.17-unstable-v5.7 # original version renamed to this
```
I have included all possible versions that work with our app but note that version: `5.0.17` at the time of writing this is deprecated but can still be accessed as `5.0.17-unstable-v5.7`. <br/>
<br />

**Note: make sure you are running these commands in your `frontend-react-js` directory.**

### Configure Amplify
Add the code below in `frontend-react-js/src/app.js`:

```js
import { Amplify } from 'aws-amplify';

Amplify.configure({
  "AWS_PROJECT_REGION": process.env.REACT_APP_AWS_PROJECT_REGION,
  "aws_cognito_region": process.env.REACT_APP_AWS_COGNITO_REGION,
  "aws_user_pools_id": process.env.REACT_APP_AWS_USER_POOLS_ID,
  "aws_user_pools_web_client_id": process.env.REACT_APP_CLIENT_ID,
  "oauth": {},
  Auth: {
    // We are not using an Identity Pool
    // identityPoolId: process.env.REACT_APP_IDENTITY_POOL_ID, // REQUIRED - Amazon Cognito Identity Pool ID
    region: process.env.REACT_APP_AWS_PROJECT_REGION,           // REQUIRED - Amazon Cognito Region
    userPoolId: process.env.REACT_APP_AWS_USER_POOLS_ID,         // OPTIONAL - Amazon Cognito User Pool ID
    userPoolWebClientId: process.env.REACT_APP_CLIENT_ID,   // OPTIONAL - Amazon Cognito Web Client ID (26-char alphanumeric string)
  }
});
```

Edit and set the env vars below in docker-compose.yml > `frontend-react-js` > `environment`:
```py
      REACT_APP_AWS_PROJECT_REGION: "${AWS_DEFAULT_REGION}"
      REACT_APP_AWS_COGNITO_REGION: "${AWS_DEFAULT_REGION}"
      REACT_APP_AWS_USER_POOLS_ID: "ca-central-1_CQ4wDfnwc"
      REACT_APP_CLIENT_ID: "5b6ro31g97urk767adrbrdj1g5"
```

### **Authentication Process** - Conditionally show components based on 'logged in' or 'logged out'.
In `frontend-react-js` > `src` > `pages` > `HomeFeedPage.js`.
< br/>
Add the import:
```js
import { Auth } from 'aws-amplify';
```

delete the code with the cookies (previously used to simulate authentication):
(hint: around line 40-49)
```js
  const checkAuth = async () => {
    console.log('checkAuth')
    // [TODO] Authenication
    if (Cookies.get('user.logged_in')) {
        display_name: Cookies.get('user.name'),
        handle: Cookies.get('user.username')
    }
  };
```
Input the following to implement Cognito Authorization:
```js
// check if we are authenicated
const checkAuth = async () => {
  Auth.currentAuthenticatedUser({
    // Optional, By default is false. 
    // If set to true, this call will send a 
    // request to Cognito to get the latest user data
    bypassCache: false 
  })
  .then((user) => {
    console.log('user',user);
    return Auth.currentAuthenticatedUser()
  }).then((cognito_user) => {
      setUser({
        display_name: cognito_user.attributes.name,
        handle: cognito_user.attributes.preferred_username
      })
  })
  .catch((err) => console.log(err));
};

// check if we are authenicated when the page loads
React.useEffect(()=>{
  //prevents double call
  if (dataFetchedRef.current) return;
  dataFetchedRef.current = true;

  loadData();
  checkAuth();
}, [])
```

Add a header to pass along the access token:
```py
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`
        },
```

The full 'HomeFeedPage.js' should now read:
```py
import './HomeFeedPage.css';
import React from "react";

import { Auth } from 'aws-amplify';

import DesktopNavigation  from '../components/DesktopNavigation';
import DesktopSidebar     from '../components/DesktopSidebar';
import ActivityFeed from '../components/ActivityFeed';
import ActivityForm from '../components/ActivityForm';
import ReplyForm from '../components/ReplyForm';

// [TODO] Authenication
import Cookies from 'js-cookie'

export default function HomeFeedPage() {
  const [activities, setActivities] = React.useState([]);
  const [popped, setPopped] = React.useState(false);
  const [poppedReply, setPoppedReply] = React.useState(false);
  const [replyActivity, setReplyActivity] = React.useState({});
  const [user, setUser] = React.useState(null);
  const dataFetchedRef = React.useRef(false);

  const loadData = async () => {
    try {
      const backend_url = `${process.env.REACT_APP_BACKEND_URL}/api/activities/home`
      const res = await fetch(backend_url, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`
        },
        method: "GET"
      });
      let resJson = await res.json();
      if (res.status === 200) {
        setActivities(resJson)
      } else {
        console.log(res)
      }
    } catch (err) {
      console.log(err);
    }
  };

  const checkAuth = async () => {
    Auth.currentAuthenticatedUser({
      // Optional, By default is false. 
      // If set to true, this call will send a 
      // request to Cognito to get the latest user data
      bypassCache: false 
    })
    .then((user) => {
      console.log('user',user);
      return Auth.currentAuthenticatedUser()
    }).then((cognito_user) => {
        setUser({
          display_name: cognito_user.attributes.name,
          handle: cognito_user.attributes.preferred_username
        })
    })
    .catch((err) => console.log(err));
  };
  
  React.useEffect(()=>{
    //prevents double call
    if (dataFetchedRef.current) return;
    dataFetchedRef.current = true;

    loadData();
    checkAuth();
  }, [])

  return (
    <article>
      <DesktopNavigation user={user} active={'home'} setPopped={setPopped} />
      <div className='content'>
        <ActivityForm  
          popped={popped}
          setPopped={setPopped} 
          setActivities={setActivities} 
        />
        <ReplyForm 
          activity={replyActivity} 
          popped={poppedReply} 
          setPopped={setPoppedReply} 
          setActivities={setActivities} 
          activities={activities} 
        />
        <ActivityFeed 
          title="Home" 
          setReplyActivity={setReplyActivity} 
          setPopped={setPoppedReply} 
          activities={activities} 
        />
      </div>
      <DesktopSidebar user={user} />
    </article>
  );
}
```
In the app.py after `origins = [frontend, backend]` around line 82 we need to update CORS:
```py
cors = CORS(
  app, 
  resources={r"/api/*": {"origins": origins}},
  headers=['Content-Type', 'Authorization'], 
  expose_headers='Authorization',
  methods="OPTIONS,GET,HEAD,POST"
)
```

At around line 157 lets enable logging so that we can get debugging info, change the `data_home` function to read:
```py
@app.route("/api/activities/home", methods=['GET'])
@xray_recorder.capture('activities_home')
def data_home():
  data = HomeActivities.run()
  return data, 200
```
Once your able to see the logs revert the code to:
```py
@xray_recorder.capture('activities_home')
def data_home():
  data = HomeActivities.run()
  return data, 200
```
We should pass the headers to the backend. File: `backend-flask` > `app.py`:
Add 'import sys'

Create the following: `backend-flask/lib/cognito_jwt_token.py` and place the code below in the file:
```py
import time
import requests
from jose import jwk, jwt
from jose.exceptions import JOSEError
from jose.utils import base64url_decode

class FlaskAWSCognitoError(Exception):
  pass

class TokenVerifyError(Exception):
  pass

def extract_access_token(request_headers):
    access_token = None
    auth_header = request_headers.get("Authorization")
    if auth_header and " " in auth_header:
        _, access_token = auth_header.split()
    return access_token

class CognitoJwtToken:
    def __init__(self, user_pool_id, user_pool_client_id, region, request_client=None):
        self.region = region
        if not self.region:
            raise FlaskAWSCognitoError("No AWS region provided")
        self.user_pool_id = user_pool_id
        self.user_pool_client_id = user_pool_client_id
        self.claims = None
        if not request_client:
            self.request_client = requests.get
        else:
            self.request_client = request_client
        self._load_jwk_keys()


    def _load_jwk_keys(self):
        keys_url = f"https://cognito-idp.{self.region}.amazonaws.com/{self.user_pool_id}/.well-known/jwks.json"
        try:
            response = self.request_client(keys_url)
            self.jwk_keys = response.json()["keys"]
        except requests.exceptions.RequestException as e:
            raise FlaskAWSCognitoError(str(e)) from e

    @staticmethod
    def _extract_headers(token):
        try:
            headers = jwt.get_unverified_headers(token)
            return headers
        except JOSEError as e:
            raise TokenVerifyError(str(e)) from e

    def _find_pkey(self, headers):
        kid = headers["kid"]
        # search for the kid in the downloaded public keys
        key_index = -1
        for i in range(len(self.jwk_keys)):
            if kid == self.jwk_keys[i]["kid"]:
                key_index = i
                break
        if key_index == -1:
            raise TokenVerifyError("Public key not found in jwks.json")
        return self.jwk_keys[key_index]

    @staticmethod
    def _verify_signature(token, pkey_data):
        try:
            # construct the public key
            public_key = jwk.construct(pkey_data)
        except JOSEError as e:
            raise TokenVerifyError(str(e)) from e
        # get the last two sections of the token,
        # message and signature (encoded in base64)
        message, encoded_signature = str(token).rsplit(".", 1)
        # decode the signature
        decoded_signature = base64url_decode(encoded_signature.encode("utf-8"))
        # verify the signature
        if not public_key.verify(message.encode("utf8"), decoded_signature):
            raise TokenVerifyError("Signature verification failed")

    @staticmethod
    def _extract_claims(token):
        try:
            claims = jwt.get_unverified_claims(token)
            return claims
        except JOSEError as e:
            raise TokenVerifyError(str(e)) from e

    @staticmethod
    def _check_expiration(claims, current_time):
        if not current_time:
            current_time = time.time()
        if current_time > claims["exp"]:
            raise TokenVerifyError("Token is expired")  # probably another exception

    def _check_audience(self, claims):
        # and the Audience  (use claims['client_id'] if verifying an access token)
        audience = claims["aud"] if "aud" in claims else claims["client_id"]
        if audience != self.user_pool_client_id:
            raise TokenVerifyError("Token was not issued for this audience")

    def verify(self, token, current_time=None):
        """ https://github.com/awslabs/aws-support-tools/blob/master/Cognito/decode-verify-jwt/decode-verify-jwt.py """
        if not token:
            raise TokenVerifyError("No token provided")

        headers = self._extract_headers(token)
        pkey_data = self._find_pkey(headers)
        self._verify_signature(token, pkey_data)

        claims = self._extract_claims(token)
        self._check_expiration(claims, current_time)
        self._check_audience(claims)

        self.claims = claims 
        return claims
```
Add the `Flask-AWSCognito` dependency to `backend-flask/requirements.txt`
Install the dependencies by running the code below from within `backend-flask`:
`pip install -r requirements.txt` <br />

At this point requirements.txt contains:
```txt
flask
flask-cors

opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests

aws-xray-sdk

watchtower

blinker
rollbar

Flask-AWSCognito
```
In our docker-compose.yml file, add the following as environment variables of backend-flask:
```txt
      REACT_APP_AWS_USER_POOLS_ID: "<user-pool-ID eg us-east-1_XXX>"
      REACT_APP_CLIENT_ID: "<Insert your client ID>" 
```
In 'app.py' add the import 'from lib.cognito_jwt_token import CognitoJwtToken, extract_access_token, TokenVerifyError' 

### Refactor 'DesktopSidebar.js': path: 'frontend-react-js/src/components/DesktopSidebar.js'
```py
import './DesktopSidebar.css';
import Search from '../components/Search';
import TrendingSection from '../components/TrendingsSection'
import SuggestedUsersSection from '../components/SuggestedUsersSection'
import JoinSection from '../components/JoinSection'

export default function DesktopSidebar(props) {
  const trendings = [
    {"hashtag": "100DaysOfCloud", "count": 2053 },
    {"hashtag": "CloudProject", "count": 8253 },
    {"hashtag": "AWS", "count": 9053 },
    {"hashtag": "FreeWillyReboot", "count": 7753 }
  ]

  const users = [
    {"display_name": "Andrew Brown", "handle": "andrewbrown"}
  ]

  let trending;
  let suggested;
  let join;
  if (props.user) {
    trending = <TrendingSection trendings={trendings} />
    suggested = <SuggestedUsersSection users={users} />
  } else {
    join = <JoinSection />
  }

  return (
    <section>
      <Search />
      {trending}
      {suggested}
      {join}
      <footer>
        <a href="#">About</a>
        <a href="#">Terms of Service</a>
        <a href="#">Privacy Policy</a>
      </footer>
    </section>
  );
}
```

### Refactor `ProfileInfo.js`

This code defines a function called `signOut` that uses the `Auth` object from the `aws-amplify` library to sign out the currently authenticated user from an AWS Amplify application.
delete the following code:
```js
import Cookies from 'js-cookie'
```
Add the code below:
```js
import { Auth } from 'aws-amplify';
```
remove the following code
```js
    console.log('signOut')
    // [TODO] Authenication
    Cookies.remove('user.logged_in')
    //Cookies.remove('user.name')
    //Cookies.remove('user.username')
    //Cookies.remove('user.email')
    //Cookies.remove('user.password')
    //Cookies.remove('user.confirmation_code')
    window.location.href = "/"
```
Add the code below:
```js
const signOut = async () => {
  try {
      await Auth.signOut({ global: true });
      window.location.href = "/"
  } catch (error) {
      console.log('error signing out: ', error);
  }
}
```

The full `ProfileInfo.js` page > `frontend-react-js/src/components/ProfileInfo.js` should now contain:
 
```py
import './ProfileInfo.css';
import {ReactComponent as ElipsesIcon} from './svg/elipses.svg';
import React from "react";

// [TODO] Authenication
import { Auth } from 'aws-amplify';

export default function ProfileInfo(props) {
  const [popped, setPopped] = React.useState(false);

  const click_pop = (event) => {
    setPopped(!popped)
  }

  const signOut = async () => {
    try {
        await Auth.signOut({ global: true });
        window.location.href = "/"
        #localStorage.removeItem("access_token")
    } catch (error) {
        console.log('error signing out: ', error);
    }
  }

  const classes = () => {
    let classes = ["profile-info-wrapper"];
    if (popped == true){
      classes.push('popped');
    }
    return classes.join(' ');
  }

  return (
    <div className={classes()}>
      <div className="profile-dialog">
        <button onClick={signOut}>Sign Out</button> 
      </div>
      <div className="profile-info" onClick={click_pop}>
        <div className="profile-avatar"></div>
        <div className="profile-desc">
          <div className="profile-display-name">{props.user.display_name || "My Name" }</div>
          <div className="profile-username">@{props.user.handle || "handle"}</div>
        </div>
        <ElipsesIcon className='icon' />
      </div>
    </div>
  )
}
```
Overall, this code provides a simple and straightforward way to sign out a user from an AWS Amplify application by using the `Auth` object from the `aws-amplify` library.

## Sign-in Page, Sign-out Page and Confirmation Page
### Implementation of the sign in page. 
From the **SigninPage.js** located at: 'frontend-react-js/src/pages/SigninPage.js', remove the following code
```
import Cookies from 'js-cookie'

```

and replace with the following
```
import { Auth } from 'aws-amplify';
```

remove the following code 
```
  const onsubmit = async (event) => {
    event.preventDefault();
    setErrors('')
    console.log('onsubmit')
    if (Cookies.get('user.email') === email && Cookies.get('user.password') === password){
      Cookies.set('user.logged_in', true)
      window.location.href = "/"
    } else {
      setErrors("Email and password is incorrect or account doesn't exist")
    }
    return false
  }
```
and replace it with the new one
```
const onsubmit = async (event) => {
    setErrors('')
    event.preventDefault();
    Auth.signIn(email, password)
    .then(user => {
      console.log('user',user)
      localStorage.setItem("access_token", user.signInUserSession.accessToken.jwtToken)
      window.location.href = "/"
    })
    .catch(error => {
      if (error.code == 'UserNotConfirmedException') {
        window.location.href = "/confirm"
      }
      setErrors(error.message)
      });
    return false
  }
```

The full `SigninPage.js` should now be similar to:
```py
import './SigninPage.css';
import React from "react";
import {ReactComponent as Logo} from '../components/svg/logo.svg';
import { Link } from "react-router-dom";

// [TODO] Authenication
import { Auth } from 'aws-amplify';

export default function SigninPage() {

  const [email, setEmail] = React.useState('');
  const [password, setPassword] = React.useState('');
  const [errors, setErrors] = React.useState('');

  const onsubmit = async (event) => {
    setErrors('')
    event.preventDefault();
    Auth.signIn(email, password)
    .then(user => {
      console.log('user',user)
      localStorage.setItem("access_token", user.signInUserSession.accessToken.jwtToken)
      window.location.href = "/"
    })
    .catch(error => { 
      if (error.code == 'UserNotConfirmedException') {
        window.location.href = "/confirm"
      }
      setErrors(error.message)
    });
    return false
  }

  const email_onchange = (event) => {
    setEmail(event.target.value);
  }
  const password_onchange = (event) => {
    setPassword(event.target.value);
  }

  let el_errors;
  if (errors){
    el_errors = <div className='errors'>{errors}</div>;
  }

  return (
    <article className="signin-article">
      <div className='signin-info'>
        <Logo className='logo' />
      </div>
      <div className='signin-wrapper'>
        <form 
          className='signin_form'
          onSubmit={onsubmit}
        >
          <h2>Sign into your Cruddur account</h2>
          <div className='fields'>
            <div className='field text_field username'>
              <label>Email</label>
              <input
                type="text"
                value={email}
                onChange={email_onchange} 
              />
            </div>
            <div className='field text_field password'>
              <label>Password</label>
              <input
                type="password"
                value={password}
                onChange={password_onchange} 
              />
            </div>
          </div>
          {el_errors}
          <div className='submit'>
            <Link to="/forgot" className="forgot-link">Forgot Password?</Link>
            <button type='submit'>Sign In</button>
          </div>

        </form>
        <div className="dont-have-an-account">
          <span>
            Don't have an account?
          </span>
          <Link to="/signup">Sign up!</Link>
        </div>
      </div>

    </article>
  );
}
```

To try, just launch the container up on **"docker-compose.yml"**  and see if the login page works. to troubleshoot open "developer tools" or use inspect (browser) if you receive "NotAuthorizedException: Incorrect user or password".This means everything is set properly. if you got an error "auth not defined", the problem is the cognito user pool configuration. needs to be recreated.

#### Manually Create a user
We could create a user manually in the cognito user pool (**NB** there is no way to change on password via console).
<br />
On AWS Cognito, select add user.
Select Email.
Dont send an invitation.
Username: 'andrewbrown'.
Email: '<use-your-preferred-email-address>'
Password: 'Testing123!'
You will be required to access the email to confirm registration.
<br />

If your do not receive an email, we can create the user in the CLI:
```sh
aws cognito-idp admin-set-user-password \
  --user-pool-id <your-user-pool-id> \
  --username <username> \
  --password <password> \
  --permanent
```


### Implementation the sign-up page
Since you have managed to access using the credential created via console, it is time to delete it as it is not needed anymore.

From the **signuppage.js** remove the following code
```
import Cookies from 'js-cookie'

```

and replace with the following
```
import { Auth } from 'aws-amplify';
```

delete the following command
```
  const onsubmit = async (event) => {
    event.preventDefault();
    console.log('SignupPage.onsubmit')
    // [TODO] Authenication
    Cookies.set('user.name', name)
    Cookies.set('user.username', username)
    Cookies.set('user.email', email)
    Cookies.set('user.password', password)
    Cookies.set('user.confirmation_code',1234)
    window.location.href = `/confirm?email=${email}`
    return false
  }
```

and add the new code
```
const onsubmit = async (event) => {
    event.preventDefault();
    setErrors('')
    try {
      const { user } = await Auth.signUp({
        username: email,
        password: password,
        attributes: {
          name: name,
          email: email,
          preferred_username: username,
        },
        autoSignIn: { // optional - enables auto sign in after user is confirmed
          enabled: true,
        }
      }) ;
      console.log(user);
      window.location.href = `/confirm?email=${email}`
    } catch (error) {
        console.log(error);
        setErrors(error.message)
    }
    return false
  }
```

### Implementation of the confirmation page
from the confirmationpage.js, remove the following code:

 ```
import Cookies from 'js-cookie'

```

and replace with the following:
```
import { Auth } from 'aws-amplify';
```

and remove the following code:
```
  const resend_code = async (event) => {
    console.log('resend_code')
    // [TODO] Authenication
  }
```
and replace with the following:
``` 
const resend_code = async (event) => {
 
    setErrors('')
    try {
      await Auth.resendSignUp(email);
      console.log('code resent successfully');
      setCodeSent(true)
    } catch (err) {
      // does not return a code
      // does cognito always return english
      // for this to be an okay match?
      console.log(err)
      if (err.message == 'Username cannot be empty'){
        setErrors("You need to provide an email in order to send Resend Activiation Code")   
      } else if (err.message == "Username/client id combination not found."){
        setErrors("Email is invalid or cannot be found.")   
      }
    }
  }

```

and remove the following code:
```
 const onsubmit = async (event) => {
    event.preventDefault();
    console.log('ConfirmationPage.onsubmit')
    // [TODO] Authenication
    if (Cookies.get('user.email') === undefined || Cookies.get('user.email') === '' || Cookies.get('user.email') === null){
      setErrors("You need to provide an email in order to send Resend Activiation Code")   
    } else {
      if (Cookies.get('user.email') === email){
        if (Cookies.get('user.confirmation_code') === code){
          Cookies.set('user.logged_in',true)
          window.location.href = "/"
        } else {
          setErrors("Code is not valid")
        }
      } else {
        setErrors("Email is invalid or cannot be found.")   
      }
    }
    return false
  }
```

and replace with the cognito code:
```
const onsubmit = async (event) => {
  event.preventDefault();
  setErrors('')
  try {
    await Auth.confirmSignUp(email, code);
    window.location.href = "/"
  } catch (error) {
    setErrors(error.message)
  }
  return false
}
```

### Implementation of the recovery page
from the recoverpage.js, add the following code

 ```
import { Auth } from 'aws-amplify';
```

remove the following code
```
  const onsubmit_send_code = async (event) => {
    event.preventDefault();
    console.log('onsubmit_send_code')
    return false
  }
```

and add the these lines
```
const onsubmit_send_code = async (event) => {
    event.preventDefault();
    setErrors('')
    Auth.forgotPassword(username)
    .then((data) => setFormState('confirm_code') )
    .catch((err) => setErrors(err.message) );
    return false
  }
```

remove the following code:
```
  const onsubmit_confirm_code = async (event) => {
    event.preventDefault();
    console.log('onsubmit_confirm_code')
    return false
  }
```

with the following new code:
```
const onsubmit_confirm_code = async (event) => {
  event.preventDefault();
  setErrors('')
  if (password == passwordAgain){
    Auth.forgotPasswordSubmit(username, code, password)
    .then((data) => setFormState('success'))
    .catch((err) => setErrors(err.message) );
  } else {
    setErrors('Passwords do not match')
  }
  return false
}
```
#### Retrive submitted values across different pages in React.js

In our application, there are 2 user experience problems:
- During the confirmation, user needs to write the email manually. this could cause possible human error.
- After the registration, user gets redirected to the home page but not signed in yet. this could create confusion and user can create a new account accidentally.

The solution is to store the value using localstorage (many thanks to Abdassalam Hashnode) and use this across other pages.

The changes will be between the signuppage.js, confirmationpage.js and signinpage.js


From the `signup page`, add the following code this will store the email to the local storage
```
// SignupPage.js
const onsubmit = async (event) => {
// ...
    try {
// ...
// Store email in local storage to use it in confirmation & sign-in page
        localStorage.setItem('email', email);
// redirect user to confirmation page after signing up
        window.location.href = `/confirm`
    } 
// ...

```

from the `confirmation page`, add the following code. this checks if the local storage contains email

```
// ConfirmationPage.js
// ...
// Get email from the signup page where we stored the email in localStorage
React.useEffect(() => {
  const storedEmail = localStorage.getItem('email');
// check if the email is set, if it's not set then we will ignore it, and use the value typed in the email box:
  if (storedEmail) {
// Filling the Email
    setEmail(storedEmail);
  }
}, []);

const onsubmit = async (event) => {
// ...
```

for the `signup page`, add the following code. this gets the email from the local storage to the `confirmation page`:
```
// SigninPage.js
// Get email from the signup page where we stored the email in localStorage
React.useEffect(() => {
  const storedEmail = localStorage.getItem('email');
  if (storedEmail) {
    setEmail(storedEmail);
// Remove the email from local storage because we're done with it.
    localStorage.removeItem('email'); 
  }
}, []);
```

To redirect the `home page` already logged in, insert the following code
```
// ConfirmationPage.js
const onsubmit = async (event) => {
// ...
  try {
    await Auth.confirmSignUp(email, code);
// Redirect user to sign-in page instead of home page.
    window.location.href = "/signin"
// ...
}
```

# Troubleshooting

  #### Force password change for your cognito registered user: 

 ```python
  aws cognito-idp admin-set-user-password --username nameofusername --password Testing1234! --user-pool-id "${AWS_USER_POOLS_ID}" --permanent
```

**Improving UI Contrast and Implementing CSS Variables for Theming**
Change the background color:
'frontend-react-js' > 'src' > 'index.css'
```
html,body { 
  height: 100%; 
  width: 100%; 
  background: rgb(61,13,123);
}
```
Change the line color between posts:
'frontend-react-js' > 'src' > 'components' > 'ActivityItem.css'
```
.activity_item {
  display: flex;
  flex-direction: column;
  border-bottom: solid 1px rgb(247,230,255);
  # border-bottom: solid 1px rgb(60,54,79);
  overflow: hidden;
  padding: 16px;
}
```

Change the hover color:
'frontend-react-js' > 'src' > 'components' > 'DesktopSidebar.css'
```
section footer a {
  text-decoration: none;
  color: rgba(255,255,255,0.5);
  font-size: 14px;
}
```
**Setting variables**
File: 'frontend-react-js' > 'src' > 'index.css'
Declare variables at the top of the file:
```
:root {
  --bg: rgb(61,13,123);
  --fg: rgb(8,1,14);

  --field-border: rgb(255,255,255,0.29);
  --field-border-focus: rgb(149,0,255,1);
  --field-bg: rgb(31,31,31);
}
```

Reference the color as shown:
```
html,body { 
  height: 100%; 
  width: 100%; 
  background: var(--bg);
}
```
File: `frontend-react-js` > `src` > `components` > `JoinSection.css`
```
.join {
  display: flex;
  flex-direction: column;
  background: var(--fg);
  border-radius: 8px;
  margin-top: 24px;
}
```
File: `frontend-react-js` > `src` > `App.css`
```
.content {
  width: 600px;
  height: 100%;
  background: var(--fg);
}
```
File: `frontend-react-js` > `src` > `components` > `Search.css`
```
.search_field input[type='text'] {
  border: solid 1px var(--field-border);
  background: var(--field-bg);
  padding: 16px;
  font-size: 16px;
  border-radius: 8px;
  width: 100%;
  outline: none;
  color: #fff;
}
.search_field input[type='text']:focus {
  border: solid 1px var(--field-border-focus)
}
```

File: `frontend-react-js` > `src` > `pages` > `SignupPage.css`
```
article.signup-article input[type='password'] {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
  border-radius: 4px;
  border: none;
  outline: none;
  display: block;
  outline: none;
  resize: none;
  width: 100%;
  padding: 16px;
  border: solid 1px var(--field-border);
  background: #1f1f1f;
  color: #fff;
}
```
and

```
article.signup-article input[type='password']:focus {
  border: solid 1px var(--field-border-focus);
}
```

File: `frontend-react-js` > `src` > `pages` > `SigninPage.css`
```
article.signin-article input[type='password'] {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
  border-radius: 4px;
  border: none;
  outline: none;
  display: block;
  outline: none;
  resize: none;
  width: 100%;
  padding: 16px;
  border: solid 1px var(--field-border);
  background: var(--field-bg);
  color: #fff;
}
```
and
```
article.signin-article input[type='password']:focus {
  border: solid 1px var(--field-border-focus);
}
```
## Updates
I ran a snyk test and realized that my docker compose version was outdated <br />
and vulnerable to attacks. An update was urgently needed:
```sh
gitpod /workspace/Cruddur-social (week-3) $ docker compose version 
Docker Compose version v2.27.0-gitpod.0
gitpod /workspace/Cruddur-social (week-3) $ sudo rm /usr/local/bin/docker-compose
gitpod /workspace/Cruddur-social (week-3) $ sudo curl -L "https://github.com/docker/compose/releases/download/v2.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 56.8M  100 56.8M    0     0  49.7M      0  0:00:01  0:00:01 --:--:-- 49.7M
gitpod /workspace/Cruddur-social (week-3) $ sudo chmod +x /usr/local/bin/docker-compose
gitpod /workspace/Cruddur-social (week-3) $ docker-compose --version
Docker Compose version v2.22.0
```


## Save the work on its own branch named "week-3"
```sh
cd aws-bootcamp-cruddur-2024
git checkout -b week-3
```
<hr/>

## Commit
Add the changes and create a commit named: "Decentralized Authentication"
```sh
git add .
git commit -m "Decentralized Authentication"
```
Push your changes to the branch
```sh
git push origin week-3
```
<hr/>

### Tag the commit
```sh
git tag -a week-3-tag -m "Setting up Decentralized Authentication"
```
<hr/>

### Push your tags
```sh
git push --tags
```
<hr/>

### Switching Between Branches back to Main
```sh
git checkout main
```
<hr/>

### Merge Changes
```sh
git merge week-3
```
<hr/>

### Push Changes to Main
```sh
git push origin main
```
<hr/>

#### Branches?
If you want to keep the "week-1" branch for future reference or additional work, 
you can keep it as is. If you no longer need the branch, you can delete it after merging.
```sh
git branch -d week-3  # Deletes the local branch
git push origin --delete week-3  # Deletes the remote branch
