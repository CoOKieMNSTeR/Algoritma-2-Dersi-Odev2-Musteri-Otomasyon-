class HesaplamaObj:

    def __init__(self, id, musteri_id, kutuphane_id, cikis_tarihi, vadesi, cezasi, toplam_ceza, islem_tipi):
        self.id = id
        self.musteri_id = musteri_id
        self.kutuphane_id = kutuphane_id
        self.cikis_tarihi = cikis_tarihi
        self.vadesi = vadesi
        self.cezasi = cezasi
        self.toplam_ceza = toplam_ceza
        self.islem_tipi = islem_tipi

    def __str__(self):
        return "ID = {}\n\t\tmusteri_id = {}\n\t\tkutuphane_id = {}\n\t\tcikis_tarihi = {}\n\t\tvadesi = {}\n\t\tceza = {}\n\t\ttoplam_ceza = {}\n\t\tislem_tipi = {}"\
            .format(self.id,
                    self.musteri_id,
                    self.kutuphane_id,
                    self.cikis_tarihi,
                    self.vadesi,
                    self.cezasi,
                    self.toplam_ceza,
                    self.islem_tipi)
