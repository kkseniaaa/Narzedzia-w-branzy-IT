if input_extension == ".json":
    try:
        with open(self.input_file_path, "r") as input_file:
            data = json.load(input_file)
    except json.JSONDecodeError as e:
        QMessageBox.warning(self, "Error", "Invalid JSON file: " + str(e))
        return
else:
    QMessageBox.warning(self, "Error", "Invalid input file format.")
    return
