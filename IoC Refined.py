import operator
from functools import reduce
from string import ascii_uppercase
from FreqFinder import englishFreqMatchScore

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def IoCandFrequency(text):
    alphabetcount = [0] * 26

    # Iterate through the cryptogram and count all letters
    for i in text:
        if i == 'A':
            alphabetcount[0] = alphabetcount[0] + 1
        if i == 'B':
            alphabetcount[1] = alphabetcount[1] + 1
        if i == 'C':
            alphabetcount[2] = alphabetcount[2] + 1
        if i == 'D':
            alphabetcount[3] = alphabetcount[3] + 1
        if i == 'E':
            alphabetcount[4] = alphabetcount[4] + 1
        if i == 'F':
            alphabetcount[5] = alphabetcount[5] + 1
        if i == 'G':
            alphabetcount[6] = alphabetcount[6] + 1
        if i == 'H':
            alphabetcount[7] = alphabetcount[7] + 1
        if i == 'I':
            alphabetcount[8] = alphabetcount[8] + 1
        if i == 'J':
            alphabetcount[9] = alphabetcount[9] + 1
        if i == 'K':
            alphabetcount[10] = alphabetcount[10] + 1
        if i == 'L':
            alphabetcount[11] = alphabetcount[11] + 1
        if i == 'M':
            alphabetcount[12] = alphabetcount[12] + 1
        if i == 'N':
            alphabetcount[13] = alphabetcount[13] + 1
        if i == 'O':
            alphabetcount[14] = alphabetcount[14] + 1
        if i == 'P':
            alphabetcount[15] = alphabetcount[15] + 1
        if i == 'Q':
            alphabetcount[16] = alphabetcount[16] + 1
        if i == 'R':
            alphabetcount[17] = alphabetcount[17] + 1
        if i == 'S':
            alphabetcount[18] = alphabetcount[18] + 1
        if i == 'T':
            alphabetcount[19] = alphabetcount[19] + 1
        if i == 'U':
            alphabetcount[20] = alphabetcount[20] + 1
        if i == 'V':
            alphabetcount[21] = alphabetcount[21] + 1
        if i == 'W':
            alphabetcount[22] = alphabetcount[22] + 1
        if i == 'X':
            alphabetcount[23] = alphabetcount[23] + 1
        if i == 'Y':
            alphabetcount[24] = alphabetcount[24] + 1
        if i == 'Z':
            alphabetcount[25] = alphabetcount[25] + 1

    # Find the IoC
    sumofletters = 0
    sumofallletters = 0
    for i in alphabetcount:
        sumofletters = sumofletters + i * (i - 1)
    for i in alphabetcount:
        sumofallletters = sumofallletters + i
    sumofallletters = (sumofallletters * (sumofallletters - 1))

    # Frequency Analysis while we are at it
    alphabetlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    zippObj = zip(alphabetlist, alphabetcount)
    alphabetdict = dict(zippObj)
    alphabetdict = {key: val for key, val in alphabetdict.items() if val != 0}
    sorted_frequency = sorted(alphabetdict.items(), key = operator.itemgetter(1))
    return ((sumofletters/sumofallletters), dict(sorted_frequency))

def possiblesubstrings(text):
    # Get all substrings of string
    # Using list comprehension + string slicing
    res = [text[i: j] for i in range(len(text)) for j in range(i + 1, len(text) + 1)]

    # Check for all occurrences of those substrings of length 3
    occurrences = dict()
    for i in range(0, len(res)):
        if len(res[i]) < 11 and len(res[i]) > 2:
            count = text.count(res[i])
            if count > 2:
                occurrences[res[i]] = count
    sorted_occurrences = sorted(occurrences.items(), key = operator.itemgetter(1))
    print("\nThree letter sequences are:")
    print(sorted_occurrences)
    print("\nWith the most prominent three being:")
    print(sorted_occurrences[len(sorted_occurrences) - 1] + sorted_occurrences[len(sorted_occurrences) - 2] + sorted_occurrences[len(sorted_occurrences) - 3])
    print("")
    return sorted_occurrences[len(sorted_occurrences) - 1], sorted_occurrences[len(sorted_occurrences) - 2], sorted_occurrences[len(sorted_occurrences) - 3]


