import utils
import unittest

def rule_1(word): # 유기음화(거센소리되기)
    AVAILABLE_PAIR = {('ㅎ', 'ㄱ'):(' ', 'ㅋ'), ('ㅎ', 'ㄷ'):(' ', 'ㅌ'), ('ㅎ', 'ㅈ'):(' ', 'ㅊ'),
                      ('ㄶ', 'ㄱ'):('ㄴ', 'ㅋ'), ('ㄶ', 'ㄷ'):('ㄴ', 'ㅌ'), ('ㄶ', 'ㅈ'):('ㄴ', 'ㅊ'),
                      ('ㅀ', 'ㄱ'):('ㄹ', 'ㅋ'), ('ㅀ', 'ㄷ'):('ㄹ', 'ㅌ'), ('ㅀ', 'ㅈ'):('ㄹ', 'ㅊ'),
                      ('ㄱ', 'ㅎ'):(' ', 'ㅋ'), ('ㄺ', 'ㅎ'):('ㄹ', 'ㅋ'), ('ㄷ', 'ㅎ'):(' ', 'ㅌ'),
                      ('ㅂ', 'ㅎ'):(' ', 'ㅍ'), ('ㄼ', 'ㅎ'):('ㄹ', 'ㅍ'), ('ㅈ', 'ㅎ'):(' ', 'ㅊ'), ('ㄵ', 'ㅎ'):('ㄴ', 'ㅊ'),
                      ('ㅅ', 'ㅎ'):(' ', 'ㅌ'), ('ㅈ', 'ㅎ'):(' ', 'ㅌ'), ('ㅊ', 'ㅎ'):(' ', 'ㅌ'), ('ㅌ', 'ㅎ'):(' ', 'ㅌ'),
                      ('ㅎ', 'ㅅ'):(' ', 'ㅆ'), ('ㄶ', 'ㅅ'):('ㄴ', 'ㅆ'), ('ㅀ', 'ㅅ'):('ㄹ', 'ㅆ'),
                      ('ㅎ', 'ㄴ'):('ㄴ', 'ㄴ'), ('ㄶ', 'ㄴ'):('ㄴ', 'ㄴ'), ('ㅀ', 'ㄴ'):('ㄹ', 'ㄹ'),
                      ('ㅎ', 'ㅇ'):(' ', 'ㅇ'), ('ㄶ', 'ㅇ'):(' ', 'ㄴ'), ('ㅀ', 'ㅇ'):(' ', 'ㄹ')}

    for (idx, w) in enumerate(word):
        if len(w) == 3 and idx+1 < len(word):
            p1 = w[2]
            p2 = word[idx+1][0]
            if (p1, p2) in AVAILABLE_PAIR:
                word[idx][2] = AVAILABLE_PAIR[(p1, p2)][0]
                word[idx+1][0] = AVAILABLE_PAIR[(p1, p2)][1]

    return word

def rule_2(word): # 음절의 끝소리 규칙
    AVAILABLE_PAIR = {('ㄲ', ''):('ㄱ')}

def text2pron(word):
    splitted_word = utils.korean_to_be_englished(word)
    changed_word = rule_1(splitted_word)
    return changed_word

