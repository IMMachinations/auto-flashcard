import arxiv


def getArxivPDF(paper_id):
    paper = next(arxiv.Client().results(arxiv.Search(id_list = [paper_id])))
    written_path = paper.download_pdf()
    return written_path
