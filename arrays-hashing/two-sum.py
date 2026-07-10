# 3. Two Sum | Arrays & Hashing
# Aslında benim çözümüm doğru fakat ana problem time complexity O(n^2) olması. Çünkü nested loop var.
# Evet elim nested loop a çok yatkın fakat bu da performans açısından verimsiz oluyor. 
# n <= 1000, olduğunda çalışır fakat mülakatlarda daha hızlı çözüm bekleniyor.

# Daha iyi bir yaklaşım: hash map kullanmak. Şimdiye kadar gördüğümüz sayıları ve indeksleri saklamak için bir hash map haritası kullanmalıyız.
# complement = target - num hesapla. complement zaten map in içindeyse iki index döner.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Boş sözlük eleman arama hızı neredeyse anındadır.

        for i, num in enumerate(nums): # enumerate fonksiyonu bize dizideki elemanları dönerken aynı anda hem o elemanın indeksini döndürür.
            complement = target - num # A + B = target ise biz şu an A'daysak bize B lazım onu hesaplar.
            if complement in seen: # complement seen de varsa complement'in indeksi ve i döner.
                return [seen[complement], i]
            seen[num] = i # Eğer aradığımız complement seen de yoksa, mevcut sayıyı key, value olarak sözlüğe yazarız ki sonraki sayılar dönüp bize bakabilsin.

# Benim çözümüm time complexity var O(n^2)
"""
for i in range(len(nums)):
    for j in range(len(i+1, nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
"""