import clipboard as c
wordList = ["a", "akesi", "ala", "alasa", "ale", "anpa", "ante", "anu", "awen",
            "e", "en", "esun", "ijo", "ike", "ilo", "insa", "jaki", "jan",
            "jelo", "jo", "kala", "kalama", "kama", "kasi", "ken", "kepeken",
            "kili", "kiwen", "ko", "kon", "kule", "kulupu", "kute", "la",
            "lape", "laso", "lawa", "len", "lete", "li", "lili", "linja",
            "lipu", "loje", "lon", "luka", "lukin", "lupa", "ma", "mama",
            "mani", "meli", "mi", "mije", "moku", "moli", "monsi", "mu",
            "mun", "musi", "mute", "nanpa", "nasa", "nasin", "nena", "ni",
            "nimi", "noka", "o", "olin", "ona", "open", "pakala", "pali",
            "palisa", "pan", "pana", "pi", "pilin", "pimeja", "pini", "pipi",
            "poka", "poki", "pona", "pu", "sama", "seli", "selo", "seme", "sewi",
            "sijelo", "sike", "sin", "sina", "sinpin", "sitelen", "sona",
            "soweli", "suli", "suno", "supa", "suwi", "tan", "taso",
            "tawa", "telo", "tenpo", "toki", "tomo", "tu", "unpa", "uta",
            "utala", "walo", "wan", "waso", "wawa", "weka", "wile", "namako",
            "kin", "oko", "kipisi", "leko", "monsuta", "tonsi", "jasima",
            "kijetesantakalu", "soko", "meso", "epiku", "kokosila", "lanpan",
            "n", "misikeke", "ku", None, None, None, None, None, None, None,
            "[", "]", "_", None, None, None, None, None, None, None, None,
            None, None, None, None, None, "pake", "apeja", "majuna", "powe"]

uniList = ["󱤀", "󱤁", "󱤂", "󱤃", "󱤄", "󱤅", "󱤆", "󱤇", "󱤈", "󱤉", "󱤊", "󱤋", "󱤌", "󱤍", "󱤎",
           "󱤏", "󱤐", "󱤑", "󱤒", "󱤓", "󱤔", "󱤕", "󱤖", "󱤗", "󱤘", "󱤙", "󱤚", "󱤛", "󱤜", "󱤝",
           "󱤞", "󱤟", "󱤠", "󱤡", "󱤢", "󱤣", "󱤤", "󱤥", "󱤦", "󱤧", "󱤨", "󱤩", "󱤪", "󱤫", "󱤬",
           "󱤭", "󱤮", "󱤯", "󱤰", "󱤱", "󱤲", "󱤳", "󱤴", "󱤵", "󱤶", "󱤷", "󱤸", "󱤹", "󱤺", "󱤻",
           "󱤼", "󱤽", "󱤾", "󱤿", "󱥀", "󱥁", "󱥂", "󱥃", "󱥄", "󱥅", "󱥆", "󱥇", "󱥈", "󱥉", "󱥊",
           "󱥋", "󱥌", "󱥍", "󱥎", "󱥏", "󱥐", "󱥑", "󱥒", "󱥓", "󱥔", "󱥕", "󱥖", "󱥗", "󱥘", "󱥙",
           "󱥚", "󱥛", "󱥜", "󱥝", "󱥞", "󱥟", "󱥠", "󱥡", "󱥢", "󱥣", "󱥤", "󱥥", "󱥦", "󱥧", "󱥨",
           "󱥩", "󱥪", "󱥫", "󱥬", "󱥭", "󱥮", "󱥯", "󱥰", "󱥱", "󱥲", "󱥳", "󱥴", "󱥵", "󱥶", "󱥷",
           "󱥸", "󱥹", "󱥺", "󱥻", "󱥼", "󱥽", "󱥾", "󱥿", "󱦀", "󱦁", "󱦂", "󱦃", "󱦄", "󱦅", "󱦆",
           "󱦇", "󱦈", "󱦐", "󱦑", "󱦒", "󱦠", "󱦡", "󱦢", "󱦣", ]

