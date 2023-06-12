import sys
import os
import json
import xml.etree.ElementTree as ET
import yaml
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox


class DataConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Converter")
        self.resize(300, 150)

        self.input_file_path = None
        self.output_file_path = None

        self.layout = QVBoxLayout()

        self.input_label = QLabel("Input File:")
        self.layout.addWidget(self.input_label)
        self.input_line_edit = QLineEdit()
        self.layout.addWidget(self.input_line_edit)
        self.input_button = QPushButton("Browse")
        self.input_button.clicked.connect(self.browse_input_file)
        self.layout.addWidget(self.input_button)

        self.output_label = QLabel("Output File:")
        self.layout.addWidget(self.output_label)
        self.output_line_edit = QLineEdit()
        self.layout.addWidget(self.output_line_edit)
        self.output_button = QPushButton("Browse")
        self.output_button.clicked.connect(self.browse_output_file)
        self.layout.addWidget(self.output_button)

        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_data)
        self.layout.addWidget(self.convert_button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def browse_input_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Input File")
        self.input_line_edit.setText(file_path)

    def browse_output_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Select Output File")
        self.output_line_edit.setText(file_path)

    def convert_data(self):
        self.input_file_path = self.input_line_edit.text()
        self.output_file_path = self.output_line_edit.text()

        if not self.input_file_path or not self.output_file_path:
            QMessageBox.warning(self, "Error", "Please select input and output files.")
            return

        input_extension = os.path.splitext(self.input_file_path)[1].lower()
        output_extension = os.path.splitext(self.output_file_path)[1].lower()

        try:
            if input_extension == ".json":
                with open(self.input_file_path, "r") as input_file:
                    data = json.load(input_file)
            elif input_extension == ".xml":
                tree = ET.parse(self.input_file_path)
                root = tree.getroot()
                data = self.xml_to_dict(root)
            elif input_extension == ".yaml" or input_extension == ".yml":
                with open(self.input_file_path, "r") as input_file:
                    data = yaml.safe_load(input_file)
            else:
                QMessageBox.warning(self, "Error", "Invalid input file format.")
                return

            if output_extension == ".json":
                with open(self.output_file_path, "w") as output_file:
                    json.dump(data, output_file, indent=4)
            elif output_extension == ".xml":
                root = self.dict_to_xml(data)
                tree = ET.ElementTree(root)
                tree.write(self.output_file_path, encoding="utf-8", xml_declaration=True)
            elif output_extension == ".yaml" or output_extension == ".yml":
                with open(self.output_file_path, "w") as output_file:
                    yaml.safe_dump(data, output_file)
            else:
                QMessageBox.warning(self, "Error", "Invalid output file format.")
                return

            QMessageBox.information(self, "Success", "Data conversion completed.")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def xml_to_dict(self, element):
        data = {}
        if element.attrib:
            data["@attributes"] = element.attrib
        if element.text:
            data["text"] = element.text.strip()
        for child in element:
            child_data = self.xml_to_dict(child)
            if child.tag in data:
                if not isinstance(data[child.tag], list):
                    data[child.tag] = [data[child.tag]]
                data[child.tag].append(child_data)
            else:
                data[child.tag] = child_data
        return data

    def dict_to_xml(self, data, parent=None):
        if parent is None:
            parent = ET.Element("root")
        for key, value in data.items():
            if key == "@attributes":
                for attr_key, attr_value in value.items():
                    parent.set(attr_key, attr_value)
            elif key == "text":
                parent.text = value
            elif isinstance(value, list):
                for item in value:
                    element = ET.Element(key)
                    self.dict_to_xml(item, parent=element)
                    parent.append(element)
            else:
                element = ET.Element(key)
                self.dict_to_xml(value, parent=element)
                parent.append(element)
        return parent


if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = DataConverter()
    converter.show()
    sys.exit(app.exec_())
