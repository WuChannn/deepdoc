
from tasks.paper import Pdf


if __name__ == "__main__":
    def dummy(prog=None, msg=""):
        pass

    filename = './assets/KOSMOS-2.5.pdf'
    binary = None
    from_page = 0
    to_page = 100000
    callback = None

    pdf_parser = Pdf()
    paper = pdf_parser(filename, from_page=from_page, to_page=to_page, callback=dummy)

    print(paper)