# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def korean_to_be_englished(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):
        ## 영어인 경우 구분해서 작성함.
        if '가' <= w <= '힣':
            ## 588개 마다 초성이 바뀜.
            ch1 = (ord(w) - ord('가')) // 588
            ## 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) - (588 * ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588 * ch1) - 28 * ch2
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
        else:
            r_lst.append([w])
    return r_lst

txt_org = korean_to_be_englished("이승훈")
txt_pro = korean_to_be_englished("이쿤")

def calc_actual_length(korean_word):
    length = 0
    for w in korean_word:
        for p in w:
            if p != ' ':
                length += 1

    return length

def flatten(korean_word):
    return sum(korean_word, [])

def longest_common_substring(word1, word2):
    word1_flat = [''] + flatten(word1)
    word2_flat = [''] + flatten(word2)

    word1_len = len(word1_flat) - 1
    word2_len = len(word2_flat) - 1


    cache = [[0] * (word2_len + 1) for _ in range(word1_len + 1)]
    for i in range(1, word1_len + 1):
        for j in range(1, word2_len + 1):
            if word1_flat[i] == word2_flat[j]:
                cache[i][j] = cache[i-1][j-1] + 1
            else:
                cache[i][j] = max(cache[i][j-1], cache[i-1][j])

    return cache

def rule_1(word): # 유기음화(거센소리되기)
    AVAILABLE_PAIR = {('ㅎ', 'ㄱ'):(' ', 'ㅋ'), ('ㅎ', 'ㄷ'):(' ', 'ㅌ'), ('ㅎ', 'ㅈ'):(' ', 'ㅈ'),
                      ('ㄶ', 'ㄱ'):('ㄴ', 'ㅋ'), ('ㄶ', 'ㄷ'):('ㄴ', 'ㅌ'), ('ㄶ', 'ㅈ'):('ㄴ', 'ㅊ'),
                      ('ㅀ', 'ㄱ'):('ㄹ', 'ㅋ'), ('ㅀ', 'ㄷ'):('ㄹ', 'ㅌ'), ('ㅀ', 'ㅈ'):('ㄹ', 'ㅊ'),
                      ('ㄱ', 'ㅎ'):(' ', 'ㅋ'), ('ㄺ', 'ㅎ'):('ㄹ', 'ㅋ'), ('ㄷ', 'ㅎ'):(' ', 'ㅌ'),
                      ('ㅂ', 'ㅎ'):(' ', 'ㅍ'), ('ㄼ', 'ㅎ'):('ㄹ', 'ㅍ'), ('ㅈ', 'ㅎ'):(' ', 'ㅊ'), ('ㄵ', 'ㅎ'):('ㄴ', 'ㅊ'),
                      ('ㅅ', 'ㅎ'):(' ', 'ㅌ'), ('ㅈ', 'ㅎ'):(' ', 'ㅌ'), ('ㅌ', 'ㅎ'):(' ', 'ㅌ'), ('ㅍ', 'ㅎ'):(' ', 'ㅌ'),
                      ('ㅎ', 'ㅅ'):(' ', 'ㅆ'), ('ㄶ', 'ㅅ'):('ㄴ', 'ㅆ'), ('ㅀ', 'ㅅ'):('ㄹ', 'ㅆ'),
                      ('ㅎ', 'ㄴ'):(' ', 'ㄴ'), ('ㄶ', 'ㄴ'):('ㄴ', 'ㄴ'), ('ㅀ', 'ㄴ'):('ㄹ', 'ㄹ'),
                      ('ㅎ', 'ㅇ'):(' ', 'ㅇ'), ('ㄶ', 'ㅇ'):(' ', 'ㄴ'), ('ㅀ', 'ㅇ'):(' ', 'ㄹ')}

    for (idx, w) in enumerate(word):
        if len(w) == 3 and idx+1 < len(word):
            p1 = w[2]
            p2 = word[idx+1][0]
            if (p1, p2) in AVAILABLE_PAIR:
                word[idx][2] = AVAILABLE_PAIR[(p1, p2)][0]
                word[idx+1][0] = AVAILABLE_PAIR[(p1, p2)][1]

    return word

def text2pron(word):
    splitted_word = korean_to_be_englished(word)
    changed_word = rule_1(splitted_word)
    print(changed_word)

text2pron('놓고')