from Products.TinyMCE.browser.style import TinyMCEStyle as Base
from zope.component.hooks import getSite
class TinyMCEStyle(Base):

    def getStyle(self):
        result = super(TinyMCEStyle, self).getStyle()
        site_url = getSite().absolute_url()
        result += '\n<!-- @import url(%s/%s); -->' % (site_url,
        '++theme++wcc.assemblytheme/public.css')
        return result
