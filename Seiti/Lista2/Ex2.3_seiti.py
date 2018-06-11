def horas(h):
	if (h>12):
		h = h-12
	return h
def fim(f):
	if (f >= 12):
		return " P.M"
	else:
		return " A.M"
i=1
while (i>0):
	h = input("digite a hora: ")
	m = input("digite os minutos: ")
	if(h>=0 and h<24 and m>=0 and m<60):
	
		if (h < 12):
			print "Sao ", horas(h), ":",  m, fim(h)
			
		elif (h==12):
			print "Sao ", horas(h), ":",  m,  fim(h)
		else:
			print "Sao ",  horas(h),  ":",  m,  fim(h)
	else:
		print("ERRO")
		exit()