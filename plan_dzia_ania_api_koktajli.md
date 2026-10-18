# Roadmapa Projektu - API Koktajli (Django)

## Etap 1: Przygotowanie środowiska pracy
- [X] Załóż na pulpicie nowy folder o nazwie np. `solvro_cocktails`.
- [X] Otwórz ten folder w swoim edytorze kodu (najlepiej Visual Studio Code).
- [X] Otwórz terminal wewnątrz edytora (w VS Code: Terminal -> New Terminal).
- [X] Utwórz wirtualne środowisko komendą: `python -m venv venv`.
- [X] Aktywuj wirtualne środowisko.
- [X] Zainstaluj potrzebne biblioteki wpisując w terminal: `pip install django djangorestframework pillow`. *(Uwaga: Pillow jest potrzebne, by móc zapisywać zdjęcia składników)*.
- [X] Zapisz listę zainstalowanych bibliotek do pliku: `pip freeze > requirements.txt`.

## Etap 2: Inicjalizacja projektu Django
- [ ] Wygeneruj główny szkielet projektu komendą: `django-admin startproject core .` (nie zapomnij o kropce na końcu!).
- [ ] Stwórz "aplikację" (moduł), w którym napiszemy nasz kod: `python manage.py startapp api`.
- [ ] Otwórz plik `core/settings.py`. Znajdź listę `INSTALLED_APPS` i dopisz do niej na samym końcu dwie linijki: `'rest_framework',` oraz `'api',`.
- [ ] Skonfiguruj foldery na zdjęcia: na samym dole pliku `core/settings.py` dodaj ustawienia `MEDIA_URL` i `MEDIA_ROOT`.

## Etap 3: Baza Danych i Modele
- [ ] Otwórz plik `api/models.py`.
- [ ] Utwórz klasę `Ingredient` (Składnik). Dodaj pola: `name` (CharField), `description` (TextField), `is_alcoholic` (BooleanField), `image` (ImageField).
- [ ] Utwórz klasę `Cocktail` (Koktajl). Dodaj pola: `name` (CharField), `category` (CharField), `instructions` (TextField).
- [ ] Utwórz klasę `RecipeIngredient` (Proporcje). To będzie łącznik! Dodaj pola: `cocktail` (ForeignKey), `ingredient` (ForeignKey), `amount` (CharField - np. na tekst "50 ml").
- [ ] Otwórz terminal i powiedz Django, by przygotowało tłumaczenie dla bazy danych: `python manage.py makemigrations`.
- [ ] Zapisz te modele do bazy SQLite: `python manage.py migrate`.

## Etap 4: Panel Administratora (Bonus dla wygody)
- [ ] Otwórz plik `api/admin.py`.
- [ ] Zarejestruj w nim swoje modele (Ingredient, Cocktail, RecipeIngredient), aby móc je wyklikać w przeglądarce.
- [ ] W terminalu stwórz głównego administratora komendą: `python manage.py createsuperuser` (podaj login, email i hasło).
- [ ] Uruchom serwer `python manage.py runserver`, wejdź na `http://127.0.0.1:8000/admin` i sprawdź, czy możesz dodać pierwszy składnik ręcznie!

## Etap 5: Serializatory (Tłumacze na JSON)
- [ ] Utwórz nowy plik w folderze aplikacji: `api/serializers.py`.
- [ ] Napisz `IngredientSerializer` (który zamieni model Ingredient na format JSON).
- [ ] Napisz `RecipeIngredientSerializer` (do tłumaczenia proporcji).
- [ ] Napisz `CocktailSerializer` (najtrudniejszy punkt - musi zawierać w sobie listę `RecipeIngredientSerializer`, żeby podając przepis, wypisało od razu wszystkie jego składniki i miarki).
- [ ] Dodaj prostą walidację w serializatorach (np. sprawdzenie, czy nazwa koktajlu nie jest zbyt krótka).

## Etap 6: Paginacja (Dzielenie na strony)
- [ ] Otwórz `core/settings.py`.
- [ ] Dodaj sekcję `REST_FRAMEWORK` i ustaw w niej globalną paginację (np. `PageNumberPagination`) z limitem np. 10 wyników na stronę.

## Etap 7: Widoki (Logika API)
- [ ] Otwórz plik `api/views.py`.
- [ ] Użyj narzędzia `ModelViewSet` z DRF, aby napisać `IngredientViewSet`. (ModelViewSet automatycznie wygeneruje za Ciebie cały CRUD!).
- [ ] Napisz `CocktailViewSet` w ten sam sposób.

## Etap 8: Adresy URL (Endpointy)
- [ ] Utwórz plik `api/urls.py`.
- [ ] Użyj `DefaultRouter` z DRF, aby automatycznie wygenerować adresy URL dla składników i koktajli.
- [ ] Otwórz główny plik `core/urls.py` i podłącz do niego zrobiony przed chwilą `api/urls.py` (dodając ścieżkę zaczynającą się od `api/`).
- [ ] W `core/urls.py` dodaj linijkę, która pozwoli przeglądarce wyświetlać wgrane zdjęcia w trybie developerskim (tzw. dopięcie `static`).

## Etap 9: Testowanie
- [ ] Uruchom serwer (`python manage.py runserver`).
- [ ] Wejdź na `http://127.0.0.1:8000/api/ingredients/` - sprawdź, czy możesz dodać składnik (Django udostępnia fajny panel w przeglądarce do testowania).
- [ ] Wejdź na `http://127.0.0.1:8000/api/cocktails/` - dodaj pierwszy przepis!
- [ ] Sprawdź, czy działa usuwanie i edycja obiektów.

## Etap 10: "Nice to have" (Opcjonalnie na koniec)
- [ ] Dodaj filtrowanie (np. django-filter), by móc wyszukiwać np. tylko bezalkoholowe składniki.
- [ ] Dodaj dokumentację Swagger/OpenAPI (za pomocą biblioteki `drf-spectacular` lub `drf-yasg`).
- [ ] Zamień bazę SQLite na PostgreSQL (będzie wymagało instalacji np. Dockera i biblioteki `psycopg2`).