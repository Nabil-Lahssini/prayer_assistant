class Prayer:
    def __init__(self, fajr, dhor, asr, maghreb, icha, date):
        self.fajr = fajr
        self.dhor = dhor
        self.asr = asr
        self.maghreb = maghreb
        self.icha = icha
        self.date = date
    
    def show(self):
        string = f"Date : {self.date} \nFajr : {self.fajr} \nDhor: {self.dhor} \nAsr : {self.asr}\nMaghreb : {self.maghreb} \nIcha : {self.icha}"
        return string