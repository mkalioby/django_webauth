import random,simplejson
from django.http import HttpResponse
import base64
def BeginMakeCredential(request):
    challenge= []
    for c in range(32):
        challenge.append(random.randint(0,64))
    #challenge=base64.encodestring(str(challenge))
    print(challenge)

    x={"rp":{"id":"django_webauth","name":"django_webauth"},"user":{"name":request.user.username,"displayName":request.user.username,"id":"bWthbGlvYnlAbWthbGlvYnkuY29t"},"challenge":"7VFehuGpKPzSQ7QZCCFP0t2qG+def7CeGmLzUGFfa98=","pubKeyCredParams":[{"type":"public-key","alg":-7},{"type":"public-key","alg":-35},{"type":"public-key","alg":-36},{"type":"public-key","alg":-257},{"type":"public-key","alg":-258},{"type":"public-key","alg":-259},{"type":"public-key","alg":-37},{"type":"public-key","alg":-38},{"type":"public-key","alg":-39}],"authenticatorSelection":{"authenticatorAttachment":"platform","requireResidentKey":False,"userVerification":"required"},"session":{"id":5700735861784576,"challenge":"7VFehuGpKPzSQ7QZCCFP0t2qG+def7CeGmLzUGFfa98=","origin":"webauthndemo.appspot.com"}}
    return HttpResponse(simplejson.dumps(x))
