from huffman.frequency import read_file_and_count_frequencies
from huffman.tree import build_huffman_tree
from huffman.codes import generate_huffman_codes
from huffman.encoder import encode_text
from huffman.encoder import write_compressed_file
from huffman.decoder import remove_padding,read_compressed_file,decode_text

if __name__ == "__main__":
    file_path = "Recources/test.txt"

    # Step 1: Frequency Table
    freq_table = read_file_and_count_frequencies(file_path)

    # Step 2: Huffman Tree
    root = build_huffman_tree(freq_table)

    # Step 3: Code Table
    code_table = generate_huffman_codes(root)

    # Step 4: Encode Text
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    encoded_bitstring = encode_text(text, code_table)
    output_file = "output/compressed.huff"
    write_compressed_file(output_file, freq_table, encoded_bitstring)
    print(f"Compression complete! Output written to {output_file}")
    # Step 6: Read Header & Rebuild Tree
    freq_table, padded_bits = read_compressed_file(output_file)
    unpadded_bits = remove_padding(padded_bits)
    root_decoding = build_huffman_tree(freq_table)

    # Step 7: Decode the bitstream
    decoded_text = decode_text(unpadded_bits, root_decoding)

    # Output file
    with open("output/decompressed.txt", "w", encoding="utf-8") as f:
        f.write(decoded_text)

    print("Decompression complete! Output saved to output/decompressed.txt")
    print(f"Encoded {len(text)} characters into {len(encoded_bitstring)} bits")
