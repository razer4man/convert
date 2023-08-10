# Convert Amount (BYN) To Another Currences

Convert your amount in BYN to another currencies by [NBRB](https://www.nbrb.by) course
use [official API](https://www.nbrb.by/apihelp/exrates).

List of currencies: USD, EUR, RUB, UAH, PLN, GBP, CHF, JPY, KZT, CZK, TRY, SEK, CNY, MDL, BRL, AUD, CAD.

## How To Use

1. Activate Python's virtual environment:

    ```
    source venv/bin/activate
    ```
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run:

    ```
    python main.py
    ```

4. Enter your amount and press 'Enter'

## How To Create Universal Symlink (optional)

1. Create 'convert' file:
   ```
   true > convert
   ```
2. Update new file 'convert' with a shebang string (enter your /path/to/dir/) and main.py's code:
   ```
   #!/path/to/dir/venv/bin/python
   
   from convert import convert_amount
   from user_input import amount
   from utils import URL_GET_CURRENCIES


   def main() -> str:
       convert_amount_string = convert_amount(amount, URL_GET_CURRENCIES)
       return '; '.join(convert_amount_string)
   
   if __name__ == '__main__':
       print(main())
   ```
3. Change chmod for the 'convert' file:
   ```
   chmod +x convert
   ```
4. Create the symlink 'convert':
   ```
   sudo ln -s $(pwd)/convert /usr/local/bin/
   ```

## How To Remove The Symlink (optional)

1. Remove the symlink:
   ```
   sudo rm -i /usr/local/bin/convert
   ```