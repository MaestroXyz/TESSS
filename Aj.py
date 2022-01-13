import marshal, zlib, base64, os, sys

try:
  r = sys.argv[1]
except:
  exit("Usage : Python2 Wizzly.py File.py")
  
if not os.path.isfile(r):
   exit("File Tidak di Temukan")
   
a = open(r).read()
b = marshal.dumps(a)
c = zlib.compress(b)
d = base64.b64encode(c)

sv = 'import marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("{}"))))'

open("enc.py","w").write(sv.format(d))
exit("Berhasil,File di simpan di enc.py")