class TestPronMethods(unittest.TestCase):
    def test_rule1_1_0(self):
        self.assertEqual(text2pron('놓고'), [['ㄴ', 'ㅗ', ' '], ['ㅋ', 'ㅗ', ' ']])
        self.assertEqual(text2pron('좋던'), [['ㅈ', 'ㅗ', ' '], ['ㅌ', 'ㅓ', 'ㄴ']])
        self.assertEqual(text2pron('쌓지'), [['ㅆ', 'ㅏ', ' '], ['ㅊ', 'ㅣ', ' ']])
        self.assertEqual(text2pron('많고'), [['ㅁ', 'ㅏ', 'ㄴ'], ['ㅋ', 'ㅗ', ' ']])
        self.assertEqual(text2pron('않던'), [['ㅇ', 'ㅏ', 'ㄴ'], ['ㅌ', 'ㅓ', 'ㄴ']])
        self.assertEqual(text2pron('닳지'), [['ㄷ', 'ㅏ', 'ㄹ'], ['ㅊ', 'ㅣ', ' ']])

    def test_rule1_1_1(self):
        self.assertEqual(text2pron('각하'), [['ㄱ', 'ㅏ', ' '], ['ㅋ', 'ㅏ', ' ']])
        self.assertEqual(text2pron('먹히다'), [['ㅁ', 'ㅓ', ' '], ['ㅋ', 'ㅣ', ' '], ['ㄷ', 'ㅏ', ' ']])
        self.assertEqual(text2pron('밟히다'), [['ㅂ', 'ㅏ', 'ㄹ'], ['ㅍ', 'ㅣ', ' '], ['ㄷ', 'ㅏ', ' ']])
        self.assertEqual(text2pron('맏형'), [['ㅁ', 'ㅏ', ' '], ['ㅌ', 'ㅕ', 'ㅇ']])
        self.assertEqual(text2pron('좁히다'), [['ㅈ', 'ㅗ', ' '], ['ㅍ', 'ㅣ', ' '], ['ㄷ', 'ㅏ', ' ']])
        self.assertEqual(text2pron('넓히다'), [['ㄴ', 'ㅓ', 'ㄹ'], ['ㅍ', 'ㅣ', ' '], ['ㄷ', 'ㅏ', ' ']])
        self.assertEqual(text2pron('꽂히다'), [['ㄲ', 'ㅗ', ' '], ['ㅊ', 'ㅣ', ' '], ['ㄷ', 'ㅏ', ' ']])
        self.assertEqual(text2pron('앉히다'), [['ㅇ', 'ㅏ', 'ㄴ'], ['ㅊ', 'ㅣ', ' '], ['ㄷ', 'ㅏ', ' ']])

    def test_rule1_1_2(self):
        self.assertEqual(text2pron('옷한벌'), [['ㅇ', 'ㅗ', ' '], ['ㅌ', 'ㅏ', 'ㄴ'], ['ㅂ', 'ㅓ', 'ㄹ']])
        self.assertEqual(text2pron('낮한때'), [['ㄴ', 'ㅏ', ' '], ['ㅌ', 'ㅏ', 'ㄴ'], ['ㄸ', 'ㅐ', ' ']])
        self.assertEqual(text2pron('꽃한송이'), [['ㄲ', 'ㅗ', ' '], ['ㅌ', 'ㅏ', 'ㄴ'], ['ㅅ', 'ㅗ', 'ㅇ'], ['ㅇ', 'ㅣ', ' ']])
        self.assertEqual(text2pron('숱하다'), [['ㅅ', 'ㅜ', ' '], ['ㅌ', 'ㅏ', ' '], ['ㄷ', 'ㅏ', ' ']])

    def test_rule1_2_0(self):
        self.assertEqual(text2pron('닿소'), [['ㄷ', 'ㅏ', ' '], ['ㅆ', 'ㅗ', ' ']])
        self.assertEqual(text2pron('많소'), [['ㅁ', 'ㅏ', 'ㄴ'], ['ㅆ', 'ㅗ', ' ']])
        self.assertEqual(text2pron('싫소'), [['ㅅ', 'ㅣ', 'ㄹ'], ['ㅆ', 'ㅗ', ' ']])

    def test_rule1_3_0(self):
        self.assertEqual(text2pron('놓는'), [['ㄴ', 'ㅗ', 'ㄴ'], ['ㄴ', 'ㅡ', 'ㄴ']])
        self.assertEqual(text2pron('쌓네'), [['ㅆ', 'ㅏ', 'ㄴ'], ['ㄴ', 'ㅔ', ' ']])

    def test_rule1_3_1(self):
        self.assertEqual(text2pron('않네'), [['ㅇ', 'ㅏ', 'ㄴ'], ['ㄴ', 'ㅔ', ' ']])
        self.assertEqual(text2pron('않는'), [['ㅇ', 'ㅏ', 'ㄴ'], ['ㄴ', 'ㅡ', 'ㄴ']])
        self.assertEqual(text2pron('뚫네'), [['ㄸ', 'ㅜ', 'ㄹ'], ['ㄹ', 'ㅔ', ' ']])
        self.assertEqual(text2pron('뚫는'), [['ㄸ', 'ㅜ', 'ㄹ'], ['ㄹ', 'ㅡ', 'ㄴ']])

