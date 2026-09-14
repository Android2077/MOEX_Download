
from __future__ import annotations
import uuid                                       #  Без этого в собранном pypinstaller`ом exe-шнике - исключение выскакивает, что нету импорта "uuid". Фиг знает почему, добавил, работает и хорошо.
from datetime import datetime
from dataclasses import fields
from dataclasses import dataclass, field
from enum import IntEnum
from enum import StrEnum
from tkinter import END
from typing import ParamSpecArgs, Self
import traceback
import zlib
from typing import Dict, List, Union
from pathlib import Path
import os
import threading
from concurrent.futures import ThreadPoolExecutor
import queue
import time
import sys

import MOEX_Download__class
import DuckDB_StockCandles__class
import Tkinter_GUI__class

import ctypes


Windows_DLL_Candle_DRAWka = True;   # ЕСЛИ НУЖНО ЧТОБЫ РАБОТАЛ ФУНАЦИОНАЛ ОТРИСОВКИ СВЕЧЕЙ ТО СТАВИМ "True" и держим рядом с исполянемым файлом DLL - но естесвенно будет работать только на Винде. "False" - ставим "false" - если нужно азпутсить код на чем-то другом отличным от Винды.




class Create_Window_GUI__class:
    
    @dataclass(slots=True)
    class Engines_Market_Board_Intrument_Intervals_struct:
        Engine:str     = "";
        Market:str     = "";
        Board:str      = "";
        Instrument:str = "";

        Engine_Clear:str     = "";
        Market_Clear:str     = "";
        Board_Clear:str      = "";
        Instrument_Clear:str = "";

        Interval:str  = "";
        Date_FROM:str = "";
        Date_TO:str   = "";

        Path_to_Save:str = "";

    class State_enum(StrEnum):
        Load_from_MOEX = "MOEX"
        Load_from_HDD  = "HDD"
        No_State       = "None"

    def __init__(self):

        self.Tkinter_GUI_obj = Tkinter_GUI__class.Tkinter_GUI__class(); 

        #--------------------------------------
        if (Windows_DLL_Candle_DRAWka == True):

            Path_Execute_Folder:str = self.Tkinter_GUI_obj.Get__ExecuteFile_PathFolder();

            self.my_DDL_Candle_DTAWka = ctypes.CDLL(str(Path(Path_Execute_Folder)/"my_DLL_Candle_DRAWka.dll"));
        #--------------------------------------


        #-------------------------------------
        self.MOEX_Download_       = MOEX_Download__class.MOEX_Download__class();                                  # Класс для скачивания данных свечей с MOEX
        self.DuckDB_StockCandles_ = DuckDB_StockCandles__class.DuckDB_StockCandles__class(self.MOEX_Download_);   # Класс для работы со свечами с помощью DuckDB

        self.State = Create_Window_GUI__class.State_enum.No_State;
        self.Folder_to_Parqet_Files:str = "";
        #-------------------------------------



                
        #----------------------------------------------------------------------------------------------------------
        self.Mutex = threading.Lock();   # Аналог мьютекса из C++.

        self.ThreadPoolExecutor_for_Laod_MOEX_Intrument = ThreadPoolExecutor(max_workers = 5);

        self.NumThread = 5;
        self.ThreadPoolExecutor_MOEX = ThreadPoolExecutor(max_workers = 1);      # Это готовый пул-поток и выполнение задач на них в Python. Типа высокоуровневого аналога std::async из C++.  Для имитиации многопоточности - чтобы Пользователь не видел застывшего окна в момент загрузки данных с MOEX.
        
        self.ThreadPoolExecutor_HDD = ThreadPoolExecutor(max_workers = 1);
        #----------------------------------------------------------------------------------------------------------




        self._Create_GUI();     # Создаем GUI

     

        #----------------------------------------------------------------------------------------------------------
        self.Engine_Market_Board_Delemiter = "<>";

        self.List_All_MOEX_Save = [];
        #----------------------------------------------------------------------------------------------------------


        self.Deque_ThreadSafe = queue.Queue();  # Потоко-безопасная очередь из коробки.

        self._Deque_Loop();


    def Main_Loop(self):
        self.Tkinter_GUI_obj.Main_Loop();


    #-------------------------------------------------------------------PRIVATE:-----------------------------------------------------------------------


    def _Create_GUI(self):

        self.Main_Window_struct   =  self.Tkinter_GUI_obj.Add_window("Main_Window","MOEX сохранение свечей", 800, 600);

        
        self.List_Intervals:list[str] = [Key for Key in self.MOEX_Download_.interval_mapping];
        # self.List_Intervals:list[str] = ["1_min","10_min","1_hour","1_day","1_week","1_month","1_kvartal"];


        #--------------------------------------
        self.With_Percent = 0.42;
        self.Offset_X = 5;
        self.Offset_Y = 5;

        self.Listbox_UserСhoice_Height_Percent = 0.5;
        self.Listbox_Intervals_Height_Percent = 0.40;

        self.With_Percent_Export_Load = 0.45;
        #--------------------------------------



        #--------------------------------------
        self.Treeview_ALLInstruments_MOEX_struct = self.Tkinter_GUI_obj.Add__Treeview(self.Main_Window_struct, "Treeview_ALLInstruments_MOEX");              # Дерево - для загрузки туда данных о всех инструментах MOEX
        self.Listbox_UserСhoice_struct           = self.Tkinter_GUI_obj.Add__OneColumnTable_aka_Listbox(self.Main_Window_struct, "Listbox_UserСhoice");      # Список куда Пользовтаель добавит Инструменты для сохранения из "Treeview_MOEX"
        self.Listbox_Intervals_struct            = self.Tkinter_GUI_obj.Add__Listbox(self.Main_Window_struct, "Listbox_Intervals");                          # Списк c доступными Интервалам MOEX
        
        self.DateTime_FROM                       = self.Tkinter_GUI_obj.Add__Entry_DateTime(self.Main_Window_struct, "DateTime_FROM", "1990-01-30", "%Y-%m-%d");
        self.DateTime_TO                         = self.Tkinter_GUI_obj.Add__Entry_DateTime(self.Main_Window_struct, "DateTime_TO",   "1990-01-30", "%Y-%m-%d");

        self.Label_FROM                          = self.Tkinter_GUI_obj.Add__Label(self.Main_Window_struct, "Label_FROM");
        self.Label_TO                            = self.Tkinter_GUI_obj.Add__Label(self.Main_Window_struct, "Label_TO");
        #--------------------------------------


        #--------------------------------------
        self.Button_Initial_Load_from_MOEX     = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_Initial_Load_from_MOEX");   # Кнопка для первончальной загркзки списка всех Классов с MOEX
        self.Button_Initial_Load_from_HDD      = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_Initial_Load_from_HDD");    # Кнопка для загрузки списка всех сохранненых Parquet-файлов для дальнейшео выбора и преобразванеия их в CSV
        #--------------------------------------

        #--------------------------------------
        self.Button_Export           = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_Export"); 
        self.Button_Load             = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_Load"); 

        self.Button_AddAll           = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_AddAll"); 
        self.Button_Add              = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_Add"); 
        self.Button_DeleteAll        = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_DeleteAll"); 
        self.Button_Delete           = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_Delete"); 
        self.Button_Height           = 25;
        self.Button_Offset_Y         = 5;
        self.Button_Offset_H         = 7;
        self.Button_Widht_Scale      = 0.27;


        self.Button_by_Intervals_AddAll           = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_by_Intervals_AddAll"); 
        self.Button_by_Intervals_Add              = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_by_Intervals_Add"); 
        self.Button_by_Intervals_DeleteAll        = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_by_Intervals_DeleteAll"); 
        self.Button_by_Intervals_Delete           = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_by_Intervals_Delete"); 
        #--------------------------------------


        #--------------------------------------
        self.Button_Popup_for_UserLoad            = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_Popup_for_UserLoad");  
        #--------------------------------------



        #--------------------------------------
        self.Button_Final_Load = self.Tkinter_GUI_obj.Add__Button(self.Main_Window_struct, "Button_Final_Load"); 
        #--------------------------------------


        #----------------------------------------------------
        self.Treeview_ALLInstruments_MOEX_struct.Set_Font_Size(12);
        self.Treeview_ALLInstruments_MOEX_struct.Set_Select_Mode(self.Tkinter_GUI_obj.Treeview_SelectMode_enum.extended);

        self.Listbox_UserСhoice_struct.Set_Font_Size(12);

        self.Listbox_Intervals_struct.Set_Font_Size(12);
        self.Listbox_Intervals_struct.Set_Select_Mode(self.Tkinter_GUI_obj.Listbox_SelectMode_enum.EXTENDED);
        #----------------------------------------------------



        #----------------------------------------------------
        self.Button_by_Intervals_Delete_Add_UserСhoice_Select:bool = False;
        self.Button_by_Intervals_Delete_Add_Intervals_Select:bool  = False;
        #----------------------------------------------------


        #----------------------------------------------------
        self.Window_for_Table_Instrument_Load   = self.Tkinter_GUI_obj.Add_window("Window_for_Table_Instrument_Load","Таблица загрузки Инструментов MOEX", 600, 400);
        self.Window_for_Table_Instrument_Load.Hidden();
        self.Table_Instrument_Load              = self.Tkinter_GUI_obj.Add__Table(self.Window_for_Table_Instrument_Load, "Table_Instrument_Load", [ ["Engine", "Engine"], ["Marker", "Marker"], ["Board", "Board"], ["Status_Load", "Статус загрузки"]]);          # Для показа процесса загрузки.
        
        self.Window_for_Table_Candles_Load      = self.Tkinter_GUI_obj.Add_window("Window_for_Table_Candles_Load","Таблица загрузки Свечей", 900, 400);
        self.Window_for_Table_Candles_Load.Hidden();
        self.Table_Candles_Load                 = self.Tkinter_GUI_obj.Add__Table(self.Window_for_Table_Candles_Load, "Table_Candles_Load", [["Engine", "Engine"], ["Marker", "Marker"], ["Board", "Board"], ["Intrument", "Intrument"], ["Interval", "Интервал"],["Date_FROM", "Дата От"] ,["Date_TO", "Дата До"], ["Path_to_Save", "Путь сохранения"], ["Status_Load", "Статус загрузки"]]);  # Для показа процесса загрузки.
        
        self.Window_for_Table_Transform_to_CSV       = self.Tkinter_GUI_obj.Add_window("Window_for_Table_Transform_to_CSV","Таблица преобразования в CSV", 900, 400);
        self.Window_for_Table_Transform_to_CSV.Hidden();
        self.Table_Transform_to_CSV                  = self.Tkinter_GUI_obj.Add__Table(self.Window_for_Table_Transform_to_CSV, "Table__Transform_to_CSV", [["Engine", "Engine"], ["Marker", "Marker"], ["Board", "Board"], ["Intrument", "Intrument"], ["Interval", "Интервал"], ["Date_FROM", "Дата От"] ,["Date_TO", "Дата До"], ["Path_to_Save", "Путь сохранения"], ["Status_Load", "Статус"]]);  # Для показа процесса загрузки.
        
        self.Button_Popup_Instrument_Reload             = self.Tkinter_GUI_obj.Add__Button(self.Window_for_Table_Instrument_Load, "Button_Intrument_Reload"); 
        self.Button_Popup_Candles_Reload                = self.Tkinter_GUI_obj.Add__Button(self.Window_for_Table_Candles_Load, "Button_Popup_Candles_Reload");
        self.Button_Popup_Transform_to_CSV_Reload       = self.Tkinter_GUI_obj.Add__Button(self.Window_for_Table_Transform_to_CSV, "Button_Popup_Transform_to_CSV_Reload");
        #----------------------------------------------------


        #---------------------------------------------------
        self.Classic_Menu = self.Tkinter_GUI_obj.Set__Classic_Menu(self.Main_Window_struct, "Classic_Menu");

        self.Window_for_SendError = self.Tkinter_GUI_obj.Add_window("Window_for_SendError","Информация", 250, 50);

        self.Window_for_SendError.Hidden();

        self.Window_for_SendError.Set_NotCloseWindow_but_Hidden();
        #---------------------------------------------------

        #---------------------------------------------------
        self.Input_Thread = self.Tkinter_GUI_obj.Add__Inputbox(self.Main_Window_struct, "Input_Thread"); 
        #---------------------------------------------------



        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



        self._Set_Treeview();                      # Устанавливаем размер и позицию Treeview-виджета.

        self._Set_Listbox_UserСhoice();            # Устанавливаем размер и позицию OneColumnTable_aka_Listbox-виджета

        self._Set_Button();                        # Кнопки для "перетскивания" Иснтурментов из Левого Списка в Правый:Добавить, Добваить Все, Удалить, Удалить Все
        
        self._Set_Button_Export_Load();            # Кнопки: Эксорт и Загрузить

        self._Set_DateTime();                      # Установка Выбора Даты-Времени ОТ и ДО

        self._Set_Button_For_Intervals();          # Кнопки под Списком выбора Интервалов:Добавить, Добваить Все, Удалить, Удалить Все

        self._Set_Button_Popup_for_UserLoad();     # "Всплывающая" кнопка загрузки конечных Инструментов/или рисовалка

        self._Set_Buttons_Popup_Reload();          # Копки для "перезагрузки" данных с сервера.
      
        self._Set_List_Intervals();                # Устанавливаем размер и позицию Списка в котором будут Интервалы для выбора

        self._Set_Button_Final_Load();                   # И последняя кнопка "SAVE"


        self._Set_Table_Instrument_Load();         #
        self._Set_Table_Candles_Load();            #
        self._Set_Table_Transform_to_CSV();        #

        self.Main_Window_struct.Add__Resizible_Callback(self._Window_Resize_Callback, []);          # Ставим колбекум, чтобы Виджеты изменялись в месте с изменнеим размера Главного окна.
        self.Main_Window_struct.Set_Overriding_Сlose_Callback(self._Window_Overriding_Сlose, []);   # Ставим колбек на закрытие Оснвного окна.


        self._Set_Button_Callback();               # Устанавливаем колбеки на кнопки.
        self._Set_SelectRow_Callback();            # Устанавливаем колбеки на Выделение/Дэвыделения строк в списках.
        self._Set_Callback_for_Empty();            # Устанавливаем колбек на "Listbox_UserСhoice_struct" на переход от Пустого к Наполенному и от Наполненного к Пустому.

        self._Set_Intervals();                     # Установим списое интервалов в окно.

        self._Set_Treeview_Right_Left_Click_Callback();             # Устанавливаем колбек на клик правой кнопкой мыши.
        self._Set_Table_Instrument_Load_Click_for_Cell();           # УСтановка колбека на клик мыши по ячейке таблицы.
        self._Set_Table_Candles_ReLoadClick_for_Cell();             # УСтановка колбека на клик мыши по ячейке таблицы.
        self._Set_Table_Transform_to_CSV_ReLoadClick_for_Cell();    # УСтановка колбека на клик мыши по ячейке таблицы.

        self._Set_Classic_Menu();

        self._Set_InputBox();

    #---------------------------------------------------------------------------------------------
    def _Initial_Load_from_MOEX(self)->bool:
        
        #---------------------------------------------------------
        self.Treeview_ALLInstruments_MOEX_struct.Clear_All();  # Очистим от возможных предыдщуих записей.
        
        self.Listbox_UserСhoice_struct.Delete_All();           # Очистим от возможных предыдщуих записей.
        #---------------------------------------------------------


        self.Table_Transform_to_CSV.Clear_All();


        #----------------------------------Запросим ВСЕ Инструменты MOEX:Начало-------------------------------------
        List_All_Intruments_MOEX, Text_Error = self._Request_ALL_INSTRUMENTS_MOEX();

        if(List_All_Intruments_MOEX != None):
            #self.MOEX_Download_.PrintToConsole__ALL_List_Engines_Market_Board_from_MOEX(List_All_Intruments_MOEX);

            Dict__All_Intruments_MOEX = self.MOEX_Download_.Convert_List_Engines_Market_Board_to_Dictonary(List_All_Intruments_MOEX);

            self.Treeview_ALLInstruments_MOEX_struct.Set_DictonaryTree(Dict__All_Intruments_MOEX);
            self.Treeview_ALLInstruments_MOEX_struct.Set_Font_Size(12);
        else:
            tb_str = traceback.format_exc();

            self.Tkinter_GUI_obj.Call_MessageBox("Сообщение об ошибке", Text_Error + ":\n" + tb_str);

            return False;

        self.Treeview_ALLInstruments_MOEX_struct.Sort_as_Text(self.Tkinter_GUI_obj.Sort_enum.ascending);  # Отсортируем

        self.Button_AddAll.Set_Active(True);
        #----------------------------------Запросим ВСЕ Инструменты MOEX:Конец-------------------------------------


        self.List_All_MOEX_Save = self.Treeview_ALLInstruments_MOEX_struct.Get_AllRows_Flat_List(self.Engine_Market_Board_Delemiter);

        return True;

    def _Initial_Load_from_HDD(self)->bool:
        
        #---------------------------------------------------------
        self.Treeview_ALLInstruments_MOEX_struct.Clear_All();  # Очистим от возможных предыдщуих записей.
        
        self.Listbox_UserСhoice_struct.Delete_All();           # Очистим от возможных предыдщуих записей.
        #---------------------------------------------------------



        #--------------------------------------------------Выбираем папку каталога Parqet-файлов:Начало------------------------------------------

        Path_to_Folder:str = self.Tkinter_GUI_obj.DialogMenu__Choose_Folder(self.Tkinter_GUI_obj.Get__ExecuteFile_PathFolder());

        if (Path_to_Folder == ""):
            # Значит Пользовтаель отменил выбор. Выходим.
            return;


        self.Folder_to_Parqet_Files = Path_to_Folder;

        #--------------------------------------------------Выбираем папку каталога Parqet-файлов:Конец------------------------------------------


        self.Table_Instrument_Load.Clear_All();


        #---------------------------------------------------------------------------------------------
        def Get__Treeview_from_Folder(Path_to_Folder: str) -> Dict:
            """
            Строит дерево вложенных папок для указанного пути.
            Файлы игнорируются полностью.
            Если у папки нет вложенных подпапок - её значение = [] (пустой список).
            Если есть - значение = Dict с рекурсивно тем же форматом.
            """
            result = {}

            try:
                entries = os.scandir(Path_to_Folder)
            except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
                raise ValueError(f"Не удалось прочитать папку '{Path_to_Folder}': {e}")

            with entries:
                for entry in entries:
                    try:
                        is_dir = entry.is_dir(follow_symlinks=False)
                    except OSError:
                        # entry исчез или недоступен (гонка, битый симлинк и т.п.) - пропускаем
                        continue

                    if is_dir:
                        try:
                            subtree = Get__Treeview_from_Folder(entry.path)
                        except ValueError:
                            # папка пропала/стала недоступна между scandir и рекурсивным вызовом
                            subtree = []
                        result[entry.name] = subtree if subtree else []

            return result
 

        Dict_return = Get__Treeview_from_Folder(Path_to_Folder);
        #print(Dict_return);

        self.Treeview_ALLInstruments_MOEX_struct.Set_DictonaryTree(Dict_return);
        self.Treeview_ALLInstruments_MOEX_struct.Set_Font_Size(12);
        self.Treeview_ALLInstruments_MOEX_struct.Set_Select_Mode(self.Tkinter_GUI_obj.Treeview_SelectMode_enum.extended);

        self.Button_AddAll.Set_Active(True);
    #---------------------------------------------------------------------------------------------


    def _Set_DateTime(self):

        self.Label_FROM.Set_AutoSize_by_Text();
        self.Label_TO.Set_AutoSize_by_Text();

        self.Label_FROM.Set_Font_Size(13);
        self.Label_TO.Set_Font_Size(13);

        self._Set_DateTime_Pos();

        self.Label_FROM.Set_Text("От:");
        self.Label_TO.Set_Text("До:");

        self.Label_FROM.Set_Background_Color("Green");
        self.Label_TO.Set_Background_Color("Green");

   
        self._Set_DateTime_Width();

        self.DateTime_FROM.Set_Pos_AutoFollow_to_Widget(self.Tkinter_GUI_obj.Anchor_enum.TopLeft, self.Label_FROM.Obj, self.Tkinter_GUI_obj.Anchor_Relative_enum.TopRight, 3, -2);
        self.DateTime_TO.Set_Pos_AutoFollow_to_Widget(  self.Tkinter_GUI_obj.Anchor_enum.TopLeft, self.Label_TO.Obj, self.Tkinter_GUI_obj.Anchor_Relative_enum.TopRight, 3, -2);
        

        self.DateTime_FROM.Set_Font_Size(13);
        self.DateTime_TO.Set_Font_Size(13);

    def _Set_DateTime_Width(self):

        Date_width = self.Listbox_UserСhoice_struct.Get__BOTTOM_RIGHT_Pos().x - self.Label_FROM.Get__BOTTOM_RIGHT_Pos().x - 2;

        self.DateTime_FROM.Set_PixelSize(Date_width, self.Label_FROM.Get__Size().height);
        self.DateTime_TO.Set_PixelSize(Date_width,   self.Label_TO.Get__Size().height);

    def _Set_DateTime_Pos(self):

        self.Label_TO.Set_Pos(self.Listbox_UserСhoice_struct.Get__BOTTOM_LEFT_Pos().x, self.Main_Window_struct.Get__BOTTOM_RIGHT_Inner_Pos().y - self.Offset_Y, self.Tkinter_GUI_obj.Anchor_enum.BottomLeft);
        self.Label_FROM.Set_Pos(self.Label_TO.Get__BOTTOM_LEFT_Pos().x, self.Label_TO.Get__TOP_LEFT_Pos().y - self.Offset_Y, self.Tkinter_GUI_obj.Anchor_enum.BottomLeft);

        
    def _Set_Treeview(self):
 
        self.Treeview_ALLInstruments_MOEX_struct.Set_Size_AutoFollow_to_Widget(self.Main_Window_struct.Obj, self.With_Percent, 1, 0, - (2*self.Offset_Y + self.Offset_Y + self.Button_Height));

        self.Treeview_ALLInstruments_MOEX_struct.Set_Pos(self.Offset_X, self.Offset_Y, Tkinter_GUI__class.Tkinter_GUI__class.Anchor_enum.TopLeft);

    def _Set_Listbox_UserСhoice(self):

        self.Listbox_UserСhoice_struct.Set_Size_AutoFollow_to_Widget(self.Main_Window_struct.Obj, self.With_Percent, self.Listbox_UserСhoice_Height_Percent, 0, 0);

        self.Listbox_UserСhoice_struct.Set_Pos_AutoFollow_to_Widget( self.Tkinter_GUI_obj.Anchor_enum.TopRight, self.Main_Window_struct.Obj, self.Tkinter_GUI_obj.Anchor_Relative_enum.TopRight, -(self.Offset_X),  self.Offset_Y);


    def _Set_Button(self):

        # Лень описывать действия.
        
        self._Set_Button_width();

        
        self.Button_Initial_Load_from_MOEX.Set_Height(self.Button_Height);
        self.Button_Initial_Load_from_MOEX.Set_Width(self.Treeview_ALLInstruments_MOEX_struct.Get__Size().width/2 - self.Offset_X);  # Ставим изначальную шиирну равную половины окна со списком загружаемых инстурметов

        self.Button_Initial_Load_from_HDD.Set_Height(self.Button_Height);
        self.Button_Initial_Load_from_HDD.Set_Width(self.Treeview_ALLInstruments_MOEX_struct.Get__Size().width/2 - self.Offset_X);   # Ставим изначальную шиирну равную половины окна со списком загружаемых инстурметов

        self.Button_Initial_Load_from_MOEX.Set_Size_AutoFollow_to_Widget(self.Treeview_ALLInstruments_MOEX_struct.Container, 0.48, -1, 0, 0);
        self.Button_Initial_Load_from_HDD.Set_Size_AutoFollow_to_Widget(self.Treeview_ALLInstruments_MOEX_struct.Container, 0.48, -1, 0, 0);




        self.Button_Add.Set_Height(self.Button_Height);
        self.Button_AddAll.Set_Height(self.Button_Height);
        self.Button_Delete.Set_Height(self.Button_Height);
        self.Button_DeleteAll.Set_Height(self.Button_Height);


        self.Button_Initial_Load_from_MOEX.Set_Pos_AutoFollow_to_Widget(self.Tkinter_GUI_obj.Anchor_enum.BottomLeft, self.Treeview_ALLInstruments_MOEX_struct.Container, self.Tkinter_GUI_obj.Anchor_Relative_enum.BottomLeft, 0,  + self.Button_Offset_Y + self.Button_Height);
        self.Button_Initial_Load_from_HDD.Set_Pos_AutoFollow_to_Widget(self.Tkinter_GUI_obj.Anchor_enum.BottomRight, self.Treeview_ALLInstruments_MOEX_struct.Container, self.Tkinter_GUI_obj.Anchor_Relative_enum.BottomRight, 0, + self.Button_Offset_Y + self.Button_Height);

        self.Button_AddAll.Set_Pos_AutoFollow_to_Widget(self.Tkinter_GUI_obj.Anchor_enum.BottomRight, self.Listbox_UserСhoice_struct.Container, self.Tkinter_GUI_obj.Anchor_Relative_enum.Left_Middle, -self.Button_Offset_H,  -(self.Button_Offset_Y));     
        self.Button_Add.Set_Pos_AutoFollow_to_Widget(self.Tkinter_GUI_obj.Anchor_enum.BottomRight, self.Listbox_UserСhoice_struct.Container, self.Tkinter_GUI_obj.Anchor_Relative_enum.Left_Middle, -self.Button_Offset_H,  -(2*self.Button_Offset_Y + self.Button_Height));
        self.Button_DeleteAll.Set_Pos_AutoFollow_to_Widget(self.Tkinter_GUI_obj.Anchor_enum.TopRight, self.Listbox_UserСhoice_struct.Container, self.Tkinter_GUI_obj.Anchor_Relative_enum.Left_Middle, -self.Button_Offset_H,  +(self.Button_Offset_Y));     
        self.Button_Delete.Set_Pos_AutoFollow_to_Widget(self.Tkinter_GUI_obj.Anchor_enum.TopRight, self.Listbox_UserСhoice_struct.Container, self.Tkinter_GUI_obj.Anchor_Relative_enum.Left_Middle, -self.Button_Offset_H,  +(2*self.Button_Offset_Y + self.Button_Height));
        

        self.Button_Initial_Load_from_MOEX.Set_Background_Color("sky blue");
        self.Button_Initial_Load_from_HDD.Set_Background_Color("sky blue");

        self.Button_Add.Set_Background_Color("sky blue");
        self.Button_AddAll.Set_Background_Color("sky blue");
        self.Button_Delete.Set_Background_Color("sky blue");
        self.Button_DeleteAll.Set_Background_Color("sky blue");


        self.Button_Initial_Load_from_MOEX.Set_Text("Загрузить с MOEX");
        self.Button_Initial_Load_from_HDD.Set_Text("Загрузить c HDD");

        self.Button_Add.Set_Text("Добавить");
        self.Button_AddAll.Set_Text("Добавить все");
        self.Button_Delete.Set_Text("Удалить");
        self.Button_DeleteAll.Set_Text("Удалить все");

        self.Button_Add.Set_Active(False);
        self.Button_AddAll.Set_Active(False);
        self.Button_Delete.Set_Active(False);
        self.Button_DeleteAll.Set_Active(False);

    def _Set_Button_width(self):

        Width_ = self.Listbox_UserСhoice_struct.Get__TOP_LEFT_Pos().x - self.Treeview_ALLInstruments_MOEX_struct.Get__TOP_RIGHT_Pos().x - 2*self.Button_Offset_H;
       
        self.Button_Add.Set_Width(Width_);
        self.Button_AddAll.Set_Width(Width_);
        self.Button_Delete.Set_Width(Width_);
        self.Button_DeleteAll.Set_Width(Width_);




    def _Set_Button_Export_Load(self):

        self.Button_Export.Set_Height(self.Button_Height);
        self.Button_Load.Set_Height(self.Button_Height);

        self.Button_Export.Set_Size_AutoFollow_to_Widget(self.Listbox_UserСhoice_struct.Container, self.With_Percent_Export_Load, -1, 0, 0);
        self.Button_Load.Set_Size_AutoFollow_to_Widget(self.Listbox_UserСhoice_struct.Container, self.With_Percent_Export_Load, -1, 0, 0);

        self.Button_Export.Set_Pos_AutoFollow_to_Widget(self.Tkinter_GUI_obj.Anchor_enum.TopLeft, self.Listbox_UserСhoice_struct.Container, self.Tkinter_GUI_obj.Anchor_Relative_enum.BottomLeft, -1,  1);
        self.Button_Load.Set_Pos_AutoFollow_to_Widget(self.Tkinter_GUI_obj.Anchor_enum.TopRight, self.Listbox_UserСhoice_struct.Container, self.Tkinter_GUI_obj.Anchor_Relative_enum.BottomRight, 0,  1);
        

        self.Button_Export.Set_Text("Экспорт");
        self.Button_Load.Set_Text("Загрузить");

        self.Button_Export.Set_Background_Color("sky blue");
        self.Button_Load.Set_Background_Color("sky blue");

        self.Button_Export.Set_Active(False);


    def _Set_Button_For_Intervals(self):
               
        self._Set_Button_For_Intervals_Size_Pos();

        self.Button_by_Intervals_Add.Set_Height(self.Button_Height);
        self.Button_by_Intervals_AddAll.Set_Height(self.Button_Height);
        self.Button_by_Intervals_Delete.Set_Height(self.Button_Height);
        self.Button_by_Intervals_DeleteAll.Set_Height(self.Button_Height);
      
        self.Button_by_Intervals_Add.Set_Background_Color("sky blue");
        self.Button_by_Intervals_AddAll.Set_Background_Color("sky blue");
        self.Button_by_Intervals_Delete.Set_Background_Color("sky blue");
        self.Button_by_Intervals_DeleteAll.Set_Background_Color("sky blue");

        self.Button_by_Intervals_Add.Set_Text("Добавить");
        self.Button_by_Intervals_AddAll.Set_Text("Добавить все");
        self.Button_by_Intervals_Delete.Set_Text("Удалить");
        self.Button_by_Intervals_DeleteAll.Set_Text("Удалить все");
 
        self.Button_by_Intervals_Add.Set_Active(False);
        self.Button_by_Intervals_AddAll.Set_Active(False);
        self.Button_by_Intervals_Delete.Set_Active(False);
        self.Button_by_Intervals_DeleteAll.Set_Active(False);

    def _Set_Button_For_Intervals_Size_Pos(self):

        width_ = self.Button_Export.Get__Size().width;

        self.Button_by_Intervals_Add.Set_Width(width_);
        self.Button_by_Intervals_AddAll.Set_Width(width_);
        self.Button_by_Intervals_Delete.Set_Width(width_);
        self.Button_by_Intervals_DeleteAll.Set_Width(width_);
            
        self.Button_by_Intervals_Add.Set_Pos(self.Label_FROM.Get__TOP_LEFT_Pos().x,                        self.Label_FROM.Get__TOP_LEFT_Pos().y                  - self.Offset_Y-5,     self.Tkinter_GUI_obj.Anchor_enum.BottomLeft);
        self.Button_by_Intervals_Delete.Set_Pos(self.DateTime_FROM.Get__TOP_RIGHT_Pos().x,                 self.DateTime_FROM.Get__TOP_RIGHT_Pos().y              - self.Offset_Y-5,     self.Tkinter_GUI_obj.Anchor_enum.BottomRight);
        self.Button_by_Intervals_AddAll.Set_Pos(self.Button_by_Intervals_Add.Get__TOP_LEFT_Pos().x,        self.Button_by_Intervals_Add.Get__TOP_LEFT_Pos().y     - self.Offset_Y-5,     self.Tkinter_GUI_obj.Anchor_enum.BottomLeft);
        self.Button_by_Intervals_DeleteAll.Set_Pos(self.Button_by_Intervals_Delete.Get__TOP_LEFT_Pos().x,  self.Button_by_Intervals_Delete.Get__TOP_LEFT_Pos().y  - self.Offset_Y-5,     self.Tkinter_GUI_obj.Anchor_enum.BottomLeft);


    def _Set_Button_Popup_for_UserLoad(self):

        self.Button_Popup_for_UserLoad.Set_Height(self.Button_Height);
        self.Button_Popup_for_UserLoad.Set_Background_Color("sky blue");
        self.Button_Popup_for_UserLoad.Set_Text("Загрузить");
        self.Button_Popup_for_UserLoad.Set_Active(True);
        self.Button_Popup_for_UserLoad.Set_Show(False);

    def _Set_Buttons_Popup_Reload(self):

        self.Button_Popup_Instrument_Reload.Set_Height(self.Button_Height);
        self.Button_Popup_Instrument_Reload.Set_Background_Color("sky blue");
        self.Button_Popup_Instrument_Reload.Set_Text("Пере-Загрузить");
        self.Button_Popup_Instrument_Reload.Set_Active(True);
        self.Button_Popup_Instrument_Reload.Set_Show(False);

        self.Button_Popup_Candles_Reload.Set_Height(self.Button_Height);
        self.Button_Popup_Candles_Reload.Set_Background_Color("sky blue");
        self.Button_Popup_Candles_Reload.Set_Text("Пере-Загрузить");
        self.Button_Popup_Candles_Reload.Set_Active(True);
        self.Button_Popup_Candles_Reload.Set_Show(False);

        self.Button_Popup_Transform_to_CSV_Reload.Set_Height(self.Button_Height);
        self.Button_Popup_Transform_to_CSV_Reload.Set_Background_Color("sky blue");
        self.Button_Popup_Transform_to_CSV_Reload.Set_Text("Пере-Сохранить");
        self.Button_Popup_Transform_to_CSV_Reload.Set_Active(True);
        self.Button_Popup_Transform_to_CSV_Reload.Set_Show(False);


    def _Set_List_Intervals(self):

        self.Listbox_Intervals_struct.Set_Size(self.Listbox_UserСhoice_struct.Get__Size().width, self.Button_by_Intervals_DeleteAll.Get__TOP_LEFT_Pos().y  - self.Button_Export.Get__BOTTOM_LEFT_Pos().y - self.Offset_Y*2);

        self.Listbox_Intervals_struct.Set_Pos(self.Button_Export.Get__BOTTOM_LEFT_Pos().x, self.Button_Export.Get__BOTTOM_LEFT_Pos().y + self.Offset_Y*2, self.Tkinter_GUI_obj.Anchor_enum.TopLeft);
         
    
    def _Set_Button_Final_Load(self):

        self._Set_Button_Final_Load_Size_Pos();

        self.Button_Final_Load.Set_Text("Загрузить");
        self.Button_Final_Load.Set_Background_Color("sky blue");

    def _Set_Button_Final_Load_Size_Pos(self):
        
        self.Button_Final_Load.Set_Size(self.Button_Delete.Get__Size().width, self.Button_Height);

        self.Button_Final_Load.Set_Pos(self.Treeview_ALLInstruments_MOEX_struct.Get__BOTTOM_RIGHT_Pos().x + self.Offset_X,  self.Treeview_ALLInstruments_MOEX_struct.Get__BOTTOM_RIGHT_Pos().y,  self.Tkinter_GUI_obj.Anchor_enum.BottomLeft);


    def _Set_Table_Instrument_Load(self):

        self.Window_for_Table_Instrument_Load.Set_NotCloseWindow_but_Hidden();

        self.Table_Instrument_Load.Set_to_Window_Fit(0,0);

        self.Table_Instrument_Load.Set_All_Columns_Equal_Width();

    def _Set_Table_Candles_Load(self):
        
        self.Window_for_Table_Candles_Load.Set_NotCloseWindow_but_Hidden();

        self.Table_Candles_Load.Set_to_Window_Fit(0,0);

        self.Table_Candles_Load.Set_All_Columns_Equal_Width();

    def _Set_Table_Transform_to_CSV(self):
        
        self.Window_for_Table_Transform_to_CSV.Set_NotCloseWindow_but_Hidden();

        self.Table_Transform_to_CSV.Set_to_Window_Fit(0,0);

        self.Table_Transform_to_CSV.Set_All_Columns_Equal_Width();


    def _Window_Resize_Callback(self, Tkinter_GUI__obj:Tkinter_GUI__class, Main_Window_struct:Tkinter_GUI__class.Main_Window_struct, With:int, Height:int, List_any:list[any]):
        # Вызываетя при изменеии размера окна Пользователем.
        

         self._Set_Button_width();                     # Устанавливае размер кнопок

         self._Set_DateTime_Pos();                     # Устанавлваем Позиции Label "ОТ" и "ДО" для Даты-Времени

         self._Set_DateTime_Width();                   # Устанавлваем Ширины Label "ОТ" и "ДО" для Даты-Времени

         self._Set_Button_For_Intervals_Size_Pos();    # Кнопки для Списка выбора Интервалов

         self._Set_List_Intervals();                   # Задаем размер и позицию Списка с Интервалами

         self._Set_Button_Final_Load_Size_Pos();             # Размер и положение кнопки "Save"

    def _Window_Overriding_Сlose(self, Window_struct:Tkinter_GUI__class.Window_struct, List_any:list[any]):

        self.Window_for_Table_Instrument_Load.Close();
        self.Window_for_Table_Candles_Load.Close();

        Window_struct.Close();

        self.ThreadPoolExecutor_for_Laod_MOEX_Intrument.shutdown(wait=False, cancel_futures=True);

        self.ThreadPoolExecutor_MOEX.shutdown(wait=False, cancel_futures=True);
        
        self.ThreadPoolExecutor_HDD.shutdown(wait=False, cancel_futures=True);

        os._exit(0);



    def _Set_Button_Callback(self):

        self.Button_Initial_Load_from_MOEX.Add_Click_Callback(self._Button_Initial_Load_from_MOEX_Callback, []);
        self.Button_Initial_Load_from_HDD.Add_Click_Callback(self._Button_Initial_Load_from_HDD_Callback, []);

        #--------------------------------------
        self.Button_Export.Add_Click_Callback(self._Button_Export_Callback, []);
        self.Button_Load.Add_Click_Callback(self._Button_Load_Callback, []);

        self.Button_AddAll.Add_Click_Callback(self._Button_AddAll_Callback, []);
        self.Button_Add.Add_Click_Callback(self._Button_Add_Callback, []); 
        self.Button_DeleteAll.Add_Click_Callback(self._Button_DeleteAll_Callback, []); 
        self.Button_Delete.Add_Click_Callback(self._Button_Delete_Callback, []);

        self.Button_by_Intervals_AddAll.Add_Click_Callback(self._Button_by_Intervals_AddAll_Callback, []); 
        self.Button_by_Intervals_Add.Add_Click_Callback(self._Button_by_Intervals_Add_Callback, []);
        self.Button_by_Intervals_DeleteAll.Add_Click_Callback(self._Button_by_Intervals_DeleteAll_Callback, []); 
        self.Button_by_Intervals_Delete.Add_Click_Callback(self._Button_by_Intervals_Delete_Callback, []); 
        #--------------------------------------

        #--------------------------------------
        self.Button_Popup_for_UserLoad.Add_Click_Callback(self._Button_Popup_for_UserLoad_Callback, []);

        self.Button_Popup_Instrument_Reload.Add_Click_Callback(self._Button_Popup_for_Instrument_Reload_Callback, []);
        self.Button_Popup_Candles_Reload.Add_Click_Callback(self._Button_Popup_for_Candles_Reload_Callback, []);
        self.Button_Popup_Transform_to_CSV_Reload.Add_Click_Callback(self._Button_Popup_for_Transform_to_CSV_Reload_Callback, []);
        #--------------------------------------

        #--------------------------------------
        self.Button_Final_Load.Add_Click_Callback(self._Button_Final_Load_Callback, []);
        #--------------------------------------

    def _Button_Initial_Load_from_MOEX_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):

        self.State = Create_Window_GUI__class.State_enum.Load_from_MOEX;  # Ставим статус чтобы различать с каким режимом сейчас работает Пользователь.

        res:bool = self._Initial_Load_from_MOEX();      # Загружаем первончальный список инструментов с MOEX

        self.Set_Name_Final_Button_by_State();  # Поменяем текст Финальной кнопки в зависимости от State

    def _Button_Initial_Load_from_HDD_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):

        self.State = Create_Window_GUI__class.State_enum.Load_from_HDD;  # Ставим статус чтобы различать с каким режимом сейчас работает Пользователь.

        res:bool = self._Initial_Load_from_HDD();

        self._Set_Button_Intervals_NotActive();  # Ставим кнопки выбора интенрвалов - неактивными, так как в Преобразовании Parqet-файлов в CSV они не нужны.

        self.Set_Name_Final_Button_by_State();  # Поменяем текст Финальной кнопки в зависимости от State

    def _Button_Export_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):
        
        self._Save_Export_Rows_for_Load_MOEX_HDD(self.State);

    def _Button_Load_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):
        
        self._Read_Load_Rows_for_Load_MOEX_HDD();

    def _Button_AddAll_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):


        #----------------------------------------------------------------------------------------------->>
        if (self.State == self.State_enum.Load_from_MOEX):

            List_All_Rows:list[str] = self.Treeview_ALLInstruments_MOEX_struct.Get_AllRows_Flat_List(self.Engine_Market_Board_Delemiter);

            # Доабвлять нужно только те строки - которые имеют загруженные Инстурменты, а не только Шаблон Engine-Market-Board. Определяется такая строка легко, по кол-ву разделителей "self.Engine_Market_Board_Delemiter" - Если 2 разделителя, то присутствует только шаблон, если три - то загрженный Инстурмент.

            #---------------------------------------------------------
            List_for_delete = [];

            for Row in (List_All_Rows):

                count = Row.count(self.Engine_Market_Board_Delemiter);

                if (count == 2):
                    List_for_delete.append(Row);


            for Row_delete in (List_for_delete):
                List_All_Rows.remove(Row_delete);
            #---------------------------------------------------------

            self.Listbox_UserСhoice_struct.Add_Row_with_Duplicate_Check(List_All_Rows, -1);  
        #----------------------------------------------------------------------------------------------->>




        #----------------------------------------------------------------------------------------------->>
        if (self.State == self.State_enum.Load_from_HDD):

            List_All_Rows:list[str] = self.Treeview_ALLInstruments_MOEX_struct.Get_AllRows_Flat_List_Only_Header(self.Engine_Market_Board_Delemiter);

            self.Listbox_UserСhoice_struct.Add_Row_with_Duplicate_Check(List_All_Rows, -1);  

        #----------------------------------------------------------------------------------------------->>


    def _Button_Add_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):

        #----------------------------------------------------------------------------------------------->>
        if (self.State == self.State_enum.Load_from_MOEX):

            List_Flat_Selected:list[str] = self.Treeview_ALLInstruments_MOEX_struct.Get_Selection_Flat_List(self.Engine_Market_Board_Delemiter);

            # Доабвлять нужно только те строки - которые имеют загруженные Инстурменты, а не только Шаблон Engine-Market-Board. Определяется такая строка легко, по кол-ву разделителей "self.Engine_Market_Board_Delemiter" - Если 2 разделителя, то присутствует только шаблон, если три - то загрженный Инстурмент.

            #---------------------------------------------------------
            List_for_delete = [];

            for Row in (List_Flat_Selected):

                count = Row.count(self.Engine_Market_Board_Delemiter);

                if (count == 2):
                    List_for_delete.append(Row);


            for Row_delete in (List_for_delete):
                List_Flat_Selected.remove(Row_delete);
            #---------------------------------------------------------

            self.Listbox_UserСhoice_struct.Add_Row_with_Duplicate_Check(List_Flat_Selected, -1);  # Добавляем выделенные строки в "Listbox_UserСhoice_struct"

        #----------------------------------------------------------------------------------------------->>




        #----------------------------------------------------------------------------------------------->>
        if (self.State == self.State_enum.Load_from_HDD):
            
            List_All_Rows:list[str] = self.Treeview_ALLInstruments_MOEX_struct.Get_Selection_Flat_List_Only_Header(self.Engine_Market_Board_Delemiter);

            self.Listbox_UserСhoice_struct.Add_Row_with_Duplicate_Check(List_All_Rows, -1);  # Добавляем выделенные строки в "Listbox_UserСhoice_struct"

        #----------------------------------------------------------------------------------------------->>


    def _Button_DeleteAll_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):

        self.Listbox_UserСhoice_struct.Delete_All();

    def _Button_Delete_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):
        
        List_Selected_Text:list[str] = self.Listbox_UserСhoice_struct.Get_Selected();

        self.Listbox_UserСhoice_struct.Delete_Row_by_List_Text(List_Selected_Text);

    def _Button_by_Intervals_AddAll_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):

        List_AllRows_Intervals:list[str]   = self.Listbox_Intervals_struct.Get_AllRows();

        List_Selected_Text_and_ID_UserСhoice:list[tuple[str,str]] = self.Listbox_UserСhoice_struct.Get_Selected_Text_and_ID();


        String_Join = ",".join(List_AllRows_Intervals);

        List_New_Text:list[str] = [];

        
        for item in (List_Selected_Text_and_ID_UserСhoice):

            pos = item[0].find("{");

            if (pos != -1):
                # Значит в строке уже есть какие то интервалы. Нужно их удалить и прорсто заменить всеми Интервалами из "String_Join"
                New_string = item[0][0:pos] + "{" + String_Join + "}"; 
                List_New_Text.append(New_string);        # Добавляем сцепку Интервалов


            List_New_Text.append(item[0] + "{" + String_Join + "}");        # Добавляем сцепку Интервалов

        cntr=0;
        for item in (List_Selected_Text_and_ID_UserСhoice):

            self.Listbox_UserСhoice_struct.Edit_Row_by_RowID(item[1], List_New_Text[cntr]);  # Заменяем существующую строку на строку с добавленными интервалами.
            cntr=cntr+1;

    def _Button_by_Intervals_Add_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):
         
        List_SelectRows_Intervals:list[str]   = self.Listbox_Intervals_struct.Get__ListSelectRow_by_Text();

        List_Selected_Text_and_ID_UserСhoice:list[tuple[str,str]] = self.Listbox_UserСhoice_struct.Get_Selected_Text_and_ID();


        User_String_Interval_Join = ",".join(List_SelectRows_Intervals);

        List_New_Text:list[tuple[str,str]] = [];




        for item in (List_Selected_Text_and_ID_UserСhoice):

            pos = item[0].find("{");

            if (pos == -1):
                # Значит у Данной строки еще не доавблено ни одного Интервала: значит просто добавим все Интервалы.

                List_New_Text.append((item[0] + "{" + User_String_Interval_Join + "}",item[1]));

            else:
                # Значит у Данной строки добавлен минимум один интервал: Значит нужно посмотреть, есть ли в доавбленных Интервалах - добавляемые и если есть, то такой интервал - не добавлять.
                

                #------------------------------------------------------------
                list_split:list[str] = (item[0][pos+1:len(item[0])-1]).split(",");   # Получим Список Интервалов в данной строке.
                    
                List_Interval_join:list[str] = [];   # Сюда будем заносить те Интервалы, которых нет в строке.
                    
                Text_without_Intervals:str = item[0][0:pos];      # Строка без Интервалов.
                #------------------------------------------------------------



                #```````````````````````````````````````````````````````````````
                for Interval in (List_SelectRows_Intervals):

                    try:
                        pos = list_split.index(Interval);  # Ищем доавбляемый интервал в уже добалвенных интервалах.
 
                        # Значит добавляемый Interval - есть в строке. Не добавляем его.

                    except(ValueError):
                        # Значит добавляемый Interval - нет в строке.

                        List_Interval_join.append(Interval);  # Добавляем
                #```````````````````````````````````````````````````````````````


                
                #------------------------------------------------------------
                List_Interval_join.extend(list_split);

                String_Interval_join = ",".join(List_Interval_join);

                New_string = Text_without_Intervals + "{" + String_Interval_join + "}";

                List_New_Text.append((New_string, item[1]));
                #------------------------------------------------------------




        for item in (List_New_Text):

            self.Listbox_UserСhoice_struct.Edit_Row_by_RowID(item[1], item[0]);  # Заменяем существующую строку на строку с добавленными интервалами.

    def _Button_by_Intervals_DeleteAll_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):
        
        List_Selected_Text_and_ID_UserСhoice:list[tuple[str,str]] = self.Listbox_UserСhoice_struct.Get_Selected_Text_and_ID();

        List_New_Text:list[tuple[str,str]] = [];


        for item in (List_Selected_Text_and_ID_UserСhoice):

            pos = item[0].find("{");

            if (pos != -1):
                # Значит в этой строке есть добавленные интервалы. Удалим их.
                List_New_Text.append((item[0][:pos] ,item[1]));



        for item in (List_New_Text):

             self.Listbox_UserСhoice_struct.Edit_Row_by_RowID(item[1], item[0]);  # Заменяем существующую строку на строку с добавленными интервалами.

    def _Button_by_Intervals_Delete_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):
        
        
        #---------------------------------------------------------
        List_SelectRows_Intervals:list[str]   = self.Listbox_Intervals_struct.Get__ListSelectRow_by_Text();

        List_Selected_Text_and_ID_UserСhoice:list[tuple[str,str]] = self.Listbox_UserСhoice_struct.Get_Selected_Text_and_ID();

        List_New_Text:list[tuple[str,str]] = [];
        #---------------------------------------------------------


        for item in (List_Selected_Text_and_ID_UserСhoice):

            pos = item[0].find("{");

            if (pos == -1):
                # Значит у Данной строки еще не доавблено ни одного Интервала: значит удалять нечего - просто ничего не делаем.
                pass

            else:
                # Значит у Данной строки добавлен минимум один интервал: Значит нужно посмотреть, есть ли в доавбленных Интервалах - удаляемые и если есть, то такой интервал - удалить.
                

                #------------------------------------------------------------
                list_split:list[str] = (item[0][pos+1:len(item[0])-1]).split(",");   # Получим Список Интервалов в данной строке.
                        
                Text_without_Intervals:str = item[0][0:pos];                         # Строка без Интервалов.
                #------------------------------------------------------------



                #```````````````````````````````````````````````````````````````
                List_for_Delete = [];

                for Interval in (List_SelectRows_Intervals):

                    if Interval in list_split:  # Ищем доавбляемый интервал в уже добалвенных интервалах.
 
                        # Значит добавляемый Interval - есть в строке. Удаляем его.
                        List_for_Delete.append(Interval);
                        #list_split.remove(Interval);

                    else:
                        # Значит добавляемый Interval - нет в строке. Ну и хорошо, ничего не делаем.
                        pass


                for item1 in (List_for_Delete):
                    list_split.remove(item1);
                #```````````````````````````````````````````````````````````````


                
                #------------------------------------------------------------
                if (len(list_split) == 0):
                    # Значит были удалены все интервалы, значит просто доавбляем строку без Интервалов.

                    List_New_Text.append((Text_without_Intervals, item[1]));

                else:

                    String_Interval_join = ",".join(list_split);

                    New_string = Text_without_Intervals + "{" + String_Interval_join + "}";

                    List_New_Text.append((New_string, item[1]));
                #------------------------------------------------------------



        for item in (List_New_Text):

            self.Listbox_UserСhoice_struct.Edit_Row_by_RowID(item[1], item[0]);  # Заменяем существующую строку на строку с добавленными интервалами.



    def _Load_Instruments_from_MOEX(self,List_Engine,List_Market,List_Board):

            Row_Size = len(List_Engine);

            #-------------------------------------Очистка Engine, Market, Board:Начало-------------------------------------------

            # Engine, Market, Board - в окне Treeview смешаны с русской расшифровкой, в таком виде: Stock(Фондовый рынок)-Shares(Рынок акций)-TQBR(Акции и ДР) - нужно учистить от скобок.

            List_Engine_clear:list[str] = [];
            List_Market_clear:list[str] = [];
            List_Board_clear:list[str]  = [];

            for i in range(Row_Size):

                Engine = List_Engine[i];
                Market = List_Market[i];
                Board  = List_Board[i];

                Engine_clear:str = Engine[0:Engine.find("(")];
                Market_clear:str = Market[0:Market.find("(")];
                Board_clear:str  = Board[0:Board.find("(")];

                List_Engine_clear.append(Engine_clear);
                List_Market_clear.append(Market_clear);
                List_Board_clear.append(Board_clear);

            #-------------------------------------Очистка Engine, Market, Board:Конец-------------------------------------------

            # ВНИМАНИЕ!!! В таблице загрузке в колонке 4-ой Статус, уже должно быть просталено занчение -> "Загружается" !!!!!!!!!!

            for i in range(Row_Size):
                try:

                #--------------------------------------------------------------------

                    List_Paper, error_text  = self.MOEX_Download_.Get__All_Instruments_from_Engine_Market_Board(List_Engine_clear[i], List_Market_clear[i], List_Board_clear[i]);  

                    if (List_Paper != None):
                        #List_Paper:list[MOEX_Download__class.Instruments_struct]

                        #class Instruments_struct:
                        #SECID:str = "";
                        #SECNAME:str = "";
                

                        # Теперь осталось просто добавить данные из List_Paper в качестве детей к хедеру - "Engine-Market-Board" в Treeview список.
                                
                        if(len(List_Paper) > 0):
                            self.Deque_ThreadSafe.put(lambda i=i, List_Paper=List_Paper, Engine = List_Engine[i], Market = List_Market[i], Board = List_Board[i], : self.Treeview_ALLInstruments_MOEX_struct.Add_Elements_to_ColapsingHeader([Engine, Market, Board],[item.SECID + "(" + item.SECNAME + ")" for item in (List_Paper)]));   # Заполянем данные в Treeview
                        else:
                            self.Deque_ThreadSafe.put(lambda i=i, Engine = List_Engine[i], Market = List_Market[i], Board = List_Board[i]: self.Treeview_ALLInstruments_MOEX_struct.Add_Elements_to_ColapsingHeader([Engine, Market, Board],["пришли пустые данные"]));

                        self.Deque_ThreadSafe.put(lambda i=i, Engine = List_Engine[i], Market = List_Market[i], Board = List_Board[i]: self.Table_Instrument_Load.Edit_Row_by_ColumnIndex_by_ValueRow((Engine, Market, Board,"Загружается"), (0,1,2,3), "Загружено", 3));
                    else:

                        self.Deque_ThreadSafe.put(lambda i=i, Engine = List_Engine[i], Market = List_Market[i], Board = List_Board[i], error_text=error_text: self.Table_Instrument_Load.Edit_Row_by_ColumnIndex_by_ValueRow((Engine, Market, Board,"Загружается"), (0,1,2,3), "Ошибка Загрузки:" + "\n" + error_text, 3));
 
                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    print("___________Exception:" + str(e));  # Ловись рыбка, большая и малая

                #--------------------------------------------------------------------


    def _Button_Popup_for_UserLoad_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):

        # Значит Пользователь кликнул по "вспылвающей" кнопки "Загрузить" или "нарисовать" - в зависимости от self.State:
        
        if (self.State == self.State_enum.Load_from_MOEX):

            self.Window_for_Table_Instrument_Load.Show()

            List_Selected_Row:list[str] = self.Treeview_ALLInstruments_MOEX_struct.Get_Selection_Flat_List(self.Engine_Market_Board_Delemiter );  # Поулчим список выделенных строк.



            #````````````````````````````Проверим какие из строк не соответвуют строкам из оригинального первончально загруженного списка "List_All_MOEX_Save":Начало```````````````````````````````````````````
       
            # Возможно Пользовтаель уже подгрузил какие то Инстурменты и выделил в том числе и их - они естесвенно не подходят для загрузки - так как они и есть загрузки.

            List_Row_for_Delete:list[str] = [];

            #--------------------------------------------------------------------

            for row_Selected in (List_Selected_Row):

                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      
                if row_Selected in self.List_All_MOEX_Save:  # Ищем строку "row_Selected" в оригинального первончально загруженного списке.
                    # Значит добавляемый "row_Selected" - есть в списке. Окей ничего не делаем. Значит строка "row_Selected" нужна.
                    # А нет, теперь нужно провериь - есть ли у этой строки Дети - так как Пользовтаель мог ранее их загрузить и поэтому потоврно загружать их етесвенно не нужно.

                    Engine, Market, Board = row_Selected.split(self.Engine_Market_Board_Delemiter );
                
                    Check_bool = self.Treeview_ALLInstruments_MOEX_struct.Check_Child_by_Header([Engine, Market, Board]);
                
                    if(Check_bool == True):
                        # Значит есть дети, значит для данного "Row_Select" - Инстурменты уже загружались Пользователем.
                        List_Row_for_Delete.append(row_Selected);  # Вносим данную строку в список удаления из загрузки.
                    else:
                        pass # Значит Детей нет и значит нет Инструментов, значит еще не загружались. Оставляем в списке - ниче не делаем.
                
                else:
                    # Значит добавляемый "row_Selected" - НЕТ в списке - по сути это значит только одно, что данная "row_Selected" - это уже ранее загруженный инстурмент Пользователем. Добавим его в список для удаления.
                
                    List_Row_for_Delete.append(row_Selected);
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            #--------------------------------------------------------------------



            #--------------------------------------------
            for Row_delete in (List_Row_for_Delete):

                List_Selected_Row.remove(Row_delete);
            #--------------------------------------------
      


            # List_Selected_Row - так!!! теперь тут готовый список строк "Engine-Market-Board" для загрузки конкретных инструментов с MOEX в формате однй строки через разделитель.



            #------------------------------------Разделим строку на отдельные Engine, Marker, Board:Начло-------------------------------------

            List_Engine:list[str] = [];
            List_Market:list[str] = [];
            List_Board:list[str]  = [];

            for Row_Select in (List_Selected_Row):

                Engine, Market, Board = Row_Select.split(self.Engine_Market_Board_Delemiter);

                List_Engine.append(Engine);
                List_Market.append(Market);
                List_Board.append(Board);

            #------------------------------------Разделим строку на отдельные Engine, Marker, Board:Начло-------------------------------------



            List_Engine_witout_dublicate:list[str] = [];
            List_Market_witout_dublicate:list[str] = [];
            List_Board_witout_dublicate:list[str]  = [];

            #-------------------------------Проверим на ДУБЛИКАТ, то есть есть ли загружаемые Инстурменты уже в таблице загрузке, и если есть - то не загружаем их повторно:-------------------------------------
            for i in range(len(List_Engine)):
            
                Row_Index_Dublicate = self.Table_Instrument_Load.Check_Duplicate((List_Engine[i], List_Market[i], List_Board[i]), (0,1,2));

                if (Row_Index_Dublicate == -1):
                    # Значит в таблице загрузок нет такой строки, значит добавляем в Список Загрузки Таблицы.

                    List_Engine_witout_dublicate.append(List_Engine[i]);
                    List_Market_witout_dublicate.append(List_Market[i]);
                    List_Board_witout_dublicate.append(List_Board[i]);
                else:
                    # Значит в таблице загрузок - есть такая строка, ЗНАЧИТ не заносим ее в финальный список.
                    pass;
            #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



            #---------------------------------------------Добавим разделенные строки из списка в таблицу загружаемых инстурментов:--------------------
            for i in range(len(List_Engine_witout_dublicate)):

                    self.Table_Instrument_Load.Add_Row([(List_Engine_witout_dublicate[i], List_Market_witout_dublicate[i], List_Board_witout_dublicate[i], "Загружается")], 0)

            #-------------------------------------------------------------------------------------------------------------------


            self.ThreadPoolExecutor_MOEX.submit(lambda List_Engine=List_Engine_witout_dublicate,List_Market=List_Market_witout_dublicate,List_Board=List_Board_witout_dublicate: self._Load_Instruments_from_MOEX(List_Engine,List_Market,List_Board));  

            #````````````````````````````Проверим какие из строк не соответвуют строкам из оригинального первончально загруженного списка "List_All_MOEX_Save":Конец```````````````````````````````````````````

            Button_struct.Set_Show(False);  # Скрываем кнопку, как Пользователь по ней кликнул Загрузить.


            self.Button_Popup_for_UserLoad.Set_Show(False);
            return;

        if (self.State == self.State_enum.Load_from_HDD):
            # Значит Пользователь хочет нарисовать данные свечей из Parget-файлов на грфике.
            # Для начала смотрим сколько элементов выделено, если больше одного, то сообщаем, что выделно больше одного элемента и тупо выходим.
            # Если Элекмент выделен одни, то получаем выделнную строку - идем в папку где лежат Parqet-файлы по выделенному инстурменту, выдергиваем оттуда даныне свечей буффер -> преобразовываем в Си-массив и передаем DLL-ке на отрисовку.

            if (Windows_DLL_Candle_DRAWka == True):

                #-------------------------------------------------------------------------------------------------------------
                List_Selected_Row:list[str] = self.Treeview_ALLInstruments_MOEX_struct.Get_Selection_Flat_List_Only_Header(self.Engine_Market_Board_Delemiter);  # Поулчим список выделенных строк.

                if (len(List_Selected_Row) > 1):
                    self.Tkinter_GUI_obj.Call_MessageBox("Сообщение", "Функция рисования работает только для одного элемента");
                    self.Button_Popup_for_UserLoad.Set_Show(False);
                    return;
                #-------------------------------------------------------------------------------------------------------------

            
                Engine,Market,Board,Instrument,Interval = List_Selected_Row[0].split(self.Engine_Market_Board_Delemiter);


                #-----------------------------Составляем список полных путей к Parquet-файлам:Начало---------------------------------
                Path_To_Folder_to_Parqet_Files:Path = Path(self.Folder_to_Parqet_Files)/Engine/Market/Board/ Instrument/Interval;  
                # Path_To_Folder_to_Parqet_Files - так тут путь к папке со всеми Parqet-файлами по Инструменту.

                List__Full_Path_to_Parqet_Files = self.Tkinter_GUI_obj.Get__FullPath_to_Files_from_Folder__Sort_Files_as_Value_From_Less_to_More(Path_To_Folder_to_Parqet_Files);  # Поулчим список полных путей ко всем Parqet-файлам в папке.
                #-----------------------------Составляем список полных путей к Parquet-файлам:Конец---------------------------------



                #-----------------------------------------------------Извлекаем данные из Parqet-файлов в стандртные Python-контейнеры:Начало-------------------------------------
            
                Tuple_List_Candle_Param:tuple[list,...] = self.DuckDB_StockCandles_.Extract_Candle_Data_from_Parqet_Files(List__Full_Path_to_Parqet_Files);

                # Tuple_List_Candle_Param - массив списков, каждый список представляет собой одну полную заполенную колонку строго последовтаельно соответвующая текущему формату колонок: open, close, high, low, value, volume, begin_date, end_date

                # print(Tuple_List_Candle_Param);

                #-----------------------------------------------------Извлекаем данные из Parqet-файлов в стандртные Python-контейнеры:Конец-------------------------------------



                #-------------------------------------------------------------Так теперь отправляем все это хоз-во в мою DLL-ку для отрисовки свечей:Начало-------------------------------------

            
                #--------------------Описаение "структуры" типа передавамых парметров из Python в DLL:----------------------------

                self.my_DDL_Candle_DTAWka.my_Draw_func.argtypes = [
                ctypes.POINTER(ctypes.c_double),
                ctypes.POINTER(ctypes.c_double),
                ctypes.POINTER(ctypes.c_double),
                ctypes.POINTER(ctypes.c_double),
                ctypes.POINTER(ctypes.c_ulonglong),
                ctypes.POINTER(ctypes.c_uint),
                ctypes.POINTER(ctypes.c_uint),
                ctypes.POINTER(ctypes.c_uint),
                ctypes.POINTER(ctypes.c_uint),
                ctypes.POINTER(ctypes.c_uint),
                ctypes.c_size_t,
                ]

                #-----------------------------------------------------------------------------------------------------------------


                #-----------------------------------------------------------------------------------------------------------

                array_db_Open_C_pointer          = (ctypes.c_double * len(Tuple_List_Candle_Param[0]))(*Tuple_List_Candle_Param[0]);
                array_db_Close_C_pointer         = (ctypes.c_double * len(Tuple_List_Candle_Param[0]))(*Tuple_List_Candle_Param[1]);
                array_db_High_C_pointer          = (ctypes.c_double * len(Tuple_List_Candle_Param[0]))(*Tuple_List_Candle_Param[2]);
                array_db_Low_C_pointer           = (ctypes.c_double * len(Tuple_List_Candle_Param[0]))(*Tuple_List_Candle_Param[3]);
                array_Ull_Volume_C_pointer       = (ctypes.c_ulonglong * len(Tuple_List_Candle_Param[0]))(*Tuple_List_Candle_Param[5]);
                # array_db_Begin_Date_C_pointer  = (ctypes.c_double * len(Tuple_List_Candle_Param[0]))(*Tuple_List_Candle_Param[6]);

                year_list, month_list, day_list, hour_list, minute_list = [], [], [], [], [];

                for dt in Tuple_List_Candle_Param[6]:
                    year_list.append(dt.year)
                    month_list.append(dt.month)
                    day_list.append(dt.day)
                    hour_list.append(dt.hour)
                    minute_list.append(dt.minute)

                array_db_Year_C_pointer   = (ctypes.c_uint * len(year_list))(*year_list)
                array_db_Month_C_pointer  = (ctypes.c_uint * len(month_list))(*month_list)
                array_db_Day_C_pointer    = (ctypes.c_uint * len(day_list))(*day_list)
                array_db_Hour_C_pointer   = (ctypes.c_uint * len(hour_list))(*hour_list)
                array_db_Minute_C_pointer = (ctypes.c_uint * len(minute_list))(*minute_list)

                Size_array = len(Tuple_List_Candle_Param[0]);

                self.my_DDL_Candle_DTAWka.my_Draw_func(array_db_Open_C_pointer,array_db_Close_C_pointer,array_db_High_C_pointer,array_db_Low_C_pointer,array_Ull_Volume_C_pointer,array_db_Year_C_pointer,array_db_Month_C_pointer,array_db_Day_C_pointer,array_db_Hour_C_pointer,array_db_Minute_C_pointer, Size_array); 
                #-----------------------------------------------------------------------------------------------------------

            

                #-------------------------------------------------------------Так теперь отправляем все это хоз-во в мою DLL-ку для отрисовки свечей:Конец-------------------------------------

                self.Button_Popup_for_UserLoad.Set_Show(False);
        




    def _Button_Popup_for_Instrument_Reload_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):

        # Значит Пользовтаель клинкнул по кнопке Пере-загрузить в таблице "Table_Instrument_Load", значится делаем следующее:
        #-Получаем выделенные в таблице строки в данный момент.
        #-Смотрим у этих строк столбец "Status_Load", "Статус загрузки" - если там стоит "Загружено" или "Загружается", то пропускаем - зачем еще раз пере-загружать, если данные были успешно загружены или ставить загрузку того чего еще не Загружено. Остальные строки оставляем и вызываем для них опять фунцию загрузки с MOEX.

        List_tuple_string_Select_Rows = self.Table_Instrument_Load.Get_Selected_Row_by_Value();


        #-------------------------------------------------------------------------------
        List_for_Delete = [];

        for Row_tuple in (List_tuple_string_Select_Rows):

            if (Row_tuple[3] == "Загружено" or Row_tuple[3] == "Загружается"):
                # Удаляем из списка.
                List_for_Delete.append(Row_tuple);


        for tuple_delete in(List_for_Delete):
            List_tuple_string_Select_Rows.remove(tuple_delete);


        # List_tuple_string_Select_Rows - так теперь тут только нужные выделнные строки, которые нужно перезапросить у MOEX.
        #-------------------------------------------------------------------------------


        #-------------------------------------------------------------------------------

        List_Engine,List_Market,List_Board, List_Status =  [], [], [], [];

        for Row_tuple in (List_tuple_string_Select_Rows):
            
             List_Engine.append(Row_tuple[0]);
             List_Market.append(Row_tuple[1]);
             List_Board.append(Row_tuple[2]);
             List_Status.append(Row_tuple[3]);
  
        #-------------------------------------------------------------------------------



        
        #---------------------------------------Проставим в таблице загрузки для строк статус "Загружается":Начало------------------------------------------------

        for i in range(len(List_Engine)):

            self.Table_Instrument_Load.Edit_Row_by_ColumnIndex_by_ValueRow((List_Engine[i], List_Market[i], List_Board[i], List_Status[i]), (0,1,2,3), "Загружается", 3);

        #---------------------------------------Проставим в таблице загрузки для строк статус "Загружается":Начало------------------------------------------------




        self.ThreadPoolExecutor_for_Laod_MOEX_Intrument.submit(lambda List_Engine=List_Engine,List_Market=List_Market,List_Board=List_Board: self._Load_Instruments_from_MOEX(List_Engine,List_Market,List_Board)); 



        self.Button_Popup_Instrument_Reload.Set_Show(False);


    def _Load_Candles_from_MOEX(self, List_Final:list[Create_Window_GUI__class.Engines_Market_Board_Intrument_Intervals_struct]):
        

        #---------------------------------Callback:-----------------------------------------------------
        def Callback_for_Load_Info(original_JSON_part, String_Date_Range_Start:str, String_Date_Range_End:str, List_Any:list[any]):
            # Вызывается изнутри функции "Get__DataCandles_JSON_Format" - при получении очередной порции свечей по Инстурменту.

            i          = List_Any[0];
            List_Final = List_Any[1];

            String_Date_Range_Start = String_Date_Range_Start[0:len(String_Date_Range_Start)-3];  # Уберем секунды с конца, чтобы глаза не мазолили.
            String_Date_Range_End   = String_Date_Range_End[0:len(String_Date_Range_End)-3];      # Уберем секунды с конца, чтобы глаза не мазолили.


            self.Deque_ThreadSafe.put(lambda i=List_Any[0], Engine = List_Final[i].Engine, Market = List_Final[i].Market, Board = List_Final[i].Board, Instrument = List_Final[i].Instrument, Interval = List_Final[i].Interval, Date_FROM = List_Final[i].Date_FROM, Date_TO = List_Final[i].Date_TO,Path_to_Save = List_Final[i].Path_to_Save: self.Table_Candles_Load.Edit_Row_by_ColumnIndex_by_ValueRow((Engine,Market,Board,Instrument,Interval,Date_FROM,Date_TO,Path_to_Save), (0,1,2,3,4,5,6,7), "Загружается:" + String_Date_Range_Start + " : " + String_Date_Range_End, 8));
        #-----------------------------------------------------------------------------------------------


        #-------------------------------------------------------Вызываем скачивалку с MOEX:Начало--------------------------------------------------------

        def Donwnload_Candles(i, List_Final):

            #------------------------------------------------------------------------------------
            List_Any = [i, List_Final];

            
            Request_struct_ = MOEX_Download__class.MOEX_Download__class.Request_struct();
            Request_struct_.Engines_Name                = List_Final[i].Engine_Clear;
            Request_struct_.Market_Name                 = List_Final[i].Market_Clear;
            Request_struct_.Board_Name                  = List_Final[i].Board_Clear;
            Request_struct_.Instrument_Name             = List_Final[i].Instrument_Clear;
            Request_struct_.Interval_string_ID          = self.MOEX_Download_.interval_mapping[List_Final[i].Interval];
            Request_struct_.Date_Begin                  = List_Final[i].Date_FROM;
            Request_struct_.Date_End                    = List_Final[i].Date_TO;
            Request_struct_.Callback_for_Load_Info      = Callback_for_Load_Info;
            Request_struct_.List_Any_for_Callback       = List_Any;


            String_Json_List2D, Error_Text = self.MOEX_Download_.Get__DataCandles_JSON_Format(Request_struct_);

            if (String_Json_List2D != None):

                if (String_Json_List2D != ""):

                    self.Deque_ThreadSafe.put(lambda i=i, Engine = List_Final[i].Engine, Market = List_Final[i].Market, Board = List_Final[i].Board, Instrument = List_Final[i].Instrument, Interval = List_Final[i].Interval, Date_FROM = List_Final[i].Date_FROM, Date_TO = List_Final[i].Date_TO, Path_to_Save = List_Final[i].Path_to_Save: self.Table_Candles_Load.Edit_Row_by_ColumnIndex_by_ValueRow((Engine,Market,Board,Instrument,Interval,Date_FROM,Date_TO, Path_to_Save), (0,1,2,3,4,5,6,7), "Загружено:Сохраняется на диск", 8));
                    
                    with self.MOEX_Download_.Mutex:
                        res = self.DuckDB_StockCandles_.Save_Candle_JSON_List_String_Format(List_Final[i].Path_to_Save, String_Json_List2D, self.MOEX_Download_.Formate_Date_from_MOEX_string, List_Final[i].Engine_Clear, List_Final[i].Market_Clear, List_Final[i].Board_Clear, List_Final[i].Instrument_Clear, List_Final[i].Interval); # Сохраняем Свечи в Паркет-файлы.

                    if (res == None):
                        # Сохранение прошло успешно. Ставим в таблицу загрузки статус -> Загружено.

                        self.Deque_ThreadSafe.put(lambda i=i, Engine = List_Final[i].Engine, Market = List_Final[i].Market, Board = List_Final[i].Board, Instrument = List_Final[i].Instrument, Interval = List_Final[i].Interval, Date_FROM = List_Final[i].Date_FROM, Date_TO = List_Final[i].Date_TO, Path_to_Save = List_Final[i].Path_to_Save: self.Table_Candles_Load.Edit_Row_by_ColumnIndex_by_ValueRow((Engine,Market,Board,Instrument,Interval,Date_FROM,Date_TO, Path_to_Save), (0,1,2,3,4,5,6,7), "Загружено", 8));
                    
                    else:
                        # Какая то ошибака.
                        self.Deque_ThreadSafe.put(lambda i=i, Engine = List_Final[i].Engine, Market = List_Final[i].Market, Board = List_Final[i].Board, Instrument = List_Final[i].Instrument, Interval = List_Final[i].Interval, Date_FROM = List_Final[i].Date_FROM, Date_TO = List_Final[i].Date_TO, Path_to_Save = List_Final[i].Path_to_Save: self.Table_Candles_Load.Edit_Row_by_ColumnIndex_by_ValueRow((Engine,Market,Board,Instrument,Interval,Date_FROM,Date_TO, Path_to_Save), (0,1,2,3,4,5,6,7), "Ошибка Загрузки:" + res, 8));

                    # print(String_Json_List2D);
                else:
                    # print("Candles Empty");
                    self.Deque_ThreadSafe.put(lambda i=i, Engine = List_Final[i].Engine, Market = List_Final[i].Market, Board = List_Final[i].Board, Instrument = List_Final[i].Instrument, Interval = List_Final[i].Interval, Date_FROM = List_Final[i].Date_FROM, Date_TO = List_Final[i].Date_TO, Path_to_Save = List_Final[i].Path_to_Save: self.Table_Candles_Load.Edit_Row_by_ColumnIndex_by_ValueRow((Engine,Market,Board,Instrument,Interval,Date_FROM,Date_TO, Path_to_Save), (0,1,2,3,4,5,6,7), "Загружено: пустые данные", 8));
            else:
                self.Deque_ThreadSafe.put(lambda i=i, Engine = List_Final[i].Engine, Market = List_Final[i].Market, Board = List_Final[i].Board, Instrument = List_Final[i].Instrument, Interval = List_Final[i].Interval, Date_FROM = List_Final[i].Date_FROM, Date_TO = List_Final[i].Date_TO, Path_to_Save = List_Final[i].Path_to_Save: self.Table_Candles_Load.Edit_Row_by_ColumnIndex_by_ValueRow((Engine,Market,Board,Instrument,Interval,Date_FROM,Date_TO, Path_to_Save), (0,1,2,3,4,5,6,7), "Ошибка Загрузки:" + Error_Text, 8));
            #------------------------------------------------------------------------------------



        for i in range(len(List_Final)):
        
            #Date_Begin:str = "2024-07-01"; # "2024-01-01";   # Начальная дата запроса Свечей. Если дату указать меньшую чем есть в системе, то дата свечей просто приет с той даты, которая есть в системе. Если указать пустую строку - "", то так же свечи прижут с той минимальной даты, что есть в системе. 
            #Date_End:str   = "2024-07-31"; # "2024-12-31";   # Конечная дата запроса Свечей. Если дату указать большу, то естесвенно она ограничится максимальной вохможной датой.  Если указать пустую строку - "", то так же свечи прижут до той максимальной даты, что есть в системе. 
            # ВАЖНОЕ УТОЧНЕНИЕ НАСЧЕТ УКАЗАНИЯ ДАТЫ: Дата указывается только с точностью до дня, ТО ЕСТЬ даже если заказывается Минутные Интервалы, то просто запросятся за весь указанный день. Я сделал это для простоты.

            # Callback_for_Load_Info - колбек в которой будет приходить диапазон загрузки на каждой итерации генерации ссылки. Если колбек не нужен - то передать None.  

            self.ThreadPoolExecutor_MOEX.submit(lambda i=i, List_Final=List_Final: Donwnload_Candles(i, List_Final));  
   
        #-------------------------------------------------------Вызываем скачивалку с MOEX:Конец--------------------------------------------------------

    def _Transform_Parquet_to_CSV(self, List_Final:list[Create_Window_GUI__class.Engines_Market_Board_Intrument_Intervals_struct]):

        for i in range(len(List_Final)):

            #----------------------------------------------------------------

            Exist_flag = self.Tkinter_GUI_obj.Check__Folder_Exist(self.Folder_to_Parqet_Files);


            if (Exist_flag == False):
                # Значит указанной папки с Parqet-файлами не существует.
                self.Deque_ThreadSafe.put(lambda i = i, List_Final = List_Final, Engine = List_Final[i].Engine_Clear, Market = List_Final[i].Market_Clear, Board = List_Final[i].Board_Clear, Instrument = List_Final[i].Instrument_Clear, Interval = List_Final[i].Interval, Date_Begin = List_Final[i].Date_FROM, Date_End = List_Final[i].Date_TO,Path_to_Save_CSV = List_Final[i].Path_to_Save: self.Table_Transform_to_CSV.Edit_Row_by_ColumnIndex_by_ValueRow((Engine, Market, Board, Instrument, Interval, Date_Begin, Date_End, Path_to_Save_CSV), (0,1,2,3,4,5,6,7), "Ошибка Сохранения: Указанной папки с Parqet-файлами:" + str(self.Folder_to_Parqet_Files) +" - не найдено", 8));
                continue;
            #----------------------------------------------------------------



            #-----------------------------Составляем список полных путей к Parquet-файлам:Начало---------------------------------
            Path_To_Folder_to_Parqet_Files:Path = Path(self.Folder_to_Parqet_Files)/ List_Final[i].Engine_Clear/ List_Final[i].Market_Clear/ List_Final[i].Board_Clear/ List_Final[i].Instrument_Clear/ List_Final[i].Interval;  
            # Path_To_Folder_to_Parqet_Files - так тут путь к папке со всеми Parqet-файлами по Инструменту.

            List__Full_Path_to_Parqet_Files = self.Tkinter_GUI_obj.Get__FullPath_to_Files_from_Folder(Path_To_Folder_to_Parqet_Files);  # Поулчим список полных путей ко всем Parqet-файлам в папке.
            #-----------------------------Составляем список полных путей к Parquet-файлам:Конец---------------------------------

            
            #-------------------------------------------Вызываем преобразовалку в CSV:Начало---------------------------------------------

            Date_Begin:str = List_Final[i].Date_FROM;     # Дата начала диапазона запроса. Должен естесвенно совпадать с данными, которые ранее сохранялись по запрашиваемому Инструменту. НО ВАЖНО: Если указать Год которого нет в ранее сохраненных Parqet-файлах то функция то функция просто проигнориует это и все и пойдет искать те даныне, которые есть в ранее сохраненных Parqet-файлах. ТО ЕСТЬ даты из Parqet-файлах берутся просто по Общему пересечению переданных дат с датами в Parqet-файлах: То есть грубо если я укажу: 30.01.2010 - 27.05.2011 и а в parqet файла за 2010 год вообще не будет, то он просто проигнорируется, а в parqet файле за 2011 год  будут даты только начиная с условно 10.04.2025 11:40:00 - по 17.04.2025 12:15:00 - то строки просто возьмутся с этими датами и сохранятся в CSV.
            Date_End:str   = List_Final[i].Date_TO;       # Дата начала диапазона запроса. Должен естесвенно совпадать с данными, которые ранее сохранялись по запрашиваемому Инструменту. НО ВАЖНО: Если указать Год которого нет в ранее сохраненных Parqet-файлах то функция то функция просто проигнориует это и все и пойдет искать те даныне, которые есть в ранее сохраненных Parqet-файлах. ТО ЕСТЬ даты из Parqet-файлах берутся просто по Общему пересечению переданных дат с датами в Parqet-файлах: То есть грубо если я укажу: 30.01.2010 - 27.05.2011 и а в parqet файла за 2010 год вообще не будет, то он просто проигнорируется, а в parqet файле за 2011 год  будут даты только начиная с условно 10.04.2025 11:40:00 - по 17.04.2025 12:15:00 - то строки просто возьмутся с этими датами и сохранятся в CSV.

            # Это тем имена, которые соответсвуют данным указанным в путях "List__Full_Path_to_Parqet_Files" к Parquet-файлам.
            Engine_name     = List_Final[i].Engine_Clear;
            Market_name     = List_Final[i].Market_Clear;
            Board_name      = List_Final[i].Board_Clear;
            Instrument_name = List_Final[i].Instrument_Clear;
            Interval_name   = List_Final[i].Interval;           # Обозначение временного интервал может быть любым, НО оно всегда должен быть одним и тем же при будущих сохранениях!!!! Так как этими именами называются папки на диске. НО лучше брать 

            Path_to_Save_CSV:str = List_Final[i].Path_to_Save;  #Папка куда сохранять CSV-файл.

            Delimiter_CSV:str = ";"

            res = self.DuckDB_StockCandles_.Transform_to_CSV_Direct_Path(Date_Begin, Date_End, List__Full_Path_to_Parqet_Files, Engine_name, Market_name, Board_name, Instrument_name, Interval_name, self.MOEX_Download_.Formate_Date_from_MOEX_string, Path_to_Save_CSV, Delimiter_CSV);

            if (res != None):
                self.Deque_ThreadSafe.put(lambda i = i, List_Final = List_Final, Engine = List_Final[i].Engine_Clear, Market = List_Final[i].Market_Clear, Board = List_Final[i].Board_Clear, Instrument = List_Final[i].Instrument_Clear, Interval = List_Final[i].Interval, Date_Begin = List_Final[i].Date_FROM, Date_End = List_Final[i].Date_TO,Path_to_Save_CSV = List_Final[i].Path_to_Save: self.Table_Transform_to_CSV.Edit_Row_by_ColumnIndex_by_ValueRow((Engine, Market, Board, Instrument, Interval, Date_Begin, Date_End, Path_to_Save_CSV), (0,1,2,3,4,5,6,7), "Ошибка Сохранения:" + str(res), 8));
            else:       
                self.Deque_ThreadSafe.put(lambda i = i, List_Final = List_Final, Engine = List_Final[i].Engine_Clear, Market = List_Final[i].Market_Clear, Board = List_Final[i].Board_Clear, Instrument = List_Final[i].Instrument_Clear, Interval = List_Final[i].Interval, Date_Begin = List_Final[i].Date_FROM, Date_End = List_Final[i].Date_TO,Path_to_Save_CSV = List_Final[i].Path_to_Save: self.Table_Transform_to_CSV.Edit_Row_by_ColumnIndex_by_ValueRow((Engine, Market, Board, Instrument, Interval, Date_Begin, Date_End, Path_to_Save_CSV), (0,1,2,3,4,5,6,7), "Сохранено", 8));
            #-------------------------------------------Вызываем преобразовалку в CSV:Начало---------------------------------------------


    def _Button_Popup_for_Candles_Reload_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):
       
        # Значит Пользовтаель клинкнул по кнопке Пере-загрузить в таблице "Table_Candles_Load", значится делаем следующее:
        #-Получаем выделенные в таблице строки в данный момент.
        #-Смотрим у этих строк столбец "Status_Load", "Статус загрузки" - если там стоит "Загружено" или "Загружается", то пропускаем - зачем еще раз пере-загружать, если данные были успешно загружены или ставить загрузку того чего еще не Загружено. Остальные строки оставляем и вызываем для них опять фунцию загрузки с MOEX.

        List_tuple_string_Select_Rows = self.Table_Candles_Load.Get_Selected_Row_by_Value();
        

        #-------------------------------Удаляем из Выделенных строк уже Загруженные строки или Загружаемые в данный момент:Начало------------------------------------------------

        List_for_Delete = [];

        for Row_tuple in (List_tuple_string_Select_Rows):

            if (Row_tuple[7] == "Загружено" or Row_tuple[7].find("Загружается") >= 0):
                # Удаляем из списка.
                List_for_Delete.append(Row_tuple);


        for tuple_delete in(List_for_Delete):
            List_tuple_string_Select_Rows.remove(tuple_delete);


        # List_tuple_string_Select_Rows - так теперь тут только нужные выделнные строки, которые нужно перезапросить у MOEX.

        #-------------------------------Удаляем из Выделенных строк уже Загруженные строки или Загружаемые в данный момент:Конец------------------------------------------------


        

        #---------------------------Теперь сформируем итоговый List_Final для загрузки свечей и для обнолвеня строк в Таблице Загрузки:Начало-------------------------

        List_Final:list[Create_Window_GUI__class.Engines_Market_Board_Intrument_Intervals_struct] = [];



        for Row in (List_tuple_string_Select_Rows):

            List_Final.append(Create_Window_GUI__class.Engines_Market_Board_Intrument_Intervals_struct());

            List_Final[-1].Engine             = Row[0];
            List_Final[-1].Market             = Row[1];
            List_Final[-1].Board              = Row[2];
            List_Final[-1].Instrument         = Row[3];

            List_Final[-1].Engine_Clear       = Row[0][0:Row[0].find("(")];
            List_Final[-1].Market_Clear       = Row[1][0:Row[1].find("(")];
            List_Final[-1].Board_Clear        = Row[2][0:Row[2].find("(")];
            List_Final[-1].Instrument_Clear   = Row[3][0:Row[3].find("(")];

            List_Final[-1].Interval           = Row[4];
            List_Final[-1].Date_FROM          = Row[5];
            List_Final[-1].Date_TO            = Row[6];

            List_Final[-1].Path_to_Save       = Row[7];


        #---------------------------Теперь сформируем итоговый List_Final для загрузки свечей и для обнолвеня строк в Таблице Загрузки:Начало-------------------------


        

                
        #---------------------------------------Проставим в таблице загрузки для строк статус "Загружается":Начало------------------------------------------------

        for Row in (List_Final):

            self.Table_Candles_Load.Edit_Row_by_ColumnIndex_by_ValueRow((Row.Engine, Row.Market, Row.Board, Row.Instrument, Row.Interval, Row.Date_FROM, Row.Date_TO, Row.Path_to_Save), (0,1,2,3,4,5,6,7), "Загружается", 8);

        #---------------------------------------Проставим в таблице загрузки для строк статус "Загружается":Начало------------------------------------------------

        

        #-------------------------------------------------------Вызываем скачивалку с MOEX:Начало--------------------------------------------------------
        
        self.ThreadPoolExecutor_MOEX.submit(lambda List_Final=List_Final: self._Load_Candles_from_MOEX(List_Final));  
   
        #-------------------------------------------------------Вызываем скачивалку с MOEX:Конец--------------------------------------------------------
        

        self.Button_Popup_Candles_Reload.Set_Show(False);

    def _Button_Popup_for_Transform_to_CSV_Reload_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):
            # PIZDA
            # Значит Пользовтаель клинкнул по кнопке Пере-сохранить в таблице "Table_Transform_to_CSV_Load", значится делаем следующее:
            #-Получаем выделенные в таблице строки в данный момент.
            #-Смотрим у этих строк столбец "Status_Load", "Статус загрузки" - если там стоит "Сохранено" или "Сохраняется", то пропускаем - зачем еще раз пере-сохронять, если данные были успешно сохранены или ставить сохранение того чего еще не Сохранено. Остальные строки оставляем и вызываем для них опять фунцию преобразования в CSV.


            List_tuple_string_Select_Rows = self.Table_Transform_to_CSV.Get_Selected_Row_by_Value();
        

            #-------------------------------Удаляем из Выделенных строк уже Загруженные строки или Загружаемые в данный момент:Начало------------------------------------------------

            List_for_Delete = [];

            for Row_tuple in (List_tuple_string_Select_Rows):

                if (Row_tuple[8] == "Сохранено" or Row_tuple[8].find("Сохраняется") >= 0):
                    # Удаляем из списка.
                    List_for_Delete.append(Row_tuple);


            for tuple_delete in(List_for_Delete):
                List_tuple_string_Select_Rows.remove(tuple_delete);


            # List_tuple_string_Select_Rows - так теперь тут только нужные выделнные строки, которые нужно перезапросить у MOEX.

            #-------------------------------Удаляем из Выделенных строк уже Загруженные строки или Загружаемые в данный момент:Конец------------------------------------------------


        

            #---------------------------Теперь сформируем итоговый List_Final для загрузки свечей и для обнолвеня строк в Таблице Загрузки:Начало-------------------------

            List_Final:list[Create_Window_GUI__class.Engines_Market_Board_Intrument_Intervals_struct] = [];



            for Row in (List_tuple_string_Select_Rows):

                List_Final.append(Create_Window_GUI__class.Engines_Market_Board_Intrument_Intervals_struct());

                List_Final[-1].Engine_Clear       = Row[0];
                List_Final[-1].Market_Clear       = Row[1];
                List_Final[-1].Board_Clear        = Row[2];
                List_Final[-1].Instrument_Clear   = Row[3];

                List_Final[-1].Interval           = Row[4];
                List_Final[-1].Date_FROM          = Row[5];
                List_Final[-1].Date_TO            = Row[6];

                List_Final[-1].Path_to_Save       = Row[7];

            #---------------------------Теперь сформируем итоговый List_Final для загрузки свечей и для обнолвеня строк в Таблице Загрузки:Начало-------------------------


        

                
            #---------------------------------------Проставим в таблице загрузки для строк статус "Загружается":Начало------------------------------------------------

            for Row in (List_Final):

                self.Table_Transform_to_CSV.Edit_Row_by_ColumnIndex_by_ValueRow((Row.Engine_Clear, Row.Market_Clear, Row.Board_Clear, Row.Instrument_Clear, Row.Interval, Row.Date_FROM, Row.Date_TO, Row.Path_to_Save), (0,1,2,3,4,5,6,7), "Сохраняется", 8);

            #---------------------------------------Проставим в таблице загрузки для строк статус "Загружается":Начало------------------------------------------------

        


            #-------------------------------------------------------Вызываем преобразовалку в CSV:Начало--------------------------------------------------------
        
            self.ThreadPoolExecutor_HDD.submit(lambda List_Final=List_Final: self._Transform_Parquet_to_CSV(List_Final));  

            #-------------------------------------------------------Вызываем преобразовалку в CSV:Конец--------------------------------------------------------

        

            self.Button_Popup_Transform_to_CSV_Reload.Set_Show(False);


    def _Button_Final_Load_Callback__MOEX(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):
        

        #--------------------------------------------------Выбираем папку для сохранения:Начало------------------------------------------

        Path_to_Folder:str = self.Tkinter_GUI_obj.DialogMenu__Choose_Folder(self.Tkinter_GUI_obj.Get__ExecuteFile_PathFolder());

        if (Path_to_Folder == ""):
            # Значит Пользовтаель отменил выбор. Выходим.
            return;

        #--------------------------------------------------Выбираем папку для сохранения:Конец------------------------------------------


        #------------------------------------Устанавливаем кол-во потоков и делаем неактивным поля ввода потоков:Начало-----------------------------
        
        InputBox_Active_flag:bool = self.Input_Thread.Get_Active();
        
        if(InputBox_Active_flag == True):
            # Значит поле ввода активно, а значит это первое нажатие кнопки "Загрузки" свечей с MOEX: Установим кол-во потоков указанное в поле ввода и сделаем егонеактивным для дальнейших изменений.
            Num_Thread = int(self.Input_Thread.Get_Text());
            self.Input_Thread.Set_Active(False);
            self.ThreadPoolExecutor_MOEX._max_workers = Num_Thread;

        #------------------------------------Устанавливаем кол-во потоков и делаем неактивным поля ввода потоков:Конец-----------------------------





        #-----------------------------------------------------------------------
        List_Selected_UserСhoice:list[str] = self.Listbox_UserСhoice_struct.Get_Selected();            # Получим выбранные Пользовталем строки
        #-----------------------------------------------------------------------



        #------------------------------------------------Получим Дату:Начало--------------------------------------------
        
        #Date_String_FROM = self.DateTime_FROM.GetDate_String();
        #Date_String_TO   = self.DateTime_TO.GetDate_String();

        #DateTime_FROM_Day, DateTime_FROM_Month, DateTime_FROM_Year = Date_String_FROM.split("-");
        #DateTime_TO_Day, DateTime_TO_Month, DateTime_TO_Year       = Date_String_TO.split("-");

        date_from:Tkinter_GUI__class.DateTime_struct =  self.DateTime_FROM.GetDate_SplitString();
        DateTime_FROM_Year   = date_from.Year;
        DateTime_FROM_Month  = date_from.Month;
        DateTime_FROM_Day    = date_from.Day;

        date_to:Tkinter_GUI__class.DateTime_struct =  self.DateTime_TO.GetDate_SplitString();
        DateTime_TO_Year   = date_to.Year;
        DateTime_TO_Month  = date_to.Month;
        DateTime_TO_Day    = date_to.Day;

        #------------------------------------------------Получим Дату:Конец--------------------------------------------
        
        






        #--------------------------------------------По быстрому проверим корректность даты:Начало------------------------------------------------------

        if (DateTime_FROM_Year == "" and DateTime_FROM_Month == "" and DateTime_FROM_Day == ""):
            pass;  # Это ОК - такое допустимо.
        else:
            if (DateTime_FROM_Year == "" or DateTime_FROM_Month == "" or DateTime_FROM_Day == ""):
                # А вот таое уже не допустимо.
                self.Tkinter_GUI_obj.Call_MessageBox("Сообщение", "Неккоректно указана дата");
                return;

        if (DateTime_TO_Year == "" and DateTime_TO_Month == "" and DateTime_TO_Day == ""):
            pass;  # Это ОК - такое допустимо.
        else:
            if (DateTime_TO_Year == "" or DateTime_TO_Month == "" or DateTime_TO_Day == ""):
                # А вот таое уже не допустимо.
                self.Tkinter_GUI_obj.Call_MessageBox("Сообщение", "Неккоректно указана дата");
                return;

        #--------------------------------------------По быстрому проверим корректность даты:Начало------------------------------------------------------



        #-----------------------------------------------Поверим Пользователь выделил ли хоть какую то строку или нет:Начало------------------------------------

        if (len(List_Selected_UserСhoice) == 0):
            # Значит Пользовтаель ничего не выделил. Выходим.
            self.Tkinter_GUI_obj.Call_MessageBox("Сообщение", f"Не выделено ни одного инструмента");
            return;

        #-----------------------------------------------Поверим Пользователь выделил ли хоть какую то строку или нет:Конец------------------------------------


        #---------------------------Проверим во всех ли добавленных Пользователем строках доабвлен Интервал:Начало--------------------------------------------

        for Row in (List_Selected_UserСhoice):

            pos = Row.find("{");

            if (pos == -1):
                # Значит в этой строке нет ни одного добавленного интервала. Сообщамем об этом и выходим.
                self.Tkinter_GUI_obj.Call_MessageBox("Сообщение", f"У инструмента:{Row} - не добавлен интервал");
                return;

        #---------------------------Проверим во всех ли добавленных Пользователем строках доабвлен Интервал:Конец--------------------------------------------


        # Если код дошел до Сюда, то все корретно. Осталось разделить строку каждую строку выделенного Пользователем инстурмента на: Engine-Marker_Board-Intrument и интервалы и собстно запрашивать свечи у MOEX.


        #-------------------------------------------Разделяем строку на  Engine-Marker_Board-Intrument-Interval-Date_FROM-Date-TO:Качало-----------------------------------------

        List_Final:list[Create_Window_GUI__class.Engines_Market_Board_Intrument_Intervals_struct] = [];


        for Row in (List_Selected_UserСhoice):
        
            Separator_Index = Row.find("{");

            Engine_Market_Board_Interument_string = Row[0:Separator_Index];   # Вычленяем данные до Интверала

            List_Interval          = (Row[Separator_Index+1:len(Row)-1]).split(",");


            for Interval in (List_Interval):

                List_Final.append(Create_Window_GUI__class.Engines_Market_Board_Intrument_Intervals_struct());


                List_Final[-1].Engine,List_Final[-1].Market,List_Final[-1].Board,List_Final[-1].Instrument = Engine_Market_Board_Interument_string.split(self.Engine_Market_Board_Delemiter);

                List_Final[-1].Engine_Clear     = List_Final[-1].Engine[0:List_Final[-1].Engine.find("(")];
                List_Final[-1].Market_Clear     = List_Final[-1].Market[0:List_Final[-1].Market.find("(")];
                List_Final[-1].Board_Clear      = List_Final[-1].Board[0:List_Final[-1].Board.find("(")];
                List_Final[-1].Instrument_Clear = List_Final[-1].Instrument[0:List_Final[-1].Instrument.find("(")];

                List_Final[-1].Interval         = Interval;
                List_Final[-1].Path_to_Save     = Path_to_Folder;

                #------------------------------------------------------------------------------------
                Date_Begin:str = "";
                Date_End:str   = "";

                if (DateTime_FROM_Year == "" and DateTime_FROM_Month == "" and DateTime_FROM_Day == ""):
                    Date_Begin = "";
                else:
                    Date_Begin = DateTime_FROM_Year + "-" + DateTime_FROM_Month + "-" + DateTime_FROM_Day;


                if (DateTime_TO_Year == "" and DateTime_TO_Month == "" and DateTime_TO_Day == ""):
                    Date_End = "";
                else:
                    Date_End = DateTime_TO_Year + "-" + DateTime_TO_Month + "-" + DateTime_TO_Day;


                List_Final[-1].Date_FROM        = Date_Begin;
                List_Final[-1].Date_TO          = Date_End;
                #------------------------------------------------------------------------------------


            #print(f"{List_Final[-1].Engine},{List_Final[-1].Market},{List_Final[-1].Board},{List_Final[-1].Instrument}");
            #print(f"{List_Final[-1].Engine_Clear},{List_Final[-1].Market_Clear},{List_Final[-1].Board_Clear},{List_Final[-1].Instrument_Clear}");
            #print(List_Final[-1].Interval);
         #-------------------------------------------Разделяем строку на  Engine-Marker_Board-Intrument-Interval-Date_FROM-Date-TO:Конец-----------------------------------------







        #---------------------------------------------Добавим строки из списка в таблицу загружаемых свечей:--------------------

        self.Window_for_Table_Candles_Load.Show();


        List_tuple_for_Table_Load:list[tuple[str,str,str,str,str,str,str,str,str]] = [];
        List_for_Delete_From_List_Final = [];


        for Row in (List_Final):

            #-------------------------------Проверим на ДУБЛИКАТ, то есть есть ли загружаемые Инстурменты уже в таблице загрузке, и если есть - то не загружаем их повторно:-------------------------------------
            Row_Index_Dublicate = self.Table_Candles_Load.Check_Duplicate((Row.Engine, Row.Market, Row.Board, Row.Instrument, Row.Interval, Row.Date_FROM, Row.Date_TO,  Row.Path_to_Save), (0,1,2,3,4,5,6,7));

            if (Row_Index_Dublicate == -1):
                # Значит в таблице загрузок нет такой строки, значит добавляем в Список Загрузки Таблицы.

                List_tuple_for_Table_Load.append((Row.Engine, Row.Market, Row.Board, Row.Instrument, Row.Interval, Row.Date_FROM, Row.Date_TO, Row.Path_to_Save, "Загружается"));
            else:
                # Значит в таблице загрузок - есть такая сттрока, ЗНАЧИТ удаляим из списка "List_Final" из которого будет братся информация для физической загруки - эту строку, чтобы она реально не загружалась повторно.
                List_for_Delete_From_List_Final.append(Row);
            #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


            #------------------------------------
            for Row_Delete in (List_for_Delete_From_List_Final):
                List_Final.remove(Row_Delete);
            #------------------------------------


        self.Table_Candles_Load.Add_Row(List_tuple_for_Table_Load, 0);  # Добавляем в таблицу Загрузки

        #-------------------------------------------------------------------------------------------------------------------



        #-------------------------------------------------------Вызываем скачивалку с MOEX:Начало--------------------------------------------------------
        
        self.ThreadPoolExecutor_MOEX.submit(lambda List_Final=List_Final: self._Load_Candles_from_MOEX(List_Final));  

        #-------------------------------------------------------Вызываем скачивалку с MOEX:Конец--------------------------------------------------------

    def _Button_Final_Load_Callback__HDD(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):


        #--------------------------------------------------Выбираем папку для сохранения:Начало------------------------------------------

        Path_to_Folder:str = self.Tkinter_GUI_obj.DialogMenu__Choose_Folder(self.Tkinter_GUI_obj.Get__ExecuteFile_PathFolder());

        if (Path_to_Folder == ""):
            # Значит Пользовтаель отменил выбор. Выходим.
            return;

        #--------------------------------------------------Выбираем папку для сохранения:Конец------------------------------------------



        #-----------------------------------------------------------------------
        List_Selected_UserСhoice:list[str] = self.Listbox_UserСhoice_struct.Get_Selected();            # Получим выбранные Пользовталем строки
        #-----------------------------------------------------------------------



        #------------------------------------------------Получим Дату:Начало--------------------------------------------
        
        Date_String_FROM = self.DateTime_FROM.GetDate_String();
        Date_String_TO   = self.DateTime_TO.GetDate_String();

        DateTime_FROM_Day, DateTime_FROM_Month, DateTime_FROM_Year = Date_String_FROM.split("-");
        DateTime_TO_Day, DateTime_TO_Month, DateTime_TO_Year       = Date_String_TO.split("-");

        #------------------------------------------------Получим Дату:Конец--------------------------------------------
        
        


        #--------------------------------------------По быстрому проверим корректность даты:Начало------------------------------------------------------

        if (DateTime_FROM_Year == "" and DateTime_FROM_Month == "" and DateTime_FROM_Day == ""):
            pass;  # Это ОК - такое допустимо.
        else:
            if (DateTime_FROM_Year == "" or DateTime_FROM_Month == "" or DateTime_FROM_Day == ""):
                # А вот таое уже не допустимо.
                self.Tkinter_GUI_obj.Call_MessageBox("Сообщение", "Неккоректно указана дата");
                return;

        if (DateTime_TO_Year == "" and DateTime_TO_Month == "" and DateTime_TO_Day == ""):
            pass;  # Это ОК - такое допустимо.
        else:
            if (DateTime_TO_Year == "" or DateTime_TO_Month == "" or DateTime_TO_Day == ""):
                # А вот таое уже не допустимо.
                self.Tkinter_GUI_obj.Call_MessageBox("Сообщение", "Неккоректно указана дата");
                return;

        #--------------------------------------------По быстрому проверим корректность даты:Начало------------------------------------------------------



        #-----------------------------------------------Поверим Пользователь выделил ли хоть какую то строку или нет:Начало------------------------------------

        if (len(List_Selected_UserСhoice) == 0):
            # Значит Пользовтаель ничего не выделил. Выходим.
            self.Tkinter_GUI_obj.Call_MessageBox("Сообщение", f"Не выделено ни одного инструмента");
            return;

        #-----------------------------------------------Поверим Пользователь выделил ли хоть какую то строку или нет:Конец------------------------------------



         # Если код дошел до Сюда, то все корретно. Осталось разделить строку каждую строку выделенного Пользователем инстурмента на: Engine-Marker_Board-Intrument и интервалы и собстно запрашивать свечи у MOEX.



        #-------------------------------------------Разделяем строку на Folder-Engine-Marker_Board-Intrument-Interval:Начало-----------------------------------------

        List_Final:list[str] = [];


        for Row in (List_Selected_UserСhoice):
        

            #----------------------------------------------------------------------------------------------------
            List_Final.append(Create_Window_GUI__class.Engines_Market_Board_Intrument_Intervals_struct());


            List_Final[-1].Engine_Clear, List_Final[-1].Market_Clear, List_Final[-1].Board_Clear, List_Final[-1].Instrument_Clear, List_Final[-1].Interval = Row.split(self.Engine_Market_Board_Delemiter);

            List_Final[-1].Date_FROM    = Date_String_FROM;
            List_Final[-1].Date_TO      = Date_String_TO;
            List_Final[-1].Path_to_Save = Path_to_Folder;

            #----------------------------------------------------------------------------------------------------


        #-------------------------------------------Разделяем строку на Folder-Engine-Marker_Board-Intrument-Interval:Конец-----------------------------------------

        

        #---------------------------------------------Добавим строки из списка в таблицу загружаемых свечей:--------------------

        self.Window_for_Table_Transform_to_CSV.Show();


        List_tuple_for_Table_Load:list[tuple[str,str,str,str,str,str,str,str,str]] = [];
        List_for_Delete_From_List_Final = [];


        for Row in (List_Final):

            #-------------------------------Проверим на ДУБЛИКАТ, то есть есть ли загружаемые Инстурменты уже в таблице загрузке, и если есть - то не загружаем их повторно:-------------------------------------
            Row_Index_Dublicate = self.Table_Transform_to_CSV.Check_Duplicate((Row.Engine_Clear, Row.Market_Clear, Row.Board_Clear, Row.Instrument_Clear, Row.Interval, Row.Date_FROM, Row.Date_TO,  Row.Path_to_Save), (0,1,2,3,4,5,6,7));

            if (Row_Index_Dublicate == -1):
                # Значит в таблице загрузок нет такой строки, значит добавляем в Список Загрузки Таблицы.
                
                List_tuple_for_Table_Load.append((Row.Engine_Clear, Row.Market_Clear, Row.Board_Clear, Row.Instrument_Clear, Row.Interval, Row.Date_FROM, Row.Date_TO, Row.Path_to_Save, "Сохраняется"));
            else:
                # Значит в таблице загрузок - есть такая сттрока, ЗНАЧИТ удаляим из списка "List_Final" из которого будет братся информация для физической загруки - эту строку, чтобы она реально не загружалась повторно.
                List_for_Delete_From_List_Final.append(Row);
            #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


            #------------------------------------
            for Row_Delete in (List_for_Delete_From_List_Final):
                List_Final.remove(Row_Delete);
            #------------------------------------


        self.Table_Transform_to_CSV.Add_Row(List_tuple_for_Table_Load, 0);  # Добавляем в таблицу Загрузки

        #-------------------------------------------------------------------------------------------------------------------



        #-------------------------------------------------------Вызываем преобразовалку в CSV:Начало--------------------------------------------------------
        try:
            self.ThreadPoolExecutor_HDD.submit(lambda List_Final=List_Final: self._Transform_Parquet_to_CSV(List_Final));  
        except Exception as e:
            print(str(e))
        #-------------------------------------------------------Вызываем преобразовалку в CSV:Конец--------------------------------------------------------



    def _Button_Final_Load_Callback(self, Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):
        
        if (self.State == self.State_enum.Load_from_MOEX):
            self._Button_Final_Load_Callback__MOEX(Button_struct, List_any);

        if (self.State == self.State_enum.Load_from_HDD):
            self._Button_Final_Load_Callback__HDD(Button_struct, List_any);


    def _Set_Treeview_Right_Left_Click_Callback(self):


        def my_Right_Left_Click_callback(Treeview_Struct:Tkinter_GUI__class.Listbox_Struct, Click_Button_enum:Tkinter_GUI__class.Tkinter_GUI__class.Click_Button_enum, List_any:list[any]):
       
            # Значит Пользователь кликнул правой или левой кнопкой мыши по Box`у Treeview.

            if (Click_Button_enum == Tkinter_GUI__class.Tkinter_GUI__class.Click_Button_enum.Right):

                #--------------------------------------
                Pos_Cursor_:Tkinter_GUI__class.Pos_struct = self.Tkinter_GUI_obj.Get__Cursor_Pos_in_Window(self.Main_Window_struct);

                self.Button_Popup_for_UserLoad.Set_Pos(Pos_Cursor_.x, Pos_Cursor_.y, self.Tkinter_GUI_obj.Anchor_enum.TopLeft);
                self.Button_Popup_for_UserLoad.Set_Show(True);
                #--------------------------------------

            else:
                    if (Click_Button_enum == Tkinter_GUI__class.Tkinter_GUI__class.Click_Button_enum.Left):

                        self.Button_Popup_for_UserLoad.Set_Show(False);  # Скроем кнопку, если Пользотваель кликнул Правой кнопкой мыши по телу Treeview



            #````````````````````````````````````````````````````````````````-Load_from_MOEX:Начало-````````````````````````````````````````````````
            if (self.State == self.State_enum.Load_from_MOEX):
                self.Button_Popup_for_UserLoad.Set_Text("Загрузить");

            #````````````````````````````````````````````````````````````````-Load_from_MOEX:Конец-````````````````````````````````````````````````

            #````````````````````````````````````````````````````````````````-Load_from_HDD:Начало-````````````````````````````````````````````````
            if (self.State == self.State_enum.Load_from_HDD):
                self.Button_Popup_for_UserLoad.Set_Text("Нарисовать");

            #````````````````````````````````````````````````````````````````-Load_from_HDD:Конец-````````````````````````````````````````````````


        self.Treeview_ALLInstruments_MOEX_struct.Set_Callback_for_Right_Left_Click(my_Right_Left_Click_callback, []);  

    def _Set_Table_Instrument_Load_Click_for_Cell(self):


        def Click_Hadler(Table_Struct:Tkinter_GUI__class.Table_Struct, Row_Index:int, Column_Index:int, Click_Button_enum:Tkinter_GUI__class.Click_Button_enum, List_any:list[any]):

            if(Click_Button_enum == self.Tkinter_GUI_obj.Click_Button_enum.Right):
                # Значит Пользовтаель кликнул Правой Кнопой мыши по какой то ячейке/строке в Таблице "Table_Instrument_Load" и значит хочет перезаказать данные с сервера.
                # Делаем кнопку "Button_Popup_Instrument_Reload" видимой.

                Pos_Cursor_:Tkinter_GUI__class.Pos_struct = self.Tkinter_GUI_obj.Get__Cursor_Pos_in_Window(self.Window_for_Table_Instrument_Load);
                self.Button_Popup_Instrument_Reload.Set_Pos(Pos_Cursor_.x, Pos_Cursor_.y, self.Tkinter_GUI_obj.Anchor_enum.TopLeft);
                self.Button_Popup_Instrument_Reload.Set_TopLevel();
                self.Button_Popup_Instrument_Reload.Set_Show(True);

            if(Click_Button_enum == self.Tkinter_GUI_obj.Click_Button_enum.Left):
                self.Button_Popup_Instrument_Reload.Set_Show(False);       # Если Пользователь кликнул Левой кнопокй мыши по какой либо ячейки то скроем кнопку.


            if(Click_Button_enum == self.Tkinter_GUI_obj.Click_Button_enum.Double_Left):
                # Значит Пользователь сделал Двойной Левый Клик по какой то ячейки - намереваясь посмотреть все ее содержимое в отдельном окне.
                pass


        self.Table_Instrument_Load.Add_Callback_for_Click_for_Cell(Click_Hadler, []);

    def _Set_Table_Candles_ReLoadClick_for_Cell(self):
        

        def Click_Hadler(Table_Struct:Tkinter_GUI__class.Table_Struct, Row_Index:int, Column_Index:int, Click_Button_enum:Tkinter_GUI__class.Click_Button_enum, List_any:list[any]):

            if(Click_Button_enum == self.Tkinter_GUI_obj.Click_Button_enum.Right):
                # Значит Пользовтаель кликнул Правой Кнопой мыши по какой то ячейке/строке в Таблице "Table_Instrument_Load" и значит хочет перезаказать данные с сервера.
                # Делаем кнопку "Button_Popup_Candles_Reload" видимой.

                Pos_Cursor_:Tkinter_GUI__class.Pos_struct = self.Tkinter_GUI_obj.Get__Cursor_Pos_in_Window(self.Window_for_Table_Candles_Load);
                self.Button_Popup_Candles_Reload.Set_Pos(Pos_Cursor_.x, Pos_Cursor_.y, self.Tkinter_GUI_obj.Anchor_enum.TopLeft);
                self.Button_Popup_Candles_Reload.Set_TopLevel();
                self.Button_Popup_Candles_Reload.Set_Show(True);

            if(Click_Button_enum == self.Tkinter_GUI_obj.Click_Button_enum.Left):
                self.Button_Popup_Candles_Reload.Set_Show(False);       # Если Пользователь кликнул Левой кнопокй мыши по какой либо ячейки то скроем кнопку.


            if(Click_Button_enum == self.Tkinter_GUI_obj.Click_Button_enum.Double_Left):
                # Значит Пользователь сделал Двойной Левый Клик по какой то ячейки - намереваясь посмотреть все ее содержимое в отдельном окне.
                pass


        self.Table_Candles_Load.Add_Callback_for_Click_for_Cell(Click_Hadler, []);

    def _Set_Table_Transform_to_CSV_ReLoadClick_for_Cell(self):
        

            def Click_Hadler(Table_Struct:Tkinter_GUI__class.Table_Struct, Row_Index:int, Column_Index:int, Click_Button_enum:Tkinter_GUI__class.Click_Button_enum, List_any:list[any]):

                if(Click_Button_enum == self.Tkinter_GUI_obj.Click_Button_enum.Right):
                    # Значит Пользовтаель кликнул Правой Кнопой мыши по какой то ячейке/строке в Таблице "Table_Instrument_Load" и значит хочет перезаказать данные с сервера.
                    # Делаем кнопку "Button_Popup_Transform_to_CSV_Reload" видимой.

                    Pos_Cursor_:Tkinter_GUI__class.Pos_struct = self.Tkinter_GUI_obj.Get__Cursor_Pos_in_Window(self.Window_for_Table_Transform_to_CSV);
                    self.Button_Popup_Transform_to_CSV_Reload.Set_Pos(Pos_Cursor_.x, Pos_Cursor_.y, self.Tkinter_GUI_obj.Anchor_enum.TopLeft);
                    self.Button_Popup_Transform_to_CSV_Reload.Set_TopLevel();
                    self.Button_Popup_Transform_to_CSV_Reload.Set_Show(True);

                if(Click_Button_enum == self.Tkinter_GUI_obj.Click_Button_enum.Left):
                    self.Button_Popup_Transform_to_CSV_Reload.Set_Show(False);       # Если Пользователь кликнул Левой кнопокй мыши по какой либо ячейки то скроем кнопку.


                if(Click_Button_enum == self.Tkinter_GUI_obj.Click_Button_enum.Double_Left):
                    # Значит Пользователь сделал Двойной Левый Клик по какой то ячейки - намереваясь посмотреть все ее содержимое в отдельном окне.
                    pass


            self.Table_Transform_to_CSV.Add_Callback_for_Click_for_Cell(Click_Hadler, []);


    def _Set_SelectRow_Callback(self):

        self.Treeview_ALLInstruments_MOEX_struct.Add_Callback_for_Select(self._Treeview_ALLInstruments_MOEX_Callback, []);
        self.Listbox_UserСhoice_struct.Add_Callback_for_Select(self._Listbox_UserСhoice_Callback, []);
        self.Listbox_Intervals_struct.Add_Callback_for_Select(self._Listbox_Intervals_Callback, []);            
 
    def _Treeview_ALLInstruments_MOEX_Callback(self, Treeview_Struct:Tkinter_GUI__class.Listbox_Struct, Flag:bool, List_any:list[any]):
    
        # Flag: True - Значит Пользователь выделил какую то строку или несколько строк, False - значит снял выделение со ВСЕХ строк.

        self.Button_Add.Set_Active(Flag);

    def _Listbox_UserСhoice_Callback(self, OneColumnTable_aka_Listbox_Struct:Tkinter_GUI__class.Listbox_Struct, Flag:bool, List_any:list[any]):

        #---------------------------------------------------------     
        self.Button_Delete.Set_Active(Flag);
        self.Button_Export.Set_Active(Flag);

        if (self.State == self.State_enum.Load_from_MOEX):
            self.Button_by_Intervals_DeleteAll.Set_Active(Flag);
            self.Button_by_Intervals_AddAll.Set_Active(Flag);
        #---------------------------------------------------------


        #--------------------------------------------------------------
        self.Button_by_Intervals_Delete_Add_UserСhoice_Select:bool = Flag;

        if(self.Button_by_Intervals_Delete_Add_Intervals_Select == True and self.Button_by_Intervals_Delete_Add_UserСhoice_Select == True):

            if(self.State == self.State_enum.Load_from_MOEX):
                self.Button_by_Intervals_Delete.Set_Active(True);
                self.Button_by_Intervals_Add.Set_Active(True);

        else:
            if(self.State == self.State_enum.Load_from_MOEX):
                self.Button_by_Intervals_Delete.Set_Active(False);
                self.Button_by_Intervals_Add.Set_Active(False);
        #--------------------------------------------------------------

    def _Listbox_Intervals_Callback(self, Listbox_Struct:Tkinter_GUI__class.Listbox_Struct, Flag:bool, List_any:list[any]):
        
        if(self.State == self.State_enum.Load_from_MOEX):
            self.Button_by_Intervals_Add.Set_Active(Flag);
            self.Button_by_Intervals_Delete.Set_Active(Flag);


        #--------------------------------------------------------------
        self.Button_by_Intervals_Delete_Add_Intervals_Select:bool = Flag;

        if(self.Button_by_Intervals_Delete_Add_Intervals_Select == True and self.Button_by_Intervals_Delete_Add_UserСhoice_Select == True):

            if(self.State == self.State_enum.Load_from_MOEX):
                self.Button_by_Intervals_Delete.Set_Active(True);
                self.Button_by_Intervals_Add.Set_Active(True);

        else:
            if(self.State == self.State_enum.Load_from_MOEX):
                self.Button_by_Intervals_Delete.Set_Active(False);
                self.Button_by_Intervals_Add.Set_Active(False);
        #--------------------------------------------------------------



    def _Set_Callback_for_Empty(self):

        self.Listbox_UserСhoice_struct.Set_Callback_for_Empty(self._Listbox_UserСhoice_for_Empty_Callback,[]);

    def _Listbox_UserСhoice_for_Empty_Callback(self, OneColumnTable_aka_Listbox_Struct:Tkinter_GUI__class.Listbox_Struct, Flag:bool, List_any:list[any]):

        self.Button_DeleteAll.Set_Active(Flag);


    def _Request_ALL_INSTRUMENTS_MOEX(self)->tuple[list[MOEX_Download__class.Engines_Market_Board_struct]|None, None|str]:
         
        List_All_Intruments_MOEX, Text_Error = self.MOEX_Download_.Get__ALL_List_Engines_Market_Board_from_MOEX();

        if (List_All_Intruments_MOEX != None):
            return List_All_Intruments_MOEX, None;
        else:
            return None, Text_Error;

    def _Set_Intervals(self):
        
        self.Listbox_Intervals_struct.Add_ListRowText(self.List_Intervals, -1);


    def _Set_Button_Intervals_NotActive(self):

        self.Button_by_Intervals_AddAll.Set_Active(False);
        self.Button_by_Intervals_Add.Set_Active(False);
        self.Button_by_Intervals_DeleteAll.Set_Active(False);
        self.Button_by_Intervals_Delete.Set_Active(False);

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def _Save_Export_Rows_for_Load_MOEX_HDD(self, Data_ID:Create_Window_GUI__class.State_enum):

        List_Selected:list[str] = self.Listbox_UserСhoice_struct.Get_Selected();

        #-----------------------------------Расчитаем CRC32 сохраняемых строк:Начало-----------------------------------------
        # Расчитаем CRC32 сохраняемых строк - чтобы потом при загрузке их в "Load" проверить, что Пользователь случайно чего нибудь там не изменил - чтобы проблем с дальнешей загрузкой с MOEX ничего не было из за некоррекных данных.


        String_:str = "".join(List_Selected);  # Обьеденим все строки в одном стринге для расчета контрольной суммы.

        crc:int = zlib.crc32(String_.encode("utf-8"));

        crc_string = str(crc);
        #-----------------------------------Расчитаем CRC32 сохраняемых строк:Конец-----------------------------------------


        #---------------------------------Собсвенно теперь сохраняем расчитанный "crc_string" и сами строки в обычный текстовый файл:Начало-----------------------------

        # "crc_string" - сохраняем как текст обычной строкой в самой первой строке.

        def Save_to_TxtFile(FullPath_to_File:str, List_string: list[str]):
            with open(FullPath_to_File, "w", encoding="utf-8") as file:       # Очищаем файл и записываем с нуля
                file.write("\n".join(List_string))                            # Разделить строк ставим обычный "\n"



        if (self.State == self.State_enum.Load_from_HDD):
            if (self.Folder_to_Parqet_Files != ""):
                List_Selected.insert(0, self.Folder_to_Parqet_Files);
            else:
               self.Tkinter_GUI_obj.Call_MessageBox("Cообщение", "Не выбрана папка расположения Parquet-файлов." + "\n" + "Выбирите ее через кнопку <Загрузить HDD>");
               return;

        List_Selected.insert(0, Data_ID);              # Доавблям условный идентификатор сохраннеых данных - то есть эти строки относятся именно к интрументам для загрузки их с MOEX.
        List_Selected.insert(0, crc_string);           # Доавблям crc_string в начало.


        Full_Path_to_File:str = self.Tkinter_GUI_obj.DialogMenu__Choose_Folder_and_EnterFileName(self.Tkinter_GUI_obj.Get__ExecuteFile_PathFolder());  # Получим папку, которую выбрал Пользователь

        if (Full_Path_to_File == ""):
            # Значит пользователь отменил выбор. Выходим.
            return;

        Save_to_TxtFile(Full_Path_to_File, List_Selected);  # Сохраняем.
        #print(List_Selected);
        #---------------------------------Собсвенно теперь сохраняем расчитанный "crc" и сами строки в обычный текстовый файл:Конец-----------------------------

    def _Read_Load_Rows_for_Load_MOEX_HDD(self):


         #---------------------------------------------------------------------------------------
         Full_Path_to_ReadFile:str = self.Tkinter_GUI_obj.DialogMenu__Choose_OneFile(self.Tkinter_GUI_obj.Get__ExecuteFile_PathFolder());

         if (Full_Path_to_ReadFile == ""):
            # Значит пользователь отменил выбор. Выходим.
            return;


         def Read_from_TxtFile(Full_path:str)->list[str]:
             with open(Full_path, "r", encoding="utf-8") as File:

                List_string = File.read().splitlines();

                return List_string;



         List_string = Read_from_TxtFile(Full_Path_to_ReadFile);
         #---------------------------------------------------------------------------------------


         #------------------------------------Проверим идентификатор загруженных данных:Начало-------------------------------
         Data_ID_:str = List_string[1];

         if (Data_ID_ == self.State_enum.Load_from_MOEX):
             self.State = self.State_enum.Load_from_MOEX;
         else:
            if (Data_ID_ == self.State_enum.Load_from_HDD):
                self.State = self.State_enum.Load_from_HDD;
            else:
                # Значит второй строкой указано что-то другое - такого быть не должно. Выходим и сообщаем об этом.
                self.Tkinter_GUI_obj.Call_MessageBox("Cообщение", "Не загружено." + "\n" + "Данные файла были изменены");
                return;
         #------------------------------------Проверим идентификатор загруженных данных:Конец-------------------------------



         #----------------------------Так проверим контрольную сумму, которую считали при Эксопрте:--------------------------
         Start_Data_Index:int = -1;

         if (self.State == self.State_enum.Load_from_MOEX):
             Start_Data_Index = 2;   # Пропускаем CRC и State_ID
         if (self.State == self.State_enum.Load_from_HDD):
             Start_Data_Index = 3;   # Пропускаем CRC и State_ID и Папку с Parqet-файлами


         String_:str = "".join(List_string[Start_Data_Index:]);  # Обьеденим все строки в одном стринге для расчета контрольной суммы начиная с 3 элемента. (1 строка это сам crc, вторая индентификатор данных, а третья сами свечи)

         crc:int = zlib.crc32(String_.encode("utf-8"));

         crc_string = str(crc);


         # И сравним с CRC из прочитанного файла первой строки:

         if(crc_string != List_string[0]):
             # Значит ранее сохраненные строки - были изменены, поэтому завершаем работу загрузки и сообщамем об этом.

             self.Tkinter_GUI_obj.Call_MessageBox("Cообщение", "Не загружено." + "\n" + "Данные файла были изменены");
         
             return;

         #-------------------------------------------------------------------------------------------------------------------


     

         #--------------------------------------------------
         if (self.State == self.State_enum.Load_from_HDD):

            self.Folder_to_Parqet_Files = List_string[2];   # Достанем путь к папке с Parqet-файлами, которыу записывали туда при Экспорте Инстурментов.
         #--------------------------------------------------


         self.Listbox_UserСhoice_struct.Delete_All();

         self.Listbox_UserСhoice_struct.Add_Row_with_Duplicate_Check__Range(List_string, -1, Start_Data_Index, -1);  # Добволяем начиная с второго элемента, так как первым идет CRC32


         self.Set_Name_Final_Button_by_State();  # Поменяем текст Финальной кнопки в зависимости от State


    def Set_Name_Final_Button_by_State(self):

         if (self.State == self.State_enum.Load_from_MOEX):
             self.Button_Final_Load.Set_Text("Загрузить");
             return;

         if (self.State == self.State_enum.Load_from_HDD): 
            self.Button_Final_Load.Set_Text("Преобразовать в CSV");
            return;

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def _Set_Classic_Menu(self):
        

        #-----------------------------------------------------------------------------
        self.Classic_Menu.Set_Font_Size(11);

        self.Classic_Menu.Add_HighLevel_Element(["Окна", "Сообщить об ошибке"], 0);

        self.Classic_Menu.Add_Child_Element(["Окна"], ["Показать окно <Загрузки Инструментов>", "Показать окно <Загрузки Свечей>", "Показать окно <Сохранения в CSV>"], 0);
        self.Classic_Menu.Add_Child_Element(["Сообщить об ошибке"], ["Писать сюда"], 0);
        #-----------------------------------------------------------------------------


        #-----------------------------------------------------------------------------
        def Callback_for_Show_Window_Load_Intrument(Classic_Menu_Struct:Tkinter_GUI__class.Classic_Menu_Struct, List_any:list[any]):
            self.Window_for_Table_Instrument_Load.Show();

        def Callback_for_Show_Window_Load_Candles(Classic_Menu_Struct:Tkinter_GUI__class.Classic_Menu_Struct, List_any:list[any]):
            self.Window_for_Table_Candles_Load.Show();

        def Callback_for_Show_Window_Save_CSV(Classic_Menu_Struct:Tkinter_GUI__class.Classic_Menu_Struct, List_any:list[any]):
            self.Window_for_Table_Transform_to_CSV.Show();


        self.Classic_Menu.Add_Callaback_for_End_Element(["Окна", "Показать окно <Загрузки Инструментов>"], Callback_for_Show_Window_Load_Intrument, []);
        self.Classic_Menu.Add_Callaback_for_End_Element(["Окна", "Показать окно <Загрузки Свечей>"], Callback_for_Show_Window_Load_Candles, []);
        self.Classic_Menu.Add_Callaback_for_End_Element(["Окна", "Показать окно <Сохранения в CSV>"], Callback_for_Show_Window_Save_CSV, []);
         #-----------------------------------------------------------------------------


         

        #-----------------------------------------------------------------------------
        self.Label_for_SendError = self.Tkinter_GUI_obj.Add__Label(self.Window_for_SendError, "Label_for_SendError");

        self.Label_for_SendError.Set_Pos(5, 5, Tkinter_GUI__class.Tkinter_GUI__class.Anchor_enum.TopLeft);
        self.Label_for_SendError.Set_Text("t.me/MOEX_Download_Candles");
        self.Label_for_SendError.Set_AutoSize_by_Text();
        self.Label_for_SendError.Set_Font_Size(12);
        self.Label_for_SendError.Set_HyperLink("t.me/MOEX_Download_Candles");

        def Callback_for_SendfError(Classic_Menu_Struct:Tkinter_GUI__class.Classic_Menu_Struct, List_any:list[any]):
            self.Window_for_SendError.Show();


        self.Classic_Menu.Add_Callaback_for_End_Element(["Сообщить об ошибке", "Писать сюда"], Callback_for_SendfError, []);
        #-----------------------------------------------------------------------------

    def _Set_InputBox(self):
         
        self.Input_Thread.Set_Size(self.Button_Final_Load.Get__Size().width, self.Button_Final_Load.Get__Size().height);
        self.Input_Thread.Set_Size_AutoFollow_to_Widget(self.Button_Final_Load.Obj, 1, -1, 0, 0);

        self.Input_Thread.Set_Pos_AutoFollow_to_Widget(self.Tkinter_GUI_obj.Anchor_enum.Bottom_Middle, self.Button_Final_Load.Obj, self.Tkinter_GUI_obj.Anchor_Relative_enum.Top_Middle, 0, - 2 * self.Button_Offset_Y);

        self.Input_Thread.Set_Text(str(self.NumThread));
        self.Input_Thread.Set_Font_Size(10);
        self.Input_Thread.Set_Restriction_for_Enter_Non_Numeric_symv(True);
        

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def _Deque_Loop(self):
        
        while not self.Deque_ThreadSafe.empty(): 
            
            self.Deque_ThreadSafe.get()();  # Достаем функцию и вызываем ее.

        self.Main_Window_struct.Obj.after(100, self._Deque_Loop);   # Помещаем задачу в некую внутреннию очередь Окна "Main_Window_struct" с 100 мс задержкой, чтобы она она туда пометила опять эту функцию, которая опять проверит чередь на наличи задач выполнит или сразу пропустит и так по кругу.

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def _Save_Candles_to_ParqetFile(self, Candle_struct_, Path_to_Folder, Engine_clear, Market_clear, Board_clear, Instrument_clear, Interval_clear)->None|str:

        
        #---------------------------------------------------Сохраняем данные свечей в формате JSON MOEX в Parqet-файлы на диск:Начало--------------------------------------
        res:str = self.DuckDB_StockCandles_.Save_Candle_JSON_Format(Path_to_Folder, Candle_struct_, self.MOEX_Download_.Formate_Date_from_MOEX_string, Engine_clear, Market_clear, Board_clear, Instrument_clear, Interval_clear);

        if (res != None):   
            return res;
        else:
            return None;
        #---------------------------------------------------Сохраняем данные свечей в формате JSON MOEX в Parqet-файлы на диск:Конец--------------------------------------




#*********************************************************Main:Начало*********************************************************
def main():

    Window_GUI = Create_Window_GUI__class();






    Window_GUI.Main_Loop();



if __name__ == "__main__":
    main()
#*********************************************************Main:Конец*********************************************************