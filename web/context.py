'''
Created on Mar 1, 2011

@author: smotko
'''

def settings(request):
    try:
        from web.models import Static
        s = Static.objects.all()[0]
        return {'SITE_TITLE': s.title, 'SITE_FOOTER': s.footer, 'settings': s}

    except:
        return {'SITE_TITLE': "Psywerx", 'SITE_FOOTER': "Psywerx"}
