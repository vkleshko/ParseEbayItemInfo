import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_base_path():
    if getattr(sys, 'frozen', False):
        # Виконуваний файл
        return sys._MEIPASS
    else:
        # Запуск скрипту
        return os.path.abspath(".")


class SheetAPI:

    def __init__(self, key_tb: str):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        # Використовуйте get_base_path для визначення шляху до credentials.json
        base_path = get_base_path()
        credentials_path = os.path.join(
            base_path, 'config', 'credentials.json')

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credentials_path, scope
        )
        gc = gspread.authorize(credentials)
        self.spreadsheet = gc.open_by_key(key_tb)

    def read(self, list_name: str, range_tb: str) -> list:
        worksheet = self.spreadsheet.worksheet(list_name)
        cell_range = worksheet.range(range_tb)
        result = [item.value for item in cell_range]
        return result

    def write(self, list_name: str, range_tb: str, data: list) -> (bool, str):
        try:
            worksheet = self.spreadsheet.worksheet(list_name)
            worksheet.update(range_tb, data)
            return True, "Successfully!"
        except Exception as e:
            return False, str(e)


if __name__ == '__main__':
    print("Sheet repository API!")