wordDict = {chr(0xf1900): "a", chr(0xf1901): "akesi", chr(0xf1902): "ala", chr(0xf1903): "alasa",
            chr(0xf1904): "ale", chr(0xf1905): "anpa", chr(0xf1906): "ante", chr(0xf1907): "anu",
            chr(0xf1908): "awen", chr(0xf1909): "e", chr(0xf190a): "en", chr(0xf190b): "esun",
            chr(0xf190c): "ijo", chr(0xf190d): "ike", chr(0xf190e): "ilo", chr(0xf190f): "insa",
            chr(0xf1910): "jaki", chr(0xf1911): "jan", chr(0xf1912): "jelo", chr(0xf1913): "jo",
            chr(0xf1914): "kala", chr(0xf1915): "kalama", chr(0xf1916): "kama", chr(0xf1917): "kasi",
            chr(0xf1918): "ken", chr(0xf1919): "kepeken", chr(0xf191a): "kili", chr(0xf191b): "kiwen",
            chr(0xf191c): "ko", chr(0xf191d): "kon", chr(0xf191e): "kule", chr(0xf191f): "kulupu",
            chr(0xf1920): "kute", chr(0xf1921): "la", chr(0xf1922): "lape", chr(0xf1923): "laso",
            chr(0xf1924): "lawa", chr(0xf1925): "len", chr(0xf1926): "lete", chr(0xf1927): "li",
            chr(0xf1928): "lili", chr(0xf1929): "linja", chr(0xf192a): "lipu", chr(0xf192b): "loje",
            chr(0xf192c): "lon", chr(0xf192d): "luka", chr(0xf192e): "lukin", chr(0xf192f): "lupa",
            chr(0xf1930): "ma", chr(0xf1931): "mama", chr(0xf1932): "mani", chr(0xf1933): "meli",
            chr(0xf1934): "mi", chr(0xf1935): "mije", chr(0xf1936): "moku", chr(0xf1937): "moli",
            chr(0xf1938): "monsi", chr(0xf1939): "mu", chr(0xf193a): "mun", chr(0xf193b): "musi",
            chr(0xf193c): "mute", chr(0xf193d): "nanpa", chr(0xf193e): "nasa", chr(0xf193f): "nasin",
            chr(0xf1940): "nena", chr(0xf1941): "ni", chr(0xf1942): "nimi", chr(0xf1943): "noka",
            chr(0xf1944): "o", chr(0xf1945): "olin", chr(0xf1946): "ona", chr(0xf1947): "open",
            chr(0xf1948): "pakala", chr(0xf1949): "pali", chr(0xf194a): "palisa", chr(0xf194b): "pan",
            chr(0xf194c): "pana", chr(0xf194d): "pi", chr(0xf194e): "pilin", chr(0xf194f): "pimeja",
            chr(0xf1950): "pini", chr(0xf1951): "pipi", chr(0xf1952): "poka", chr(0xf1953): "poki",
            chr(0xf1954): "pona", chr(0xf1955): "pu", chr(0xf1956): "sama", chr(0xf1957): "seli",
            chr(0xf1958): "selo", chr(0xf1959): "seme", chr(0xf195a): "sewi", chr(0xf195b): "sijelo",
            chr(0xf195c): "sike", chr(0xf195d): "sin", chr(0xf195e): "sina", chr(0xf195f): "sinpin",
            chr(0xf1960): "sitelen", chr(0xf1961): "sona", chr(0xf1962): "soweli", chr(0xf1963): "suli",
            chr(0xf1964): "suno", chr(0xf1965): "supa", chr(0xf1966): "suwi", chr(0xf1967): "tan",
            chr(0xf1968): "taso",
            chr(0xf1969): "tawa", chr(0xf196a): "telo", chr(0xf196b): "tenpo", chr(0xf196c): "toki",
            chr(0xf196d): "tomo", chr(0xf196e): "tu", chr(0xf196f): "unpa", chr(0xf1970): "uta",
            chr(0xf1971): "utala", chr(0xf1972): "walo", chr(0xf1973): "wan", chr(0xf1974): "waso",
            chr(0xf1975): "wawa", chr(0xf1976): "weka", chr(0xf1977): "wile", chr(0xf1978): "namako",
            chr(0xf1979): "kin", chr(0xf197a): "oko", chr(0xf197b): "kipisi", chr(0xf197c): "leko",
            chr(0xf197d): "monsuta", chr(0xf197e): "tonsi", chr(0xf197f): "jasima",
            chr(0xf1980): "kijetesantakalu", chr(0xf1981): "soko", chr(0xf1982): "meso",
            chr(0xf1983): "epiku", chr(0xf1984): "kokosila", chr(0xf1985): "lanpan",
            chr(0xf1986): "n", chr(0xf1987): "misikeke", chr(0xf1988): "ku",
            chr(0xf1990): "[", chr(0xf1991): "]", chr(0xf1992): "_", chr(0xf19a0): "pake",
            chr(0xf19a1): "apeja", chr(0xf19a2): "majuna", chr(0xf19a3): "powe"}

#switches lowercase toki pona words to UCSUR unicodepoints
#leaves all other text and codepoints unchanged
def unicodify(vvod):
    vyvod = ""
    sequence = vvod.split()
    for word in sequence:
        if word in wordList:
            vyvod += (chr(0xF1900 + wordList.index(word)))
        else:
            vyvod += word + " "
    return vyvod

#switches unicode characters in the toki pona UCSUR range to the romanization of toki pona
#leaves all other text and codepoints unchanged
def uncodify(vvod):
    vyvod = ""
    sequenceA = list(vvod)
    for character in sequenceA:
        if character in uniList:
            vyvod += wordDict[character] + " "
        else:
            vyvod += character
    return vyvod

#switches unicode characters in the toki pona UCSUR range with romanized toki pona
#text or codepoints that are not in either catigory will be converted to lowercase, otherwise unchanged
def switchcodify(vvod):
    vyvod = vvod.swapcase()
    vyvod = uncodify(vyvod)
    vyvod = vyvod.swapcase()
    vyvod = unicodify(vyvod)
    vyvod = vyvod.lower()
    return vyvod

#infinite loop functional within IDLE.
#type any input to apply switchcodify to it - type exit to end program
while True: 
    j = input("\n---------------------------------------------------------" +
              "\ninput UCSUR characters, toki pona words, or anything else\n")
    if j == "exit":
        break
    n = switchcodify(j)
    print (n)
    c.copy(n) #turn clipboard functionality off by typing # at the beninning of this line
