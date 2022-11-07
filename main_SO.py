import parser_stakeout
import UI_pars_SO
import pandas as pd


def main():
    data = pd.DataFrame()
    while True:
        reply = UI_pars_SO.main_menu()
        if reply == "Парсинг":
            file = UI_pars_SO.parsing()
            if file:
                for f in file:
                    dframe = parser_stakeout.get_dataframe(f)
                    data = data.append(dframe,  ignore_index=True)
                data.to_csv(UI_pars_SO.save_file(data), sep=";", index=False)
        elif reply == "Просмотр логов":
            UI_pars_SO.logs(logs)
        elif reply == "Выход" or reply is None:
            break

if __name__ == "__main__":
    main()