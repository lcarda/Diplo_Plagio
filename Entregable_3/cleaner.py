SPECIAL_CHARACTERS = []

SPECIAL_CHARACTERS.extend(map(chr, range(0, 32)))
SPECIAL_CHARACTERS.extend(map(chr, range(33, 48)))
SPECIAL_CHARACTERS.extend(map(chr, range(58, 65)))
SPECIAL_CHARACTERS.extend(map(chr, range(91, 97)))
SPECIAL_CHARACTERS.extend(map(chr, range(123, 225)))
SPECIAL_CHARACTERS.extend(map(chr, range(226, 233)))
SPECIAL_CHARACTERS.extend(map(chr, range(234, 237)))
SPECIAL_CHARACTERS.extend(map(chr, range(238, 241)))
SPECIAL_CHARACTERS.extend(map(chr, range(242, 243)))
SPECIAL_CHARACTERS.extend(map(chr, range(244, 250)))
SPECIAL_CHARACTERS.extend(map(chr, range(251, 880)))

class CleanText():

    def __init__(self, text, language="english"):

        self.text = text

        self.language = language

        self.clean_text = None

        self.remove_spec_text = None

        self.remove_stop_text = None

        self.lemma_text = None

    def removePatterns(self):

        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )

        self.text = str(self.text)

        self.clean_text = self.text.lower()

        self.clean_text = re.sub(r"\s{2,}", " ", self.clean_text)

        self.clean_text = re.sub(r"\n", " ", self.clean_text)

        self.clean_text = re.sub(r"\d+", " ", self.clean_text)

        self.clean_text = re.sub(r"^\s+", " ", self.clean_text)

        self.clean_text = re.sub(r"\s+", " ", self.clean_text)

        for a, b in replacements:

            self.clean_text = self.clean_text.replace(a, b).replace(a.upper(), b.upper())

        return self.clean_text

    def removeSpecChars(self):

        remove_patterns = self.removePatterns()

        tokens = list(word_tokenize(remove_patterns))

        clean_tokens = tokens.copy()

        for i in range(len(clean_tokens)):

            for special_character in SPECIAL_CHARACTERS:

                clean_tokens[i] = clean_tokens[i].replace(special_character, '')

        clean_tokens = [token for token in clean_tokens if token]

        self.remove_spec_text = " ".join(clean_tokens)

        return self.remove_spec_text