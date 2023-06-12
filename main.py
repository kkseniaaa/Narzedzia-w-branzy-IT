if input_extension == ".xml":
    try:
        tree = ET.parse(self.input_file_path)
        root = tree.getroot()
        data = self.xml_to_dict(root)
    except ET.ParseError as e:
        QMessageBox.warning(self, "Error", "Invalid XML file: " + str(e))
        return
else:
    QMessageBox.warning(self, "Error", "Invalid input file format.")
    return
