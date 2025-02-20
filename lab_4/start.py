"""
Language generation starter
"""

import os
from lab_4.main import (
    tokenize_by_letters,
    encode_corpus,
    LetterStorage,
    LanguageProfile,
    PublicLanguageProfile,
    NGramTextGenerator,
    LikelihoodBasedTextGenerator,
    BackOffGenerator
)

PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':

    # find the appropriate start.py task in your lab_4 description file
    # your code goes here
    print("--- 4 ---")
    with open(os.path.join(PATH_TO_LAB_FOLDER, "reference_text.txt"), encoding="utf-8") as f:
        corpus = tokenize_by_letters(f.read())
    storage = LetterStorage()
    storage.update(corpus)
    print(len(storage.storage))
    print(list(storage.storage.items())[:5])
    print(list(storage.storage.items())[-5:])

    print("--- 6 ---")
    profile = LanguageProfile(storage, "idk")
    profile.create_from_tokens(encode_corpus(storage, corpus), (1, 2,))
    generator = NGramTextGenerator(profile)
    for length in range(5, 11):
        print(generator.generate_decoded_sentence((1,), length))

    print("--- 8 ---")
    generator = LikelihoodBasedTextGenerator(profile)
    for length in range(5, 11):
        print(generator.generate_decoded_sentence((1,), length))

    print("--- 10 ---")
    profile = PublicLanguageProfile(LetterStorage(), "ne")
    profile.open(os.path.join(PATH_TO_LAB_FOLDER, "ne"))

    for generator in [NGramTextGenerator(profile),
                      LikelihoodBasedTextGenerator(profile),
                      BackOffGenerator(profile)]:
        print(generator.generate_decoded_sentence((profile.storage.get_special_token_id(),), 5))

    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    # assert RESULT, 'Detection not working'
