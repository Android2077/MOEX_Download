
from __future__ import annotations
import json
import urllib.request
import http.client
import ssl
from html.parser import HTMLParser
import time
import csv
from dataclasses import fields
from dataclasses import dataclass, field
from enum import Enum
from enum import IntEnum
from enum import StrEnum
import os
from datetime import datetime
from collections.abc import Callable
import threading
import traceback


def Callback_for_Load_Info(json_data_part, String_Date_Range_Start:str, String_Date_Range_End:str,  List_Any_for_Callback:list[any]):
    # json_data_part - оригинальный JSON который пришел с MOEX в очередной итерации цикла.
    print(String_Date_Range_Start + " : " + String_Date_Range_End);



class MOEX_Download__class():

    interval_mapping: dict = {
    "1_min": "1",
    "10_min": "10",
    "1_hour": "60",
    "1_day": "24",
    "1_week": "7",
    "1_month": "31",
    "1_kvartal": "4",
    };
    
    
    class Intervals_enum(StrEnum):
        M1       = "1"
        M10      = "10"
        H1       = "60"
        Day      = "24"
        Week     = "7"
        Month    = "31"
        Kvartal  = "4"


    class Candle_enum(IntEnum): # ВНИМАНИЕ!!!!!!!!!!! ПОЛЯ ДОЛЖНЫ ПОЛНОСТЬ СООТВЕТВОВАТЬ ПОРЯДКУ КАК ОНИ УКАЗАНЫ В "self.list_benchmark_Columns_from_MOEX" !!!!!!!!!!
        Open   = 0
        Close  = 1
        High   = 2
        Low    = 3
        Value  = 4
        Volume = 5
        Begin  = 6
        End    = 7
     

    @dataclass(slots=True)
    class Candle_struct:

        SECID:str           = "";   # Код бумаги типа GAZP, SBER...    # Данное поле чисто инофрмационное
        Interval_string:str = "";   # Временной интервал               # Данное поле чисто инофрмационное

        List_Candles_2D:list[list] = field(default_factory=list);      # Тут список параметров свечи - то есть список свечей. Каждая свеча - это также список, который полностью СООТВЕТВУЕТ списку пришедшему в JSON с MOEX

        def __init__(self, SECID_, Interval_string_, List_Candles_2D:list[list]):
            self.SECID            = SECID_;
            self.Interval_string  = Interval_string_;
            self.List_Candles_2D  = list(List_Candles_2D);


        def Add_to_ListCandles(self, List_Candles_2D:list[list]):
            self.List_Candles_2D.extend(List_Candles_2D);

        def Get_ListCandles(self):
            return self.List_Candles_2D;

    @dataclass(slots=True)
    class Engines_Market_Board_struct:
        trade_engine_name:str  = "";
        trade_engine_title:str = "";
        
        @dataclass
        class Sub_Market_struct:
            market_name:str  = "";
            market_title:str = "";
            
            @dataclass
            class Sub_sub_Boards_struct:
                boardid:str  = "";
                board_title:str = "";
                
            Board_List:list[Sub_sub_Boards_struct] = field(default_factory=list);
      
        Market_List:list[Sub_Market_struct] = field(default_factory=list);
    
    @dataclass(slots=True)
    class Instruments_struct:
        SECID:str = "";
        SECNAME:str = "";
        
    @dataclass(slots=True)
    class Request_struct:

        #--------------------Параметры Пользовательского запроса:Начало----------------
        Engines_Name:str                = "";
        Market_Name:str                 = "";
        Board_Name:str                  = "";
        Instrument_Name:str             = "";
        Interval_string_ID:str          = "";
        Date_Begin:str                  = "";
        Date_End:str                    = "";
        Callback_for_Load_Info:Callable = None;
        List_Any_for_Callback:list[any] =  field(default_factory=list); 
        #--------------------Параметры Пользовательского запроса:Конец----------------


        def __hash__(self):
            return hash((self.Engines_Name, self.Market_Name, self.Board_Name, self.Instrument_Name, self.Interval_string_ID, self.Date_Begin, self.Date_End));   # Чтобы можно было использовать в контейнере "Set" - указываем НЕИЗМЕНЯМЫЕ ПОЛЯ, то есть те поля, которые не не будут менятся ПОСЛЕ добавления в SET и поля котоыре Уникальным образом индетифицирует данный обьект класса.


        #-----------------------------------Служебные данные:--------------------------------------

        _List_Part_Download:list[str] =  field(default_factory=list);   # Сюда будет складировать скачаные части до тех пор, пока все не скачается.
        _Last_Use_URL:str = "";                                         # Последний-текущий использованный URL для скачки данных.
        _Error_Flag:bool = False;                                       # Флаг ошибки, произошла ли ошибка при скачивании или нет.
        _counter_page:int = 0;
        _http_conn: http.client.HTTPSConnection = field(default=None);  # Отдельный обьект соединения для каждого запроса.



    class engines_enum(Enum): # ["id", "name", "title"]
        id=0
        name=1
        title=2
          
    class markets_enum(Enum): # ["id", "trade_engine_id", "trade_engine_name", "trade_engine_title", "market_name", "market_title", "market_id", "marketplace", "is_otc", "has_history_files", "has_history_trades_files", "has_trades", "has_history", "has_candles", "has_orderbook", "has_tradingsession", "has_extra_yields", "has_delay"]
        id=0
        trade_engine_id=1
        trade_engine_name=2
        trade_engine_title=3
        market_name=4
        market_title=5
        market_id=6
        marketplace=7
        is_otc=8
        has_history_files=9
        has_history_trades_files=10
        has_trades=11
        has_history=12
        has_candles=13
        has_orderbook=14
        has_tradingsession=15
        has_extra_yields=16
        has_delay=17

    class boards_enum(Enum): # ["id", "board_group_id", "engine_id", "market_id", "boardid", "board_title", "is_traded", "has_candles", "is_primary"]
        id=0
        board_group_id=1
        engine_id=2
        market_id=3
        boardid=4
        board_title=5
        is_traded=6
        has_candles=7
        is_primary=8


    def __init__(self):

        self.TextExtractor_from_HTML_ = self.TextExtractor_from_HTML();

        self.list_benchmark_Columns_from_MOEX = ["open", "close", "high", "low", "value", "volume", "begin", "end"];   # Это название и порядок стобцов свечей приходящих с MOEX и этот формат используется для парсинга и нужен для проверки. # ВНИМАНИЕ!!!!!!! ПОРЯДОК полей в "Candle_enum" должен быть, как они указаны в данном списке!!!!!!
        self.Formate_Date_from_MOEX_string    = "%Y-%m-%d %H:%M:%S";                                                   # Это формат даты и времени свечи приходящих с MOEX и этот формат используется для парсинга и нужен для проверки.

        self.http_host = "iss.moex.com"
        # self.http_conn: http.client.HTTPSConnection | None = None
        
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "sec-ch-ua": '"Chromium";v="152", "Not?A_Brand";v="24", "Google Chrome";v="152"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        }

        self.Dict_Request: dict[str, MOEX_Download__class.Request_struct] = {};   # Короче суть: MOEX очень часто разрывает соединения, и если на интервала типа Дневных и часовых еще можно за раз попытатся успеть скачать полный достыный диапазон свечей, то уже на 10 минутнках и 1 минутка - это тупо не получится, потому что на половине MOEX разорвет соединение, ну или просто сбой соединения какой то произойдет и опять скачивать с самого начала диапазона - в итоге так можно бесконечно раз скачивать, и так и не скачать. ПОЭТОМУ придется держать для каждого запроса на скачивание - скаченные данные, чтобы при ошибке, начать скачивание с последней ссылки, а не с начала диапазона, которые указал пользователь.
        self.Mutex = threading.Lock();


    def Get__ALL_List_Engines_Market_Board_from_MOEX(self)->tuple[list[MOEX_Download__class.Engines_Market_Board_struct] | None, str|None]:
        # Короче, для начала получим список вообще всех инстурментов с MOEX: то есть класс и список итнстурментов соответвущих этому класу, причем список, как активных инстурментов, так уже и не активных. Для примера: Фьючерсы - активные, и уже завершившиеся; Валюта - доллар, евро - по изветсным причинам уже и пока не торгуется, то есть наактивные; Тоже самое по акциям обыкновенным TQBR - есть акиции, которые уже не торгуются.    
        # Как я понял вся необходимая информация для получения всех торгуемых ан данынй момент инстурментов есть в:https://iss.moex.com/iss/index.json?iss.only=trade_engines (эта ссылка указана в самом https://iss.moex.com/iss/reference/205)

        # Можнро открыть в браузере https://iss.moex.com/iss/index.json?iss.only=trade_engines - и посмотреть Json-структуру, три основых массива это:

        #- "engines"[data]
        #- "markets"[data]
        #- "boards"[data]

        # Все что нужно - это сопоставить данные из таблицы "boards"[data] с "markets"[data]. "markets"[data] с "engines"[data] - можно не сопоставлять, так как в "markets"[data] - уже есть столбцы с сопаставленой информацей из "engines"[data].

        url:str = "https://iss.moex.com/iss/index.json?iss.only=trade_engines";

        json_data, error_text  =  self._Get__Http_Request_JSON__NewConnect(url);

        if (json_data != None):


            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Engine_List_2d:list[list] = json_data["engines"]["data"];
            Market_List_2d:list[list] = json_data["markets"]["data"];
            Boards_List_2d:list[list] = json_data["boards"]["data"];

            Market_List_2d.sort(key=lambda x: x[self.markets_enum.trade_engine_id.value]);   # Отсортируем по столбцу "trade_engine_id"
            Boards_List_2d.sort(key=lambda x: x[self.boards_enum.market_id.value]);         # Отсортируем по столбцу "market_id"
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





            List_All_Intruments_MOEX_3D:list[MOEX_Download__class.Engines_Market_Board_struct] = [];    # Сюда занесем итоговую сопоставленную информацию.
            
            
            Market_flag_find:bool = False;
            Boards_flag_find:bool = False;
            
            for i in range(len(Engine_List_2d)):
                
                List_All_Intruments_MOEX_3D.append(self.Engines_Market_Board_struct());
                
                List_All_Intruments_MOEX_3D[-1].trade_engine_name  = Engine_List_2d[i][self.engines_enum.name.value];
                List_All_Intruments_MOEX_3D[-1].trade_engine_title = Engine_List_2d[i][self.engines_enum.title.value];
        
        
        
                Market_flag_find = False;  # Сбрасываем перед циклом.
            
                for y in range(len(Market_List_2d)):   # Теперь ищем ключ "trade_engine_id" в таблице "Market_List_2d" и найденные строки добовляем в список: Доавбляем только нужные столбцы.
                    
                    if (Market_List_2d[y][self.markets_enum.trade_engine_id.value] == Engine_List_2d[i][self.engines_enum.id.value]):     # Так, значит нашли свопадение ключей,  
                        
                        Market_flag_find = True;
                        
                        List_All_Intruments_MOEX_3D[-1].Market_List.append(self.Engines_Market_Board_struct.Sub_Market_struct());
                        
                        List_All_Intruments_MOEX_3D[-1].Market_List[-1].market_name  = Market_List_2d[y][self.markets_enum.market_name.value]
                        List_All_Intruments_MOEX_3D[-1].Market_List[-1].market_title = Market_List_2d[y][self.markets_enum.market_title.value]



                        Boards_flag_find:bool = False;  # Сбрасываем перед циклом.
                        #_______________________________________________________________________________
                        for q in range(len(Boards_List_2d)):   # Теперь ищем ключ "market_id" в таблице "Boards_List_2d" и найденные строки добовляем в список: Доавбляем только нужные столбцы.
                        
                            if (Boards_List_2d[q][self.boards_enum.market_id.value] == Market_List_2d[y][self.markets_enum.id.value]):     # Так, значит нашли свопадение ключей,  
                        
                                Boards_flag_find = True;
                        
                                List_All_Intruments_MOEX_3D[-1].Market_List[-1].Board_List.append(self.Engines_Market_Board_struct.Sub_Market_struct.Sub_sub_Boards_struct());
                        
                                List_All_Intruments_MOEX_3D[-1].Market_List[-1].Board_List[-1].boardid     = Boards_List_2d[q][self.boards_enum.boardid.value];
                                List_All_Intruments_MOEX_3D[-1].Market_List[-1].Board_List[-1].board_title = Boards_List_2d[q][self.boards_enum.board_title.value];
                                
                            else:
                                if (Boards_flag_find == True):
                                    break; # Так как таблица "Boards_List_2d" у нас отсортирована по столбцу "market_id" и если мы наткнулись на строку где совпадения ключей нет, то значит ключи для этой итерации цикоа закончились выходим из цикла.
                                else:
                                    pass   # Ничего не делаем продалжаем цикл в поисках совпадения ключа.
                        #_______________________________________________________________________________
                        
                                   
                    else:
                        if (Market_flag_find == True):
                            break; # Так как таблица "Market_List_2d" у нас отсортирована по столбцу "trade_engine_id" и если мы наткнулись на строку где совпадения ключей нет, то значит ключи для этой итерации цикоа закончились выходим из цикла.
                        else:
                            pass   # Ничего не делаем продалжаем цикл в поисках совпадения ключа.
                    
                  
                  
                    
            if (len(List_All_Intruments_MOEX_3D) != 0):
                return  List_All_Intruments_MOEX_3D, None;
            else:    
                return None, "len(List_All_Intruments_MOEX_3D) == 0";
                                                          
        else:
            return None, error_text;

    def Save_to_CSV__ALL_List_Engines_Market_Board_from_MOEX(self, List_All_Intruments_MOEX_3D: list[Engines_Market_Board_struct], path_folder: str, filename: str) -> None:

        fieldnames: list = [
            "trade_engine_name",
            "trade_engine_title",
            "market_name",
            "market_title",
            "boardid",
            "board_title",
        ]

        os.makedirs(path_folder, exist_ok=True)  # exist_ok=True - создаст папку, если её нет
        full_path = os.path.join(path_folder, filename)



        with open(full_path, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";");
            writer.writeheader();


            for engine_item in List_All_Intruments_MOEX_3D:
                for market_item in engine_item.Market_List:
                    for board_item in market_item.Board_List:

                        writer.writerow({
                            "trade_engine_name": engine_item.trade_engine_name,
                            "trade_engine_title": engine_item.trade_engine_title,
                            "market_name": market_item.market_name,
                            "market_title": market_item.market_title,
                            "boardid": board_item.boardid,
                            "board_title": board_item.board_title,
                        })
      
    def PrintToConsole__ALL_List_Engines_Market_Board_from_MOEX(self, List_All_Intruments_MOEX_3D: list[Engines_Market_Board_struct]):
        
        print("trade_engine_name  trade_engine_title  market_name  market_title  boardid  board_title");
              
        for Engine_item in List_All_Intruments_MOEX_3D:
            for Market_item in Engine_item.Market_List:
                for Board_item in Market_item.Board_List:
                    print(Engine_item.trade_engine_name + ":" + Engine_item.trade_engine_title  + ":" + Market_item.market_name + ":" + Market_item.market_title + ":" + Board_item.boardid + ":" + Board_item.board_title);
      
    def Convert_List_Engines_Market_Board_to_Flat_Listok(self, List_All_Intruments_MOEX_3D: list[Engines_Market_Board_struct])->list[str]:

        List_return:list[str] = [];


        for Engine_item in List_All_Intruments_MOEX_3D:
            for Market_item in Engine_item.Market_List:
                for Board_item in Market_item.Board_List:

                    List_return.append(Engine_item.trade_engine_name + ":" + Engine_item.trade_engine_title  + ":" + Market_item.market_name + ":" + Market_item.market_title + ":" + Board_item.boardid + ":" + Board_item.board_title);
    
    def Convert_List_Engines_Market_Board_to_Dictonary(self, List_All_Intruments_MOEX_3D: list[Engines_Market_Board_struct])->dict:

        Dict_Engine_Level:dict = {};


        for Engine_item in List_All_Intruments_MOEX_3D:

            Dict_Market_Level:dict = {};

            for Market_item in Engine_item.Market_List:

                List_Boards:list[str] = [];

                for Board_item in Market_item.Board_List:

                    Boards_string =  Board_item.boardid + "(" + Board_item.board_title + ")";
                    List_Boards.append(Boards_string);


                Key_Market_string = Market_item.market_name + "(" + Market_item.market_title + ")";
                Dict_Market_Level[Key_Market_string] = List_Boards;


            Key_Engine_string = Engine_item.trade_engine_name + "(" + Engine_item.trade_engine_title + ")";
            Dict_Engine_Level[Key_Engine_string] = Dict_Market_Level;
     
        
        # Формат словаря "Dict_Engine_Level": Словарь_Engine[Key=Engine_string , value = Словарь_Market[key=Market_string, value = Список_Boards_string]]

        return Dict_Engine_Level;

    
    def Get__All_Instruments_from_Engine_Market_Board(self, Engines_Name:str, Market_Name:str, Board_Name:str)->[list[MOEX_Download__class.Instruments_struct] | None, str|None]:
      
        Generate_URL:str = f"https://iss.moex.com/iss/engines/{Engines_Name}/markets/{Market_Name}/boards/{Board_Name}/securities.json";
        # print(Generate_URL)      
        Json_data, error_text  = self._Get__Http_Request_JSON__NewConnect(Generate_URL);

        List_instruments_for_Return:list[MOEX_Download__class.Instruments_struct] = [];
               
               
        if (Json_data != None):
            List_instruments:list[list] = Json_data["securities"]["data"];
            
            #--------------------------Выясним номера "колонок" SECID и SECNAME:Начало------------------------------
            SECID_int:int   = 0;
            SECNAME_int:int = 0;
            
            Columns:dict = Json_data["securities"]["columns"];
            
            cntr:int = -1;
            for key in Columns:
                cntr = cntr+1;
                
                if key == "SECID":
                    SECID_int = cntr;
                if key == "SECNAME":
                    SECNAME_int = cntr;
                    break;         
            #--------------------------Выясним номера "колонок" SECID и SECNAME:Конец------------------------------
            
            
            
            for instruments_item in List_instruments:
                List_instruments_for_Return.append(MOEX_Download__class.Instruments_struct(instruments_item[SECID_int], instruments_item[SECNAME_int]));
                
            return List_instruments_for_Return,None;
        else:
            # Значит ошибка:
            return None, error_text;
             
    def Save_to_CSV__All_Instruments_from_Engine_Market_Board(self, List_Instruments:list[Instruments_struct], path_folder: str, filename: str):
          
        Header_names: list = ["SECID","SECNAME"];
        
        os.makedirs(path_folder, exist_ok=True)  # создаст папку, если её нет
        full_path = os.path.join(path_folder, filename)


        with open(full_path, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=Header_names, delimiter=";", lineterminator="\n");
            writer.writeheader();

            for item in List_Instruments:

                writer.writerow({
                        "SECID": item.SECID,
                        "SECNAME": item.SECNAME,
                    })
                                                   
    def PrintToConsole__All_Instruments_from_Engine_Market_Board(self, List_Instruments:list[Instruments_struct]):
        print("SECID  SECNAME");
        
        for intrument_iter in List_Instruments:
            print(intrument_iter.SECID + ":" + intrument_iter.SECNAME);
    

    def Get__DataCandles(self, Engines_Name:str, Market_Name:str, Board_Name:str, Instrument_Name:str, Interval_string_ID:str, Date_Begin:str, Date_End:str, Callback_for_Load_Info, List_Any_for_Callback:list[any])->tuple[Candle_struct|None, None|str]:
        

        #---------------Проверим корректность соответствия полей в "Candle_enum" и в "self.list_benchmark_Columns_from_MOEX"-----------------------------
        res_check = self._Check_Candle_enum();

        if (res_check != None):
            return res_check;
        #------------------------------------------------------------------------------------------------------------------------------------------------



        #------------------------------------------------------------------------------------
        # Начинаем отсюда: https://iss.moex.com/iss/reference/
        # Запрос на получение данных описан тут: https://iss.moex.com/iss/reference/205       

        
        Candle_struct_:MOEX_Download__class.Candle_struct = MOEX_Download__class.Candle_struct(Instrument_Name, Interval_string_ID, []); 
        #------------------------------------------------------------------------------------



        #````````````````````````````````````````````````````````````````````````````````
        counter_page:int = 0;

        Generate_URL:str = "";

        while True:

            # Цикл крутим до тех пор, пока сервер в своем ответе на запрос не пришел нулевое кол-во свечей.

            #time.sleep(1)  # Небольшая пауза между запросами, чтобы сервер вдруг не забанил.
            

            #-------------------------------------------------Генерируем URL-запроса:Начало-----------------------------------------------

            if (Date_Begin == "" and Date_End == ""):
                Generate_URL = f"https://iss.moex.com/iss/engines/{Engines_Name}/markets/{Market_Name}/boards/{Board_Name}/securities/{Instrument_Name}/candles.json?interval={Interval_string_ID}&start={str(counter_page)}";
            else:
                if (Date_Begin != "" and Date_End == ""):
                    Generate_URL = f"https://iss.moex.com/iss/engines/{Engines_Name}/markets/{Market_Name}/boards/{Board_Name}/securities/{Instrument_Name}/candles.json?interval={Interval_string_ID}&from={Date_Begin}&start={str(counter_page)}";  #Формируем URL-запроса
                else:
                    if (Date_Begin == "" and Date_End != ""):
                         Generate_URL = f"https://iss.moex.com/iss/engines/{Engines_Name}/markets/{Market_Name}/boards/{Board_Name}/securities/{Instrument_Name}/candles.json?interval={Interval_string_ID}&till={Date_End}&start={str(counter_page)}";  #Формируем URL-запроса
                    else:
                        if (Date_Begin != "" and Date_End != ""):
                            Generate_URL = f"https://iss.moex.com/iss/engines/{Engines_Name}/markets/{Market_Name}/boards/{Board_Name}/securities/{Instrument_Name}/candles.json?interval={Interval_string_ID}&from={Date_Begin}&till={Date_End}&start={str(counter_page)}";  #Формируем URL-запроса
          
            #-------------------------------------------------Генерируем URL-запроса:Конец-----------------------------------------------

            #print("Step");
            #print(Generate_URL);

            json_data, exception = self._Get__Http_Request_JSON__NewConnect(Generate_URL);
            
            if (json_data != None):          


                #------------------------Проверка формата JSON:----------------------------
                res_string = self.Check_JSON(json_data);  # Проверим JSON`а Statham`а на СООТВЕТСТВИЕ формату - который используется для разбора из него данных, и если MOEX вдруг изменила формат отдоваемых данных - все сломается и нужон переделывать под новый формат.

                if(res_string != None):
                    # Значит формат изменился.
                    return None, res_string;
                #---------------------------------------------------------------------------



                List_Candles:list[list] = json_data["candles"]["data"];
               

                if (len(List_Candles) > 0):
                    
                    #``````````````````````````````````````````````````````````````````````
                    Candle_struct_.List_Candles_2D.extend(List_Candles);
                    #``````````````````````````````````````````````````````````````````````
                    
                    
                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    String_Range_Start:str = Candle_struct_.List_Candles_2D[0][MOEX_Download__class.Candle_enum.Begin];
                    String_Range_End:str   = Candle_struct_.List_Candles_2D[-1][MOEX_Download__class.Candle_enum.End];

                    if (Callback_for_Load_Info != None):
                        Callback_for_Load_Info(json_data,String_Range_Start, String_Range_End, List_Any_for_Callback);  # Поповещаем Пользователя о том, какой диапазон свечей был загружен в этой итерации цикла, чтобы он видел процесс загрузки и сколько еще осталось. String_Range_Start - всегда будет самой начальной датой.
                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~


                    counter_page = counter_page + len(List_Candles);   # Увеличиваем на кол-во пришедших свечей в поле "data"
                else:
                    return Candle_struct_, None;                       # Значит сервер вернул пустой список свечей, значит дошли до конца. Выходим.
            else:
                return None, str(exception);                  
   
    def PrintToConsole__DataCandles(self, DataCandles_:MOEX_Download__class.Candle_struct):

        print("SECID:" + DataCandles_.SECID);
        print("Interval_string:" + DataCandles_.Interval_string);

        for Candle in DataCandles_.List_Candles_2D:
            print(Candle[MOEX_Download__class.Candle_enum.Open], " ", Candle[MOEX_Download__class.Candle_enum.High], " ", Candle[MOEX_Download__class.Candle_enum.Low], " ", Candle[MOEX_Download__class.Candle_enum.Close], " ", Candle[MOEX_Download__class.Candle_enum.Value], " ", Candle[MOEX_Download__class.Candle_enum.Volume], " ", Candle[MOEX_Download__class.Candle_enum.Begin], " ", Candle[MOEX_Download__class.Candle_enum.End]);
            print();
         
      
    def Get__DataCandles_JSON_Format(self, Request_struct_ref:MOEX_Download__class.Request_struct)->tuple[str|None, None|str]:


        Key:str = Request_struct_ref.Engines_Name + Request_struct_ref.Market_Name + Request_struct_ref.Board_Name+Request_struct_ref.Instrument_Name+Request_struct_ref.Interval_string_ID+Request_struct_ref.Date_Begin+Request_struct_ref.Date_End;
        
        #--------------------------------------------------------
        with self.Mutex:

            if (Key in self.Dict_Request) == True:
                # Значит такой запрос еще в работе. Проверим: если он оставновился из за ошибки, то возобновим скачку с последненй используемой ссылки на которой и произошла ошибака, если поле ошибки == False - значит еще идет скачка и просто делаем return, хотя теоретически данная функция не должна вызватся для Запроса по которому идет активная скачка.

                Obj_ref = self.Dict_Request[Key];

                if (Obj_ref._Error_Flag == True):
                    # Значит ошибка. Просто ничего не делаем и пропускаем выполнение кода дальше - на возобновление скачки.
                    pass
                else:

                    return;  # Ошмбки нет - в данный момент идет активная скачка - просто выходим и не мешаем.
            else:
                # Значит такого запроса в работе нет, доабвим его в Dict_Request:

                self.Dict_Request[Key] = Request_struct_ref;
        #--------------------------------------------------------



        #---------------Проверим корректность соответствия полей в "Candle_enum" и в "self.list_benchmark_Columns_from_MOEX"-----------------------------
        res_check = self._Check_Candle_enum();

        if (res_check != None):
            return res_check;
        #------------------------------------------------------------------------------------------------------------------------------------------------


        #------------------------------------------------------------------------------------
        # Начинаем отсюда: https://iss.moex.com/iss/reference/
        # Запрос на получение данных описан тут: https://iss.moex.com/iss/reference/205       
        #------------------------------------------------------------------------------------



        #----------------------------------------------
        Request_Obj = None;

        with self.Mutex:
            Request_Obj = self.Dict_Request[Key];
        #----------------------------------------------

        if (Request_Obj._Error_Flag == False):
            # Значит это только что добавленный запрос:

            #````````````````````````````````````````````````````````````````````````````````
            while True:

                # Цикл крутим до тех пор, пока сервер в своем ответе на запрос не пришел нулевое кол-во свечей.

                # time.sleep(1)  # Небольшая пауза между запросами, чтобы сервер вдруг не забанил. ЗЫ: короче можно не ставить, и так работает.
        
                self._Generate_URL_Request(Request_Obj);
            
                #-----------------------------------------------------------------------------------------
                res_1, res_2 = self._Func_Http_Request_JSON(Request_Obj, Key);

                if (res_1 != None):
                    if (res_1 == "-1"):
                        # Значит еще не все скачалось, пожтому продолжаем вызывать функцию. То есть ничего не делаем, так как мы под While()
                        pass;
                    else: 
                        if(res_1 == "" or len(res_1) > 0):
                            # Значит скачка завеошена успешно: или скачались все данные или просто MOEX прислал пустые данные.
                            return res_1, res_2;
                else:
                    # Значит ошибка.
                    return res_1, res_2;
                #-----------------------------------------------------------------------------------------

        else:
            # Значит это возобновление скачки после ошибки: То есть возобновляем скачку с URL, который записан в поле "_Last_Use_URL" на котором произошла ошибка.

            while True:

                #-----------------------------------------------------------------------------------------
                res_1, res_2 = self._Func_Http_Request_JSON(Request_Obj, Key);

                if (res_1 != None):
                    if (res_1 == "-1"):
                        # Значит еще не все скачалось, пожтому продолжаем вызывать функцию. То есть ничего не делаем, так как мы под While()
                        pass;
                    else: 
                        if(res_1 == "" or len(res_1) > 0):
                            # Значит скачка завеошена успешно: или скачались все данные или просто MOEX прислал пустые данные.
                            return res_1, res_2;
                else:
                    # Значит ошибка.
                    return res_1, res_2;
                #-----------------------------------------------------------------------------------------

                self._Generate_URL_Request(Request_Obj);


