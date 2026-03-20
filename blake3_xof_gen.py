import sys                     # Moduł do obsługi argumentów wiersza poleceń
import os                      # Moduł do operacji na plikach i ścieżkach
import blake3                  # Biblioteka implementująca algorytm BLAKE3
import base64                  # Moduł do kodowania Base64

# Klasa przechowująca kody kolorów ANSI do kolorowego tekstu w terminalu
class Colors:
    Purple      = "\033[95m"   # Kolor fioletowy
    LightOrange = "\033[93m"   # Jasny pomarańczowy
    LightGreen  = "\033[92m"   # Jasny zielony
    LightRed    = "\033[91m"   # Jasny czerwony
    Reset       = "\033[0m"    # Reset kolorów

# Banner ASCII wyświetlany przy uruchomieniu programu
BLAKE3_XOF_BANNER = rf"""{Colors.Purple}
┳┓┓ ┏┓┓┏┓┏┓┏┓    ┏┓┏┓┏┓┏┓  ┏┓┏┓┳┓
┣┫┃ ┣┫┃┫ ┣  ┫     ┃┃ ┃┃┣   ┃┓┣ ┃┃
┻┛┗┛┛┗┛┗┛┗┛┗┛    ┗┛┗┛┗┛┻   ┗┛┗┛┛┗
{Colors.Reset}
{Colors.LightOrange}
> BLAKE3 XOF Generator v1.2
> Extendable Output Functions
> (c) by Łukasz Wójcik 2026
> MIT license
> Github: https://github.com/lukaszwojcikdev/blake3-xof-generator
{Colors.Reset}"""

# Domyślna długość wyjściowa hasha: 256 bajtów (2048 bitów)
DEFAULT_OUTPUT_LENGTH = 256 

# Funkcja generująca hash BLAKE3 XOF
def generate_blake3_xof(input_filename, output_length=DEFAULT_OUTPUT_LENGTH):
    try:
        # Wczytanie pliku wejściowego w trybie binarnym
        with open(input_filename, 'rb') as f:
            data = f.read()                              # Odczyt całej zawartości pliku

        # Tworzenie obiektu haszującego BLAKE3
        hasher = blake3.blake3()
        hasher.update(data)                              # Aktualizacja hashera danymi z pliku
        hash_bytes = hasher.digest(length=output_length) # Generowanie XOF o zadanej długości

        # Kodowanie wyniku do Base64 (łatwiejsze do odczytu i zapisu)
        hash_base64 = base64.b64encode(hash_bytes).decode('utf-8')

        # Tworzenie nazwy pliku wyjściowego (zastępuje rozszerzenie na .b3x)
        base_name = os.path.splitext(input_filename)[0]  # Usuwa rozszerzenie
        output_filename = f"{base_name}.b3x"             # Dodaje nowe rozszerzenie

        # Zapis zakodowanego hasha do pliku tekstowego
        with open(output_filename, 'w') as f:
            f.write(hash_base64)

        # Wyświetlanie informacji o wyniku w kolorach
        print(f"\n--- Wynik ---")
        print(f"{Colors.LightGreen}Plik wejściowy:{Colors.Reset} {input_filename}")
        print(f"{Colors.LightGreen}Długość hasha:{Colors.Reset} {Colors.LightRed}{output_length*8} bitów ({output_length} bajtów){Colors.Reset}")
        print(f"{Colors.LightGreen}Hash (Base64):{Colors.Reset} {hash_base64}")
        print(f"{Colors.LightGreen}Zapisano do:{Colors.Reset} {output_filename}")
        print(f"-------------")

        return output_filename                                  # Zwraca nazwę pliku wyjściowego

    except FileNotFoundError:
        
        # Obsługa błędu: plik nie istnieje
        print(f"{Colors.LightRed}Błąd:{Colors.Reset} Plik '{input_filename}' nie istnieje.")
        return None

    except Exception as e:
        print(f"{Colors.LightRed}Błąd:{Colors.Reset} {str(e)}") # Obsługa innych błędów
        return None

# Główna część programu
if __name__ == "__main__":              
    
    print(BLAKE3_XOF_BANNER)            # Wyświetlenie bannera
    if len(sys.argv) < 2:               # Sprawdzenie, czy podano argumenty
        
                                        # Brak pliku wejściowego – wyświetlenie instrukcji
        print(f"{Colors.LightGreen}Użycie:{Colors.Reset} python blake3_xof_gen.py <plik_wejsciowy>")
        print(f"{Colors.LightGreen}Przykład:{Colors.Reset} python blake3_xof_gen.py test.bin")
        sys.exit(1)                     # Zakończenie programu z kodem błędu
    
    input_file = sys.argv[1]            # Pierwszy argument: nazwa pliku wejściowego
    output_len = DEFAULT_OUTPUT_LENGTH  # Domyślna długość wyjściowa
    
    # Obsługa opcjonalnego argumentu długości hasha
    if len(sys.argv) > 2:
        try:
            output_len = int(sys.argv[2])                 # Konwersja argumentu na liczbę
            if output_len <= 0:
                raise ValueError("Długość musi być > 0")  # Wymuszenie poprawnej wartości
        except ValueError as e:
            
            # Obsługa błędnej wartości długości
            print(f"{Colors.LightRed}Błąd:{Colors.Reset} Nieprawidłowa długość '{sys.argv[2]}': {e}")
            sys.exit(1)
    
    # Wywołanie funkcji generującej hash
    generate_blake3_xof(input_file, output_len)
