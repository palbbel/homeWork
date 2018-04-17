plates = int(input())
detergent = float(input())
for plate in list(range(plates)):
    plate += 1
    detergent -= 0.5
    if 0 < detergent < 0.5 or (plate < plates and detergent == 0):
        plates = plates - plate
        print('Моющее средство закончилось. Осталось %s тарелок' %(plates))
        break
    elif detergent < 0:
        print('Моющее средство закончилось. Осталось %s тарелок' %(plates))
        break
    elif plate == plates and detergent == 0:
        print('Все тарелки вымыты, моющее средство закончилось')
    elif plate == plates and detergent > 0:
        print('Все тарелки вымыты. Осталось %.1f ед. моющего средства' %(detergent))
if plates == 0 and detergent != 0:
    print('Все тарелки вымыты. Осталось %.1f ед. моющего средства' % (detergent))
if plates == 0 and detergent == 0:
    print('Все тарелки вымыты, моющее средство закончилось')







