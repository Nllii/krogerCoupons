# krogerCoupons

# This is not ideal, you will have to provide your own tokens. Research on how to use.
- https://docs.authlib.org/en/v0.12.1/client/flask.html

Kroger uses Auth 2.0 for Bearer Tokens for the consumer or client side.
The way this is designed makes it a bit of a nuisance.


You will ned to provide this for the header. 

``` bash 
    'User-Agent': 'krogerco/55.0/iOS',
    'User-Time-Zone': 'America/Chicago',
    'X-Correlation-Id': '',
    'X-KROGER-TENANT': 'kroger',
    'X-KROGER-CHANNEL': 'MOBILE;IOS',
    'Accept-Language': 'en-US;q=1',
    'Authorization': '',
    'X-ApplicationAuthorizationToken':  '',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-LAF-OBJECT':'' ,

```