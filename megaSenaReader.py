import json

with open("sorteios.json") as s:
	sorteios = json.load(s)

#print(sorteios)
# sorteios = [
# {
# 	"sorteio": "1",
# 	"dezenas": ["03", "03", "04", "03", "30", "33"],
# 	"data_sorteio": "11/03/1996"
# },
# {
# 	"sorteio": "2",
# 	"dezenas": ["01", "02", "04", "52", "30", "33"],
# 	"data_sorteio": "11/03/2001"
# }
# ]


def getAno(sorteio):
	data = sorteio["data_sorteio"]
	return int(data.split("/")[2])


def getSorteiosPorPeriodoAno(sorteios, inicio, fim):
	sorteios_do_periodo = []

	for sorteio in sorteios:
		ano = getAno(sorteio)
		if(ano >= inicio and ano <= fim):
			sorteios_do_periodo.append(sorteio)

	return sorteios_do_periodo


def getOcorrenciaDezena(sorteios, dezena):
	ocorrencia = 0

	for sorteio in sorteios:

		for dez in sorteio["dezenas"]:

			if(dez == dezena):
				ocorrencia += 1

	# Retira 1,pois seria a propria ocorrencia
	return ocorrencia - 1


def getDezenasMaisRepetidas(sorteios):

	dezenas_repetidas = []

	for sorteio in sorteios:

		for dez in sorteio["dezenas"]:	

			dezena = {
				"numero": dez,
				"ocorrencias": getOcorrenciaDezena(sorteios, dez)
			}

			if not dezena in dezenas_repetidas:
				dezenas_repetidas.append(dezena)

	dezenas_repetidas = sorted(dezenas_repetidas, key=lambda dezena: dezena["ocorrencias"])
	dezenas_repetidas.reverse()

	return dezenas_repetidas


def getDezenasMaisSortidas(dezenas):
	dezenas_premiadas = []

	for i in range(0, 6):
		dezenas_premiadas.append(dezenas[i]["numero"])

	dezenas_premiadas.sort()

	return dezenas_premiadas


def getTotalOcorrencias(dezenas):
	total = 0

	for dezena in dezenas:
		total += dezena["ocorrencias"]

	return total


def getMediaOcorrencias(dezenas, total):
	return total / len(dezenas)


def getVarianciaOcorrencias(dezenas, media):
	variancia = 0
	for dezena in dezenas:
		variancia += (dezena["ocorrencias"] - media)**2

	return variancia / len(dezenas)


def getDesvioPadrao(variancia):
	return variancia ** (1/2)


sorteios = getSorteiosPorPeriodoAno(sorteios, 2010, 2018)

dezenas = getDezenasMaisRepetidas(sorteios)

total = getTotalOcorrencias(dezenas)

media = getMediaOcorrencias(dezenas, total)

variancia = getVarianciaOcorrencias(dezenas, media)

desvio = getDesvioPadrao(variancia)

print(dezenas)
print('media:', media)
print('variancia:', variancia)
print('desvio:', desvio)

dezenas_premiada = getDezenasMaisSortidas(dezenas)

print(dezenas_premiada)