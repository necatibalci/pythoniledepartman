import numpy as np               
import matplotlib.pyplot as plt  


np.random.seed(42)


maaslar = np.random.randint(3000, 15001, size=500)


departmanlar = np.random.choice([1, 2, 3], size=500)


ortalama = np.mean(maaslar)      
maksimum = np.max(maaslar)        
minimum = np.min(maaslar)         


print("Genel Maaş İstatistikleri")
print(f"Ortalama Maaş : {ortalama:.2f} TL")
print(f"Maksimum Maaş : {maksimum} TL")
print(f"Minimum Maaş  : {minimum} TL\n")


departman_etiketleri = {
    1: "Mühendislik",
    2: "Muhasebe",
    3: "Pazarlama"
}


print("Departmanlara Göre Ortalama Maaşlar:")
for dep in [1, 2, 3]:
    maaslar_dep = maaslar[departmanlar == dep]   
    ortalama_dep = np.mean(maaslar_dep)          
    print(f"{departman_etiketleri[dep]}: {ortalama_dep:.2f} TL ({len(maaslar_dep)} kişi)")


plt.figure(figsize=(10, 6))  
plt.hist(maaslar, bins=20, color='orange', edgecolor='black')  
plt.title('500 Çalışanın Maaş Dağılımı')  
plt.xlabel('Maaş (TL)')                  
plt.ylabel('Çalışan Sayısı')             
plt.grid(True, linestyle='--', alpha=0.6) 
plt.tight_layout()                        
plt.show()                                
