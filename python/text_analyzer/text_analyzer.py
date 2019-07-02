import click

word_occurence = dict()
letter_occurence = dict()
paragraph_starter_occurence = dict()
ALPHABET = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
symbol_count = 0


def analyze_letters(word: str):
    global symbol_count, letter_occurence
    letterized_word = list(word.lower())
    for letter in letterized_word:
        if letter in ALPHABET:
            letter_occurence[letter] = letter_occurence.get(letter, 0) + 1
        else:
            symbol_count += 1


def analyze_words(paragraph: str):
    global word_occurence, paragraph_starter_occurence
    worded_paragraph = paragraph.lower().split(' ')
    for idx, word in enumerate(worded_paragraph):
        if idx == 0:
            paragraph_starter_occurence[word] = \
                paragraph_starter_occurence.get(word, 0) + 1
        word_occurence[word] = word_occurence.get(word, 0) + 1
        analyze_letters(word)


def parse_to_string(file):
    text_string: str
    with open(file, 'r') as _file:
        text_string = ''.join(_file.readlines())
    return text_string


@click.command()
@click.option("--file", "-f", default="lorem_ipsum.txt")
def analyze_text(file):
    global word_occurence, letter_occurence, paragraph_starter_occurence,\
        symbol_count
    paragraphized_text = parse_to_string(file).split("\n\n")
    for paragraph in paragraphized_text:
        analyze_words(paragraph)
    click.secho(f"Input file: {file}", fg="green")
    click.echo("=============================================================")
    total_words = sum([occurence for occurence in word_occurence.values()])
    total_letters = sum([occurence for occurence in letter_occurence.values()])
    words_by_occurence = sorted(word_occurence.items(), key=lambda kv: kv[1],
                                reverse=True)
    letters_by_occurence = sorted(
        letter_occurence.items(), key=lambda _: _[1], reverse=True)
    starter_by_occurence = sorted(
        paragraph_starter_occurence.items(), key=lambda _: _[1], reverse=True)
    words_used_once = [word for word, count in word_occurence.items()
                       if count == 1]
    lonely_letters = [letter for letter in ALPHABET
                      if letter not in letter_occurence.keys()]
    click.echo(f"Number of words: {total_words}")
    click.echo(f"Number of letters: {total_letters}")
    click.echo(f"Number of symbols: {symbol_count}")
    click.echo(f"Top 3 most common words: {words_by_occurence[:3]}")
    click.echo(f"Top 3 most common letters: {letters_by_occurence[:3]}")
    click.echo(
        f"Most common first word for paragraphs: {starter_by_occurence[0]}")
    click.echo(f"Words only used once: {words_used_once}")
    click.echo(f"Letters not used in the document: {lonely_letters}")


if __name__ == "__main__":
    analyze_text()
