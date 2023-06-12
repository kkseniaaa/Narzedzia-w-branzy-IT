if output_extension == ".json":
    try:
        with open(self.output_file_path, "w") as output_file:
            json.dump(data, output_file, indent=4)
    except Exception as e:
        QMessageBox.warning(self, "Error", "Failed to save data as JSON: " + str(e))
        return
else:
    QMessageBox.warning(self, "Error", "Invalid output file format.")
    return
