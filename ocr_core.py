import operator

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core1(filename):
    pytesseract.pytesseract.tesseract_cmd = (
        r'C:\Program Files\Tesseract-OCR\tesseract.exe')

    text = pytesseract.image_to_string(Image.open(filename))

    return text


def ocr_core2(filename):
    pytesseract.pytesseract.tesseract_cmd = (
        r'C:\Program Files\Tesseract-OCR\tesseract.exe')

    text = pytesseract.image_to_string(Image.open(filename))
    text = text.strip()
    text_lines = text.split('\n')
    while '' in text_lines:
        text_lines.remove('')
    while ' ' in text_lines:
        text_lines.remove(' ')
    result = ""
    for line, text in enumerate(text_lines):

        result = result + (str(line+1) + ": " + text + "\n")

    return result


def ocr_core3(filename):
    pytesseract.pytesseract.tesseract_cmd = (
        r'C:\Program Files\Tesseract-OCR\tesseract.exe')

    text = pytesseract.image_to_string(Image.open(filename))
    text = text.strip().lower()
    words = text.split()
    while '' in words:
        words.remove('')
    while ' ' in words:
        words.remove(' ')
    number_repeated_word = []
    for w in words:
        number_repeated_word.append(words.count(w))
    list_words_frequency = list(zip(words, number_repeated_word))
    list_without_rw = []
    for i in list_words_frequency:
        if i not in list_without_rw:
            list_without_rw.append(i)
    d = dict(list_without_rw)
    d_sort = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    d_sort = d_sort[0:7]
    dnew = dict(d_sort)
    list_result = list(dnew.keys())
    print(list_result)
    return (str(list_result)).replace("'"," ").replace("[","").replace("]","")


def ocr_core4(filename):
    pytesseract.pytesseract.tesseract_cmd = (
        r'C:\Program Files\Tesseract-OCR\tesseract.exe')

    text = pytesseract.image_to_string(Image.open(filename))
    text = text.strip().lower()
    words = text.split()
    while '' in words:
        words.remove('')
    while ' ' in words:
        words.remove(' ')
    number_repeated_word = []
    for w in words:
        number_repeated_word.append(words.count(w))
    list_words_frequency = list(zip(words, number_repeated_word))
    list_without_rw = []
    for i in list_words_frequency:
        if i not in list_without_rw:
            list_without_rw.append(i)
    list_without_rw.sort()
    ll=str(list_without_rw)
    ll='\n'.join(ll.split(")"))

    #return (str(list_without_rw)).replace("'"," ").replace("[","").replace("]","")
    return ll.replace("'"," ").replace("[","").replace("]","").replace("(","").replace(","," ")



