def generate_huffman_codes(root):
    codes = {}

    def _generate_codes(node, current_code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = current_code
            return

        _generate_codes(node.left, current_code + "0")
        _generate_codes(node.right, current_code + "1")

    _generate_codes(root, "")
    return codes
