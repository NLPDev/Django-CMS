# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from aldryn_translation_tools.sitemaps import I18NSitemap

from ..models import Dashboard


class Dashboards_appSitemap(I18NSitemap):

    changefreq = "never"
    priority = 0.5

    def __init__(self, *args, **kwargs):
        self.namespace = kwargs.pop('namespace', None)
        super(Dashboards_appSitemap, self).__init__(*args, **kwargs)

    def items(self):
        qs = Dashboard.objects.published()
        if self.language is not None:
            qs = qs.translated(self.language)
        if self.namespace is not None:
            qs = qs.filter(app_config__namespace=self.namespace)
        return qs

    def lastmod(self, obj):
        return obj.publishing_date
