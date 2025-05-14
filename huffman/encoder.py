import json

def encode_text(text, code_table):
    return ''.join(code_table[char] for char in text)

def pad_bitstring(bitstring):
    extra_padding = 8 - len(bitstring) % 8
    bitstring += '0' * extra_padding
    padded_info = "{0:08b}".format(extra_padding)
    return padded_info + bitstring

def bitstring_to_bytes(bitstring):
    return bytes(int(bitstring[i:i+8], 2) for i in range(0, len(bitstring), 8))

def write_compressed_file(output_path, freq_table, encoded_bits):
    with open(output_path, 'wb') as f:
        # Header
        freq_json = json.dumps(freq_table)
        freq_bytes = freq_json.encode('utf-8')
        f.write(len(freq_bytes).to_bytes(4, 'big'))  # 4-byte length prefix
        f.write(freq_bytes)

        # Body
        padded_bitstring = pad_bitstring(encoded_bits)
        byte_data = bitstring_to_bytes(padded_bitstring)
        f.write(byte_data)
