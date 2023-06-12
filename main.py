if output_extension == ".xml":
    try:
        root = self.dict_to_xml(data)
        tree = ET.ElementTree(root)
        tree.write(self.output_file_path, encoding="utf-8", xml_declaration=True)
    except Exception as e:
        QMessageBox.warning(self, "Error", "Failed to save data as XML: " + str(e))
        return
else:
    QMessageBox.warning(self, "Error", "Invalid output file format.")
    return
