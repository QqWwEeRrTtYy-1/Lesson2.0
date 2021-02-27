import string

def is_palindrom(pal_text: str):
	pal_text_transformation = pal_text.upper()
	pal_text_without_signs = pal_text_transformation.translate(str.maketrans('', '', string.punctuation)).replace(" ", "")
	pal_text_letter = list(pal_text_without_signs)
	pal_text_letter_reversed = list(reversed(pal_text_without_signs))

	return pal_text_letter == pal_text_letter_reversed

finish = is_palindrom("То-п,о.т !")
print(finish)