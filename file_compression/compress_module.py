import zlib,base64


def compress(inputfile,outputfile):
    data = open(inputfile, 'r').read()
    data_bytes = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))
    encoded_string = compressed_data.decode('utf-8')
    # Write encoded data to compressed.txt
    compressed_file = open(outputfile, 'w', encoding='utf-8')
    compressed_file.write(encoded_string)

def decompres(inputfile,outputfile):
    file_content =open(inputfile,'r').read()
    encode_data =file_content.encode('utf-8')
    decompressd_data = zlib.decompress(base64.b64decode(encode_data))
    decoded_data = decompressd_data.decode('utf-8')
    file=open(outputfile,'w')
    file.write(decoded_data)
    # print(decoded_data)
    file.close()
    # compressed_file = open(outputfile, 'w', encoding='utf-8')
    # compressed_file.write(store_data)

