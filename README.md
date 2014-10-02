django-canvas-oauth
===================

A django app to make acquiring a canvas oauth token easy

## Installation

In your Django project settings, add the following to `MIDDLEWARE_CLASSES`,
```
    'django_auth_lti.middleware.LTIAuthMiddleware',
    'django_canvas_oauth.middleware.OAuthMiddleware'
```

add the following to `INSTALLED_APPS`,
```
    'django_canvas_oauth',
```

add the following to your root url conf,
```
    url(r'^oauth/', include("django_canvas_oauth.urls", namespace="django_canvas_oauth")),
```

Generate a client ID and secret in the Site Admin account of your Canvas install.
There will be a "Developer Keys" tab on the left navigation sidebar.
and define the following two settings:
```
CANVAS_OAUTH_CLIENT_ID = "TODO: canvas client id"
CANVAS_OAUTH_CLIENT_SECRET = "TODO: canvas client secret"
```

## Use

```
from django_canvas_oauth import get_token

def django_view(request):
    token = get_token(request)
    # This token can then be used to make Django SDK calls
```

If there ins't a token for the current user, the middleware automatically begins
the oauth dance with canvas to get one.  Once a token is acquired, it is stored
so that a user doesn't need to reauthenticate.

## Caveats and room for improvement

* The burden is on the application that uses the token to deal with tokens
that are no longer valid.  If an invalid token is encountered in a Django view,
simply raise a `NewTokenNeeded` exception
(`from django_canvas_oauth import NewTokenNeeded`) and the middleware will catch
this and begin an oauth dance to get a new token

* This library is primarily designed for use in view functions, since in the
event that a token is missing or invalid, the user needs to go through several
steps in-browser to aquire a new token.  That said, the function
`get_token_backend` is exposed to allow retrieval and use of tokens by the data
pair `(admin_id, course_id)`.  In the event you are using a token retrieved this
way in a backend function and you get a NewTokenNeeded error, or the token
returned is invalid, there isn't much you can do at the moment.