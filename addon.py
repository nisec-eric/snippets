import mitmproxy.http
from mitmproxy import ctx, http
from urllib.parse import parse_qs,parse_qsl, urlencode
from cf import enc,dec

class Joker:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        if "video-progress" not in flow.request.path:
            return

        qs = parse_qsl(flow.request.text)
        qs_d = parse_qs(flow.request.text)
        qs_new = []
        for key, value in qs:
            if "studyTime" in key or "lessonLocation" in key:
                qs_new.append((key,enc(str(int(dec(qs_d[key][0]))+5))))
                #qs_new.append((key,enc(str(int(dec(qs_d["resourceTotalTime"][0]))-10))))
            else:
                qs_new.append((key,value))

        ctx.log.info("Find video-progress")
        for (key, value),(k2,v2) in zip(qs_new,qs):
            ctx.log.info("\tget %s: %s (%s)->%s (%s)" % (key,dec(v2),v2,dec(value),value))

        flow.request.text = urlencode(qs_new)

addons = [ Joker() ]
