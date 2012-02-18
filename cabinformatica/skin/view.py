# coding=utf-8
from five import grok
from zope import schema

from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite 
from Products.CMFCore.interfaces import ISiteRoot


class HomePageView(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('home-page')
    
    def get_Noticias(self):    
        local = self.context.getPhysicalPath()
        self.pc = getToolByName(self.context, 'portal_catalog')
        news = self.pc(portal_type=('News Item'),
                       review_state='published',
                       path={'query':'/'.join(local)},
                       sort_on='effective',
                       sort_order='descending',)
        
        if news:
            return [i.getObject() for i in news]
        else:
            return []
        
        
    def get_text_frontpage(self):
        
        if 'front-page' in getSite():
            obj = getSite()['front-page']
            return obj
        else:
            return None
    
    def get_last_Sites(self):
        
        if 'last-sites' in getSite():
            obj = getSite()['last-sites']
            return obj
        else:
            return None