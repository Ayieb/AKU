import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode('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'))))
