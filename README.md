```markdown
# 🔐 BLAKE3 XOF Generator
```
> **Narzędzie do generowania rozszerzalnych hashy Blake3 (XOF)**  
> **Wersja:** 1.0 | **Autor:** Łukasz Wójcik | **Rok:** 2025

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Blake3](https://img.shields.io/badge/Algorithm-BLAKE3-orange.svg)](https://www.blake3.io/)

Skrypt Python wykorzystujący bibliotekę `blake3` do generowania **Extendable Output Function (XOF)**. 
W przeciwieństwie do tradycyjnych hashy (np. SHA-256), Blake3 XOF pozwala na wygenerowanie digestu o dowolnej długości. 
Narzędzie zapisuje wynik w formacie Base64 do pliku `.b3x` oraz wyświetla go w konsoli.

---

## ✨ Funkcje

✅ **Blake3 XOF** – generowanie hashy o dowolnej długości (nie tylko fixed-size)  
✅ **Konfigurowalna długość** – domyślnie 256 bajtów (2048 bitów), możliwość zmiany  
✅ **Encoding Base64** – czytelny zapis wyniku w pliku tekstowym  
✅ **Automatyczne nazewnictwo** – plik wyjściowy otrzymuje rozszerzenie `.b3x`  
✅ **Obsługa błędów** – informowanie o brakujących plikach i exceptionach  
✅ **Szybkość** – Blake3 jest szybszy od MD5, SHA-1, SHA-2 i SHA-3  
✅ **Bezpieczeństwo** – kryptograficznie bezpieczny algorytm hashowania  

---

## 🛠 Wymagania

- Python 3.7+
- Biblioteka `blake3` (oficjalne bindingi Python)
- Dostęp do systemu plików (odczyt/zapis)

### Instalacja zależności

```bash
pip install blake3
```

---

## 📦 Instalacja

```bash
# 1. Sklonuj repozytorium
git clone https://github.com/lukaszwojcikdev/blake3-xof-gen.git
cd blake3-xof-gen

# 2. Zainstaluj zależności
pip install -r requirements.txt

# 3. Uruchom skrypt
python blake3_xof.py <nazwa_pliku> [dlugosc_w_bajtach]
```

---

## 🚀 Użycie

### Tryb podstawowy (Domyślna długość 256 bajtów)

```bash
python blake3_xof.py moj_plik.txt
```

### Tryb zaawansowany (Własna długość hasha)

```bash
# Generuje hash o długości 512 bajtów (4096 bitów)
python blake3_xof.py moj_plik.txt 512
```

### Wyjście

Skrypt generuje plik `<nazwa_pliku>.b3x` zawierający hash w kodowaniu Base64.

---

## 📄 Przykład wyjścia (Konsola)

```
--- Wynik ---
Plik wejściowy: moj_plik.txt
Długość hasha: 2048 bitów (256 bajtów)
Hash (Base64): 8J+YgyYx... (długi ciąg znaków)
Zapisano do: moj_plik.b3x
-------------
```

### Przykład zawartości pliku `.b3x`

```text
8J+YgyYxKz5vN2mP9qL... (ciąg Base64)
```

---

## 🧠 Dlaczego Blake3 XOF?

Tradycyjne funkcje hashujące (jak SHA-256) zwracają wynik o stałej długości (np. 32 bajty). **Blake3 XOF** (Extendable Output Function) pozwala na wygenerowanie strumienia bajtów o **dowolnej długości**.

| Cecha | SHA-256 | Blake3 XOF |
|-------|---------|------------|
| Długość wyjścia | Stała (256 bitów) | Dowolna (np. 2048, 4096 bitów) |
| Wydajność | Szybki | Bardzo szybki (wielowątkowy) |
| Zastosowanie | Integralność danych | Derivacja kluczy, RNG, fingerprinting |

---

## ⚙️ Parametry funkcji

| Parametr | Typ | Opis |
|----------|-----|------|
| `input_filename` | `str` | Ścieżka do pliku, który ma zostać zhashowany |
| `output_length` | `int` | Długość hasha w bajtach (domyślnie 256) |

---

## 📂 Struktura projektu

```
.
├── blake3_xof.py       # Główny skrypt
├── requirements.txt    # Dependencje Python
├── README.md           # Dokumentacja
└── LICENSE             # Licencja
```

---

## 🤝 Wkład w projekt

Pull requesty są mile widziane! Przed wysłaniem:

1. Fork repozytorium
2. Utwórz branch (`git checkout -b feature/NowaFunkcja`)
3. Commit zmian (`git commit -m 'Dodaj nową funkcję'`)
4. Push (`git push origin feature/NowaFunkcja`)
5. Otwórz Pull Request

---

## 📜 Licencja

Projekt dostępny na licencji **MIT** – zobacz plik [LICENSE](LICENSE) po szczegóły.

---

## 🧑‍💻 Autor

**Łukasz Wójcik**  
🔗 GitHub: [lukaszwojcikdev](https://github.com/lukaszwojcikdev)  

> 💬 *"Kryptografia to sztuka ukrywania informacji w pełnym świetle."*

---

## ⚠️ Disclaimer

Narzędzie przeznaczone jest do celów **edukacyjnych i badawczych**. Autor nie ponosi odpowiedzialności za wykorzystanie oprogramowania w sposób niezgodny z prawem. Upewnij się, że masz prawo do hashowania przetwarzanych plików.

---

> 🌟 **Podoba Ci się projekt?** Daj ⭐ na GitHubie – to motywuje do dalszego rozwoju!
```
