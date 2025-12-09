from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, text):
        pass


class PDFExporter(Exporter):
    def export(self, text):
        print("PDF created:", text)


class CSVExporter(Exporter):
    def export(self, text):
        print("CSV created:", text)


class TXTExporter(Exporter):
    def export(self, text):
        print("TXT file created:", text)


class ExportFactory:
    @staticmethod
    def create(format_type):
        f = format_type.lower()
        if f == "pdf":
            return PDFExporter()
        if f == "csv":
            return CSVExporter()
        if f == "txt":
            return TXTExporter()
        raise ValueError("Unknown format!")


# DEMO
if __name__ == "__main__":
    factory = ExportFactory()
    exporter = factory.create("csv")
    exporter.export("User data, 2025")
