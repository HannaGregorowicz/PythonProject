# PythonProject

Raport I

Planuję zrobić stronę internetową na temat kuchni.
Będą przepisy, polecane restauracje w okolicy. Będzie to strona w formie bloga, więc tylko administrator będzie dodawać przepisy.

Wykorzystam framework Django.
Do strony zostanie "wbudowana" baza danych w sqlite3.
W Django znajdują się dwa pliki - models.py oraz admin.py. Jeden z nich tworzy bazę danych natomiast drugi pozwala na administrowanie nią. Samo zarządzanie bazą danych typu dodowanie nowych przepisów będzie odbywało się poprzez request.

Z kolei jeśli chodzi o restauracje w okolicy - "okolicą" będzie najbliższe 20 lokali od podanej przez użytkownika (!) lokalizacji. Uznałam, że pobieranie lokalizacji przez adres IP byłoby niefunkcjonalne w przypadku, gdyby użytkownik na przykład planował znaleźć jakieś restauracje w nowym, nieznanym miejscu, w którym będzie się znajdować np. następnego dnia. Wykorzystam do tego API google z tej strony: https://developers.google.com/places/


Raport II

Utworzyłam pliki projektu w Django. Zrobiłam już model bazy danych dla przepisów, znajduje się on w pliku models.py i przekształciłam go na bazę możliwą do obsługi w sqlite3, dodałam też do niej dwa przykładowe obiekty na próbę. W tej chwili zajmuję się pierwszą podstroną (/recipes - blog z przepisami). Na tą chwilę powstało już odwołanie do niej w pliku urls.py. W najbliższym czasie będę się zajmować wstępnym zarysem front-endu oraz wykorzystaniem tej bazy danych bezpośrednio na stronie. Na tą chwilę założenia projektu pozostają niezmienne.


Raport III

Od prototypu utworzony został cały system rejestracji nowych użytkowników oraz logowania już istniejących. Użytkownicy mają również możliwość dodawania własnych przepisów do bazy danych. W chwili obecnej zostały mi do końca jedynie opcje dodawania komentarzy, wyszukiwania słów kluczowych na stronie, opcjonalnie, jeżeli wystarczy czasu, system oceniania przepisów w skali 1-10, a także doszlifowanie front-endu i dodanie większej liczby przepisów do bazy danych, żeby strona nie była "pusta". :)
Postanowiłam zrezygnować z google api, ponieważ nie do końca komponowałoby się to z treścią strony, a także częściowo z braku czasu. Zamiast tego postanowiłam pójść bardziej w stronę społeczności jak właśnie wyżej wymienione komentarze, oceny i tym podobne.
