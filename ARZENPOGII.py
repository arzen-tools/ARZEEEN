#ENCODED BY : ARZEN R. CRESCENT
#FB LINK : https://www.facebook.com/arzenramospogi
#GITHUB : https://github.com/ARZEN -TOOLS
#----------------------------------------------
import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))