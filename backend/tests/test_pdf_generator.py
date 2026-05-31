import pytest
from io import BytesIO


class TestPDFGeneration:
    def test_generate_pdf_from_lecture_data(self):
        from app.services.pdf_generator import generate_bilingual_pdf

        lecture_data = {
            "title_de": "Erster Vortrag",
            "title_zh": "第一讲",
            "location": "Dornach",
            "lecture_date": "1915-08-23",
            "paragraphs": [
                {
                    "sentences": [
                        {"text_de": "Dies ist ein Testsatz.", "text_zh": "这是一个测试句子。"},
                        {"text_de": "Noch ein Satz.", "text_zh": "另一个句子。"},
                    ]
                },
                {
                    "sentences": [
                        {"text_de": "Zweiter Absatz.", "text_zh": "第二段。"},
                    ]
                },
            ],
        }

        pdf_bytes = generate_bilingual_pdf(lecture_data)
        assert isinstance(pdf_bytes, bytes)
        assert len(pdf_bytes) > 100
        assert pdf_bytes[:4] == b"%PDF"

    def test_generate_pdf_handles_missing_zh(self):
        from app.services.pdf_generator import generate_bilingual_pdf

        lecture_data = {
            "title_de": "Test Lecture",
            "title_zh": "",
            "paragraphs": [
                {
                    "sentences": [
                        {"text_de": "Nur Deutsch.", "text_zh": None},
                    ]
                },
            ],
        }

        pdf_bytes = generate_bilingual_pdf(lecture_data)
        assert isinstance(pdf_bytes, bytes)
        assert pdf_bytes[:4] == b"%PDF"

    def test_generate_pdf_handles_empty_lecture(self):
        from app.services.pdf_generator import generate_bilingual_pdf

        lecture_data = {
            "title_de": "Empty",
            "title_zh": "",
            "paragraphs": [],
        }

        pdf_bytes = generate_bilingual_pdf(lecture_data)
        assert isinstance(pdf_bytes, bytes)
        assert pdf_bytes[:4] == b"%PDF"
