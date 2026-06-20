# online_sales_analysis
online sales analysis
# Online Sales Analysis

## Opis projekta
Projekat simulira sistem za upravljanje online prodajom koristeći Python i Git.  
Kroz više faza implementirane su klase za proizvode, menadžment inventara i korpu kupca, uz primenu Git grana, spajanja i rešavanja konflikata.

## Struktura projekta
- `product.py` – klasa **Product** sa atributima `name`, `price`, `quantity` i metodama za prikaz i ažuriranje količine.
- `product_manager.py` – klasa **ProductManager** koja upravlja listom proizvoda, dodavanjem, prikazom i ukupnom vrednošću inventara.
- `cart.py` – klasa **Cart** za upravljanje korpom kupca (dodavanje proizvoda, računanje ukupne vrednosti, prikaz sadržaja).
- `main.py` – glavni program koji povezuje sve klase i demonstrira funkcionalnosti.
- `.gitignore` – ignoriše poverljive fajlove (`config.json`) i snimke ekrana.
- `README.md` – opis projekta i uputstvo za korišćenje.

## Funkcionalnosti
- Dodavanje i ažuriranje proizvoda.
- Upravljanje inventarom i računanje ukupne vrednosti.
- Upravljanje korpom kupca sa slučajnim izborom proizvoda.
- Git verzionisanje: kreiranje grana, spajanje, rešavanje konflikata.
- Ignorisanje poverljivih podataka i privremenih fajlova.

## Pokretanje
Pokreni glavni program:
```bash
python main.py