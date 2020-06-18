class KutuphaneObj:

    def __init__(self, id, isim, yazar, tur, yayin_tarihi, tam_fiyat):
        self.id = id
        self.isim = isim
        self.yazar = yazar
        self.tur = tur
        self.yayin_tarihi = yayin_tarihi
        self.tam_fiyat = tam_fiyat

    def __str__(self):
        return "[{}]\t{}\n\t\tyazar = {}\n\t\ttur = {}\n\t\tyayin_tarihi = {}\n\t\ttam_fiyat = {}"\
            .format(self.id,
                    self.isim,
                    self.yazar,
                    self.tur,
                    self.yayin_tarihi,                  
                    self.tam_fiyat)

# return "[{}]\t{}\n\tyazar = {}\n\ttur = {}\n\t\tyayin_tarihi = {}\n\t\ttam_fiyat = {}"\
     #   return "Kitap İsmi: {}\nYazar: {}\nYayinevi: {}\nTür: {}\nBaski: {}\n".format(self.isim,self.yazar,self.yayinevi,self.tür,self.baski)


