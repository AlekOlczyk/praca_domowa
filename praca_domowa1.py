imie_odbiorcy = input("Podaj imie solenizanta/ solenizantki: ")

rok_urodzenia = int(input("Podaj rok urodzenia solenizanta/ solenizantki: "))

wiadomosc = input("Napisz wiadomość dla solenizanta/ solenizantki: ")

imie_nadawcy = input("Podaj swoje imię: ")

wiek_solenizanta = 2024 - rok_urodzenia

print(f"Witaj {imie_odbiorcy}! \nWszystkiego najlepszego z okazji {wiek_solenizanta} urodzin! \n{wiadomosc} \n{imie_nadawcy}")
