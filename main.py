from Sheet.sheetAPI import SheetAPI
from Parser.parser import parser_run
from secondary_functions import sort_arrays


def process_chunk(tb, start_row, end_row):
    print(f"Обробка рядків з {start_row} по {end_row}")
    sku = tb.read("LISTINGS", f"D{start_row}:D{end_row}")
    links = tb.read("LISTINGS", f"G{start_row}:G{end_row}")
    result = parser_run(links, sku)
    data, variation = sort_arrays(result, sku)
    tb.write("LISTINGS", f"H{start_row}:L{end_row}", data)
    print(f"Завершено обробку рядків з {start_row} по {end_row}")


def main():
    tb_key = str(input("Введи ID таблиці: "))
    start_row = int(input("Введи початковий рядок: "))
    end_row = int(input("Введи кінцевий рядок: "))

    tb = SheetAPI(tb_key)

    chunk_size = 200
    for i in range(start_row, end_row + 1, chunk_size):
        chunk_end_row = min(i + chunk_size - 1, end_row)
        process_chunk(tb, i, chunk_end_row)


if __name__ == '__main__':
    main()
