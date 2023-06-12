import asyncio

async def convert_data_async(self):

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = DataConverter()
    converter.show()
    asyncio.run(converter.convert_data_async())
    sys.exit(app.exec_())
