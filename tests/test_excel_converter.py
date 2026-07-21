from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Excel converter.py"
SPEC = spec_from_file_location("excel_converter", SOURCE)
assert SPEC is not None and SPEC.loader is not None

excel_converter = module_from_spec(SPEC)
SPEC.loader.exec_module(excel_converter)


def test_local_icon_resource_is_project_icon():
    assert excel_converter.caminho_recurso("icon.ico") == ROOT / "icon.ico"


def test_bundled_icon_resource_uses_pyinstaller_directory(monkeypatch, tmp_path):
    monkeypatch.setattr(excel_converter.sys, "_MEIPASS", str(tmp_path), raising=False)

    assert excel_converter.caminho_recurso("icon.ico") == tmp_path / "icon.ico"


def test_xlsx_can_be_read_and_converted_to_pdf(tmp_path):
    spreadsheet = tmp_path / "sample.xlsx"
    source_data = pd.DataFrame({"Name": ["Alice", "Bob"], "Value": [10, 20]})
    source_data.to_excel(spreadsheet, index=False)

    loaded_data = pd.read_excel(spreadsheet)
    pd.testing.assert_frame_equal(loaded_data, source_data)

    pdf = excel_converter.PDF(orientation="L")
    pdf.add_page()
    pdf.add_table(loaded_data)
    pdf_bytes = bytes(pdf.output())

    assert pdf_bytes.startswith(b"%PDF")
    assert len(pdf_bytes) > 100
