import gevent
from gevent import monkey
monkey.patch_all()

import urllib
import urllib2
import xml.dom.minidom


class Translator(object):
    """ Microsoft Translator using Bing API """

    def __init__(self, appid, from_lang, to_lang):
        """ Constructor """
        self.appid = appid
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate_list(self, texts):
        jobs = [gevent.spawn(self.translate, text) for text in texts]
        gevent.joinall(jobs)
        return [job.value for job in jobs]

    def translate(self, text):
        if not text:
            return ""

        # We can use TranslateArray for better performance
        # But I'd like to use gevent for testing
        base_url = 'http://api.microsofttranslator.com/v2/Http.svc/Translate?'
        data = urllib.urlencode({'appId': self.appid,
                                 'from': self.from_lang.encode('utf-8'),
                                 'to': self.to_lang.encode('utf-8'),
                                 'text': text.encode('utf-8')
                                })

        url = base_url + data
        response = urllib2.urlopen(url).read()

        dom = xml.dom.minidom.parseString(response)
        result = dom.documentElement.childNodes[0].nodeValue
        return result.encode('utf-8')
