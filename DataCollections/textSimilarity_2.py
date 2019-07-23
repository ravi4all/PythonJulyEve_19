def textProcessing(text):
    #1. Tokenization
    t = text.lower().split()

    #2. Remove Stopwords
    stopwords = ['is','a','at','am','and','as','be','by','could','can','the','that',
                 'to','this','in','of','for','if','from','or','with','it','its','so',
                 'on','are','also','used','they','which','has','been','an','have']

    words = []
    for token in t:
        if token not in stopwords:
            words.append(token)

    c = ['.',",","'","-"]
    for i in range(len(c)):
        for j in range(len(words)):
            if words[j].endswith(c[i]):
                words[j] = words[j].replace(c[i],'')
    return words

text_1 = '''Python is a high-level programming language designed to be easy to read and simple to implement. It is open source, which means it is free to use, even for commercial applications. Python can run on Mac, Windows, and Unix systems and has also been ported to Java and .NET virtual machines.
Python is considered a scripting language, like Ruby or Perl and is often used for creating Web applications and dynamic Web content. It is also supported by a number of 2D and 3D imaging programs, enabling users to create custom plug-ins and extensions with Python. Examples of applications that support a Python API include GIMP, Inkscape, Blender, and Autodesk Maya.
Scripts written in Python (.PY files) can be parsed and run immediately. They can also be saved as a compiled programs (.PYC files), which are often used as programming modules that can be referenced by other Python programs.'''

text_2 = """Python is a multiparadigm, general-purpose, interpreted, high-level programming language. Python allows programmers to use different programming styles to create simple or complex programs, get quicker results and write code almost as if speaking in a human language. Some of the popular systems and applications that have employed Python during development include Google Search, YouTube, BitTorrent, Google App Engine, Eve Online, Maya and iRobot machines. Python is an interpreted language, which precludes the need to compile code before executing a program because Python does the compilation in the background. Because Python is a high-level programming language, it abstracts many sophisticated details from the programming code. Python focuses so much on this abstraction that its code can be understood by most novice programmers."""

words_1 = textProcessing(text_1)
words_2 = textProcessing(text_2)

numer = len(set(words_1).intersection(set(words_2)))
denom = len(set(words_1).union(set(words_2)))
d = numer/denom
print("Sim is",d*100)
