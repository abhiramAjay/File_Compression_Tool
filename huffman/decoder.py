import json
from huffman.tree import build_huffman_tree

def read_compressed_file(file_path):
    with open(file_path, 'rb') as f:
        header_len = int.from_bytes(f.read(4), 'big')
        header_json = f.read(header_len).decode('utf-8')
        freq_table = json.loads(header_json)

        bit_data = f.read()
        bitstring = ''.join(f"{byte:08b}" for byte in bit_data)

    return freq_table, bitstring

def remove_padding(padded_bitstring):
    padded_info = padded_bitstring[:8]
    extra_padding = int(padded_info, 2)
    return padded_bitstring[8:-extra_padding]

def decode_text(bitstring, root):
    decoded_text = []
    current = root

    for bit in bitstring:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_text.append(current.char)
            current = root

    return ''.join(decoded_text)
