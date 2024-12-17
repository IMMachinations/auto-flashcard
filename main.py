import argparse, os, csv, json
from arxiv_calls import getArxivPDF
import llm_calls

delete_file_after = True
parser = argparse.ArgumentParser()
parser.add_argument("arxiv_id")
parser.add_argument("-k", "--keep", help = "keeps the pdf on-system instead of cleaning", action="store_true")
parser.add_argument("-c", "--count", help = "number of flash cards to produce, defaults to 10", action ="store_const", const=10)
if __name__ == '__main__':
    args = parser.parse_args()
    delete_file_after = not args.keep
    pdf_path = getArxivPDF(args.arxiv_id)
    print(pdf_path)
    response = llm_calls.readPDF(pdf_path, count=args.count, prompt=0)
    print(response.text)
    json_cards = json.loads(response.text)
    with(open('out.csv', 'w', newline='') as csv_file):
        writer = csv.writer(csv_file)
        for row in json_cards:
            writer.writerow(list(row.values())[::-1])
    if(delete_file_after):
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
            print("File deleted successfully.")
        else:
            print("File not found.")
