# -*- coding: utf-8 -*-
"""
"""

from findimagespdf.pdffile import PDFFile

from tests.samples import *

import unittest
import io



class PDFFileTestCase(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.correct_PDF_direct = io.BytesIO(correct_PDF_direct)
        self.no_height_width_image = io.BytesIO(no_height_width_image)
        self.correct_PDF_indirect = io.BytesIO(correct_PDF_indirect)
        self.no_height_image_indirect = io.BytesIO(no_height_image_indirect)
        self.pdf_invalid_ref_indirect = io.BytesIO(pdf_invalid_ref_indirect)
        self.pdf_mixed_images_indirect = io.BytesIO(pdf_mixed_images_indirect)

    def test_correct_pdf_direct(self) -> None:
        """
        """
        with PDFFile(self.correct_PDF_direct) as pdf:
            pdf.find_startxref()
            pdf.search_deep()
            pdf.search_images()
            self.assertEqual(len(pdf.images), 1)

    def test_no_height_width_image(self) -> None:
        """
        """
        with PDFFile(self.no_height_width_image) as pdf:
            pdf.find_startxref()
            pdf.search_deep()
            pdf.search_images()
            self.assertEqual(len(pdf.images), 0)

    def test_correct_PDF_indirect(self) -> None:
        """
        """
        with PDFFile(self.correct_PDF_indirect) as pdf:
            pdf.find_startxref()
            pdf.search_deep()
            pdf.search_images()
            self.assertEqual(len(pdf.images), 1)

    def test_pdf_mixed_images_indirect(self) -> None:
        """
        """
        with PDFFile(self.pdf_mixed_images_indirect) as pdf:
            pdf.find_startxref()
            pdf.search_deep()
            pdf.search_images()
            self.assertEqual(len(pdf.images), 2)

    def test_no_height_image_indirect(self) -> None:
        """
        """
        with PDFFile(self.no_height_image_indirect) as pdf:
            pdf.find_startxref()
            pdf.search_deep()
            pdf.search_images()
            self.assertEqual(pdf.images, [])

    def test_pdf_invalid_ref_indirect(self) -> None:
        """
        """
        with PDFFile(self.pdf_invalid_ref_indirect) as pdf:
            pdf.find_startxref()
            pdf.search_deep()
            pdf.search_images()
            self.assertEqual(pdf.images, [])
