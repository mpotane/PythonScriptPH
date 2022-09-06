from langdetect import detect

# Get user input
text = input("I-type ang kahit anong mga salitang ginagamit sa wika na ito: ")

# Detect the language used from text
lang = detect(text) 
match lang:
    case 'en':
        print("Ang ginamit na wika ay wikang 'Ingles'.")
    case 'tl':
        print("Ang ginamit na wika ay wikang 'Tagalog'.")
    case other:
        print(f"'{lang}' Ang wika na ginamit.\nHanapin ang ISO code ng wikang ginamit sa link na ito https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes.")