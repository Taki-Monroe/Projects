import string
import secrets

def get_input() -> tuple[bool, bool, int]:
        
        has_uppercase: bool = input("Do you want uppercase? (Y/n)").strip().lower() == 'y'
        has_symbols: bool = input("Do you want symbols? (Y/n)").strip().lower() == 'y'
        pass_length: int = int(input("What should be the length?"))
        return has_uppercase, has_symbols, pass_length


def gen_pass(has_uppercase, has_symbols, pass_length) -> str:
        
        new_pass: str = ''
        combination: str = string.ascii_lowercase
        
        if has_uppercase:
          combination += string.ascii_uppercase
        
        if has_symbols:
          combination += string.punctuation
        
        new_pass += ''.join(combination[secrets.randbelow(len(combination))] for _ in range(pass_length))
        return new_pass
        
def main() -> None:
  has_uppercase, has_symbols, pass_length = get_input()
  
  for i in range(5):
      new_pass: str = gen_pass(has_uppercase, has_symbols, pass_length)
      print(f"{i+1}. Password: {new_pass}")

if __name__ == '__main__':
  main()
