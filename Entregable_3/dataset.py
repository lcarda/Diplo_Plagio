# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:18:29 2020

@author: pablonicolasr
"""

import nlp
import pandas as pd
import re

from seg import Segmentation



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




def getRow(originalFileName, originalText, language, index):

    fleshReadingEase = getfleshReadingEase(originalText)
    numOfPunctN = getnumOfPunctN(originalText)
    typeToken = gettypeToken(originalText, language)
    automated_readability_index = calculate_automated_readability_index(originalText)
    dale_chall_readability_score = calculate_dale_chall_readability_score(originalText)
    polysyllable_count = count_polysyllables(originalText)
    monosyllable_count = count_monosyllables(originalText)
    #ahora calculamos las metricas para el texto limpio
    cleanText = CleanText(originalText).removeSpecChars()
    fleshReadingEase_cl = getfleshReadingEase(cleanText)
    automated_readability_index_cl = calculate_automated_readability_index(cleanText)
    dale_chall_readability_score_cl = calculate_dale_chall_readability_score(cleanText)
    polysyllable_count_cl = count_polysyllables(cleanText)
    monosyllable_count_cl = count_monosyllables(cleanText)

    row = [index,
           originalFileName,
           fleshReadingEase,
           numOfPunctN,
           typeToken,
           automated_readability_index,
           dale_chall_readability_score,
           polysyllable_count,
           monosyllable_count,
           fleshReadingEase_cl,
           automated_readability_index_cl,
           dale_chall_readability_score_cl,
           polysyllable_count_cl,
           monosyllable_count_cl]

    return row


def generate(rootPath, outputPath, file, language):

    csvMode = "a"
    csvHeader = False
    csvIndex = False
    index = 1

    print("***Generating CSV***\n")

    header = [["index",
               "suspicious",
               "fleshReadingEase",
               "numOfPunctN",
               "typeToken",
               "automated_readability_index",
               "dale_chall_readability_score",
               "polysyllable_count",
               "monosyllable_count",
               "fleshReadingEase_cl",
               "automated_readability_index_cl",
               "dale_chall_readability_score_cl",
               "polysyllable_count_cl",
               "monosyllable_count_cl"
               ]]



    df = pd.DataFrame(header)

    df.to_csv(outputPath, mode = csvMode, header = csvHeader, index = csvIndex)

    f = open(rootPath, encoding= "utf-8-sig")

    text = f.read()

    f.close()

    segm = Segmentation(text)

    text = segm.paraSegmentation()

    text = [re.sub("\n", " ", sentence) for sentence in text]

    for j in range(len(text)):

        text2 = text[j-1]

        plagiarismRow = getRow(file, text2, language, index)

        print("Row: " + str(plagiarismRow))

        df = pd.DataFrame([plagiarismRow])

        df.to_csv(outputPath, mode = csvMode, header = csvHeader, index = csvIndex)

        index = index + 1


    print("\n***End generating***")