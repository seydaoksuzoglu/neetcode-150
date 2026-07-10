# 2. Valid Anagram | Arrays & Hashing
# Anagram sorularında sıralama (order) önemsizdir.
# Sadece harf miktarı (frekans) önemlidir. 
# İki farklı diziyi (string/liste) birebir karşılaştırırken iç içe döngü kurmak genellikle
# mantık hatasına veya performans kaybına yola açar.
# Frekans sayımı (Counter/Hash Map) her zaman daha güvenlidir. 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        countS = Counter(s)
        countT = Counter(t)

        if countS == countT:
            return True

        return False
    
# --- İlk kendi çözümüm
# Buradaki benim mantık hatam "anagram" kelimelerin ters yazılışı değildir.
# Bu iki kelimenin sadece birbirinin tam tersi (palindromik yapı) olup olmadığını kontrol eder.
# s = "rat" ve t = "tar" olsun. t[::-1] yaptığında "rat" olur. Kod bunu yakalar ve True döner.
# Ana anagramda harflerin sayısı rastgeledir. 
# Ayrıca iç içe döngüler performansı düşürür. (O(n^2)) zaman karmaşıklığı yaratır.

#for i in s:
#for j in t[::-1]:
    #if i != j:
        #return False
#return True
