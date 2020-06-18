class MusteriObj:

    def __init__(self, musteri_id, adi, soyadi):
       self.musteri_id = musteri_id
       self.adi = adi
       self.soyadi = soyadi
        

    def __str__(self):
        return "[{}] {} {}".format(self.musteri_id, self.adi, self.soyadi)
