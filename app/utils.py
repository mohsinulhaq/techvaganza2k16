from app import app
from flask import make_response, url_for, redirect, request
from functools import wraps, update_wrapper
from datetime import datetime
from flask_assets import Bundle, Environment
from rauth import OAuth2Service

assets = Environment(app)

bundles = {
    'landing_css': Bundle(
        'css/index.css',
        'css/font-awesome.min.css',
        'css/comfortaa.css',
        'css/lato.css',
        filters='cssmin',
        output='gen/landing_styles.css'),

    'landing_js': Bundle(
        'js/jquery.min.js',
        'js/index.js',
        'js/skrollr.min.js',
        'js/skrollr.menu.min.js',
        filters='jsmin',
        output='gen/landing_scripts.js'),

    'css': Bundle(
        'css/bootstrap.min.css',
        'css/component.css',
        'css/animate.min.css',
        'css/ct-paper.css',
        'css/lato.css',
        'css/examples.css',
        'css/font-awesome.min.css',
        'css/montserrat.css',
        filters='cssmin',
        output='gen/styles.css'),

    'js': Bundle(
        'js/jquery.min.js',
        'js/index.js',
        'js/jquery-ui-1.10.4.custom.min.js',
        'js/bootstrap.min.js',
        'js/classie.js',
        'js/ct-paper.js',
        filters='jsmin',
        output='gen/scripts.js'),

}

assets.register(bundles)


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers[
            'Cache-Control'] = 'no-store, no-cache, must-revalidate,' \
                               ' post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)


class OAuthSignIn(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self):
        return url_for('authentication.oauth_callback',
                       provider=self.provider_name,
                       _external=True)

    @classmethod
    def get_provider(self, provider_name):
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.provider_name] = provider
        return self.providers[provider_name]


class FacebookSignIn(OAuthSignIn):
    def __init__(self):
        super(FacebookSignIn, self).__init__('facebook')
        self.service = OAuth2Service(
            name='facebook',
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url='https://graph.facebook.com/oauth/authorize',
            access_token_url='https://graph.facebook.com/oauth/access_token',
            base_url='https://graph.facebook.com/'
        )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='public_profile, email, user_education_history',
            response_type='code',
            redirect_uri=self.get_callback_url())
        )

    def callback(self):
        if 'code' not in request.args:
            return None, None, None
        oauth_session = self.service.get_auth_session(
            data={'code': request.args['code'],
                  'grant_type': 'authorization_code',
                  'redirect_uri': self.get_callback_url()}
        )
        me = oauth_session.get('me').json()
        return (
            'facebook$' + me['id'],
            me.get('email').split('@')[0],  # Facebook does not provide
            # username, so the email's user
            # is used instead
            me.get('email')
        )


class GoogleSignIn(OAuthSignIn):
    pass
