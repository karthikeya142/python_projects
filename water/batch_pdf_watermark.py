import fitz  # PyMuPDF

class BatchPDFWatermark:
    @staticmethod
    def add_watermark(input_stream, watermark_text):
        try:
            document = fitz.open(stream=input_stream.read(), filetype="pdf")
            for page in document:
                page_width = page.rect.width
                page_height = page.rect.height

                # Add watermark text
                watermark = fitz.Point(page_width / 4, page_height / 4)  # Adjust watermark position
                page.insert_text(watermark, watermark_text, fontsize=48, fontname="helv", color=(0, 0, 0), rotate=0)

            return document
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
