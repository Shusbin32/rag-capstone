def clean_text(text:str)-> str:
    return " ".join(text.split())

def count_words(text:str)->int:
    return len(text.split())

def split_into_chunks(text:str,chunk_size:int=50)-> list[str]:
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than 0")
    words=text.split()
    return [
       " ".join(words[i:i+chunk_size])
          for i in range(0,len(words),chunk_size)
    ]
    
def find_longest_word(words:list[str])-> str| None:
    if not words:
        return None
    return max(words,key=len)

