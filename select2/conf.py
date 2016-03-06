from appconf import AppConf
from django.conf import settings


class Select2Conf(AppConf):
    STATIC_URL = u'/static/'
    JQUERY_LIB = u"{0}{1}".format(
        getattr(settings, u'STATIC_URL', u'/static/'),
        u"select2/select2-4.0.2/lib/jquery-2.1.0.min.js"
    )
    SELECT2_LIB = u"{0}{1}".format(
        getattr(settings, u'STATIC_URL', u'/static/'),
        u"select2/select2-4.0.2/js/select2.full.min.js"
    )
    SELECT2_CSS_LIB = u"{0}{1}".format(
        getattr(settings, u'STATIC_URL', u'/static/'),
        u"select2/select2-4.0.2/css/select2.min.css"
    )
    SELECT2_DEFAULTS = {u"width": "300"}

    def configure_static_url(self, value):
        if not getattr(settings, 'STATIC_URL', None):
            self._meta.holder.STATIC_URL = value
            return value
        return getattr(settings, 'STATIC_URL')

    def configure_jquery_lib(self, value):
        if not getattr(settings, 'JQUERY_LIB', None):
            self._meta.holder.JQUERY_LIB = value
            return value
        return getattr(settings, 'JQUERY_LIB')

    def configure_select2_lib(self, value):
        if not getattr(settings, 'SELECT2_LIB', None):
            self._meta.holder.SELECT2_LIB = value
            return value
        return getattr(settings, 'SELECT2_LIB')

    def configure_select2_css_lib(self, value):
        if not getattr(settings, 'SELECT2_CSS_LIB', None):
            self._meta.holder.SELECT2_CSS_LIB = value
            return value
        return getattr(settings, 'SELECT2_CSS_LIB')

    def configure_select2_defaults(self, value):
        if not getattr(settings, 'SELECT2_DEFAULTS', None):
            self._meta.holder.SELECT2_DEFAULTS = value
            return value
        return getattr(settings, 'SELECT2_DEFAULTS')
