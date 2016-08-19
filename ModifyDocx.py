# -*- coding: utf-8 -*-
from docx import Document


class ModifyDocx:
    def set_report_id_in_docx(self, report_id, old_file, new_file):
        document = Document(old_file)
        document.add_paragraph(u'报告编号： ' + report_id)
        document.save(new_file)


if __name__ == "__main__":
    ab = ModifyDocx()
    ab.set_report_id_in_docx('201609091221', u'光大银行_temp.docx', u'光大银行.docx')
