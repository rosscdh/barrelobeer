# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url

from rest_framework import routers

from beer.apps.monitor.api.views import (SiteViewset,
                                         UrlViewset,
                                         UrlLogViewset,
                                         FetchUrlView,
                                         DiffUrlView)

from beer.apps.monitor.views import (UrlLogScreenshotView,
                                     UrlLogScreenshotCompareView,)

from beer.apps.me.api.views import (MeView,
                                    ChangePasswordView,
                                    RegisterView,
                                    VerifyUserView,
                                    ForgotPasswordView)

router = routers.SimpleRouter(trailing_slash=False)

"""
Generic ViewSets
"""
router.register(r'sites', SiteViewset, base_name='monitor')
router.register(r'url', UrlViewset, base_name='url')
router.register(r'log', UrlLogViewset, base_name='log')


urlpatterns = patterns('',
                       # User
                       url(r'^auth/jwt/refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
                       # Register
                       url(r'^auth/register/$', RegisterView.as_view(), name='register'),
                       url(r'^auth/verify/$', VerifyUserView.as_view(), name='verify'),
                       url(r'^auth/forgot-password/$', ForgotPasswordView.as_view(), name='forgot_password'),
                       # Current user
                       url(r'^me/change-password', ChangePasswordView.as_view(), name='change-password'),
                       url(r'^me/$', MeView.as_view(), name='me'),

                       # Url
                       url(r'url/check', FetchUrlView.as_view(), name='url_check'),
                       url(r'url/(?P<a_pk>\d+)/(?P<b_pk>\d+)/diff', DiffUrlView.as_view(), name='url_diff'),
                       url(r'url/(?P<pk>\d+)/screenshot', UrlLogScreenshotView.as_view(), name='url_screenshot'),
                       url(r'url/(?P<pk>\d+)/(?P<pk_b>\d+)/compare', UrlLogScreenshotCompareView.as_view(), name='url_compare'),
                       ) + router.urls
