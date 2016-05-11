pocz = 0
paki = 50
konto = 0
wplacone = 2500
do_zarobienia = 250
lacznie = wplacone + do_zarobienia

licznik = 55
p_licznik = 55

print "wplacono: " + str(wplacone)
for i in range(1, 201):

	print "dzien " + str(i) + ": konto=" + str(konto) + ", adpaki=" + str(paki) + ", wplynie jeszcze=" + str(
		lacznie) + " w ciagu ok. " + str(lacznie / paki) + " dni"

	konto = konto + paki
	lacznie = lacznie - paki

	if konto >= 50:
		do_inw = konto - (konto % 50)
		konto = konto - do_inw
		lacznie = lacznie + do_inw
		nowe_paki = do_inw / 50
		do_zarobienia = nowe_paki * 5
		paki = paki + nowe_paki
		lacznie = lacznie + do_zarobienia

	licznik = licznik - 1
	if licznik == 0:
		paki = paki - 1
		licznik = 55
	p_licznik = p_licznik - 1
	if p_licznik == 0:
		paki = paki - 50
		p_licznik = 999999