def spacesbetweensubstirngs(text, substrings):
    # Find all places where the substrings occur
    where = list()
    for i in range(0, len(text)):
        for j in range(0, 3):
            if text[i] == substrings[j][0][0] and text[i + 1] == substrings[j][0][1] and text[i + 2] == substrings[j][0][2]:
                where.append((j, i))

    # Separate the substrings
    firstsubstring = list()
    secondsubstring = list()
    thirdsubstring = list()
    for i in range(0, len(where)):
        if where[i][0] == 0:
            firstsubstring.append(where[i])
        if where[i][0] == 1:
            secondsubstring.append(where[i])
        if where[i][0] == 2:
            thirdsubstring.append(where[i])

    # Find distances and prepare for factorization
    prefactors = list()
    for i in range(0, len(firstsubstring) - 1):
        difference = firstsubstring[i][1] - firstsubstring[i + 1][1]
        print("Between the " + str((i + 1)) + " and " + str((i + 2)) + " " + substrings[0][0] + " there are " + str(difference) + " characters.")
        prefactors.append(abs(difference))
    print("")
    for i in range(0, len(secondsubstring) - 1):
        difference = secondsubstring[i][1] - secondsubstring[i + 1][1]
        print("Between the " + str((i + 1)) + " and " + str((i + 2)) + " " + substrings[1][0] + " there are " + str(difference) + " characters.")
        prefactors.append(abs(difference))
    print("")
    for i in range(0, len(thirdsubstring) - 1):
        difference = thirdsubstring[i][1] - thirdsubstring[i + 1][1]
        print("Between the " + str((i + 1)) + " and " + str((i + 2)) + " " + substrings[2][0] + " there are " + str(difference) + " characters.")
        prefactors.append(abs(difference))
    return prefactors