#---------------------------------------------------------------Private:Начало------------------------------------------------------

    def _Generate_URL_Request(self, Request_Obj):

        #-------------------------------------------------Генерируем URL-запроса:Начало-----------------------------------------------

        if (Request_Obj.Date_Begin == "" and Request_Obj.Date_End == ""):
            Request_Obj._Last_Use_URL = f"https://iss.moex.com/iss/engines/{Request_Obj.Engines_Name}/markets/{Request_Obj.Market_Name}/boards/{Request_Obj.Board_Name}/securities/{Request_Obj.Instrument_Name}/candles.json?interval={Request_Obj.Interval_string_ID}&start={str(Request_Obj._counter_page)}";
        else:
            if (Request_Obj.Date_Begin != "" and Request_Obj.Date_End == ""):
                Request_Obj._Last_Use_URL = f"https://iss.moex.com/iss/engines/{Request_Obj.Engines_Name}/markets/{Request_Obj.Market_Name}/boards/{Request_Obj.Board_Name}/securities/{Request_Obj.Instrument_Name}/candles.json?interval={Request_Obj.Interval_string_ID}&from={Request_Obj.Date_Begin}&start={str(Request_Obj._counter_page)}";  #Формируем URL-запроса
            else:
                if (Request_Obj.Date_Begin == "" and Request_Obj.Date_End != ""):
                        Request_Obj._Last_Use_URL = f"https://iss.moex.com/iss/engines/{Request_Obj.Engines_Name}/markets/{Request_Obj.Market_Name}/boards/{Request_Obj.Board_Name}/securities/{Request_Obj.Instrument_Name}/candles.json?interval={Request_Obj.Interval_string_ID}&till={Request_Obj.Date_End}&start={str(Request_Obj._counter_page)}";  #Формируем URL-запроса
                else:
                    if (Request_Obj.Date_Begin != "" and Request_Obj.Date_End != ""):
                        Request_Obj._Last_Use_URL = f"https://iss.moex.com/iss/engines/{Request_Obj.Engines_Name}/markets/{Request_Obj.Market_Name}/boards/{Request_Obj.Board_Name}/securities/{Request_Obj.Instrument_Name}/candles.json?interval={Request_Obj.Interval_string_ID}&from={Request_Obj.Date_Begin}&till={Request_Obj.Date_End}&start={str(Request_Obj._counter_page)}";  #Формируем URL-запроса
          
        #-------------------------------------------------Генерируем URL-запроса:Конец-----------------------------------------------

    def _Func_Http_Request_JSON(self, Request_Obj, Key)->tuple[str|None, None|str]:

        json_data, exception = self._Get__Http_Request_JSON(Request_Obj);

        if (json_data != None):          

            #------------------------Проверка формата JSON:----------------------------
            res_string = self.Check_JSON(json_data);  # Проверим JSON`а Statham`а на СООТВЕТСТВИЕ формату - который используется для разбора из него данных, и если MOEX вдруг изменила формат отдоваемых данных - все сломается и нужон переделывать под новый формат.

            if(res_string != None):
                # Значит формат изменился.
                return None, res_string;
            #---------------------------------------------------------------------------


            List_Candles:list[list] = json_data["candles"]["data"];

            if (len(List_Candles) > 0):

                #------------------------------------------
                Request_Obj._List_Part_Download.append((json.dumps(List_Candles))[1:-1]);       # Добавляем в список очередную пришедшую часть JSON-свчей. Незабываем убирать первый и последний символы - это типа [] первый список, внутри торого влоденный списоек самих свечей.
                #------------------------------------------


                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                String_Range_Start:str = List_Candles[0][6];
                String_Range_End:str   = List_Candles[-1][6];

                if (Request_Obj.Callback_for_Load_Info != None):
                    Request_Obj.Callback_for_Load_Info(json_data,String_Range_Start, String_Range_End, Request_Obj.List_Any_for_Callback);  # Поповещаем Пользователя о том, какой диапазон свечей был загружен в этой итерации цикла, чтобы он видел процесс загрузки и сколько еще осталось. String_Range_Start - всегда будет самой начальной датой.
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~


                Request_Obj._counter_page = Request_Obj._counter_page + len(List_Candles);   # Увеличиваем на кол-во пришедших свечей в поле "data"

                return "-1", None;
            else:

                # Значит сервер вернул пустой список свечей, значит дошли до конца. Выходим и возвращаем результат.

                if (len(Request_Obj._List_Part_Download) > 0):

                    String_Final = "[" + ",".join(Request_Obj._List_Part_Download) + "]";          # Обьеденяем все в один String      

                    with self.Mutex:
                        self.Dict_Request.pop(Key);   # Скачка завершилась успешно, поэтому стурктуру запроса удаляем - так как она больше не нужна.

                    return String_Final, None;        
                else:
                    with self.Mutex:
                        self.Dict_Request.pop(Key);   # Скачка завершилась успешно(просто данных нет), поэтому стурктуру запроса удаляем - так как она больше не нужна.

                    return "", None;   # Значит пришел JSON с пустыми свечами.

        else:
            Request_Obj._Error_Flag = True;

            return None, str(exception);
                

    def _Get__Http_Request_JSON__NewConnect(self, URL_request:str)->tuple[dict|None, str|None]:

        raw_data: bytes | None = None;    # Обьявляем заранее, чтобы в случае искючения она была дсоутпна из "except"

        try:

            with urllib.request.urlopen(URL_request) as response:     # КАЖДЫЙ РАЗ устанавливает новое сокединение с нуля, то есть никакого Keep-Alive нет.

                raw_data: bytes = response.read();

                #json_data = json.loads(raw_data.decode("utf-8")) ;
                json_data = json.loads(raw_data);

                return json_data, None;

        except Exception as e:

            if (raw_data != None):
                # Для случая, когда в ответе может прийти не JSON Statham.

                encoding     = response.headers.get_content_charset() or 'utf-8'   # Получим кодировку из HTML или если не указана использует UTF-8
                data_str     = raw_data.decode(encoding)                           # Преобразуем в строку в соовтетвсвии с кодировкой.
                Text_extract = self.TextExtractor_from_HTML_.extract(data_str);    # Извлечем или попробуем извелчь только текст из HTML - минуя данные скриптов, картинок и прочей ненжности.

                return None, str(e) + ":" + "\n" + Text_extract;
            else:
                return None, str(e);   # Значит ошибка самого HTTPS Соединения.

    def _Get_Connection(self, Request_Obj) -> http.client.HTTPSConnection:
        # Переиспользуем соединение, если оно живо; иначе создаём новое.
        if Request_Obj._http_conn is None:
            Request_Obj._http_conn = http.client.HTTPSConnection(self.http_host, timeout=30)
        return Request_Obj._http_conn

    def _Get__Http_Request_JSON(self, Request_Obj) -> tuple[dict | None, str | None]:
        import time

        raw_data: bytes | None = None

        # Из полного URL убираем домен, оставляем только путь+query

        path = Request_Obj._Last_Use_URL.replace(f"https://{self.http_host}", "")

        try:
            conn = self._Get_Connection(Request_Obj);

            try:
                #t0 = time.monotonic() #>>>>>>>>>>>>>>

                conn.request("GET", path)
                response = conn.getresponse()
                raw_data = response.read()

                #t1 = time.monotonic() #>>>>>>>>>>>>>>
                #print(f"[{Request_Obj._counter_page}] {t1 - t0:.3f} сек") #>>>>>>>>>>>>>>

            except (http.client.HTTPException, ConnectionError, OSError):
                # Соединение могло быть закрыто сервером (keep-alive timeout) — пересоздаём и пробуем ещё раз
                Request_Obj._http_conn = None;
                conn = self._Get_Connection(Request_Obj);

                #t0 = time.monotonic() #>>>>>>>>>>>>>>

                conn.request("GET", path)
                response = conn.getresponse()
                raw_data = response.read()

                #t1 = time.monotonic() #>>>>>>>>>>>>>>
                #print(f"[{Request_Obj._counter_page}] {t1 - t0:.3f} сек") #>>>>>>>>>>>>>>

            json_data = json.loads(raw_data)
            return json_data, None

        except Exception as e:

            if raw_data is not None:
                encoding = response.headers.get_content_charset() or 'utf-8'
                data_str = raw_data.decode(encoding)
                Text_extract = self.TextExtractor_from_HTML_.extract(data_str)
                return None, str(e) + ":" + "\n" + Text_extract
            else:
                return None, str(e)

    def _Reset_Connection(self, Request_Obj):

        if Request_Obj._http_conn is not None:
            Request_Obj._http_conn.close()
            Request_Obj._http_conn = None



    def Check_JSON(self, JSON_MOEX)->None|str:

        # Действубщий формат JSON который приходи c MOEX: на его соответвие и будеи проверить "JSON_MOEX".

        """
        	    {
	    "candles": {
	    "metadata": {
		    "open": {"type": "double"},
		    "close": {"type": "double"},
		    "high": {"type": "double"},
		    "low": {"type": "double"},
		    "value": {"type": "double"},
		    "volume": {"type": "double"},
		    "begin": {"type": "datetime", "bytes": 19, "max_size": 0},
		    "end": {"type": "datetime", "bytes": 19, "max_size": 0}
	    },
	    "columns": ["open", "close", "high", "low", "value", "volume", "begin", "end"], 
	    "data": [
		    [144.02, 143.89, 144.78, 143.03, 599770205.4000001, 4171150, "2014-06-09 10:00:00", "2014-06-09 10:59:59"],
		    [143.86, 144.97, 145.26, 143.57, 1206317361.0000002, 8338580, "2014-06-09 11:00:00", "2014-06-09 11:59:59"],
		    [144.96, 145.3, 146.2, 144.96, 1530742644.3999999, 10507930, "2014-06-09 12:00:00", "2014-06-09 12:59:59"],
		    [145.22, 145.01, 145.47, 144.7, 369374963.79999995, 2546180, "2014-06-09 13:00:00", "2014-06-09 13:59:59"],
		    [145.07, 145.21, 145.5, 144.76, 543374940, 3742340, "2014-06-09 14:00:00", "2014-06-09 14:59:59"],
		    [145.22, 144.86, 145.47, 144.86, 238874904.7, 1645730, "2014-06-09 15:00:00", "2014-06-09 15:59:59"],
		    [144.86, 145.31, 145.77, 144.85, 551761845.9999998, 3799290, "2014-06-09 16:00:00", "2014-06-09 16:59:59"],
		    [145.29, 145.01, 145.42, 144.88, 211899942, 1460330, "2014-06-09 17:00:00", "2014-06-09 17:59:59"],
		    [145.03, 144.7, 145.43, 144.37, 576957581.9000001, 3982260, "2014-06-09 18:00:00", "2014-06-09 18:59:59"],
		    [144.4, 142.95, 144.76, 142.67, 1082133942.7999997, 7541900, "2014-06-10 10:00:00", "2014-06-10 10:59:59"],
		    [142.95, 143.2, 143.2, 142.79, 531498884.00000006, 3715540, "2014-06-10 11:00:00", "2014-06-10 11:59:59"],
		    [143.16, 143.33, 143.68, 142.99, 670457563.9000001, 4677260, "2014-06-10 12:00:00", "2014-06-10 12:59:59"],
		    [143.35, 143.41, 143.58, 143.02, 553291826.2, 3860950, "2014-06-10 13:00:00", "2014-06-10 13:59:59"],
		    [143.39, 144.54, 144.75, 143.16, 848878425.8000002, 5893160, "2014-06-10 14:00:00", "2014-06-10 14:59:59"],
		    [144.51, 144.2, 144.55, 143.91, 548883535.6999999, 3805720, "2014-06-10 15:00:00", "2014-06-10 15:59:59"],
		    [144.15, 143.12, 144.22, 143.07, 535073088.20000005, 3725500, "2014-06-10 16:00:00", "2014-06-10 16:59:59"],
		    [143.12, 143.55, 143.6, 143.06, 312095268.5999999, 2177360, "2014-06-10 17:00:00", "2014-06-10 17:59:59"],
		    [143.55, 144.51, 144.67, 143.37, 808924153.3000002, 5615690, "2014-06-10 18:00:00", "2014-06-10 18:59:59"],
		    [144.75, 145.21, 145.8, 144.21, 1051136941.7999995, 7239070, "2014-06-11 10:00:00", "2014-06-11 10:59:59"],
		    [145.25, 145.1, 145.59, 144.9, 329098434.00000006, 2266580, "2014-06-11 11:00:00", "2014-06-11 11:59:59"],
		    [145.07, 143.91, 145.15, 143.9, 469714854.4, 3247340, "2014-06-11 12:00:00", "2014-06-11 12:59:59"],
		    [143.97, 144.78, 144.8, 143.92, 609529524.4000002, 4221390, "2014-06-11 13:00:00", "2014-06-11 13:59:59"],
		    [144.02, 143.89, 144.78, 143.03, 599770205.4000001, 4171150, "2014-06-12 10:00:00", "2014-06-12 10:59:59"],
		    [144.97, 144.78, 144.8, 143.92, 609529524.4000002, 4221390, "2015-06-11 13:00:00", "2015-06-11 13:59:59"]
			    ]
		    }}
		    """


        #----------------------------------Проверяем наличие Ключа "candles" и его тип:Начало-------------------------------------
        if "candles" in JSON_MOEX:

            # Значит существует. Проверям тип:

            if not isinstance(JSON_MOEX["candles"], dict):   # Проверяем совпадения типов
                # Значит НЕ совпадает
                return "Пришедший JSON формат содержит Ключ <candles> другого типа"

        else:
            # Значит НЕ существует. Выходим.
            return "Пришедший JSON формат не содержит Ключа <candles>"

        #----------------------------------Проверяем наличие Ключа "candles" и его тип:Конец-------------------------------------



        #-----------------------Проверяем наличие Ключа "columns" и его тип:Начало-------------------------
        List_Columns:list[str] = [];


        if "columns" in JSON_MOEX["candles"]:

	        # Значит существует. Проверям тип:

            List_Columns = JSON_MOEX["candles"]["columns"];

            if not isinstance(List_Columns, list) or not all(isinstance(x, str) for x in List_Columns):   # Проверяем совпадения типов
                # Значит НЕ совпадает
                return "Пришедший JSON формат содержит Ключ <columns> другого типа";

        else:
            # Значит НЕ существует. Выходим.
            return "Пришедший JSON формат не содержит Ключа <columns>";

        #-----------------------Проверяем наличие Ключа "columns" и его тип:Конец-------------------------



        #-----------------------Проверяем кол-во и порядок столбцов в "columns":Начало----------------------------------

        if (len(List_Columns) != len(self.list_benchmark_Columns_from_MOEX)):
            # Значит кол-во столбцов не совпадает.
            return "Пришедший JSON формат содержит Ключ <columns> друого размера"
        else:
            if (List_Columns != self.list_benchmark_Columns_from_MOEX):
                # Значит столбцы отличаются.
                return "Пришедший JSON формат содержит Ключ <columns> друого формата"
            
        #-----------------------Проверяем кол-во и порядок столбцов в "columns":Конец----------------------------------




        #-----------------------Проверяем наличие Ключа "data" и его тип:Начало-------------------------

        if "data" in JSON_MOEX["candles"]:

	        # Значит существует. Проверям тип:

         
            if not isinstance(JSON_MOEX["candles"]["data"], list):   # Проверяем совпадения типов
            # Значит НЕ совпадает
                return "Пришедший JSON формат содержит Ключ <data> другого типа";
            else:
            # Значит тип совпадает - это list, но теперь нужно проверить что элеметы этого List - тоже тип list:

                if (len(JSON_MOEX["candles"]["data"]) > 0):

                    List_First_Candle = JSON_MOEX["candles"]["data"][0];  # Возьмем первую свечу.

                    if not isinstance(List_First_Candle, list):
                    # Значит не совпадает.
                        return "Пришедший JSON формат содержит элементы Ключа <data> другого типа";
                
        else:
            # Значит НЕ существует. Выходим.
            return "Пришедший JSON формат не содержит Ключа <data>";

        #-----------------------Проверяем наличие Ключа "data" и его тип:Конец-------------------------



        #-------------------------------------------Проверяем формат даты:Начало----------------------------------------------------------
        if (len(JSON_MOEX["candles"]["data"]) > 0):

            date_string = JSON_MOEX["candles"]["data"][0][6];  # Берем первую свечу и ее дату.

            try:
                date_ = datetime.strptime(date_string, self.Formate_Date_from_MOEX_string)
            except Exception as e:
                return "Формат даты свечи не соответвует формату - " + self.Formate_Date_from_MOEX_string;

        #-------------------------------------------Проверяем формат даты:Конец----------------------------------------------------------

        return None;

    def _Check_Candle_enum(self)->None|str:
        
        #-------------------------Проверим Соответствие полей в "Candle_enum" и в "self.list_benchmark_Columns_from_MOEX":---------------------------
        
        if [e.name.lower() for e in self.Candle_enum] != self.list_benchmark_Columns_from_MOEX:
            return "Поля в <Candle_enum> не соовететвуют <list_benchmark_Columns_from_MOEX>";

        #------------------------------------------------------------------------------------------------------------------------------------------

    class TextExtractor_from_HTML(HTMLParser):
        def __init__(self):
            super().__init__()
            self.text_parts = []
            self.skip = False  # чтобы не брать содержимое <script>/<style>

        def handle_starttag(self, tag, attrs):
            if tag in ('script', 'style'):
                self.skip = True

        def handle_endtag(self, tag):
            if tag in ('script', 'style'):
                self.skip = False

        def handle_data(self, data):
            if not self.skip:
                text = data.strip()
                if text:
                    self.text_parts.append(text)

        def _get_text(self):
            return '\n'.join(self.text_parts)

        @classmethod
        def extract(cls, html: str) -> str:
            parser = cls()
            parser.feed(html)
            return parser._get_text()















