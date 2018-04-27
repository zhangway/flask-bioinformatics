#Demo app for PaaS
#Kidane M. Tekle, 16 Feb 2017

import os
from flask import Flask, request

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

html = '''
        <h1>Simple python demo app!</h1>
        <span>A sample application which allows the translation of a nucleotide (DNA/RNA) sequence to a protein sequence. </span>
        <form method="POST">
            <textarea name="seq" type="text"  rows="10" cols ="70">%s</textarea>
            <br/> * Example input: ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG 
            <br/> <input value="Translate" type="submit" />
        </form>
        <h2> Result </h2>
        %s
        <hr/>
        <a href="https://web.expasy.org/translate/" target="_blank" > Similar app online</a> 
        
    '''

app = Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return html % ("","")

def is_sequence_valid(user_seq):
    return True


def translate(user_seq):
    try:
        coding_dna = Seq(user_seq, generic_dna)
        result = coding_dna.translate(to_stop=True)
        return str(result)
    except Exception as e:
        return str(e)


@app.route('/', methods=['POST'])
def convert():
    user_seq = request.form['seq']
    if not user_seq:
        return html % ("","Missing input")
    
    if not is_sequence_valid(user_seq):
        return html % (user_seq, "Invalid sequence. Adjust your input and try again")
    result = translate(user_seq)
    return html % (user_seq, result)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(host='0.0.0.0', port=port)
    
    
    
    
    