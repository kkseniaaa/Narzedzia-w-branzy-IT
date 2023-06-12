if input_extension == ".yaml" or input_extension == ".yml":
    try:
        with open(self.input_file_path, "r") as input_file:
            data = yaml.safe_load(input_file)
    except yaml.YAMLError as e:
        QMessageBox.warning(self, "Error", "Invalid YAML file: " + str(e))
        return
else:
    QMessageBox.warning(self, "Error", "Invalid input file format.")
    return
