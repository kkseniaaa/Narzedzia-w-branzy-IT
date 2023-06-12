if output_extension == ".yaml" or output_extension == ".yml":
    try:
        with open(self.output_file_path, "w") as output_file:
            yaml.safe_dump(data, output_file)
    except Exception as e:
        QMessageBox.warning(self, "Error", "Failed to save data as YAML: " + str(e))
        return
else:
    QMessageBox.warning(self, "Error", "Invalid output file format.")
    return
