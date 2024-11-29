import base64
import zlib

data = open("demo.txt",'r').read()
data_bytes=bytes(data,'utf-8')
compressed_data =base64.b64encode(zlib.compress(data_bytes,9))
encoded_string=compressed_data.decode('utf-8')
# Write encoded data to compressed.txt
compressed_file = open('compressed.txt','w',encoding='utf-8')
compressed_file.write(encoded_string)

# #decomress the data
decompressd_data = zlib.decompress(base64.b64decode(encoded_string))
print(decompressd_data)
store_data= decompressd_data.decode('utf-8')
compressed_file = open('compressed.txt','w',encoding='utf-8')
compressed_file.write(store_data)