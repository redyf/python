class Datas:
    def __init__(self, data):
        self.data = data

    def data_formatada(self, data):
        data = self.data

        if "," in data:
            data = self.data.replace(",", "/")
        elif "-" in data:
            data = self.data.replace("-", "/")
        elif " " in data:
            data = self.data.replace(" ", "/")
        elif "." in data:
            data = self.data.replace(".", "/")

        print(data)


data = Datas("11,08,1994")
data2 = Datas("11-08-1994")
data3 = Datas("11 08 1994")
data4 = Datas("11.08.1994")

data.data_formatada(data)
data2.data_formatada(data)
data3.data_formatada(data)
data4.data_formatada(data)
