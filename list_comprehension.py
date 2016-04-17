__author__ = 'nikhil'


def comp():
    sent = "Hello there i am python"
    words = sent.split()
    word_len = []
    for word in words:
        if not word == "there":
            word_len.append(len(word))
    return word_len

def l_comp():
    sent = "Hello there i am python"
    words = sent.split()
    word_len = [len(word) for word in words if word != "there"]
    return word_len

def Main():
    print "both the functions do same thing"
    print comp()
    print l_comp()

if __name__ == "__main__":
    Main()