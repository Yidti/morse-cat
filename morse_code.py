def _arabic_numbers(dit, dah) -> dict:
    arabic_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    code_1 = "".join([dit, dah, dah, dah, dah])
    code_2 = "".join([dit, dit, dah, dah, dah])
    code_3 = "".join([dit, dit, dit, dah, dah])
    code_4 = "".join([dit, dit, dit, dit, dah])
    code_5 = "".join([dit, dit, dit, dit, dit])
    code_6 = "".join([dah, dit, dit, dit, dit])
    code_7 = "".join([dah, dah, dit, dit, dit])
    code_8 = "".join([dah, dah, dah, dit, dit])
    code_9 = "".join([dah, dah, dah, dah, dit])
    code_0 = "".join([dah, dah, dah, dah, dah])
    arabic_number_codes = [code_1, code_2, code_3, code_4, code_5, code_6, code_7, code_8, code_9, code_0]
    morse_dict = dict(zip(arabic_numbers, arabic_number_codes))
    return morse_dict


def _basic_latin_letters(dit, dah) -> dict:
    latin_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                     'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    code_a = "".join([dit, dah])
    code_b = "".join([dah, dit, dit, dit])
    code_c = "".join([dah, dit, dah, dit])
    code_d = "".join([dah, dit, dit])
    code_e = "".join([dit])
    code_f = "".join([dit, dit, dah, dit])
    code_g = "".join([dah, dah, dit])
    code_h = "".join([dit, dit, dit, dit])
    code_i = "".join([dit, dit])
    code_j = "".join([dit, dah, dah, dah])
    code_k = "".join([dah, dit, dah])
    code_l = "".join([dit, dah, dit, dit])
    code_m = "".join([dah, dah])
    code_n = "".join([dah, dit])
    code_o = "".join([dah, dah, dah])
    code_p = "".join([dit, dah, dah, dit])
    code_q = "".join([dah, dah, dit, dah])
    code_r = "".join([dit, dah, dit])
    code_s = "".join([dit, dit, dit])
    code_t = "".join([dah])
    code_u = "".join([dit, dit, dah])
    code_v = "".join([dit, dit, dit, dah])
    code_w = "".join([dit, dah, dah])
    code_x = "".join([dah, dit, dit, dah])
    code_y = "".join([dah, dit, dah, dah])
    code_z = "".join([dah, dah, dit, dit])

    latin_letter_codes = [code_a, code_b, code_c, code_d, code_e, code_f, code_g, code_h, code_i, code_j, code_k,
                          code_l,
                          code_m, code_n, code_o, code_p, code_q, code_r, code_s, code_t, code_u, code_v, code_w,
                          code_x,
                          code_y, code_z]

    morse_dict = dict(zip(latin_letters, latin_letter_codes))
    return morse_dict


class morse_code:

    def __init__(self, dit='.', dah='-', **space):
        self.dit = dit
        self.dah = dah
        self.space = space
        space.setdefault('btw_dits_n_dahs', '*')
        space.setdefault('btw_letters', '***')
        space.setdefault('btw_words', '*******')
        self.gap_intra_character = space['btw_dits_n_dahs']
        self.gap_short = space['btw_letters']
        self.gap_medium = space['btw_words']
        self.latin_letters = _basic_latin_letters(self.dit, self.dah)
        self.arabic_numbers = _arabic_numbers(self.dit, self.dah)
        self.dict = self.latin_letters | self.arabic_numbers
        self.rev_dict = self._rev_dict()

    def _rev_dict(self):
        return {v: k for k, v in self.dict.items()}

    def encode(self, message: str) -> str:
        encode_word_list = []
        message = message.strip().upper()
        words = message.split(" ")
        print(f"Content of original message: {words}")

        for index, word in enumerate(words):
            encode_letter_list = []
            letter_list = list(word)
            print(f"Content of word_{index+1}: {letter_list}")

            # handle with every letter
            for letter in word:
                if letter in self.dict.keys():
                    # insert space btw intra_character
                    _encode = self.dict[letter]
                    _encode = self.gap_intra_character.join(_encode[i:i+1] for i in range(0, len(_encode)))
                    encode_letter_list.append(_encode)
                else:
                    print("Please check your string.")
            print(f"Convert to Morse Code: {encode_letter_list}")

            # combine every letter and store in list
            encode_word_list.append(self.gap_short.join(encode_letter_list))

        # insert space btw words
        encode_str = self.gap_medium.join(encode_word_list)
        print(f"Encode string for Morse code: {encode_str}")

        return encode_str

    def decode(self, message: str) -> str:

        # test code: ... --- ... / ...
        # test code: .*.*.***-*-*-***.*.*. / .*.*.***..-
        decode_word_list = []
        message = message.strip()
        # handle with every word - split with medium
        words = message.split(self.gap_medium)
        print(f"Content of original message: {words}")

        for index, word in enumerate(words):
            decode_letter_list = []
            # handle with every letter - split with gap_short
            letter_list = word.split(self.gap_short)
            print(f"Content of word_{index+1}: {letter_list}")

            for letter in letter_list:
                # remove gap_intra_character from letter
                letter = letter.replace(self.gap_intra_character, '')
                if letter in self.rev_dict.keys():
                    _decode = self.rev_dict[letter]
                    decode_letter_list.append(_decode)
                else:
                    print("Please check your code.")
            print(f"Convert to Text: {decode_letter_list}")

            # combine every letter and store in list
            decode_word_list.append("".join(decode_letter_list))

        # insert space btw words
        decode_str = " ".join(decode_word_list)
        print(f"Decode string for Morse code: {decode_str}")

        return decode_str


