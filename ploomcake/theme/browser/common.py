from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import GlobalSectionsViewlet as OriginalGlobalSectionsViewlet

class GlobalSectionsViewlet(OriginalGlobalSectionsViewlet):
    """ """
    index = ViewPageTemplateFile('sections.pt')