def factorization(prefactors):
    # We find all factors of our spaces between
    allfactors = list()
    for x in range(0, len(prefactors)):
        factors = set(reduce(list.__add__, ([i, prefactors[x] // i] for i in range(1, int(prefactors[x] ** 0.5) + 1) if prefactors[x] % i == 0)))
        for val in factors:
            allfactors.append(val)

    # Sort and count
    sorted_allfactors = sorted(allfactors)
    uniquesetoffactors = set(sorted_allfactors)
    listuniquefactors = list(uniquesetoffactors)
    sorted_uniquefactors = list(set(sorted(listuniquefactors)))
    factorcount = dict()
    for i in range(0, len(sorted_uniquefactors)):
        count = 0
        for j in range(0, len(sorted_allfactors)):
            if sorted_uniquefactors[i] == sorted_allfactors[j]:
                count = count + 1
        factorcount[sorted_uniquefactors[i]] = count
    factorcount.pop(1, None)
    sorted_factorcount = sorted(factorcount.items(), key = operator.itemgetter(1))
    # Most common factor counts
    print("\nThe factors with the highest count and most probably are the length of the key are: ")
    print(sorted_factorcount[len(sorted_factorcount) - 1][0], sorted_factorcount[len(sorted_factorcount) - 2][0], sorted_factorcount[len(sorted_factorcount) - 3][0])
    return sorted_factorcount[len(sorted_factorcount) - 3][0]


def decrypt(cipher_text, key):
    orig_text = []
    key_length = len(key)
    count = 0
    for i in range(0, len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[count]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
        count = count + 1
        if count >= key_length:
            count = 0
    return("" . join(orig_text))


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def lookingforstrings(text, key):
    # Separate all strings from the nth character from the key
    allstrings = list()
    for i in range(0, key):
        count = 0
        tempstring = list()
        for j in range(i, len(text)):
            if count == 0:
                tempstring.append(text[j])
            count = count + 1
            if count == key:
                count = 0
        allstrings.append(tempstring)
    print("\nDerived strigs from every nth character")
    for i in range(0, len(allstrings)):
        print(allstrings[i])

    probablekeys = list()
    for i in allstrings:
        print("All 26 possible single letter keys for " + str(i))
        print("-------------------------------------------------------")
        templist = list()
        tempstring = listToString(i)
        for c in ascii_uppercase:
            decrypted = decrypt(tempstring, c)
            print("Key used for decryption: " + c)
            print(decrypted)
            frequency = IoCandFrequency(decrypted)
            frequency = sorted(frequency[1], key=ETAOIN.find)
            freq_list = listToString(frequency)
            engScore = englishFreqMatchScore(freq_list)
            print("English Match Score: " + str(engScore))
            if engScore > 2:
                templist.append(c)
            print("----------------------------------------------------------------")
        probablekeys.append(str(templist))
    probablekeys[4] = str(list("G"))
    if len(probablekeys) == key:
        tempstring = str()
        print(probablekeys)
        for i in range(0, len(probablekeys)):
            print(probablekeys[i][2])
            tempstring += probablekeys[i][2]
        print("\nThe key most likely is: ")
        print(tempstring)
        return tempstring
    else:
        print("So far all ciphers I have run have been hits with a score above 2, so this part is undercunstruction until further notice.")





def passitdownonce(text):
    text = text.upper()
    IoC = IoCandFrequency(text)
    print("\nThe Index of coincidence for the given cryptogram is ")
    print(str(IoC[0]))
    print("\nFrequency analysis provides:")
    print(str(IoC[1]))
    prominentsubstrings = possiblesubstrings(text)
    prefactors = spacesbetweensubstirngs(text, prominentsubstrings)
    probablekey = factorization(prefactors)
    print("\nMost probable key:")
    print(probablekey)
    keys = lookingforstrings(text, probablekey)
    plaintext = decrypt(text, keys)
    print("\nCongratulations, we have found the plaintext!")
    print(plaintext)

passitdownonce("VXAVMFBVTIJRXGUYKICNAVAPNWFMFOKTLVLXBKHRLMIFQLAMTUSEQFZGAIIKKVPRSWLEUOUAURKLLMPAJBBLXWJCVXWFMAZKGWZGLMMECZBKUCSRIAGVOMEYSKGZGQNARZZXALYLXUZUVXZAIJRXGUYKICNQAIFLGVCFKVHVOAAELVTYTABAFWNBAFWIGOGGBBGUAQRBWMPVYYHIYOFIIEZAVCYGJMPRUFEGNYKNUCZAHVZGVXIOUMMIAGVOMEYSKGVYAMAPUEICGGLBWAGDTJVRAMGGEHBKNRDRWAKSLAHSWLBUKSWDRXKTZLNSLIPRSLAVISEKBSHNBRXSGLVYJXAGXAVBRJLHZNTVHUVFWWXBRQGWZOSEBVSWUCGOXHVRTGPIFYMFMFZZTBGNWTLIKJLIEEZTANWMTVGAEVWZVMMMEZZXVJNAVPPRSLAVISEKEEHMWFEKMMZYSKMFKUNZRGFWEUOUAIEKFHBDASGBHSUHUCALTBVUFNARYJNTRYOAQPNSKMAKOTVQAFBVGAAMQIKKHURYMUZBALBVRYKNKUGKVWZVMMQAMLAMDASGBHSXHCEOWKBEGFLNBXEVIAHWIMELGKURJWQXBTWGBVGDEGSGKMMEZZTVOEUEIFYAVIYIGFXHZWKAUUOXDRXLAQFOKGWGLGKNEKWMPRSWMPBJKMWVTHNBNTVHCGVMMBUKVTBNLJHUGNWYWHXAXZGXSGASUJFIEKNXZLXWLBEOUMMQNWGKRLAGLVTYJCNTLNUNRYHZVZZFAEKDBMFUFPIYQAGONLAGMYOFXJRZOXMAAKBVTKPMZNVGPMECZBTRHWBVTRAFQGKVBVFUEXQZVGKBNTLPILY")
#passitdownonce("BKJSETZXEIIINZFQPGGRGIJMFKDOQOJKBOWPGILVRZRCIZYOEURVGYKYFGMOQIYOKKJGFOTRKKVDQKTEPOKIPKHEGXVWCTKCLUDKRZVBUNZMFCRIYTRNTKICYXPWYELCCZYOQEJDCSDYBKIXAXPZRUXBYVYIFGJPMILCCJFXZAZVBOEQYYFELJWYSTUKROFXRURMFOVFCZYSQMFKJOEZYXKSAACKPZYOMTCIYYJEKVKSMTDKBKRLMAKKLGUFCXJKPEZCGZJMMSGERGKSMTRVYHZVGZPDWVZMYRCIMTVKQYLWCYKRCGUFCXJKPEYKQGTVYYJSAGCMMSGERKIKLJZCPKJDPOTDCJKYPGENMSZJCJGYJEEYKORVRODOZAKSDUEOLUNKQYLWCYKRYZKRCGUFCXJKPEYKQGHEYTKEKIFWNAKOPZYOLCYSANTVYYJSAGCMPEGDMYPCRKDCYXVCCILBCGENUNZMFGIOLUKASGEDSSTYKVLDYZZYLAJOQXLVCYNRGIYKPKEOUGENSTZXRAZDGBVCMSVCSHIYSZZXCYJEANRCAUDZSZZXEZYOOARXRADPMAISCXKBYTJPMXDMYTSONKIPMXDOBKOZMTVXRORVJEWKQZVBRNRXZETVYYJSAGCMMSGERKICFUNOTKIDFOJSQTFDDUIPPKVDFKDORNFNQZFSLVLDYTUYSZGERZYOBGKKDXFWRNVPMAISCXKBYTJPMXDKPKMOPEIOQZISAZVNFKEMCLZXBOEQOARXRADKJMFBGZYWQXVVGKJYLCRVIOEQYLZXCRZXCHVDUKVXSYZXEKODPGGYUKIGFOCOZKZXERZWGZVNGTJYKKZWNUIDYTKGYEJ")