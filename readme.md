This is a guide on how to use the scraping code in this repository.

Technologies used :
- Python :used for sendrequests and parsing the data
- BeautifulSoup:used for parsing the HTML content and extracting the required data
- csv:used for storing the extracted data in a structured format

data extracted from 'https://books.toscrape.com/catalogue/category/books_1/index.html':
- Title of the article
- Price of the article
- Category of the article

how this file is structured :
|--scraping.py : This file contains the code for scraping the data.
|--requirements.txt : This file contains the list of required libraries for running the code.
|--README.md : This file contains the instructions for using the code.
|--output.csv : This file contains the output of the code in CSV format.

how to run the code :
1.first copy this folder to your laptop or pc
2.open the folder using vs code or any code editor of your choice
3.run the command 'pip install -r requirements.txt' in the terminal to install the required libraries
4.run the command 'python scraping.py' in the terminal to execute the code
5.fter running the code, you will find a file named 'output.csv' in the same folder which contains the extracted data in CSV format.
You can open this file using Excel or any CSV viewer to see the results.

note: Make sure you have Python installed on your system before running the code.
You can download it from https://www.python.org/downloads/.