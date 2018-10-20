import random,simplejson
from django.http import HttpResponse
import base64

def getRpId():
    return {"id":"pri.local.mkalioby.com","name":"django_webauth"}

def BeginMakeCredential(request):
    challenge= []
    for c in range(32):
        challenge.append(random.randint(0,64))
    #challenge=base64.encodestring(str(challenge))
    print(challenge)

    x={"rp":getRpId,
       "user":{"name":request.user.username,"displayName":request.user.username,"id":""},"challenge":challenge,
       "pubKeyCredParams":[{"type":"public-key","alg":-7},{"type":"public-key","alg":-35},{"type":"public-key","alg":-36},{"type":"public-key","alg":-257},{"type":"public-key","alg":-258},{"type":"public-key","alg":-259},{"type":"public-key","alg":-37},{"type":"public-key","alg":-38},{"type":"public-key","alg":-39}],
       "authenticatorSelection":{"authenticatorAttachment":"platform","requireResidentKey":False,"userVerification":"required"},
       }
    return HttpResponse(simplejson.dumps(x))


def FinishMakeCredential(request):
    request.user.public_key=simplejson.loads(request.POST["data"])["rawId"]
    request.user.save()
    return HttpResponse(simplejson.dumps({"msg":"Credentials Saved, try to login"}))


def genToken(request):
    challenge = []
    for c in range(32):
        challenge.append(random.randint(0, 64))
    return HttpResponse(simplejson.dumps({"challenge":challenge,"rp":getRpId()}))

