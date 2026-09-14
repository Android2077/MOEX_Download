
from ast import Pass
from dataclasses import fields
from dataclasses import dataclass, field
from enum import Enum
from enum import IntEnum
from enum import StrEnum
from collections.abc import Callable
from imaplib import ParseFlags
import tkinter
import tkinter.ttk
from tkinter import messagebox
import tkinter.font as tkFont
import random
import string
from datetime import datetime
import math
from tkinter import filedialog
from pathlib import Path
import os 
import sys
import webbrowser


def Window_Resize_Callback(Tkinter_wrapper__obj:Tkinter_GUI__class, Window_struct:Tkinter_GUI__class.Window_struct, With:int, Height:int, List_any:list[any]):
    print(f"Window_Resize: {Window_struct.Window_Name} : {With} {Height} {len(List_any)}");

def Window_Close_Callback(Window_struct:Tkinter_GUI__class.Window_struct, List_any:list[any]):

    # Колбек вызывается при клике на крестик закрытия окна.
    # Тут прописываются действия при этой клике. Если ничего не указать, то окно даже не закроется

    print("Window_Close_Callback");

    Window_struct.Close();

def Button_Click_Callback(Button_struct:Tkinter_GUI__class.Button_Struct, List_any:list[any]):
    print(f"Button_Click: {Button_struct.Name}");
    print(f"Button_Click: {Button_struct.Window_struct_ref.Window_Name}");
    print(f"Button_Click: {Button_struct.Window_struct_ref.Tkinter_GUI__Obj}");

    List_selected:list[Tkinter_GUI__class.Treeview_Select_struct] = Button_struct.Window_struct_ref.Tkinter_GUI__Obj.Get__Treeview_Struct_by_Name(Button_struct.Window_struct_ref.Window_Name, "My_Treeview_Name_1").Get_Selected();
    
    print(len(List_selected));
    
    for item in List_selected:

        for item_Header in item.List_Path_Header:
            print(item_Header, end = "_");

        print(":", end="");
        for item_Element in item.List_Elements:
            print(item_Element, end = "_");

        print("");



    List_selected_flat:list[str] = Button_struct.Window_struct_ref.Tkinter_GUI__Obj.Get__Treeview_Struct_by_Name(Button_struct.Window_struct_ref.Window_Name, "My_Treeview_Name_1").Get_Selection_Flat_List("-----");
    
    print(len(List_selected_flat));
    
    for item in List_selected_flat:
        print(item);

    print("");
    print("");
    print("");

    List_selected_flat_OnlyHeader:list[str] = Button_struct.Window_struct_ref.Tkinter_GUI__Obj.Get__Treeview_Struct_by_Name(Button_struct.Window_struct_ref.Window_Name, "My_Treeview_Name_1").Get_Selection_Flat_List_Only_Header("-----");
    
    print(len(List_selected_flat_OnlyHeader));
    
    for item in List_selected_flat_OnlyHeader:
        print(item);

    print("");
    print("");
    print("");


    List_selected_1:list[Tkinter_GUI__class.Treeview_Select_struct] = Button_struct.Window_struct_ref.Tkinter_GUI__Obj.Get__OneColumnTable_aka_Listbox_Struct_by_Name(Button_struct.Window_struct_ref.Window_Name, "My_OneColumnTable_Name_1").Get_Selected();
    
    for item in List_selected_1:
        print(f"{item} ");


    List_:list[Tkinter_GUI__class.Treeview_Select_struct] = Button_struct.Window_struct_ref.Tkinter_GUI__Obj.Get__OneColumnTable_aka_Listbox_Struct_by_Name(Button_struct.Window_struct_ref.Window_Name, "My_OneColumnTable_Name_1").Get_AllRows();
    
    for item in List_:
        print(f"{item} ");



    Date_Struct =  Button_struct.Window_struct_ref.Tkinter_GUI__Obj.Get__Entry_DateTime_Struct_by_Name(Button_struct.Window_struct_ref.Window_Name, "My_DateTime_Name_1");

    #date:Tkinter_GUI__class.DateTime_struct =  Date_Struct.GetDate_SplitString();
    #print(date.Year);

    print(Date_Struct.GetDate_String());




    Context_Menu_Struct:Tkinter_GUI__class.Context_Menu_Struct = Button_struct.Window_struct_ref.Tkinter_GUI__Obj.Get__Context_Menu_Struct_by_Name(Button_struct.Window_struct_ref.Window_Name, "My_Context_menu");
    Context_Menu_Struct.Set_Show_and_Pos(100,100);






def Inputbox_Enter_Callback(Tkinter_wrapper__obj:Tkinter_GUI__class, Window_struct:Tkinter_GUI__class.Window_struct, Inputbox_struct:Tkinter_GUI__class.Inputbox_Struct, List_any:list[any], Enter_Text:str):
    print(f"Inputbox_Name: {Inputbox_struct.Name}");
    print(f"Inputbox: {Enter_Text}");

def Listbox_Enter_Callback(Listbox_Struct:Tkinter_GUI__class.Listbox_Struct, Flag:bool, List_any:list[any]):
    
    # Flag: True - Значит Пользователь выделил какую то строку или несколько строк, False - значит снял выделение со ВСЕХ строк.

    print(f"Listbox_Enter_Callback: {Listbox_Struct.Name}");
    print(f"Listbox_Enter_Callback: {Listbox_Struct.Window_struct_ref.Window_Name}");
    print(f"Listbox_Enter_Callback: {Listbox_Struct.Window_struct_ref.Tkinter_GUI__Obj}");
    print(f"Listbox_Enter_Callback: {Flag}");

def Treeview_Enter_Callback(Treeview_Struct:Tkinter_GUI__class.Listbox_Struct, Flag:bool, List_any:list[any]):
    
    # Flag: True - Значит Пользователь выделил какую то строку или несколько строк, False - значит снял выделение со ВСЕХ строк.

    print(f"Listbox_Enter_Callback: {Treeview_Struct.Name}");
    print(f"Listbox_Enter_Callback: {Treeview_Struct.Window_struct_ref.Window_Name}");
    print(f"Listbox_Enter_Callback: {Treeview_Struct.Window_struct_ref.Tkinter_GUI__Obj}");
    print(f"Listbox_Enter_Callback: {Flag}");

def OneColumnTable_aka_Listbox_Enter_Callback(OneColumnTable_aka_Listbox_Struct:Tkinter_GUI__class.Listbox_Struct, Flag:bool, List_any:list[any]):
    
    # Flag: True - Значит Пользователь выделил какую то строку или несколько строк, False - значит снял выделение со ВСЕХ строк.

    print(f"Listbox_Enter_Callback: {OneColumnTable_aka_Listbox_Struct.Name}");
    print(f"Listbox_Enter_Callback: {OneColumnTable_aka_Listbox_Struct.Window_struct_ref.Window_Name}");
    print(f"Listbox_Enter_Callback: {OneColumnTable_aka_Listbox_Struct.Window_struct_ref.Tkinter_GUI__Obj}");
    print(f"Listbox_Enter_Callback: {Flag}");
  
def OneColumnTable_aka_Listbox_Callback_for_Empty(OneColumnTable_aka_Listbox_Struct:Tkinter_GUI__class.Listbox_Struct, Flag:bool, List_any:list[any]):
    
    # Flag: True - Значит Пользователь выделил какую то строку или несколько строк, False - значит снял выделение со ВСЕХ строк.

    print(f"OneColumnTable_aka_Listbox_Callback_for_Empty: {OneColumnTable_aka_Listbox_Struct.Name}");
    print(f"OneColumnTable_aka_Listbox_Callback_for_Empty: {OneColumnTable_aka_Listbox_Struct.Window_struct_ref.Window_Name}");
    print(f"OneColumnTable_aka_Listbox_Callback_for_Empty: {OneColumnTable_aka_Listbox_Struct.Window_struct_ref.Tkinter_GUI__Obj}");
    print(f"OneColumnTable_aka_Listbox_Callback_for_Empty: {Flag}");

def Callback_Right_Left_Click_Treeview(Treeview_Struct:Tkinter_GUI__class.Listbox_Struct, Click_Button_enum:Tkinter_GUI__class.Click_Button_enum, List_any:list[any]):


    print(Tkinter_GUI__class.Click_Button_enum)

    if(Click_Button_enum == Tkinter_GUI__class.Click_Button_enum.Left):
        print("Left CLick");
    
    
    if(Click_Button_enum == Tkinter_GUI__class.Click_Button_enum.Right):
        print("Right CLick");

def Table__Callback_for_Click_for_Cell(Table_Struct:Tkinter_GUI__class.Table_Struct, Row_Index:int, Column_Index:int, Click_Button_enum:Tkinter_GUI__class.Click_Button_enum, List_any:list[any]):

    print(str(Row_Index) + ":" + str(Column_Index));
    Cell_string = Table_Struct.Get_Cell_Value(Row_Index, Column_Index);
    print(Cell_string);

    Row_tuple_string = Table_Struct.Get_Row_Value(Row_Index);
    print(Row_tuple_string);



    if(Click_Button_enum == Tkinter_GUI__class.Click_Button_enum.Left):
        print("Left");

    if(Click_Button_enum == Tkinter_GUI__class.Click_Button_enum.Right):
        print("Right");

    if(Click_Button_enum == Tkinter_GUI__class.Click_Button_enum.Double_Left):
        print("Double_Left");

    if(Click_Button_enum == Tkinter_GUI__class.Click_Button_enum.Double_Right):
        print("Double_Right");

def Menu__Callback_for_Click_to_Element(Classic_Menu_Struct:Tkinter_GUI__class.Classic_Menu_Struct, List_any:list[any]):
    print("Menu__Callback_for_Click_to_Element")







class Tkinter_GUI__class():

    class Click_Button_enum(IntEnum):
        Left        = 1
        Right       = 2
        Double_Left = 3
        Double_Right= 4

    class Anchor_enum(StrEnum):
        TopLeft       = "nw"
        TopRight      = "ne"
        BottomLeft    = "sw"
        BottomRight   = "se"
        Top_Middle    = "n"
        Bottom_Middle = "s"
        Left_Middle   = "w"
        Right_Middle  = "e"
        Center        = "center"

    class Anchor_Relative_enum(Enum):
        TopLeft       = (0.0, 0.0)
        TopRight      = (1.0, 0.0)
        BottomLeft    = (0.0, 1.0)
        BottomRight   = (1.0, 1.0)
        Top_Middle    = (0.5, 0.0)
        Bottom_Middle = (0.5, 1.0)
        Left_Middle   = (0.0, 0.5)
        Right_Middle  = (1.0, 0.5)
        Center        = (0.5, 0.5)



    #-------------------------------------------------------Enums:Начало--------------------------------------------------
    class Sort_enum(IntEnum):
        descending = 0  # по убыванию
        ascending  = 1  # по возростанию
        none       = 2

    class Filter_enum(IntEnum):
        Equals          = 0
        Not_equals      = 1
        Contains        = 2
        Not_contain     = 3
        Starts_with     = 4
        Not_start_with  = 5

    class Listbox_SelectMode_enum(IntEnum):
        BROWSE   = 0 # (по умолчанию) — один элемент, клик просто переносит выделение
        SINGLE   = 1 #  один элемент, но без "перетаскивания" выделения при зажатой кнопке
        MULTIPLE = 2 #  можно кликать по нескольку элементов, каждый клик toggle'ит выделение
        EXTENDED = 3 # обычный клик, Shift — диапазон, Ctrl — добавить/убрать элемент  (Все остальные режимы по сути неудобное дерьмо)

    class Treeview_SelectMode_enum(StrEnum):
        browse   = "browse"   # можно выделить только одну строку
        extended = "extended" # можно выделить несколько (Ctrl/Shift)
        none     = "none"     # выделение вообще запрещено

    class Before_After_enum(IntEnum):
        Before = 0  # До
        After  = 1  # После
    #-------------------------------------------------------Enums:Начало--------------------------------------------------
    

    #-------------------------------------------------------------------------------------
    
    @dataclass
    class Size_struct:
        width:int  = 0;
        height:int = 0;

    @dataclass
    class Pos_struct:
        x:int  = 0;
        y:int = 0;

    @dataclass
    class Treeview_Select_struct:
        List_Path_Header:list[str] = field(default_factory=list);  # Полный путь до Хедера
        List_Elements:list[str]    = field(default_factory=list);  # Список элементов Хедера

    @dataclass
    class DateTime_struct:
        Year:str  = "";
        Month:str = "";
        Day:str   = "";
        Hour:str  = "";
        Min:str   = "";
    
    @dataclass
    class Menu_Separator_struct:
        List_Path_to_Parent_element:list[str] = field(default_factory=list);   # Указывается путь до Родителького элемента в элементах которого нужно установить "разделитель". Последовталеьно начиная от самого Родительского до нужного.
        Element_name:str                      = 0;                             # Позиция элемента среди элементов Родителя указанного в "List_Path_to_Parent_element" ДО или ПОСЛЕ которого нужно установить разделитель. ЕСЛИ "-1" - то значит самый нижний элемент.
        Before_After_Flag:Tkinter_GUI__class.Before_After_enum = lambda:field(default_factory=Tkinter_GUI__class.Before_After_enum.Before);
    
    @dataclass
    class Menu_Element_Struct:
        Name:str = "";
        List_Elements:Tkinter_GUI__class.Menu_Element_Struct = field(default_factory=list);
        Menu_Obj:tkinter.Menu = None;    # Если None - значит детей нет.
        Pos = -1;                        # Позиция элемента
        Parent_Classic_Menu_Struct:Tkinter_GUI__class.Menu_Element_Struct = None;     # Ссылка на Родительскую стрктуру.
    #-------------------------------------------------------------------------------------

    

    @dataclass(slots=True)
    class Callback_struct:
        Callback:Callable = None;
        List_any:list[any] = field(default_factory=list);


    @dataclass(slots=True)
    class Window_struct:
        Tkinter_GUI__Obj: "Tkinter_GUI__class" = None;

        Window_Name:str = "";
        Obj:tkinter.Tk = field(default_factory=tkinter.Tk);

        List_Buttons:list[Tkinter_GUI__class.Button_Struct]          = field(default_factory =list);
        List_Listbox:list[Tkinter_GUI__class.Listbox_Struct]         = field(default_factory =list);
        List_Treeview:list[Tkinter_GUI__class.Treeview_Struct]       = field(default_factory =list);
        List_Inputbox:list[Tkinter_GUI__class.Inputbox_Struct]       = field(default_factory =list);
        List_Table:list[Tkinter_GUI__class.Table_Struct]             = field(default_factory =list);
        List_ProgressBar:list[Tkinter_GUI__class.ProgressBar_Struct] = field(default_factory =list);
        List_OneColumnTable_aka_Listbox:list[Tkinter_GUI__class.OneColumnTable_aka_Listbox_Struct] = field(default_factory =list);
        List_Entry_DateTime:list[Tkinter_GUI__class.Entry_DateTime_Struct]                         = field(default_factory =list);
        List_Label:list[Tkinter_GUI__class.Label_Struct]                                           = field(default_factory =list);
        Classic_Menu:Tkinter_GUI__class.Classic_Menu_Struct                                        = field(default_factory = lambda: Tkinter_GUI__class.Classic_Menu_Struct());
        List_Context_Menu:Tkinter_GUI__class.Context_Menu_Struct                                   = field(default_factory =list);


        current_size_for_Resize_Callback:Tkinter_GUI__class.Size_struct     = field(default_factory      = lambda: Tkinter_GUI__class.Size_struct);
        List_Callback_for_Resize:list[Tkinter_GUI__class.Callback_struct]   = field(default_factory = list);


        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------
        def Set_Size(self, Width:int, Height:int):
            self.Obj.geometry(f"{Width}x{Height}");

        def Set_Resizeble_flags(self, Width_flag:bool, Height_flag:bool):
            self.Obj.resizable(Width_flag, Height_flag);  # Width_flag=True/False - Блокирует или разрешает изменение Ширины окна курсором мыши. Height_flag - тоже самое только по высоте.

        def Add__Resizible_Callback(self, Callback_func, List_any:list[any]):

            self.current_size_for_Resize_Callback:Tkinter_GUI__class.Size_struct = self.Get_Size();

            self.List_Callback_for_Resize.append(Tkinter_GUI__class.Callback_struct(Callback_func, List_any));


            def _on_configure(event):
                if event.widget == self.Obj:
                    if (event.width != self.current_size_for_Resize_Callback.width or event.height != self.current_size_for_Resize_Callback.height):
                    
                        for callback_item in self.List_Callback_for_Resize:
                    
                            callback_item.Callback(self, self, event.width, event.height, callback_item.List_any)


                        self.current_size_for_Resize_Callback.width  = event.width; # Обновим данные
                        self.current_size_for_Resize_Callback.height = event.height;

            if len(self.List_Callback_for_Resize) == 1:
                self.Obj.bind("<Configure>", _on_configure)   # Это первый вызов функции "Set__Resizible_Callback" - поэтому привяжим колбек к данному окну.

        def Set_NotCloseWindow_but_Hidden(self):

            def Close_callback(Window_struct):
                Window_struct.Hidden();

            self.Obj.protocol("WM_DELETE_WINDOW", lambda self = self: Close_callback(self));

        def Set_Overriding_Сlose_Callback(self, Callback_func, List_any:list[any]):

            # Устанавливает колбек который будет вызываться при клике по крестику закртия и переопределять поведение.

            def Close_callback(Window_struct, user_Callback_func, List_any):
                user_Callback_func(Window_struct, List_any);


            self.Obj.protocol("WM_DELETE_WINDOW", lambda self = self, Callback_func=Callback_func, List_any=List_any: Close_callback(self, Callback_func, List_any));

        def Show(self):
            self.Obj.deiconify();  # Показать
        def Hidden(self):
            self.Obj.withdraw();   # Скрыть
        def Close(self):
            self.Obj.destroy();

        def Get__TOP_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y());
   
        def Get__TOP_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width(), self.Obj.winfo_y());
            
        def Get__BOTTOM_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height());

        def Get__BOTTOM_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width(), self.Obj.winfo_y() + self.Obj.winfo_height());
        
        def Get__CENTRE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width()/2, self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__TOP_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() +  self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__BOTTOM_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__LEFT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__RIGHT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);
       

        def Get__TOP_LEFT_Inner_Pos(self)->Tkinter_GUI__class.Pos_struct:

            return Tkinter_GUI__class.Pos_struct(0, 0);
   
        def Get__TOP_RIGHT_Inner_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_width(), 0);
            
        def Get__BOTTOM_LEFT_Inner_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(0, self.Obj.winfo_height());

        def Get__BOTTOM_RIGHT_Inner_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_width(), self.Obj.winfo_height());
        
        def Get__CENTRE_Inner_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_width()/2,self.Obj.winfo_height()/2);

        def Get__TOP_MIDDLE_Inner_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_width()/2, 0);

        def Get__BOTTOM_MIDDLE_Inner_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__LEFT_MIDDLE_Inner_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(0, self.Obj.winfo_height()/2);

        def Get__RIGHT_MIDDLE_Inner_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_height()/2);
       

        def Get_Size(self)->Tkinter_GUI__class.Size_struct:

            self.Obj.update()  # или update()

            return Tkinter_GUI__class.Size_struct(self.Obj.winfo_width(), self.Obj.winfo_height());

        #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------

    @dataclass(slots=True)
    class Button_Struct:
        Window_struct_ref:Tkinter_GUI__class.Window_struct = None;

        Name:str = "";
        Obj:tkinter.Button = field(default_factory=tkinter.Button);

        Font_Name:str = "Arial";
        Font_Size:int = 12;

        List_Callback_for_Click:list[Tkinter_GUI__class.Callback_struct]   = field(default_factory = list);



        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------

        def Add_Click_Callback(self, Callback_func, List_any:list[any]):

              self.List_Callback_for_Click.append(Tkinter_GUI__class.Callback_struct(Callback_func, List_any));

              def _on_click():
                for callback_item in self.List_Callback_for_Click:
                    callback_item.Callback(self, callback_item.List_any);

              if len(self.List_Callback_for_Click) == 1:
                self.Obj.config(command = _on_click);    # Это первый вызов функции "Set_Click_Callback" - поэтому привяжим колбек к данной кнопке.




        def Set_Size(self, Width:int, Height:int):

            self.Obj.place(width=Width, height=Height);

        def Set_Height(self, Height:int):

            self.Obj.place(height=Height);

        def Set_Width(self, Width:int):

            self.Obj.place(width=Width);

        def Set_Pos(self, X:int, Y:int, Anchor_ID:Anchor_enum):

            self.Obj.place(x=X, y=Y, anchor = Anchor_ID);


        def Set_Active(self, Flag:bool):

            if (Flag == True):
                # Значит сделать кнопку Активной:
                self.Obj.config(state="normal");
            else:
                # значит не активной:
                self.Obj.config(state="disabled");

        def Set_TopLevel(self):
            self.Obj.lift();

        def Set_Show(self, Flag:bool):

            if(Flag == True):
                self.Set_Pos(self.Get__TOP_LEFT_Pos().x,self.Get__TOP_LEFT_Pos().y, Tkinter_GUI__class.Anchor_enum.TopLeft);
            else:
                self.Obj.place_forget();


        def Set_Pos_AutoFollow_to_Widget(self, Widget_From_Anchor_ID:Anchor_enum, Widget_To, Widget_To_Anchor_ID:Anchor_Relative_enum, Offset_Anchor_X,  Offset_Anchor_Y):     

            # Функция устанавливаем автоматическое следование заданного угла одного Виджета за заданным углом друого виджета.

            # Widget_From                       - виджет которй должен следовать.
            # Widget_From_Anchor_ID             - угол-якорь виджета "Widget_From" которым он должен следовать за указанной позицией у виджета "Widget_To" в углке-якоре "Widget_To_Anchor_ID"
            # Widget_To                         - виджет за координатами которого должен следовать виджет "Widget_From"
            # Offset_Anchor_X и Offset_Anchor_Y - АБСОЛЮТНОЕ смещение смещение от координаты привязки, короче коррекитровка, если она нужна.


            relative_X, relative_Y = Widget_To_Anchor_ID.value;

            self.Obj.place(in_ = Widget_To,  relx = relative_X, rely = relative_Y, x=Offset_Anchor_X, y=Offset_Anchor_Y, anchor = Widget_From_Anchor_ID);

        def Set_Size_AutoFollow_to_Widget(self, Widget_To, Relative_Width, Relative_Height, Width_Offset, Height_Offset):
        
            # Функция устанавливаем автоматическое следование размера одного Виджета за размером друого виджета.
        
            # Widget_From    - виджет которй должен следовать.
            # Widget_To      - виджет за размерами которого должен следовать виджет "Widget_From"
            # Relative_Width - ОТНОСИТЕЛЬНЫЙ размер виджета "Widget_To" который будет автоматически передаватся на виджет "Widget_From". Вообщем Relative_Width = 1, то значит это Полная Ширина виджета "Widget_To", Relative_Width = 0.5 - половина Ширины вижета и так далее, то есть Ширина Виджета "Widget_From" всегда будет автоматически подстраиватся под указанную Ширину.
            # Relative_Height - тоже самое, что и "Relative_Width" - только для высоты.
            # Width_Offset, Height_Offset - это АБСОЛЮТНОЕ смешение в Ширине или Высоте - если нужна более точная настрока. Потому что в относительных процентах не всегда увилирно можно настроить.

            # Если один из Relative_Width или Relative_Height указаны = -1, то значит автоследование по этому параметру не будет ставится.
            
            
            if (Relative_Width != -1 and Relative_Height != -1):
                self.Obj.place(in_ = Widget_To, relwidth = Relative_Width, relheight = Relative_Height, width = Width_Offset, height = Height_Offset);
                return;

            if (Relative_Width == -1 and Relative_Height != -1):
                self.Obj.place(in_ = Widget_To, relheight = Relative_Height, height = Height_Offset);
                return;

            if (Relative_Height == -1 and Relative_Width != -1):
                self.Obj.place(in_ = Widget_To, relwidth = Relative_Width, width = Width_Offset);
                return;


        def Set_Text(self, Button_Text:str):

            self.Obj.config(text=Button_Text);

        def Set_Background_Color(self, Color:str):

            self.Obj.config(bg=Color);

        def Set_Text_Color(self, Color:str):

            self.Obj.config(fg=Color);

        def Set_Font_Name(self, Font_Name:str):

            self.Font_Name = Font_Name;

            self.Obj.config(font=(Font_Name, self.Font_Size))

        def Set_Font_Size(self, Font_Size:int):

            self.Obj.config(font=(self.Font_Name, Font_Size));

            self.Font_Size = Font_Size;

    
        def Get__TOP_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y());
   
        def Get__TOP_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width(), self.Obj.winfo_y());
            
        def Get__BOTTOM_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height());

        def Get__BOTTOM_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width(), self.Obj.winfo_y() + self.Obj.winfo_height());
        
        def Get__CENTRE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width()/2, self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__TOP_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() +  self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__BOTTOM_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__LEFT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__RIGHT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);
       

        def Get__Size(self)->Tkinter_GUI__class.Size_struct:

            self.Window_struct_ref.Obj.update();

            return Tkinter_GUI__class.Size_struct(self.Obj.winfo_width(), self.Obj.winfo_height());

        #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------

    @dataclass(slots=True)
    class Listbox_Struct:
        Window_struct_ref: Tkinter_GUI__class.Window_struct = None;

        Name: str = "";
        Obj: tkinter.Listbox = field(default_factory=tkinter.Listbox);
        Container:Frame      = field(default_factory=tkinter.Frame);

        Font_Name:str = "Arial";
        Font_Size:int = 12;
        V_scroll_obj:Scrollbar = field(default_factory=tkinter.Scrollbar);
        H_scroll_obj:Scrollbar = field(default_factory=tkinter.Scrollbar);


        List_Callback_for_Select:list[Tkinter_GUI__class.Callback_struct]   = field(default_factory = list);
    
        Callback_Right_Left_Click:Tkinter_GUI__class.Callback_struct =  field(default_factory = lambda: Tkinter_GUI__class.Callback_struct());   # Колбек на Правый клик мыши по Box`у виджета.

        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------

        def Add_Callback_for_Select(self, Callback_func, List_any:list[any]):
              
              self.List_Callback_for_Select.append(Tkinter_GUI__class.Callback_struct(Callback_func, List_any));
              
              def _on_select(event):

                selected = event.widget.curselection();
                Flag:bool = False;

                if selected:
                    Flag =True;  # Значит Пользовтаель что-то выбрал.
                else:
                    Flag = False; # Значит Пользователь снял выделение со всех строк.

                for callback_item in self.List_Callback_for_Select:
                    callback_item.Callback(self, Flag, callback_item.List_any);


              if len(self.List_Callback_for_Select) == 1:
                self.Obj.bind("<<ListboxSelect>>", _on_select);      # Это первый вызов функции "List_Callback_for_Click" - поэтому привяжим колбек к данной кнопке.
        
        def Set_Callback_for_Right_Left_Click(self, Callback_Right_Left_Click, List_any:list[any]):

            # Ставит колбек на Правый клик мыши по Box`у виджета.

            self.Callback_Right_Left_Click.Callback = Callback_Right_Left_Click;
            self.Callback_Right_Left_Click.List_any = List_any;

            def _intermediate_func(event):

                if event.num == 1:
                    self.Callback_Right_Left_Click.Callback(self, Tkinter_GUI__class.Click_Button_enum.Left, self.Callback_Right_Left_Click.List_any);  # Значит Левая
                elif event.num == 3:
                    self.Callback_Right_Left_Click.Callback(self, Tkinter_GUI__class.Click_Button_enum.Right, self.Callback_Right_Left_Click.List_any);  # Значит Правая

           

            self.Obj.bind("<Button-1>", _intermediate_func);   # Левая Button
            self.Obj.bind("<Button-3>", _intermediate_func);   # Правая Button



        def Set_Size(self,Width:int, Height:int):

            self.Container.place(width=Width, height=Height);

        def Set_Pos(self,X:int, Y:int, Anchor_ID:Anchor_enum):

            self.Container.place(x=X, y=Y, anchor = Anchor_ID);


        def Set_Pos_AutoFollow_to_Widget(self, Widget_From_Anchor_ID:Anchor_enum, Widget_To, Widget_To_Anchor_ID:Anchor_Relative_enum, Offset_Anchor_X,  Offset_Anchor_Y):     

            # Функция устанавливаем автоматическое следование заданного угла одного Виджета за заданным углом друого виджета.

            # Widget_From                       - виджет которй должен следовать.
            # Widget_From_Anchor_ID             - угол-якорь виджета "Widget_From" которым он должен следовать за указанной позицией у виджета "Widget_To" в углке-якоре "Widget_To_Anchor_ID"
            # Widget_To                         - виджет за координатами которого должен следовать виджет "Widget_From"
            # Offset_Anchor_X и Offset_Anchor_Y - АБСОЛЮТНОЕ смещение смещение от координаты привязки, короче коррекитровка, если она нужна.


            relative_X, relative_Y = Widget_To_Anchor_ID.value;

            self.Container.place(in_ = Widget_To,  relx = relative_X, rely = relative_Y, x=Offset_Anchor_X, y=Offset_Anchor_Y, anchor = Widget_From_Anchor_ID);

        def Set_Size_AutoFollow_to_Widget(self, Widget_To, Relative_Width, Relative_Height, Width_Offset, Height_Offset):
        
            # Функция устанавливаем автоматическое следование размера одного Виджета за размером друого виджета.
        
            # Widget_From    - виджет которй должен следовать.
            # Widget_To      - виджет за размерами которого должен следовать виджет "Widget_From"
            # Relative_Width - ОТНОСИТЕЛЬНЫЙ размер виджета "Widget_To" который будет автоматически передаватся на виджет "Widget_From". Вообщем Relative_Width = 1, то значит это Полная Ширина виджета "Widget_To", Relative_Width = 0.5 - половина Ширины вижета и так далее, то есть Ширина Виджета "Widget_From" всегда будет автоматически подстраиватся под указанную Ширину.
            # Relative_Height - тоже самое, что и "Relative_Width" - только для высоты.
            # Width_Offset, Height_Offset - это АБСОЛЮТНОЕ смешение в Ширине или Высоте - если нужна более точная настрока. Потому что в относительных процентах не всегда увилирно можно настроить.

            # Если один из Relative_Width или Relative_Height указаны = -1, то значит автоследование по этому параметру не будет ставится.
            
            
            if (Relative_Width != -1 and Relative_Height != -1):
                self.Container.place(in_ = Widget_To, relwidth = Relative_Width, relheight = Relative_Height, width = Width_Offset, height = Height_Offset);
                return;

            if (Relative_Width == -1 and Relative_Height != -1):
                self.Container.place(in_ = Widget_To, relheight = Relative_Height, height = Height_Offset);
                return;

            if (Relative_Height == -1 and Relative_Width != -1):
                self.Container.place(in_ = Widget_To, relwidth = Relative_Width, width = Width_Offset);
                return;


        def Set_Background_Color(self, Color:str):

            self.Obj.config(bg=Color);

        def Set_Select_Mode(self,SelectMode:Tkinter_GUI__class.Listbox_SelectMode_enum):
        
            if (SelectMode == Tkinter_GUI__class.Listbox_SelectMode_enum.BROWSE):
                self.Obj.config(selectmode=tkinter.BROWSE)
            if (SelectMode == Tkinter_GUI__class.Listbox_SelectMode_enum.SINGLE):
                self.Obj.config(selectmode=tkinter.SINGLE)
            if (SelectMode == Tkinter_GUI__class.Listbox_SelectMode_enum.MULTIPLE):
                self.Obj.config(selectmode=tkinter.MULTIPLE)
            if (SelectMode == Tkinter_GUI__class.Listbox_SelectMode_enum.EXTENDED):
                self.Obj.config(selectmode=tkinter.EXTENDED)

       

        def Add_RowText(self,Text:str, Index:int):

            # Index - позиция вставки

            if(Index == -1):
                self.Obj.insert(tkinter.END, Text);
            else:

                if(Index == 0):
                    self.Obj.insert(1, Text); # Вставляем вторым элементом - с учетом резевра первой строки под ввод фильтрации.
                else:

                    # Значит Пользователь хочет вставить текст в нужное ему место: то есть Index = 1, значит вставка элемента идет после первого элемента.

                    if (Index < self.Obj.size()):
                        self.Obj.insert(Index, Text);
                    else:
                        self.Obj.insert(tkinter.END, Text);
        
        def Add_ListRowText(self,ListText:list[str], Index:int):
        
            # Index - актуален только при Listbox_InsrtPos_enum = Index


            if(Index == -1):
                self.Obj.insert(tkinter.END, *ListText);
            else:
                if(Index == 0):
                    self.Obj.insert(1, *ListText);     # Вставляем вторым элементом - с учетом резевра первой строки под ввод фильтрации.
                else:
                # Значит Пользователь хочет вставить текст в нужное ему место: то есть Index = 1, значит вставка элемента идет после первого элемента.
                    if (Index < self.Obj.size()):
                        self.Obj.insert(Index, *ListText);
                    else:
                        self.Obj.insert(tkinter.END, *ListText);



        def Delete_Row_by_Index(self,Index:int):

            if (Index == -1):
                Index = self.Obj.size() - 1;

            self.Obj.delete(Index);


        def Delete_Row_by_Text(self,Text:str):
        
            all_elements = self.Obj.get(0, tkinter.END)  # Возвращает tuple соссылками на строки в каждм элемента, а не сами строки. Странное решение.


            #------------------------Найдем номер Индекса, который соответвует искомому тексту строки:Начало----------------------------------------
            Index_find:int = -1;

            for i in range(len(all_elements)):
                if all_elements[i] == Text:
                    Index_find = i;
                    break 

            if (Index_find == -1):
                # Значит указаной строки нет в списке.
                return;
            #------------------------Найдем номер Индекса, который соответвует искомому тексту строки:Конец----------------------------------------

            self.Obj.delete(Index_find);

        def Delete_Row_by_List_Text(self, List_Text:list[str]):

            all_elements = self.Obj.get(0, tkinter.END)

            # Собирамем все Индексы совпадающие с удалямым элемментом.
            List_Index_for_Delete = [
                i for i, element in enumerate(all_elements)
                if element in List_Text
            ]

            for i in reversed(List_Index_for_Delete):    # Удаляем с конца, чтобы не сломать Индексы
                self.Obj.delete(i)

        def Delete_All(self):
            self.Obj.delete(0, tkinter.END);


        def Set_Color_Text(self,Color:str):
            self.Obj.config(fg=Color);

        def Set_SelectColor_Text(self,Color:str):
            self.Obj.config(selectforeground=Color)

        def Set_Font_Name(self,Font_Name:str):
            self.Font_Name = Font_Name;

            self.Obj.config(font=(Font_Name, self.Font_Size));

        def Set_Font_Size(self,Font_Size:int):

             self.Obj.config(font=(self.Font_Name, Font_Size));

             self.Font_Size = Font_Size;

        def Set_Sort(self,Sort_flag:Tkinter_GUI__class.Sort_enum):
      
            all_elements = self.Obj.get(0, tkinter.END)  # Возвращает tuple соссылками на строки в каждм элемента, а не сами строки.


            if (Sort_flag == Tkinter_GUI__class.Sort_enum.ascending):   # По Возростанию
                all_elements = sorted(all_elements, reverse=False);

            if (Sort_flag == Tkinter_GUI__class.Sort_enum.descending):  # По Убыванию
                all_elements = sorted(all_elements, reverse=True);

            self.Obj.delete(0, tkinter.END);
            self.Obj.insert(tkinter.END, *all_elements);



        def Get__ListSelectRow_by_Index(self)->tuple[int, ...]:

            return self.Obj.curselection();

        def Get__ListSelectRow_by_Text(self)->list[str]:

            Tuple_select:tuple[int, ...] = self.Obj.curselection();


            List_str:list[str] = [];

            for i in range(len(Tuple_select)):
                List_str.append(self.Obj.get(Tuple_select[i]));

            return List_str;
  
        def Get_AllRows(self)->list[str]:

            all_elements = self.Obj.get(0, tkinter.END)  # Возвращает tuple соссылками на строки в каждм элемента, а не сами строки.

            return list(all_elements);



        def Get__TOP_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y());

        def Get__TOP_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width(), self.Container.winfo_y());
            
        def Get__BOTTOM_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height());
  
        def Get__BOTTOM_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width(), self.Container.winfo_y() + self.Container.winfo_height());

        def Get__CENTRE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width()/2, self.Container.winfo_y() + self.Container.winfo_height()/2);

        def Get__TOP_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() +  self.Container.winfo_width()/2, self.Container.winfo_y());

        def Get__BOTTOM_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width()/2, self.Container.winfo_y());

        def Get__LEFT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height()/2);

        def Get__RIGHT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height()/2);
   

        def Get__Size(self)->Tkinter_GUI__class.Size_struct:

             self.Window_struct_ref.Obj.update()  # или update()

             return Tkinter_GUI__class.Size_struct(self.Container.winfo_width(), self.Container.winfo_height());

        #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------


    # V_H_ScrollBar_Width_Height:int  = 15;  # Ширина Вертикального Скроллбара и высота Вертикального скроллбара.


    @dataclass(slots=True)
    class Treeview_Struct:
        Window_struct_ref: Tkinter_GUI__class.Window_struct = None;

        Name: str = "";
        Obj: tkinter.ttk.Treeview = field(default_factory=tkinter.ttk.Treeview);
        Container:Frame      = field(default_factory=tkinter.Frame);

        Font_Name:str = "Arial";
        Font_Size:int = 12;
        V_scroll_obj:Scrollbar = field(default_factory=tkinter.Scrollbar);
        H_scroll_obj:Scrollbar = field(default_factory=tkinter.Scrollbar);

        Hidden_Items: list[tuple[str, str, int]] = field(default_factory=list); # Нужен для фильтрации по призанку "Содержит" 
        
        Inputbox_obj:Entry =  field(default_factory=tkinter.Entry); # Поле Ввода для филтрации
        
        Font_Measurement:tkinter.font.Font = field(default_factory=tkinter.font.Font);
        Max_width:int = 0;
        
        List_Callback_for_Select:list[Tkinter_GUI__class.Callback_struct]   = field(default_factory = list);

        Callback_Right_Left_Click:Tkinter_GUI__class.Callback_struct =  field(default_factory = lambda: Tkinter_GUI__class.Callback_struct());   # Колбек на Правый клик мыши по Box`у виджета.
        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------

        def Add_Callback_for_Select(self, Callback_func, List_any:list[any]):
              
              self.List_Callback_for_Select.append(Tkinter_GUI__class.Callback_struct(Callback_func, List_any));
              
              def _on_select(event):

                selected = event.widget.selection();
                Flag:bool = False;

                if selected:
                    Flag =True;  # Значит Пользовтаель что-то выбрал.
                else:
                    Flag = False; # Значит Пользователь снял выделение со всех строк.

                for callback_item in self.List_Callback_for_Select:
                    callback_item.Callback(self, Flag, callback_item.List_any);


              if len(self.List_Callback_for_Select) == 1:
                self.Obj.bind("<<TreeviewSelect>>", _on_select);      # Это первый вызов функции "List_Callback_for_Click" - поэтому привяжим колбек к данной кнопке.
           
        def Set_Callback_for_Right_Left_Click(self, Callback_Right_Left_Click, List_any:list[any]):

            # Ставит колбек на Правый клик мыши по Box`у виджета.

            self.Callback_Right_Left_Click.Callback = Callback_Right_Left_Click;
            self.Callback_Right_Left_Click.List_any = List_any;

            def _intermediate_func(event):

                if event.num == 1:
                    self.Callback_Right_Left_Click.Callback(self, Tkinter_GUI__class.Click_Button_enum.Left, self.Callback_Right_Left_Click.List_any);  # Значит Левая
                elif event.num == 3:
                    self.Callback_Right_Left_Click.Callback(self, Tkinter_GUI__class.Click_Button_enum.Right, self.Callback_Right_Left_Click.List_any);  # Значит Правая

           

            self.Obj.bind("<Button-1>", _intermediate_func);   # Левая Button
            self.Obj.bind("<Button-3>", _intermediate_func);   # Правая Button


        def Set_Size(self, Width:int, Height:int):

            self.Container.place(width=Width, height=Height);
        
        def Set_Pos(self,  X:int, Y:int, Anchor_ID:Anchor_enum):

            self.Container.place(x=X, y=Y, anchor = Anchor_ID);


        def Set_Pos_AutoFollow_to_Widget(self, Widget_From_Anchor_ID:Anchor_enum, Widget_To, Widget_To_Anchor_ID:Anchor_Relative_enum, Offset_Anchor_X,  Offset_Anchor_Y):     

            # Функция устанавливаем автоматическое следование заданного угла одного Виджета за заданным углом друого виджета.

            # Widget_From                       - виджет которй должен следовать.
            # Widget_From_Anchor_ID             - угол-якорь виджета "Widget_From" которым он должен следовать за указанной позицией у виджета "Widget_To" в углке-якоре "Widget_To_Anchor_ID"
            # Widget_To                         - виджет за координатами которого должен следовать виджет "Widget_From"
            # Offset_Anchor_X и Offset_Anchor_Y - АБСОЛЮТНОЕ смещение смещение от координаты привязки, короче коррекитровка, если она нужна.


            relative_X, relative_Y = Widget_To_Anchor_ID.value;

            self.Container.place(in_ = Widget_To,  relx = relative_X, rely = relative_Y, x=Offset_Anchor_X, y=Offset_Anchor_Y, anchor = Widget_From_Anchor_ID);

        def Set_Size_AutoFollow_to_Widget(self, Widget_To, Relative_Width, Relative_Height, Width_Offset, Height_Offset):
        
            # Функция устанавливаем автоматическое следование размера одного Виджета за размером друого виджета.
        
            # Widget_From    - виджет которй должен следовать.
            # Widget_To      - виджет за размерами которого должен следовать виджет "Widget_From"
            # Relative_Width - ОТНОСИТЕЛЬНЫЙ размер виджета "Widget_To" который будет автоматически передаватся на виджет "Widget_From". Вообщем Relative_Width = 1, то значит это Полная Ширина виджета "Widget_To", Relative_Width = 0.5 - половина Ширины вижета и так далее, то есть Ширина Виджета "Widget_From" всегда будет автоматически подстраиватся под указанную Ширину.
            # Relative_Height - тоже самое, что и "Relative_Width" - только для высоты.
            # Width_Offset, Height_Offset - это АБСОЛЮТНОЕ смешение в Ширине или Высоте - если нужна более точная настрока. Потому что в относительных процентах не всегда увилирно можно настроить.

            # Если один из Relative_Width или Relative_Height указаны = -1, то значит автоследование по этому параметру не будет ставится.
            
            
            if (Relative_Width != -1 and Relative_Height != -1):
                self.Container.place(in_ = Widget_To, relwidth = Relative_Width, relheight = Relative_Height, width = Width_Offset, height = Height_Offset);
                return;

            if (Relative_Width == -1 and Relative_Height != -1):
                self.Container.place(in_ = Widget_To, relheight = Relative_Height, height = Height_Offset);
                return;

            if (Relative_Height == -1 and Relative_Width != -1):
                self.Container.place(in_ = Widget_To, relwidth = Relative_Width, width = Width_Offset);
                return;


        def Set_Select_Mode(self,  SelectMode:Tkinter_GUI__class.Treeview_SelectMode_enum):
        
            self.Obj.config(selectmode=SelectMode);
      

        def Add_ColapsingHeader_by_FullTreePath(self,  Tree_ColapsingHeader_path:list[str]):

            # Функция добавляет Заголовок по полному пути - попутно добавляя ВСЕ Родительские Заголовки из указанного пути.
            # Tree_ColapsingHeader_path - список в котором указан полный путь Заголовоком от Самого Верхнего до самого Нижнего, то есть вот так: ["Header_main", "Sub_header_1", "Sub_header_2","Sub_header_3"] - функция добавит полность последотвалеьно все заголовки - "Header_main" самый верхний заголовок, "Sub_header_3" - самый вложенный.

           Header_1 = self.Obj.insert("", "end", text=Tree_ColapsingHeader_path[0], open=False, tags=("Header",))

           for i in range(1, len(Tree_ColapsingHeader_path)):       # Начинаем со второго элемента.
           
               if (i == 1):
                   Header_X = self.Obj.insert(Header_1, "end", text=Tree_ColapsingHeader_path[i], open=False, tags=("Header",))
               else:
                   Header_X = self.Obj.insert(Header_X, "end", text=Tree_ColapsingHeader_path[i], open=False, tags=("Header",))



           #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
           self._Set_Max_Width(Tree_ColapsingHeader_path);
           #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        def Add_ColapsingHeader_by_FullTreePath_OnlyEnd(self,  Tree_ColapsingHeader_EXIST:list[str], Added_Header:str):

            # Функция добавляет указанный Заголовок "Added_Header" в указанное дерево-пути "Tree_ColapsingHeader_EXIST". Самое дерево-пути "Tree_ColapsingHeader_EXIST" - ДОЛЖНО УЖЕ СУЩЕСТОВАТЬ.
      
            # Так по сути нужно в обьекте Treeview найти последний обьект Хедера из "Tree_ColapsingHeader_EXIST". Для этого придется пройтись по Всему Treeview в его поисках:

            #--------------------------------------------------------------------
            Header_END = self._Find_ID_by_FullTreePath(Tree_ColapsingHeader_EXIST);

            self.Obj.insert(Header_END, "end", text=Added_Header, open=False, tags=("Header",));
            #--------------------------------------------------------------------


        
            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            self._Set_Max_Width([Added_Header]);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        def Add_Elements_to_ColapsingHeader(self,  Tree_ColapsingHeader_EXIST:list[str], List_Elements:list[str]):

            # Функция добавляет список Элементов к указанному пути-заголовку в "Tree_ColapsingHeader_EXIST"

            Find_End_Header = self._Find_ID_by_FullTreePath(Tree_ColapsingHeader_EXIST);   # Ищем последний Header-Обьект - по указанному в "Tree_ColapsingHeader_EXIST" пути.

            self.Obj.item(Find_End_Header, tags=("Header",));   # Принудительно ставим тег Header, т.к. узел теперь становится родителем Element'ов


            for add_element in List_Elements:

                self.Obj.insert(Find_End_Header, "end", text=add_element, open=False, tags=("Element",));


      
            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            self._Set_Max_Width(List_Elements);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


        def Set_DictonaryTree(self,  Dictonary_tree:dict)-> None|str:

            # Данная функция Устанавливает данные из Dictonary_tree в Treeview. Если какие то данные уже были, то полностью удалаяет их.
            # Dictonary_tree - должен быть строго следующего формата: Текстовый Ключ - это Хедер, значение ключа может быть или опять Dict - то есть вложенный Хедер/Хедеры(если у Хедера нет вложенных значений, то значение - это пустой List) или List[str] - то есть значения Хедера у котороых нет своих вложений/детей. 
            # То есть в таком формате:
            """
            test_dict = {
                "Фрукты": {
                    "Цитрусовые": {
                        "Апельсин": [],
                        "Лимон": [],
                        "Грейпфрут": ["Грейпфрут222"],
                    },
                    "Грейпфрут1": ["Клубника", "Малина", "Апельсун"]
                },
                "Овощи": ["Морковь", "Картофель", "Огурец", "Апель"],
                "Пустой раздел": {}
            }
            """




            # Удаляем всё, что уже было в дереве:
            for child_id in self.Obj.get_children(""):
                self.Obj.delete(child_id)


            def Add_Level(parent_id, tree_dict: dict) -> None | str:
                for key, value in tree_dict.items():
                    header_id = self.Obj.insert(parent_id, "end", text=key, open=False, tags=("Header",))

                    if isinstance(value, dict):
                        error = Add_Level(header_id, value)
                        if error is not None:
                            return error
                    elif isinstance(value, list):
                        for leaf_text in value:
                            self.Obj.insert(header_id, "end", text=leaf_text, open=False, tags=("Element",))
                    else:
                        return f"Wrong key type '{key}': {type(value)}. Must be Dict or List[str]."

                return None

              
            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            List_RowID = list(self.Obj.get_children(""));

            self._Set_Max_Width_(List_RowID);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


            return Add_Level("", Dictonary_tree)


        def Delete_Header(self,  Tree_ColapsingHeader_EXIST:list[str]):

            # Удаляет Хедер и соответвенно всех его детей.
            # Tree_ColapsingHeader_EXIST - список Хедеров полного пути до нужного Хедера.


            Header_END = self._Find_ID_by_FullTreePath(Tree_ColapsingHeader_EXIST);

            if (Header_END == None):
                return f"Path not found: {Tree_ColapsingHeader_EXIST}";

            self.Obj.delete(Header_END);

                
            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            #self._Set_Max_Width(List_RowID);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


            return None;

        def Delete_Elements_from_Header(self,  Tree_ColapsingHeader_EXIST:list[str], List_Elements:list[str]):

            # Удаляет список элементов у Хедера.
            # Tree_ColapsingHeader_EXIST - список Хедеров полного пути до нужного Хедера.

            Header_END = self._Find_ID_by_FullTreePath(Tree_ColapsingHeader_EXIST);


            if Header_END is None:
                return f"Path not found: {Tree_ColapsingHeader_EXIST}";

            children_tuple = self.Obj.get_children(Header_END);

        
            #---------------------Пройдемся по всему списку детей и соберем все id элементов детей, которые совапдает с удаляемыми строками из List_Elements:Начало-----------------
            child_id_List:list = [];

            for child_item in children_tuple:

                if self.Obj.item(child_item, "text") in List_Elements:
                    child_id_List.append(child_item);


            if len(child_id_List) != 0:
                self.Obj.delete(*child_id_List)      # Удаляем.
            #---------------------Пройдемся по всему списку детей и соберем все id элементов детей, которые совапдает с удаляемыми строками из List_Elements:Конец-----------------

               
            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            #self._Set_Max_Width(List_RowID);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


            return None

        def Set_Header_Open_Close(self,  Tree_ColapsingHeader_EXIST: list[str], Action: str):
            # Action: "Open" - открывает заголовок, "Close" - закрывает заголовок.

            Header_END = self._Find_ID_by_FullTreePath(Tree_ColapsingHeader_EXIST);

            if Action == "Open":
                self.Obj.item(Header_END, open=True);
            elif Action == "Close":
                self.Obj.item(Header_END, open=False);

        def Set_Header_All_Open(self) -> None:
            # Открывает ВСЕ заголовки.

            def Recursive_func(parent_id):
                for child_id in self.Obj.get_children(parent_id):
                    self.Obj.item(child_id, open=True);
                    Recursive_func(child_id);

            Recursive_func("");

        def Set_Header_All_Close(self) -> None:
            # Закрывает ВСЕ заголовки.

            def Recursive_func(parent_id):
                for child_id in self.Obj.get_children(parent_id):
                    self.Obj.item(child_id, open=False);
                    Recursive_func(child_id);

            Recursive_func("");

        def Clear_All(self):

            self.Obj.delete(*self.Obj.get_children());
            self.Hidden_Items.clear();


        def Get_Selected(self) -> list[Tkinter_GUI__class.Treeview_Select_struct]:
            # Отдал на аутсорс Нейронке.
        
            # Возвращает список выделенных элементов, сгруппированных по Header'у.
            # Каждый Treeview_Select_struct содержит полный путь до Header'а и список его Element-детей.
            # Дубликаты (например, если выделен и Header, и его же Element) объединяются автоматически.

            selected_ids = self.Obj.selection()

            # Словарь: ключ - кортеж пути до Header, значение - множество текстов Element'ов
            Result_dict: dict[tuple, set] = {}

            def Get_Full_Path(item_id) -> list[str]:
                # Строит полный путь от корня до указанного item_id (включительно)
                path = []
                current_id = item_id
                while current_id != "":
                    text = self.Obj.item(current_id, "text")
                    path.insert(0, text)
                    current_id = self.Obj.parent(current_id)
                return path

            def Is_Header(item_id) -> bool:
                tags = self.Obj.item(item_id, "tags")
                return "Header" in tags

            def Collect_SubHeaders_with_Elements(header_id):
                # Рекурсивно находит все под-Header'ы (включая сам header_id),
                # у которых есть прямые Element-дети, и добавляет их в Result_dict.
                direct_elements = []
                child_headers = []

                for child_id in self.Obj.get_children(header_id):
                    if Is_Header(child_id):
                        child_headers.append(child_id)
                    else:
                        direct_elements.append(self.Obj.item(child_id, "text"))

                if direct_elements:
                    path = Get_Full_Path(header_id)
                    key = tuple(path)
                    if key not in Result_dict:
                        Result_dict[key] = set()
                    Result_dict[key].update(direct_elements)

                for child_header_id in child_headers:
                    Collect_SubHeaders_with_Elements(child_header_id)

            for item_id in selected_ids:
                if Is_Header(item_id):
                    Collect_SubHeaders_with_Elements(item_id)
                else:
                    # Это Element - берём путь до его родителя-Header
                    parent_id = self.Obj.parent(item_id)
                    path = Get_Full_Path(parent_id)
                    key = tuple(path)
                    if key not in Result_dict:
                        Result_dict[key] = set()
                    Result_dict[key].add(self.Obj.item(item_id, "text"))

            # Конвертируем словарь в список Treeview_Select_struct
            List_result: list[Tkinter_GUI__class.Treeview_Select_struct] = []
            for path_tuple, elements_set in Result_dict.items():
                struct = Tkinter_GUI__class.Treeview_Select_struct()
                struct.List_Path_Header = list(path_tuple)
                struct.List_Elements = list(elements_set)
                List_result.append(struct)

            return List_result

        def Get_Selection_Flat_List(self, Delimetr: str) -> list[str]:

            selected_ids = self.Obj.selection()
            # Ключ - кортеж пути до Header, значение - множество текстов Element'ов
            # (используем тот же принцип дедупликации, что и в Get_Selected)
            Result_dict: dict[tuple, set] = {}

            def Get_Full_Path(item_id) -> list[str]:
                path = []
                current_id = item_id
                while current_id != "":
                    text = self.Obj.item(current_id, "text")
                    path.insert(0, text)
                    current_id = self.Obj.parent(current_id)
                return path

            def Is_Header(item_id) -> bool:
                tags = self.Obj.item(item_id, "tags")
                return "Header" in tags

            def Collect_SubHeaders_with_Elements(header_id):
                direct_elements = []
                child_headers = []
                for child_id in self.Obj.get_children(header_id):
                    if Is_Header(child_id):
                        child_headers.append(child_id)
                    else:
                        direct_elements.append(self.Obj.item(child_id, "text"))
                if direct_elements:
                    path = Get_Full_Path(header_id)
                    key = tuple(path)
                    if key not in Result_dict:
                        Result_dict[key] = set()
                    Result_dict[key].update(direct_elements)
                for child_header_id in child_headers:
                    Collect_SubHeaders_with_Elements(child_header_id)

            for item_id in selected_ids:
                if Is_Header(item_id):
                    Collect_SubHeaders_with_Elements(item_id)
                else:
                    parent_id = self.Obj.parent(item_id)
                    path = Get_Full_Path(parent_id)
                    key = tuple(path)
                    if key not in Result_dict:
                        Result_dict[key] = set()
                    Result_dict[key].add(self.Obj.item(item_id, "text"))

            # Сразу собираем плоский список строк, без промежуточных структур
            List_Result: list[str] = []
            for path_tuple, elements_set in Result_dict.items():
                for element in elements_set:
                    List_Result.append(Delimetr.join(path_tuple) + Delimetr + element)

            return List_Result

        def Get_Selection_Flat_List_Only_Header(self, Delimetr: str) -> list[str]:

            selected_ids = self.Obj.selection()
            Result_dict: dict[tuple, None] = {}
            def Get_Full_Path(item_id) -> list[str]:
                path = []
                current_id = item_id
                while current_id != "":
                    text = self.Obj.item(current_id, "text")
                    path.insert(0, text)
                    current_id = self.Obj.parent(current_id)
                return path
            def Is_Header(item_id) -> bool:
                tags = self.Obj.item(item_id, "tags")
                return "Header" in tags
            def Collect_Leaf_Headers(header_id):
                child_headers = [c for c in self.Obj.get_children(header_id) if Is_Header(c)]
                if child_headers:
                    # Есть дочерние Header'ы - значит текущий Header не конечный,
                    # сам путь не добавляем, спускаемся глубже
                    for child_header_id in child_headers:
                        Collect_Leaf_Headers(child_header_id)
                else:
                    # Дочерних Header'ов нет - это конечный (листовой) Header
                    path = Get_Full_Path(header_id)
                    Result_dict[tuple(path)] = None
            for item_id in selected_ids:
                if Is_Header(item_id):
                    Collect_Leaf_Headers(item_id)
                else:
                    parent_id = self.Obj.parent(item_id)
                    if parent_id != "":
                        Collect_Leaf_Headers(parent_id)
            List_Result: list[str] = [Delimetr.join(path_tuple) for path_tuple in Result_dict]
            return List_Result

        def Get_AllRows(self) -> list[Tkinter_GUI__class.Treeview_Select_struct]:
            # Возвращает список ВСЕХ строк, сгруппированных по Header'у.
            # Аналог Get_Selected, но без учёта выделения.

            Result_dict: dict[tuple, set] = {}

            def Get_Full_Path(item_id) -> list[str]:
                path = []
                current_id = item_id
                while current_id != "":
                    text = self.Obj.item(current_id, "text")
                    path.insert(0, text)
                    current_id = self.Obj.parent(current_id)
                return path

            def Is_Header(item_id) -> bool:
                tags = self.Obj.item(item_id, "tags")
                return "Header" in tags

            def Collect_SubHeaders_with_Elements(header_id):
                direct_elements = []
                child_headers = []

                for child_id in self.Obj.get_children(header_id):
                    if Is_Header(child_id):
                        child_headers.append(child_id)
                    else:
                        direct_elements.append(self.Obj.item(child_id, "text"))

                if direct_elements:
                    path = Get_Full_Path(header_id)
                    key = tuple(path)
                    if key not in Result_dict:
                        Result_dict[key] = set()
                    Result_dict[key].update(direct_elements)

                for child_header_id in child_headers:
                    Collect_SubHeaders_with_Elements(child_header_id)

            # Обходим все корневые Header'ы дерева (root = "")
            for item_id in self.Obj.get_children(""):
                if Is_Header(item_id):
                    Collect_SubHeaders_with_Elements(item_id)
                else:
                    # Элемент на верхнем уровне без родителя-Header
                    key = tuple()
                    if key not in Result_dict:
                        Result_dict[key] = set()
                    Result_dict[key].add(self.Obj.item(item_id, "text"))

            List_result: list[Tkinter_GUI__class.Treeview_Select_struct] = []
            for path_tuple, elements_set in Result_dict.items():
                struct = Tkinter_GUI__class.Treeview_Select_struct()
                struct.List_Path_Header = list(path_tuple)
                struct.List_Elements = list(elements_set)
                List_result.append(struct)

            return List_result

        def Get_AllRows_Flat_List(self, Delimetr: str) -> list[str]:
            # Аналог Get_Selection_Flat_List, но для ВСЕХ строк дерева.

            Result_dict: dict[tuple, set] = {}

            def Get_Full_Path(item_id) -> list[str]:
                path = []
                current_id = item_id
                while current_id != "":
                    text = self.Obj.item(current_id, "text")
                    path.insert(0, text)
                    current_id = self.Obj.parent(current_id)
                return path

            def Is_Header(item_id) -> bool:
                tags = self.Obj.item(item_id, "tags")
                return "Header" in tags

            def Collect_SubHeaders_with_Elements(header_id):
                direct_elements = []
                child_headers = []
                for child_id in self.Obj.get_children(header_id):
                    if Is_Header(child_id):
                        child_headers.append(child_id)
                    else:
                        direct_elements.append(self.Obj.item(child_id, "text"))
                if direct_elements:
                    path = Get_Full_Path(header_id)
                    key = tuple(path)
                    if key not in Result_dict:
                        Result_dict[key] = set()
                    Result_dict[key].update(direct_elements)
                for child_header_id in child_headers:
                    Collect_SubHeaders_with_Elements(child_header_id)

            for item_id in self.Obj.get_children(""):
                if Is_Header(item_id):
                    Collect_SubHeaders_with_Elements(item_id)
                else:
                    key = tuple()
                    if key not in Result_dict:
                        Result_dict[key] = set()
                    Result_dict[key].add(self.Obj.item(item_id, "text"))

            List_Result: list[str] = []
            for path_tuple, elements_set in Result_dict.items():
                for element in elements_set:
                    if path_tuple:
                        List_Result.append(Delimetr.join(path_tuple) + Delimetr + element)
                    else:
                        List_Result.append(element)

            return List_Result

        def Get_AllRows_Flat_List_Only_Header(self, Delimetr: str) -> list[str]:
            Result_dict: dict[tuple, None] = {}

            def Get_Full_Path(item_id) -> list[str]:
                path = []
                current_id = item_id
                while current_id != "":
                    text = self.Obj.item(current_id, "text")
                    path.insert(0, text)
                    current_id = self.Obj.parent(current_id)
                return path

            def Is_Header(item_id) -> bool:
                tags = self.Obj.item(item_id, "tags")
                return "Header" in tags

            def Collect_Leaf_Headers(header_id):
                child_headers = [c for c in self.Obj.get_children(header_id) if Is_Header(c)]
                if child_headers:
                    for child_header_id in child_headers:
                        Collect_Leaf_Headers(child_header_id)
                else:
                    path = Get_Full_Path(header_id)
                    Result_dict[tuple(path)] = None

            root_ids = self.Obj.get_children("")
            for item_id in root_ids:
                if Is_Header(item_id):
                    Collect_Leaf_Headers(item_id)

            List_Result: list[str] = [Delimetr.join(path_tuple) for path_tuple in Result_dict]
            return List_Result


        def Set_Color_Text(self,  Color: str):
            pass # Короче не знаю, не рботает почему то.

        def Set_SelectColor_Text(self,  Color: str):
            pass # Короче не знаю, не рботает почему то.

        def Set_Font_Name(self,  Font_Name: str):

            style = tkinter.ttk.Style()
            style_name = f"Custom{id(self.Obj)}.Treeview"
            style.configure(style_name, font=(Font_Name, self.Font_Size))
            self.Obj.configure(style=style_name)

        
            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            self.Font_Measurement.config(family=Font_Name);
        
            List_RowID = list(self.Obj.get_children(""));

            self._Set_Max_Width_(List_RowID);
            #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        def Set_Font_Size(self,  Font_Size: int):
            style = tkinter.ttk.Style()
            style_name = f"Custom{id(self.Obj)}.Treeview"  # уникальное имя стиля для этой таблицы

            style.configure(style_name, font=("TkDefaultFont", Font_Size))
            style.configure(f"{style_name}.Heading", font=("TkDefaultFont", Font_Size, "bold"))  # шрифт заголовков (опционально)

            # высота строки под новый размер шрифта (иначе текст будет обрезаться)
            style.configure(style_name, rowheight=int(Font_Size * 2))

            self.Obj.configure(style=style_name)

            self.Font_Size = Font_Size;
            self.Inputbox_obj.place(height = Font_Size*2);                            # Синхронизируем Высоту Inputbox с высотой строки при измении размера шрифта.
            self.Inputbox_obj.config(font=(self.Font_Name, Font_Size));    # Синхронизируем размер шрифта текста поля ввода.

        
            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            self.Font_Measurement.config(size=Font_Size);
        
            List_RowID = list(self.Obj.get_children(""));

            self._Set_Max_Width_(List_RowID);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


        def Reset_Filter(self):

            # Восстанавливает все элементы, скрытые предыдущим фильтром, обратно в дерево.
            for item_id, parent_id, index in self.Hidden_Items:
                
                self.Obj.reattach(item_id, parent_id, index)

            self.Hidden_Items.clear()

            self.Set_Header_All_Close();

        def Filter_Elements_Contains(self, Filter_text: str) -> None:

            self.Reset_Filter()
            if Filter_text == "":
                return

            Filter_text_lower = Filter_text.lower()

            # Шаг 1: заранее зафиксировать индексы ВСЕХ узлов, пока дерево ещё полностью attached
            Original_Index_Map = {}
            def Collect_Indices(parent_id):
                for i, child_id in enumerate(self.Obj.get_children(parent_id)):
                    Original_Index_Map[child_id] = i
                    Collect_Indices(child_id)
            Collect_Indices("")

            # Шаг 2: обычный Walk, но берём индекс из Original_Index_Map, а не из self.Obj.index()
            def Walk(child_id, Force_Show=False) -> bool:
                parent_id = self.Obj.parent(child_id)
                text = self.Obj.item(child_id, "text")
                self_match = Force_Show or (Filter_text_lower in text.lower())
                any_child_match = False
                for grandchild_id in list(self.Obj.get_children(child_id)):
                    if Walk(grandchild_id, Force_Show=self_match):
                        any_child_match = True
                if self_match or any_child_match:
                    self.Obj.item(child_id, open=True)
                    return True
                else:
                    self.Hidden_Items.append((child_id, parent_id, Original_Index_Map[child_id]))
                    self.Obj.detach(child_id)
                    return False

            for top_id in list(self.Obj.get_children("")):
                Walk(top_id)

        def Sort_Elements_of_Header(self, Tree_ColapsingHeader_EXIST: list[str], Sort_type: Tkinter_GUI__class.Sort_enum):

            # Функция сортирует ВСЕ элементы по указанному к Хедеру пути "Tree_ColapsingHeader_EXIST".


            Header_END = self._Find_ID_by_FullTreePath(Tree_ColapsingHeader_EXIST);

            if (Header_END == None):
                return;


            children = self.Obj.get_children(Header_END);   # Поулчим tuple все детей.


            Reverse_bool = False;

            if(Sort_type == Tkinter_GUI__class.Sort_enum.descending):
                    Reverse_bool = True;



            items = [(self.Obj.item(child_id, "text"), child_id) for child_id in children];   # Преобразовываем всех ID Детей в текст и получаем пару текс-id для последущей сортировки или точнее пермещения.
            items.sort(key=lambda x: x[0], reverse=Reverse_bool)

            for index, (text, child_id) in enumerate(items):
                self.Obj.move(child_id, Header_END, index)

        def Get_List_Headers_TOP_LEVEL(self) -> list[str]:

            List_Headers: list[str] = [];

            for item_id in self.Obj.get_children(""):
                Tags = self.Obj.item(item_id, option="tags");
                if "Header" in Tags:
                    List_Headers.append(self.Obj.item(item_id, option="text"));

            return List_Headers;

        def Get_Child_by_Header(self, list_path_to_Header: list[str]) -> list[str]:

            # Функция возвращает список детей указанного в "list_path_to_Header" Хедера.

            # list_path_to_Header - это путь разделенный на элементы, то есть для примера: Top_Level_header, Sub_Level, Sub_Sub_Level и вот у Sub_Sub_Level - и получаем  список детей. Если Sub_Sub_Level не имеет список детей - то возвращаем пустой список.
            # Важно: список только непосредственных детей, если у детей есть свои дети - то их не учитываем.


            Header_ID = self._Find_ID_by_FullTreePath(list_path_to_Header);

            if Header_ID is None:
                return [];

            # Берем только непосредственных детей (без рекурсии вглубь).
            List_Children_ID = self.Obj.get_children(Header_ID);

            List_Result: list[str] = [];
            for child_id in List_Children_ID:
                List_Result.append(self.Obj.item(child_id, option="text"));

            return List_Result;

        
        def Check_Child_by_Header(self, list_path_to_Header: list[str]) -> bool:

            # Функция проверяет есть ли у указанного в "list_path_to_Header" Хедера. - дети или нет.

            # list_path_to_Header - это путь разделенный на элементы, то есть для примера: Top_Level_header, Sub_Level, Sub_Sub_Level и вот у Sub_Sub_Level - и получаем  список детей. Если Sub_Sub_Level не имеет список детей - то возвращаем пустой список.

            Header_ID = self._Find_ID_by_FullTreePath(list_path_to_Header);

            if Header_ID is None:
                return [];

            # Берем только непосредственных детей (без рекурсии вглубь).
            List_Children_ID = self.Obj.get_children(Header_ID);

            if (len(List_Children_ID) > 0):
                return True;  # Значит дети есть.
            else:
                return False;

        def Sort_as_Text(self, Sort_Type: Tkinter_GUI__class.Sort_enum):

            #---------------------------------------------------------------------------------
            def _Sort_as_Text_Level(Parent_item: str, Reverse_flag: bool):

                Children_ids = list(self.Obj.get_children(Parent_item));
                Children_ids.sort(key=lambda item_id: str(self.Obj.item(item_id, option="text")).lower(), reverse=Reverse_flag);

                for Index, item_id in enumerate(Children_ids):
                    self.Obj.move(item_id, Parent_item, Index);

                for item_id in Children_ids:
                    _Sort_as_Text_Level(item_id, Reverse_flag);  # спускаемся к детям каждого узла
            #---------------------------------------------------------------------------------


            #---------------------------------------------------------------------------------
            if (Sort_Type == Tkinter_GUI__class.Sort_enum.ascending):
                _Sort_as_Text_Level("", False);
            else:
                if (Sort_Type == Tkinter_GUI__class.Sort_enum.descending):
                    _Sort_as_Text_Level("", True);
            #---------------------------------------------------------------------------------


             
        def Get__TOP_LEFT_Pos(self, )->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update();

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y());
                       
        def Get__TOP_RIGHT_Pos(self, )->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width(), self.Container.winfo_y());
            
        def Get__BOTTOM_LEFT_Pos(self, )->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height());

        def Get__BOTTOM_RIGHT_Pos(self, )->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width(), self.Container.winfo_y() + self.Container.winfo_height());
  
        def Get__CENTRE_Pos(self, )->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width()/2 , self.Container.winfo_y() + self.Container.winfo_height()/2);

        def Get__TOP_MIDDLE_Pos(self, )->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() +  self.Container.winfo_width()/2 , self.Container.winfo_y());

        def Get__BOTTOM_MIDDLE_Pos(self, )->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width()/2, self.Container.winfo_y());

        def Get__LEFT_MIDDLE_Pos(self, )->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height()/2 );

        def Get__RIGHT_MIDDLE_Pos(self, )->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height()/2 );
   

        def Get__Size(self)->Tkinter_GUI__class.Size_struct:

             self.Window_struct_ref.Obj.update()  # или update()

             return Tkinter_GUI__class.Size_struct(self.Container.winfo_width(), self.Container.winfo_height());

        #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------
                
        #---------------------------------------------------------------------PRIVATE:---------------------------------------------------------

        def _Inputbox_Enter_Callback(self, Enter_Text:str):
            
            if (Enter_Text == ""):
                self.Reset_Filter();
            else:
                self.Filter_Elements_Contains(Enter_Text);

        def _Recursive(self, item_ID, depth=0):
            row_text = self.Obj.item(item_ID, "text");
    
            # width = self.Font_Measurement.measure(row_text) + (math.ceil((depth+1) * 4 * 1.5) * self.Font_Size);   # Вообщем суть: виджет Treeview - сам не умеет определять ширину текста строки, а значит матоматического H-скролла нету. Ладно, можно через обеькт Font - НО это гарантировано рабоатет, если список строк в Treeview - идет как "плоский" список, то есть БЕЗ отсупов с ЛЕВОЙ строны, а в формате Дерева - идет отступ Слева в зависимости от уровня Вложенности и вот этот оступ слева, как я понял нихуя посчитать нельзя (при этом он еще и разный в зависимости от размера шрифта) - поэтому едисвеное что можно сделать - это тупо просто попробовать дполнительно у измеренному тексту + подобрать условный коэфициент с запасом.
            width = len(row_text)*self.Font_Size + (math.ceil((depth+1) * 4 * 1.5) * self.Font_Size);    # self.Font_Measurement.measure(row_text) - слишком медленная функция
            if (width > self.Max_width):
                self.Max_width = width;
            for child_ID in self.Obj.get_children(item_ID):
                self._Recursive(child_ID, depth + 1);

        def _Set_Max_Width_(self, List_RowID: list[str]):
            self.Max_width = 0;
            for top_ID in List_RowID:
                self._Recursive(top_ID, depth=0);
            self.Obj.column("#0", width=self.Max_width + 10, stretch=False);

        def _Set_Max_Width(self, List_RowText:list[str]):
            
            for row_text in (List_RowText):
                width =  len(row_text)*self.Font_Size; # self.Font_Measurement.measure(row_text); measure - просто эпически медленная операция. Придется заменить на примерное с запасом вычисления ширины.

                if(width > self.Max_width):
                    self.Max_width = width;

            self.Obj.column("#0", width=self.Max_width+10, stretch=False);

        def _Find_ID_by_FullTreePath(self, Tree_ColapsingHeader_EXIST: list[str]):

            parent = "";
            for name in Tree_ColapsingHeader_EXIST:
                found = None;

                # Ищем среди видимых (прикреплённых) детей
                for child_id in self.Obj.get_children(parent):
                    if self.Obj.item(child_id, "text") == name:
                        found = child_id;
                        break;

                # Если не нашли — ищем среди скрытых фильтром элементов
                # Hidden_Items хранит (item_id, parent_id, index)
                if found is None:
                    for hidden_item_id, hidden_parent_id, index in self.Hidden_Items:
                        if hidden_parent_id == parent and self.Obj.item(hidden_item_id, "text") == name:
                            found = hidden_item_id;
                            break;

                if found is None:
                    return None;
                parent = found;

            return parent;


    @dataclass(slots=True)
    class Inputbox_Struct:
        Window_struct_ref:Tkinter_GUI__class.Window_struct = None;

        Name:str = "";
        Obj:tkinter.Entry = field(default_factory=tkinter.Entry);

        Font_Name:str = "Arial";
        Font_Size:int = 12;
        
        List_Callback_for_Input:list[Tkinter_GUI__class.Callback_struct]   = field(default_factory = list);

        Flag_Restrict_Non_Numeric: bool = False;   # флаг текущего состояния ограничения на ввод символов кроме натуральных числовых.

        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------

        def Enter_Callback(self,  Callback_func, List_any:list[any]):

            # Добавляет колбек на изменение ввода в Inputbox

              self.List_Callback_for_Input.append(Tkinter_GUI__class.Callback_struct(Callback_func, List_any));

              def on_change(change_text):
                for callback_item in self.List_Callback_for_Input:
                    callback_item.Callback(self, self.Window_struct_ref, self, callback_item.List_any, change_text);

                return True         # обязательно True, иначе ввод не применится

              if len(self.List_Callback_for_Input) == 1:
                vcmd = (self.Obj.register(on_change), '%P')
                self.Obj.config(validate="key", validatecommand=vcmd);    # Это первый вызов функции "Set_Click_Callback" - поэтому привяжим колбек к данной кнопке.


        def Set_Size(self,  Width:int, Height:int):

            self.Obj.place(width=Width, height=Height);

        def Set_Pos(self,  X:int, Y:int, Anchor_ID:Anchor_enum):

            self.Obj.place(x=X, y=Y, anchor = Anchor_ID);


        def Set_Pos_AutoFollow_to_Widget(self, Widget_From_Anchor_ID:Anchor_enum, Widget_To, Widget_To_Anchor_ID:Anchor_Relative_enum, Offset_Anchor_X,  Offset_Anchor_Y):     

            # Функция устанавливаем автоматическое следование заданного угла одного Виджета за заданным углом друого виджета.

            # Widget_From                       - виджет которй должен следовать.
            # Widget_From_Anchor_ID             - угол-якорь виджета "Widget_From" которым он должен следовать за указанной позицией у виджета "Widget_To" в углке-якоре "Widget_To_Anchor_ID"
            # Widget_To                         - виджет за координатами которого должен следовать виджет "Widget_From"
            # Offset_Anchor_X и Offset_Anchor_Y - АБСОЛЮТНОЕ смещение смещение от координаты привязки, короче коррекитровка, если она нужна.


            relative_X, relative_Y = Widget_To_Anchor_ID.value;

            self.Obj.place(in_ = Widget_To,  relx = relative_X, rely = relative_Y, x=Offset_Anchor_X, y=Offset_Anchor_Y, anchor = Widget_From_Anchor_ID);

        def Set_Size_AutoFollow_to_Widget(self, Widget_To, Relative_Width, Relative_Height, Width_Offset, Height_Offset):
        
            # Функция устанавливаем автоматическое следование размера одного Виджета за размером друого виджета.
        
            # Widget_From    - виджет которй должен следовать.
            # Widget_To      - виджет за размерами которого должен следовать виджет "Widget_From"
            # Relative_Width - ОТНОСИТЕЛЬНЫЙ размер виджета "Widget_To" который будет автоматически передаватся на виджет "Widget_From". Вообщем Relative_Width = 1, то значит это Полная Ширина виджета "Widget_To", Relative_Width = 0.5 - половина Ширины вижета и так далее, то есть Ширина Виджета "Widget_From" всегда будет автоматически подстраиватся под указанную Ширину.
            # Relative_Height - тоже самое, что и "Relative_Width" - только для высоты.
            # Width_Offset, Height_Offset - это АБСОЛЮТНОЕ смешение в Ширине или Высоте - если нужна более точная настрока. Потому что в относительных процентах не всегда увилирно можно настроить.

            # Если один из Relative_Width или Relative_Height указаны = -1, то значит автоследование по этому параметру не будет ставится.
            
            
            if (Relative_Width != -1 and Relative_Height != -1):
                self.Obj.place(in_ = Widget_To, relwidth = Relative_Width, relheight = Relative_Height, width = Width_Offset, height = Height_Offset);
                return;

            if (Relative_Width == -1 and Relative_Height != -1):
                self.Obj.place(in_ = Widget_To, relheight = Relative_Height, height = Height_Offset);
                return;

            if (Relative_Height == -1 and Relative_Width != -1):

                self.Obj.place(in_ = Widget_To, relwidth = Relative_Width, width = Width_Offset);
                return;


        def Set_Text(self,  Inputbox_Text:str):

            self.Obj.delete(0, tkinter.END);
            self.Obj.insert(0, Inputbox_Text);

        def Set_Background_Color(self,  Color:str):

            self.Obj.config(bg=Color);

        def Set_Text_Color(self,  Color:str):

            self.Obj.config(fg=Color);

        def Set_Active(self, Flag:bool):

            if (Flag == True):
                self.Obj.config(state="normal");
            else:
                self.Obj.config(state="readonly");

        def Get_Active(self)->bool:

            state_str = self.Obj.cget("state");

            if(state_str == "normal"):
                return True;
            else:
                return False;

        def Set_Font_Name(self,  Font_Name:str):

            self.Font_Name = Font_Name;

            self.Obj.config(font=(Font_Name, self.Font_Size))

        def Set_Font_Size(self, Font_Size:int):

            self.Obj.config(font=(self.Font_Name, Font_Size));

            self.Font_Size = Font_Size;


        def Set_Restriction_for_Enter_Non_Numeric_symv(self, Flag: bool):

            # Flag = True  - запретить ввод/вставку любых символов кроме 0-9
            # Flag = False - снять запрет, если стоит

            self.Flag_Restrict_Non_Numeric = Flag;

            if Flag or len(self.List_Callback_for_Input) > 0:
                self.Obj.config(validate="key", validatecommand=self.__Build_Vcmd());
            else:
                # Ограничение снято и колбеков нет - отключаем валидацию полностью.
                self.Obj.config(validate="none");

    
        def Clear(self):
            self.Obj.delete(0, tkinter.END);

        def Set_Font_Size(self,  Font_Size:int):

            self.Obj.config(font=(self.Font_Name, Font_Size));

            self.Font_Size = Font_Size;
        
        def Get_Text(self)->str:
            return self.Obj.get();   # Возвращает значение введенное в поле ввода в формате str.

        def Get__TOP_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y());
        
        def Get__TOP_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width(), self.Obj.winfo_y());
            
        def Get__BOTTOM_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height());
  
        def Get__BOTTOM_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width(), self.Obj.winfo_y() + self.Obj.winfo_height());

        def Get__CENTRE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width()/2, self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__TOP_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() +  self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__BOTTOM_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__LEFT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__RIGHT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);
       

        def Get__Size(self)->Tkinter_GUI__class.Size_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Size_struct(self.Obj.winfo_width(), self.Obj.winfo_height());


        #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------

        #-----------------------------------------------------------------PRIVATE:Начало-----------------------------------------------------------------

        def __Build_Vcmd(self):

            # Строит единый validatecommand, объединяющий:
            # 1) проверку на числовой ввод (если включена)
            # 2) вызов всех пользовательских callback'ов из Enter_Callback

            def on_validate(change_text):

                # 1) Проверка ограничения на нечисловые символы.
                if self.Flag_Restrict_Non_Numeric:
                    if change_text != "" and not change_text.isdigit():
                        return False;   # блокируем ввод/вставку недопустимого символа

                # 2) Прогон пользовательских колбеков (как и раньше).
                for callback_item in self.List_Callback_for_Input:
                    callback_item.Callback(self, self.Window_struct_ref, self, callback_item.List_any, change_text);

                return True;            # обязательно True, иначе ввод не применится

            return (self.Obj.register(on_validate), '%P');




    @dataclass(slots=True)
    class Table_Struct:
        Window_struct_ref: Tkinter_GUI__class.Window_struct = None;

        Name: str = "";
        Obj: tkinter.ttk.Treeview = field(default_factory=tkinter.ttk.Treeview);
        Container:Frame      = field(default_factory=tkinter.Frame);

        Font_Name:str = "Arial";
        Font_Size:int = 12;
        V_scroll_obj:Scrollbar = field(default_factory=tkinter.Scrollbar);
        H_scroll_obj:Scrollbar = field(default_factory=tkinter.Scrollbar);
        
        Popup_Filter_for_Table_Obj:Tkinter_GUI__class.Popup_Filter_for_Table__class = None;  # Обьект popup окна для ввода филтрации
        Popup_CellViewerText_Obj:Tkinter_GUI__class.Popup_CellViewerText_for_Table__class = None; # Обьект popup окна для вывода туда текста ячейки таблицы.

        Hidden_Items: list[tuple[str, str, int]] = field(default_factory=list);    # (item_id, parent_id, index)    - для восстановления скрытых строк
        Column_Filters: dict[str, str] = field(default_factory=dict);              # {Column_ID: filter_text_lower} - активные фильтры по колонкам, накапливаются

        ColumnID_Last_Click:str = field(default_factory=str);

        List_Columns_Name:list[tuple[str,str]] = field(default_factory=list);      # Список столбцов установленных Пользтватлем при создании виджета. Нужен для функции "Set_All_Columns_Equal_Width".

        List_Callback_for_Click:list[Tkinter_GUI__class.Callback_struct] =  field(default_factory = list);   # Колбек на клик мыши по ячейке таблицы.

        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------
         
        def Print__Table(self, Table_struct: Tkinter_GUI__class.Table_Struct):

            #-------------------------------------------------------------------------------
            List_Column_ID = Table_struct.Obj["columns"];   # Получаем список ID всех колонок таблицы

            #--------------------------------Выводим Заголовки:-----------------------------
            List_Header_Text = [Table_struct.Obj.heading(Column_ID)["text"] for Column_ID in List_Column_ID];
            print("\t".join(List_Header_Text));
            #---------------------------------------------------------------------------------


            #-------------------------------Построчно выводим значения ячеек:-----------------
            for Item_ID in Table_struct.Obj.get_children():

                List_Row_Values = Table_struct.Obj.item(Item_ID)["values"];   # Получаем значения строки (кортеж/список по индексам колонок)

                List_Row_Values_Str = [str(Value) for Value in List_Row_Values];   # Приводим все значения к строке (на случай чисел/None)

                print("\t".join(List_Row_Values_Str));
            #-----------------------------------------------------------------------------------

            return;



        def Add_Callback_for_Click_for_Cell(self, user_callback, List_any:list[any]):

             # Колбек который будет вызыватся при Клике по ячейке таблицы.

            self.List_Callback_for_Click.append(Tkinter_GUI__class.Callback_struct(user_callback, List_any));


            def Click_Handler(event, Click_ID):

                Region = self.Obj.identify_region(event.x, event.y)
                if Region != "cell":
                    return  # клик не по ячейке (например, по заголовку или разделителю)

                Row_ID = self.Obj.identify_row(event.y)
                Col_ID_hash = self.Obj.identify_column(event.x)  # вида "#1", "#2"...

                if not Row_ID or not Col_ID_hash:
                    return

                Row_Index = self.Obj.index(Row_ID)
                Column_Index = int(Col_ID_hash.replace("#", "")) - 1  # "#1" -> 0

                for callback_struct in (self.List_Callback_for_Click):

                    callback_struct.Callback(self, Row_Index, Column_Index, Click_ID, callback_struct.List_any);


            self.Obj.bind("<Double-1>", lambda event: Click_Handler(event, Tkinter_GUI__class.Click_Button_enum.Double_Left));
            self.Obj.bind("<Double-3>", lambda event: Click_Handler(event, Tkinter_GUI__class.Click_Button_enum.Double_Right));
            self.Obj.bind("<Button-1>", lambda event: Click_Handler(event, Tkinter_GUI__class.Click_Button_enum.Left));
            self.Obj.bind("<Button-3>", lambda event: Click_Handler(event, Tkinter_GUI__class.Click_Button_enum.Right));


        def Add_Row(self,  Added_Data:list[tuple], Add_pos:int):

            if (Add_pos == -1):

                for item in Added_Data:
                    self.Obj.insert("", tkinter.END, values=item);
            else:
                 for i in range(len(Added_Data)):
                    self.Obj.insert("", Add_pos+i, values=Added_Data[i]);


        def Delete_Row_by_FullValueRow(self,  Full_Value_Row:tuple)->bool:
            Row_ID = self._Get_RowID_by_FullValueRow(self, Full_Value_Row);

            if (Row_ID != None):
                self.Obj.delete(Row_ID);
                return True;
            else:
                return False;

        def Delete_Row_by_IndexRow(self,  Row_Index:int):

            Row_ID = self._Get_RowID_by_Index(Row_Index);

            if Row_ID != None:
                self.Obj.delete(Row_ID)
                return True
            else:
                return False

        def Clear_All(self):
            # Удаляет все строки в таблице
            for item in self.Obj.get_children():
                self.Obj.delete(item);

            self.Hidden_Items.clear();
            self.Column_Filters.clear();

        def Edit_Row_by_ColumnIndex_by_ValueRow(self, Rows_Value_tuple: tuple[str, ...], Columns_Index_tuple: tuple[int, ...], NewValue: str, Column_Index_NewValue: int) -> bool:

            #Rows_Value_tuple        - искомые значения ячеек;
            #Columns_Index_tuple     - индексы столбцов (в List_Columns_Name), которым соответствуют значения из Rows_Value_tuple;
            #NewValue                - новое значение;
            #Column_Index_NewValue   - индекс столбца (в List_Columns_Name), куда записать NewValue;

            #--------------------------------------------------------------------------------------------
            if len(Rows_Value_tuple) != len(Columns_Index_tuple):
                return False;

            Max_Index_Needed = max(max(Columns_Index_tuple), Column_Index_NewValue);
            if Max_Index_Needed >= len(self.List_Columns_Name):
                return False;
            #--------------------------------------------------------------------------------------------


            #-------------------------Получим ID реальных Column-ов Treeview по индексам:------------------
            List_ColumnID_for_Search = [self.List_Columns_Name[Index][0] for Index in Columns_Index_tuple];
            ColumnID_for_NewValue     = self.List_Columns_Name[Column_Index_NewValue][0];
            #--------------------------------------------------------------------------------------------


            #-------------------------Собираем ВСЕ item_id: видимые + скрытые фильтром:----------------------
            List_All_Item_ID = list(self.Obj.get_children());                                    # видимые (attached) строки

            List_Hidden_Item_ID = [Hidden_Tuple[0] for Hidden_Tuple in self.Hidden_Items];        # detach'нутые строки

            List_All_Item_ID.extend(List_Hidden_Item_ID);
            #--------------------------------------------------------------------------------------------


            #-------------------------Ищем первую подходящую строку среди ВСЕХ строк:------------------------
            Found_Item_ID = None;

            for Item_ID in List_All_Item_ID:

                Is_Match = True;

                for ColumnID, Search_Value in zip(List_ColumnID_for_Search, Rows_Value_tuple):

                    Cell_Value = self.Obj.set(Item_ID, ColumnID);            # .set() читает значение даже у detach'нутого item, т.к. он физически всё ещё существует в Treeview, просто отсоединён от дерева отображения.

                    if Cell_Value != Search_Value:
                        Is_Match = False;
                        break;

                if Is_Match:
                    Found_Item_ID = Item_ID;
                    break;
            #--------------------------------------------------------------------------------------------


            if Found_Item_ID is None:
                return False;


            #-------------------------Записываем новое значение в найденную строку:--------------------------
            self.Obj.set(Found_Item_ID, ColumnID_for_NewValue, NewValue);
            #--------------------------------------------------------------------------------------------

            return True;

        def Edit_Row_by_ColumnIndex_by_RowIndex(self,  Row_Index:int, ColumnIndex:int, NewValue:str):

            # Заменяет ячейку соответвующую столбцу под индексом "ColumnIndex" в строку под индексом "Row_Index" на значение NewValue.

            # ColumnIndex - стандартно с 0.

            if (Row_Index == -1):
                Row_Index = len(self.Obj.get_children("")) - 1;

            Row_ID = self._Get_RowID_by_Index(Row_Index)  # был Row_ID напрямую использован — баг
            if Row_ID == None:
                return False
            values = list(self.Obj.item(Row_ID, "values"))
            values[ColumnIndex] = NewValue
            self.Obj.item(Row_ID, values=values)
            return True


        def Set_Size(self,  Width:int, Height:int):

            self.Container.place(width=Width, height=Height);
        
        def Set_Pos(self,  X:int, Y:int, Anchor_ID:Anchor_enum):

            self.Container.place(x=X, y=Y, anchor = Anchor_ID);


        def Set_Pos_AutoFollow_to_Widget(self, Widget_From_Anchor_ID:Anchor_enum, Widget_To, Widget_To_Anchor_ID:Anchor_Relative_enum, Offset_Anchor_X,  Offset_Anchor_Y):     

            # Функция устанавливаем автоматическое следование заданного угла одного Виджета за заданным углом друого виджета.

            # Widget_From                       - виджет которй должен следовать.
            # Widget_From_Anchor_ID             - угол-якорь виджета "Widget_From" которым он должен следовать за указанной позицией у виджета "Widget_To" в углке-якоре "Widget_To_Anchor_ID"
            # Widget_To                         - виджет за координатами которого должен следовать виджет "Widget_From"
            # Offset_Anchor_X и Offset_Anchor_Y - АБСОЛЮТНОЕ смещение смещение от координаты привязки, короче коррекитровка, если она нужна.


            relative_X, relative_Y = Widget_To_Anchor_ID.value;

            self.Container.place(in_ = Widget_To,  relx = relative_X, rely = relative_Y, x=Offset_Anchor_X, y=Offset_Anchor_Y, anchor = Widget_From_Anchor_ID);

        def Set_Size_AutoFollow_to_Widget(self, Widget_To, Relative_Width, Relative_Height, Width_Offset, Height_Offset):
        
            # Функция устанавливаем автоматическое следование размера одного Виджета за размером друого виджета.
        
            # Widget_From    - виджет которй должен следовать.
            # Widget_To      - виджет за размерами которого должен следовать виджет "Widget_From"
            # Relative_Width - ОТНОСИТЕЛЬНЫЙ размер виджета "Widget_To" который будет автоматически передаватся на виджет "Widget_From". Вообщем Relative_Width = 1, то значит это Полная Ширина виджета "Widget_To", Relative_Width = 0.5 - половина Ширины вижета и так далее, то есть Ширина Виджета "Widget_From" всегда будет автоматически подстраиватся под указанную Ширину.
            # Relative_Height - тоже самое, что и "Relative_Width" - только для высоты.
            # Width_Offset, Height_Offset - это АБСОЛЮТНОЕ смешение в Ширине или Высоте - если нужна более точная настрока. Потому что в относительных процентах не всегда увилирно можно настроить.

            # Если один из Relative_Width или Relative_Height указаны = -1, то значит автоследование по этому параметру не будет ставится.
            
            
            if (Relative_Width != -1 and Relative_Height != -1):
                self.Container.place(in_ = Widget_To, relwidth = Relative_Width, relheight = Relative_Height, width = Width_Offset, height = Height_Offset);
                return;

            if (Relative_Width == -1 and Relative_Height != -1):
                self.Container.place(in_ = Widget_To, relheight = Relative_Height, height = Height_Offset);
                return;

            if (Relative_Height == -1 and Relative_Width != -1):
                self.Container.place(in_ = Widget_To, relwidth = Relative_Width, width = Width_Offset);
                return;

        def Set_to_Window_Fit(self, Offset_X, Offset_Y):

            # Вписывает таблицу по размеру окна и следует при измении размеров окна.
            # Offset_X - отступ по боками по оси X
            # Offset_Y - оступ сверху и снизу по оси Y

            self.Set_Pos(Offset_X, Offset_Y, Tkinter_GUI__class.Anchor_enum.TopLeft);

            self.Set_Size_AutoFollow_to_Widget(self.Window_struct_ref.Obj, 1,1,-2*Offset_X,-2*Offset_Y);


        def Set_Column_Width(self,  Column_Text_ID:str, Width:int):
            self.Obj.column(Column_Text_ID, width=Width);

        def Set_All_Columns_Equal_Width(self):

            # Просто едиоразово устанавливает ширину всех колонок в таблице - по ровну.

            width = self.Get__Size().width;

            Average_width = int(width/len(self.List_Columns_Name));  # Средняя ширина колонок.

            for column in (self.List_Columns_Name):

                self.Set_Column_Width(column[0], Average_width);


        def Set_Background_Color(self,  Color:str):
            pass

        def Set_Color_Text(self,  Color: str):
            style = tkinter.ttk.Style()
            style_name = f"Custom{id(self.Obj)}.Treeview"
            style.configure(style_name, foreground=Color)
            self.Obj.configure(style=style_name)

        def Set_SelectColor_Text(self,  Color: str):
            style = tkinter.ttk.Style()
            style_name = f"Custom{id(self.Obj)}.Treeview"
            # цвет текста выделенной строки
            style.map(style_name, foreground=[("selected", Color)])
            self.Obj.configure(style=style_name)

        def Set_Font_Name(self,  Font_Name: str):
            style = tkinter.ttk.Style()
            style_name = f"Custom{id(self.Obj)}.Treeview"
            style.configure(style_name, font=(Font_Name, self.Font_Size))
            self.Obj.configure(style=style_name)

        def Set_Font_Size(self,  Font_Size: int):
            style = tkinter.ttk.Style()
            style_name = f"Custom{id(self.Obj)}.Treeview"  # уникальное имя стиля для этой таблицы

            style.configure(style_name, font=("TkDefaultFont", Font_Size))
            style.configure(f"{style_name}.Heading", font=("TkDefaultFont", Font_Size, "bold"))  # шрифт заголовков (опционально)

            # высота строки под новый размер шрифта (иначе текст будет обрезаться)
            style.configure(style_name, rowheight=int(Font_Size * 2))

            self.Obj.configure(style=style_name)

            self.Font_Size = Font_Size;


        def Add_filter_to_Column_by_Contain(self,  Column_ID: str, Filter_words: str) -> None:
            # Добавляет (или обновляет, если уже был) фильтр "Содержит" для конкретной колонки.
            # Фильтры по разным колонкам накапливаются - действуют одновременно (AND).
            # Если Filter_words == "" - фильтр для этой колонки просто снимается (эквивалент Reset_Filter_to_Column).

            if Filter_words == "":
                self.Column_Filters.pop(Column_ID, None)
            else:
                self.Column_Filters[Column_ID] = Filter_words.lower()

            self._Recalculate_Filter()

        def Reset_Filter_to_Column(self,  Column_ID: str) -> None:
            # Снимает фильтр только для указанной колонки, остальные активные фильтры не трогает.
            self.Column_Filters.pop(Column_ID, None)
            self._Recalculate_Filter()

        def Reset_all_Filter(self) -> None:
            # Полностью снимает все активные фильтры по всем колонкам, возвращает все строки.
            self.Column_Filters.clear()
            self._Recalculate_Filter()


        def Sort_as_Text(self,  List_Sort_Param: list[tuple[str, Tkinter_GUI__class.Sort_enum]]) -> None:
            # List_Sort_Param - список туплов типа: [("Column_Text_ID_1",Sort_enum), ("Column_Text_ID_2",Sort_enum)] - то есть, если указать более одного столбца, то сортировка будет последовательно по указанными столбцам.
            # Сортировка колонок как текст (лексикографически, регистронезависимо).
            self._Sort_Core(List_Sort_Param, Key_Func=lambda cell: str(cell).lower())

        def Sort_as_Value(self,  List_Sort_Param: list[tuple[str, Tkinter_GUI__class.Sort_enum]]) -> None:
            # List_Sort_Param - список туплов типа: [("Column_Text_ID_1",Sort_enum), ("Column_Text_ID_2",Sort_enum)] - то есть, если указать более одного столбца, то сортировка будет последовательно по указанными столбцам.
            # Сортировка колонок как числовое значение. Нечисловые/пустые значения уходят в конец (независимо от direction),
            # чтобы "мусор" не искажал порядок нормальных чисел.
            def Key_Func(cell):
                try:
                    return (0, float(cell))
                except (ValueError, TypeError):
                    return (1, 0.0)  # не число - всегда после чисел

            self._Sort_Core(self, List_Sort_Param, Key_Func=Key_Func)

        def Check_Duplicate(self, Row_tuple:tuple[str,...], Column_Index_tuple:tuple[int,...])->int:

            # Проверяет переданную строку Row_tuple на дубликат, то есть на присутвие уже в таблице.
            # Row_tuple - tuple текстовых значений ячеек строки - соответвующих указанным столбцам "Column_Index_tuple"
            # Column_Index_tuple - это индексы Столбцов, которые нужно проверть на дубликат - то есть дубликат строка будет проверена именно на указанных столбцах, а не на всей строке.

            All_Item_IDs = list(self.Obj.get_children(""));

            All_Item_IDs.extend(Hidden_Item[0] for Hidden_Item in self.Hidden_Items);

            for Index, Item_ID in enumerate(All_Item_IDs):

                Existing_Row             = self.Obj.item(Item_ID, "values");
                Existing_Values_to_Check = tuple(Existing_Row[i] for i in Column_Index_tuple);

                if Existing_Values_to_Check == Row_tuple:
                    return Index;   # Индекс строки которая повторяется.

            return -1;  # Дубликатор нет

        def Get__Column_Index_by_Name(self, Column_Name: str) -> int:

            # Ищем позицию столбца по его Name_ID (техническое имя) среди List_Columns_Name.
            # List_Columns_Name - list[tuple[Name_ID, Display_Name]]

            for index, (Name_ID, _Display_Name) in enumerate(self.List_Columns_Name):
                if Name_ID == Column_Name:
                    return index;
            return -1;  # Столбец с таким Name_ID не найден

        def Get_Cell_Value(self, Row_Index, Column_Index) -> str:

            # Возвращает текстовое значение ячейки по числовому индексу строки и индексу столбца.

            Children = self.Obj.get_children();  # Список item_id всех (видимых) строк по порядку


            if (Row_Index < 0 or Row_Index >= len(Children)):
                return "";  # Индекс строки вне диапазона

            Item_ID = Children[Row_Index];
            Row_Values = self.Obj.item(Item_ID, "values");  # tuple/list значений строки

            if (Column_Index < 0 or Column_Index >= len(Row_Values)):
                return "";  # Индекс столбца вне диапазона

            return str(Row_Values[Column_Index]);

        def Get_Row_Value(self, Row_Index) -> tuple[str, ...]:

            # Возвращает tuple строковых значений строки по кол-ву столбцов.

            Children = self.Obj.get_children();  # Список item_id всех (видимых) строк по порядку

            if (Row_Index < 0 or Row_Index >= len(Children)):
                return tuple();  # Индекс строки вне диапазона - возвращаем пустой tuple

            Item_ID = Children[Row_Index];
            Row_Values = self.Obj.item(Item_ID, "values");  # tuple/list значений строки

            return tuple(str(Value) for Value in Row_Values);

        def Get_Row_Size(self) -> int:
            # Возвращает кол-во строк в таблице (только видимые, т.е. не скрытые фильтром).
            return len(self.Obj.get_children());

        def Get_Selected_Row_by_Index(self) -> list[int]:

            # Возвращает список порядковых номеров (индексов) выделенных строк, а не их item_id.

            Children = self.Obj.get_children();       # Все (видимые) строки таблицы по порядку
            Selected_Items = self.Obj.selection();     # tuple item_id выделенных строк

            Result = [];
            for Item_ID in Selected_Items:
                if Item_ID in Children:
                    Result.append(Children.index(Item_ID));  # Переводим item_id в порядковый индекс

            return Result;

        def Get_Selected_Row_by_Value(self) -> list[tuple[str, ...]]:

            # Возвращает список tuple по кол-ву столбцов значений для каждой выделенной строки.

            Selected_Indexes = self.Get_Selected_Row_by_Index();  # Список порядковых индексов выделенных строк

            Result = [];
            for Row_Index in Selected_Indexes:
                Result.append(self.Get_Row_Value(Row_Index));

            return Result;           


        def Get__TOP_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update();

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y());
                       
        def Get__TOP_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width() , self.Container.winfo_y());
            
        def Get__BOTTOM_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height() );

        def Get__BOTTOM_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width() , self.Container.winfo_y() + self.Container.winfo_height() );
  
        def Get__CENTRE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width()/2 , self.Container.winfo_y() + self.Container.winfo_height()/2 );

        def Get__TOP_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() +  self.Container.winfo_width()/2 , self.Container.winfo_y());

        def Get__BOTTOM_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width()/2 , self.Container.winfo_y());

        def Get__LEFT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height()/2 );

        def Get__RIGHT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height()/2 );
   

        def Get__Size(self)->Tkinter_GUI__class.Size_struct:

             self.Window_struct_ref.Obj.update()  # или update()

             return Tkinter_GUI__class.Size_struct(self.Container.winfo_width() , self.Container.winfo_height() );

        #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------

        #------------------------------------------------------------------PRIVAE:-----------------------------------------------------------------

        def _Set_Column(self, List_Column_Name:list[tuple[str,str]]):

            # tuple[str,str] - [0] Name_ID столбца, [1] - само отображаемое текстовое имя столбца которые видит Пользователь в таблице.

            Columnd_ID, Column_Name =  zip(*List_Column_Name);  # распакоука на*й


            self.Obj["columns"] = list(Columnd_ID);

            for i in range(len(Columnd_ID)):
                self.Obj.heading(Columnd_ID[i], text = Column_Name[i]);
                self.Obj.column(Columnd_ID[i], stretch=False);


        def _Get_RowID_by_FullValueRow(self, Full_Value_Row: tuple):
            #Ищем в Таблице Row_ID по полной сцепце значений столбцов для искомой строки. SomeValue - соовттевенно tuple этих значений. И внимание - если даже я добавлял в строку таблицы прямое числовое значение, то в tuple`е - его все равно нужно казать, как тестовое.

            for item_id in self.Obj.get_children():
                values = tuple(self.Obj.item(item_id, "values"))
                if values == Full_Value_Row:
                    return item_id
            return None

        def _Get_RowID_by_Index(self, index: int):
            children = self.Obj.get_children()
            if 0 <= index < len(children):
                return children[index]
            return None

        def _Set_Header_Click_Callback(self, Callback):
            #print("_Table__Set_Header_Click_Callback");
            # Callback должен принимать (col_id: str, x: int)
            columns = self.Obj["columns"]
            for col_id in columns:
                # используем lambda с захватом col_id по умолчанию (иначе все колбеки будут ссылаться на последний col_id)
                self.Obj.heading(col_id, command=lambda c=col_id: self._Header_Click_Handler(c, Callback));

        def _Header_Click_Handler(self, col_id: str, Callback):

            # координата X начала столбца
            bbox = self.Obj.bbox(self.Obj.get_children()[0], col_id) if self.Obj.get_children() else None
            x = self.Obj.column(col_id)  # это вернёт словарь с width, но не x-координату напрямую
    
            # для точной x-координаты заголовка нужно вычислить через порядок столбцов и их width
            columns = self.Obj["columns"]
        
            x_pos_local = 0
            y_pos_local = 0

            for c in columns:
                if c == col_id:
                    break
                x_pos_local += self.Obj.column(c, "width");
            
            x_pos_window = x_pos_local  + self.Obj.winfo_x();
            x_pos_screen = x_pos_window + self.Window_struct_ref.Obj.winfo_x();

            y_pos_screen = self.Obj.winfo_rooty();

            Callback(col_id, x_pos_screen, y_pos_screen);

        def _Click_for_Header_Callback(self, col_id, x_screen:int, y_screen:int):
            # x_screen/y_screen - X коордианта начала колонки "col_id" в координатах Монитора.

            self.Popup_Filter_for_Table_Obj.Set_Pos(x_screen, y_screen);

            self.ColumnID_Last_Click = col_id;          # ДОЛЖНО БЫТЬ ПЕРЕД вызвовом show()!!!
            self.Popup_Filter_for_Table_Obj.show();
        
        
            # print(f"Click for Header Table: {col_id}, x_coordinate_screen{x_screen}")

        def _Recalculate_Filter(self) -> None:
            # Общая точка пересчёта видимости строк для ВСЕХ функций фильтрации таблицы.
            # Вызывается после любого изменения self.Column_Filters.
            # Сначала возвращаем всё на место, потом заново скрываем то, что не проходит ВСЕ активные фильтры (AND).

            # Возвращаем все скрытые строки обратно в дерево, в исходную позицию:
            for item_id, parent_id, index in self.Hidden_Items:
                self.Obj.move(item_id, parent_id, index)
            self.Hidden_Items.clear()

            if not self.Column_Filters:
                return  # активных фильтров нет - все строки видимы, дальше делать нечего

            All_items = list(self.Obj.get_children(""))

            for item_id in All_items:
                match_all = True
                for col_id, filt_lower in self.Column_Filters.items():
                    cell_value = str(self.Obj.set(item_id, col_id))
                    if filt_lower not in cell_value.lower():
                        match_all = False
                        break

                if not match_all:
                    parent_id = self.Obj.parent(item_id)  # всегда "" для таблицы, но берём честно
                    index = self.Obj.index(item_id)
                    self.Hidden_Items.append((item_id, parent_id, index))
                    self.Obj.detach(item_id)

        def _Sort_Core(self, List_Sort_Param: list[tuple[str, Tkinter_GUI__class.Sort_enum]], Key_Func) -> None:
            # Общее ядро сортировки для Text и Value версий.
            # Сортируем ВСЕ строки, включая скрытые фильтром (detached) - чтобы порядок не разъезжался
            # с Hidden_Items после снятия/изменения фильтра.
            # Key_Func(cell_value: str) -> сравниваемое значение (str для текста, число для значения).

            All_item_ids = list(self.Obj.get_children("")) + [item_id for item_id, _, _ in self.Hidden_Items]

            # Сортируем последовательно с конца списка параметров к началу -
            # Python's sort стабилен, поэтому последовательные stable-сортировки дают эффект ORDER BY col1, col2, ...
            for Column_ID, Sort_Direction in reversed(List_Sort_Param):
                Reverse_Flag = (Sort_Direction == Tkinter_GUI__class.Sort_enum.descending)
                All_item_ids.sort(key=lambda item_id: Key_Func(self.Obj.set(item_id, Column_ID)),reverse=Reverse_Flag);

            # Переставляем элементы в дереве в новом порядке (работает и для detached item_id):
            for New_Index, item_id in enumerate(All_item_ids):
                self.Obj.move(item_id, "", New_Index)

            # Пересчитываем index в Hidden_Items под новый порядок, чтобы восстановление после снятия фильтра было консистентным:
            if self.Hidden_Items:
                New_Index_By_Id = {item_id: idx for idx, item_id in enumerate(All_item_ids)}
                self.Hidden_Items = [
                    (item_id, parent_id, New_Index_By_Id[item_id])
                    for item_id, parent_id, _ in self.Hidden_Items
                ]
                # После move detached-элементы снова окажутся видимыми - "прячем" их обратно:
                for item_id, _, _ in self.Hidden_Items:
                    self.Obj.detach(item_id)

        def _set_Popup_CellViewerText_for_Table(self):

            self.Popup_CellViewerText_Obj = self.Window_struct_ref.Tkinter_GUI__Obj.Popup_CellViewerText_for_Table__class(self);


            def _callback_click(Table_Struct:Tkinter_GUI__class.Table_Struct, Row_Index:int, Column_Index:int, Click_Button_enum:Tkinter_GUI__class.Click_Button_enum, List_any:list[any]):

                if(Click_Button_enum == Tkinter_GUI__class.Click_Button_enum.Double_Left):
                    Cell_string = Table_Struct.Get_Cell_Value(Row_Index, Column_Index);

                    Table_Struct.Popup_CellViewerText_Obj.Set_Text(Cell_string);

                    Table_Struct.Popup_CellViewerText_Obj.Show();


            self.Add_Callback_for_Click_for_Cell(_callback_click, []);

    class Popup_Filter_for_Table__class:


        def __init__(self, Table_struct):
            #-----------------------------------------------------------------
            self.Table_struct        = Table_struct;

            self.popup = tkinter.Toplevel(Table_struct.Window_struct_ref.Obj);
            self.entry = tkinter.Entry(self.popup);
            self.btn_reset       = tkinter.Button(self.popup, text="Сбросить фильтр",      command=self._on_reset_filter);
            self.btn_reset_all   = tkinter.Button(self.popup, text="Сбросить все фильтры", command=self._on_reset_all_filter);

            self.btn_sort_as_Text      = tkinter.Button(self.popup, text="Сортировка", command=self._on_sort_text);
            #self.btn_sort_as_Value    = tkinter.Button(self.popup, text="Сортировка как числа", command=self._on_sort_value);
            self.Last_SortText_Apply   = Tkinter_GUI__class.Sort_enum.none;
            #self.Last_SortValue_Apply = Tkinter_GUI__class.Sort_enum.none;
            #-----------------------------------------------------------------

            #-----------------------------------------------------------------
            self.popup.title("Фильтр <Содержит>");
            self.popup.geometry("300x150");
            self.popup.protocol("WM_DELETE_WINDOW", self._on_close);    # Перехватываем клик по крестику закрктия и направляем его в "_on_close"

            self.popup.columnconfigure(0, weight=1);
            self.popup.rowconfigure(0, weight=1);
            self.popup.rowconfigure(1, weight=1);
            self.popup.rowconfigure(2, weight=1);
            self.popup.rowconfigure(3, weight=1);

            self.entry.grid(row=0, column=0, sticky="nsew", padx=10, pady=5);

            self.btn_reset.grid(row=1, column=0, sticky="nsew", padx=10, pady=5);
            self.btn_reset_all.grid(row=2, column=0, sticky="nsew", padx=10, pady=5);
            self.btn_sort_as_Text.grid(row=3, column=0, sticky="nsew", padx=10, pady=5);

            self.popup.bind("<Configure>", self._on_popup_resize);
            #-----------------------------------------------------------------

            #------------------------------------------------
            #Устанавливаем колбек на ввод текста в Поле Ввода:

            self.vcmd = (self.entry.register(self._on_change), '%P')
            self.entry.config(validate="key", validatecommand=self.vcmd);
            #------------------------------------------------

            self.popup.withdraw();   # Изначально скрываем окно.


        #----------------------------------------------
        def Set_Pos(self, X:int, Y:int):
            self.popup.geometry(f"+{X}+{Y}");

        def show(self):
            self.entry.config(validate="none");                             # Временно отключим колбек на изменения в "поле ввода", чтобы он не сработал при вызове очищения "поля ввода".
            self.entry.delete(0, tkinter.END);                              # Очистим поле ввода, помле нажатия Пользователя на крестик закртия окна фильтрации.
            self.entry.config(validate="key", validatecommand=self.vcmd);   # Восстанавливаем колбек на место.

            self.popup.deiconify(); # Показываем окно.
        #----------------------------------------------



        #---------------------------------------------------------------------
        def _on_reset_filter(self):
            self.Table_struct.Reset_Filter_to_Column(self.Table_struct.ColumnID_Last_Click);
            #print("Reset Filter clicked")
            
        def _on_reset_all_filter(self):
            self.Table_struct.Reset_all_Filter();
            #print("Reset All Filter clicked")
            
        def _apply_fonts(self):
            h = self.popup.winfo_height() // 4;
            entry_size = max(8, int(h * 0.5));
            btn_size = max(8, int(h * 0.4));
            self.entry.config(font=("TkDefaultFont", entry_size));
            self.btn_reset.config(font=("TkDefaultFont", btn_size));
            self.btn_reset_all.config(font=("TkDefaultFont", btn_size));
            self.btn_sort_as_Text.config(font=("TkDefaultFont", btn_size));

        def _on_popup_resize(self, event):
            self._apply_fonts();

        def _on_change(self, change_text):
            # print(change_text);
            self.Table_struct.Add_filter_to_Column_by_Contain(self.Table_struct.ColumnID_Last_Click, change_text);
            return True         # обязательно True, иначе ввод не применится
        
        def _on_close(self):
            self.popup.withdraw();  # Перехватываем клик по крестику закрытия и скрываем окно, а не закрываем его.
            
        def _on_sort_text(self):
            if(self.Last_SortText_Apply == Tkinter_GUI__class.Sort_enum.none):
                #print("none");
                # Значит это первое нажатие кнопки "Сортировка". Значит применим сортировку по "Возростанию":
                self.Table_struct.Sort_as_Text([( self.Table_struct.ColumnID_Last_Click,Tkinter_GUI__class.Sort_enum.descending)]);
                self.Last_SortText_Apply = Tkinter_GUI__class.Sort_enum.descending;
                self.btn_sort_as_Text.config(text="Сортировка(по Убыванию)");
                return;

            if(self.Last_SortText_Apply == Tkinter_GUI__class.Sort_enum.descending):
                #print("descending");
                self.Table_struct.Sort_as_Text([( self.Table_struct.ColumnID_Last_Click,Tkinter_GUI__class.Sort_enum.ascending)]);
                self.Last_SortText_Apply = Tkinter_GUI__class.Sort_enum.ascending;
                self.btn_sort_as_Text.config(text="Сортировка(по Возрастанию)");
                return;

            if(self.Last_SortText_Apply == Tkinter_GUI__class.Sort_enum.ascending):
                #print("ascending");
                self.Table_struct.Sort_as_Text([( self.Table_struct.ColumnID_Last_Click,Tkinter_GUI__class.Sort_enum.descending)]);
                self.Last_SortText_Apply = Tkinter_GUI__class.Sort_enum.descending;
                self.btn_sort_as_Text.config(text="Сортировка(по Убыванию)");
                return;
        #--------------------------------------------------------------------

    class Popup_CellViewerText_for_Table__class:
        
        def __init__(self, Table_struct):

            self.Table_struct        = Table_struct;

            self.popup = tkinter.Toplevel(Table_struct.Window_struct_ref.Obj);
            self.popup.title("Cell Viewer");
            self.popup.geometry("300x150");
            self.popup.protocol("WM_DELETE_WINDOW", self._on_close);    # Перехватываем клик по крестику закрктия и направляем его в "_on_close"
            self.popup.withdraw();

            self.text = tkinter.Text(self.popup, wrap="none")  # wrap="none" - переноса строк по ширине нет, строки переностся только если в текстае есть "\n". wrap="word" - перенос по словам, то есть если слово по ширине не умешается, то переносится. wrap="char" — по символам

            # скроллбары
            self.yscroll = tkinter.Scrollbar(self.popup, command=self.text.yview)
            self.xscroll = tkinter.Scrollbar(self.popup, orient="horizontal", command=self.text.xview)
            self.text.config(yscrollcommand=self.yscroll.set, xscrollcommand=self.xscroll.set)

            self.text.grid(row=0, column=0, sticky="nsew")
            self.yscroll.grid(row=0, column=1, sticky="ns")
            self.xscroll.grid(row=1, column=0, sticky="ew")

            self.popup.grid_rowconfigure(0, weight=1)
            self.popup.grid_columnconfigure(0, weight=1)


        def Set_Text(self, Text_string):
            self.text.delete("1.0", "end");  # Удаляет все содержимое
            self.text.insert("1.0", Text_string);

        def Show(self):
            self.popup.deiconify();

        def _on_close(self):
            self.popup.withdraw();  # Перехватываем клик по крестику закрытия и скрываем окно, а не закрываем его.



    @dataclass(slots=True)
    class ProgressBar_Struct:
        Window_struct_ref:Tkinter_GUI__class.Window_struct = None;

        Name:str = "";
        Obj:tkinter.ttk.Progressbar = field(default_factory=tkinter.ttk.Progressbar);
        Label:tkinter.ttk.Label     = field(default_factory=tkinter.ttk.Label);

        Font_Name:str = "Arial";
        Font_Size:int = 12;


        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------

        def Set_Size(self, Width:int, Height:int):

            self.Obj.place(width=Width, height=Height);

            self.Label.place(width=Width);

        def Set_Pos(self, X:int, Y:int, Anchor_ID:Anchor_enum):

            self.Obj.place(x=X, y=Y, anchor = Anchor_ID);

            self.Window_struct_ref.Obj.update();

            self.Label.place(x=self.Obj.winfo_x(), y=self.Obj.winfo_y() + self.Obj.winfo_height() + 1, anchor = Tkinter_GUI__class.Anchor_enum.TopLeft);


        def Set_Font_Name(self, Font_Name:str):

            self.Font_Name = Font_Name;

            self.Label.config(font=(Font_Name, self.Font_Size));


        def Set_Font_Size(self, Font_Size:int):

            self.Font_Name = Font_Size;

            self.Label.config(font=(self.Font_Name, Font_Size));


        def Set_Text(self, ProgressBar_Text:str):

            self.Label.config(text=ProgressBar_Text);


        def Set_Label_Background_Color(self, Color:str):

            self.Label.config(background=Color);

        def Set_Text_Color(self, Color:str):

            self.Label.config(foreground=Color);


        def Set_ProgressValue(self, Value:float):

            self.Obj['value'] = Value;
    
        def Get__TOP_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y());
   
        def Get__TOP_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width(), self.Obj.winfo_y());
            
        def Get__BOTTOM_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Label.winfo_x(), self.Label.winfo_y() + self.Label.winfo_height());

        def Get__BOTTOM_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Label.winfo_x() + self.Label.winfo_width(), self.Label.winfo_y() + self.Label.winfo_height());
        
        def Get__CENTRE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width()/2, self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__TOP_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() +  self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__BOTTOM_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Label.winfo_x() + self.Label.winfo_width()/2, self.Label.winfo_y());

        def Get__LEFT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__RIGHT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);
       

        def Get__Size(self)->Tkinter_GUI__class.Size_struct:

            self.Window_struct_ref.Obj.update();

            return Tkinter_GUI__class.Size_struct(self.Obj.winfo_width(), self.Obj.winfo_height());


         #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------

    @dataclass(slots=True)
    class OneColumnTable_aka_Listbox_Struct:
        Window_struct_ref: Tkinter_GUI__class.Window_struct = None;

        Name: str = "";
        Obj: tkinter.ttk.Treeview = field(default_factory=tkinter.ttk.Treeview);
        Container:Frame           = field(default_factory=tkinter.Frame);

        Font_Name:str = "Arial";
        Font_Size:int = 12;
        V_scroll_obj:Scrollbar = field(default_factory=tkinter.Scrollbar);
        H_scroll_obj:Scrollbar = field(default_factory=tkinter.Scrollbar);
        
        Hidden_Items: list[tuple[str, str, int]] = field(default_factory=list); # Нужен для фильтрации по призанку "Содержит" 
        
        Inputbox_obj:Entry =  field(default_factory=tkinter.Entry); # Поле Ввода для филтрации
        
        Font_Measurement:tkinter.font.Font = field(default_factory=tkinter.font.Font);


        List_Callback_for_Select:list[Tkinter_GUI__class.Callback_struct]   = field(default_factory = list);

        Set_:set =  field(default_factory=set);  # придется держать дубликат "Set" для быстрого поиска дулей при добавлении.
    
        Callback_for_Empty:Tkinter_GUI__class.Callback_struct = field(default_factory = lambda:Tkinter_GUI__class.Callback_struct());   # Для кобека когда список становится полностью пустым или когда из пустого доавбляется хотя один элемент.
        Element_Size:int = 0;

        Max_width:int = 0;

        Callback_Right_Left_Click:Tkinter_GUI__class.Callback_struct =  field(default_factory = lambda: Tkinter_GUI__class.Callback_struct());   # Колбек на Правый клик мыши по Box`у виджета.
        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------

        

        def Add_Callback_for_Select(self, Callback_func, List_any:list[any]):
              
              self.List_Callback_for_Select.append(Tkinter_GUI__class.Callback_struct(Callback_func, List_any));
              
              def _on_select(event):

                selected = event.widget.selection();
                Flag:bool = False;

                if selected:
                    Flag =True;  # Значит Пользовтаель что-то выбрал.
                else:
                    Flag = False; # Значит Пользователь снял выделение со всех строк.

                for callback_item in self.List_Callback_for_Select:
                    callback_item.Callback(self, Flag, callback_item.List_any);


              if len(self.List_Callback_for_Select) == 1:
                self.Obj.bind("<<TreeviewSelect>>", _on_select);      # Это первый вызов функции "List_Callback_for_Click" - поэтому привяжим колбек к данной кнопке.

        def Set_Callback_for_Empty(self, Callback_func, List_any:list[any]):
              
              self.Callback_for_Empty.Callback = Callback_func;
              self.Callback_for_Empty.List_any = List_any;
          
        def Set_Callback_for_Right_Left_Click(self, Callback_Right_Left_Click, List_any:list[any]):

            # Ставит колбек на Правый клик мыши по Box`у виджета.

            self.Callback_Right_Left_Click.Callback = Callback_Right_Left_Click;
            self.Callback_Right_Left_Click.List_any = List_any;

            def _intermediate_func(event):

                if event.num == 1:
                    self.Callback_Right_Left_Click.Callback(self, Tkinter_GUI__class.Click_Button_enum.Left, self.Callback_Right_Left_Click.List_any);  # Значит Левая
                elif event.num == 3:
                    self.Callback_Right_Left_Click.Callback(self, Tkinter_GUI__class.Click_Button_enum.Right, self.Callback_Right_Left_Click.List_any);  # Значит Правая

           

            self.Obj.bind("<Button-1>", _intermediate_func);   # Левая Button
            self.Obj.bind("<Button-3>", _intermediate_func);   # Правая Button


        def Add_Row_with_Duplicate_Check(self, Added_Data:list[str], Add_pos:int):


            if(Add_pos == -1):         # добавляем в конец списка
                for item in (Added_Data):

                    if (item in self.Set_) == False:
                        # Значит такого эелмента еще не доавбяллось:
                        self.Set_.add(item);
                        self.Obj.insert("", tkinter.END, values=(item,))    # insert - принимает tuple[] - сам tuple должен быть равен по размерку кол-ву колонок, так как у меня эмуляция простого одноколоночного списка, то колонка одна, поэтому саму строку "item" оборачиваем в tuple.
            else:
                for item in reversed(Added_Data):    # В Treeview нельзя вставить срзу весь список, поэтому только по одному элемету - и в обратном цикле, иначе все ставится наоборот, так как каждый последующий элемент будет вставлятся каждый раз ПЕРЕД предыдущим.
                     
                    if (item in self.Set_) == False:
                        # Значит такого эелмента еще не доавбяллось:
                        self.Set_.add(item);
                    
                        self.Obj.insert("", Add_pos, values=(item,))



            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            self._Set_Max_Width(Added_Data);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


            self._Check_for_Empty_and_Call_Callback();    # Проверяем на переход списка с Пустого на Наполненный или с Наполненого на Пустой и оповещаем Пользователя.

        def Add_Row_with_Duplicate_Check__Range(self, Added_Data:list[str], Add_pos:int, Start_Index_Use:int, End_Index_Use:int):


            # Start_Index_Use - индекс в списке Added_Data - с котрого нужно доавблять в Treeview
            # End_Index_Use   - индекс в списке Added_Data - до которого включительно нужно доавблять в Treeview
            # End_Index_Use = -1 - значит до конечного элемента Added_Data

            if End_Index_Use == -1:         # добавляем в конец списка
                End_Index_Use = len(Added_Data) - 1;

            if(Add_pos == -1):

                for index in range(Start_Index_Use, End_Index_Use + 1):
                    item = Added_Data[index];
                    if (item in self.Set_) == False:
                        # Значит такого эелмента еще не доавбяллось:
                        self.Set_.add(item);
                        self.Obj.insert("", tkinter.END, values=(item,))    # insert - принимает tuple[] - сам tuple должен быть равен по размерку кол-ву колонок, так как у меня эмуляция простого одноколоночного списка, то колонка одна, поэтому саму строку "item" оборачиваем в tuple.
            else:
               
               for index in range(End_Index_Use, Start_Index_Use - 1, -1):    # В Treeview нельзя вставить срзу весь список, поэтому только по одному элемету - и в обратном цикле, иначе все ставится наоборот, так как каждый последующий элемент будет вставлятся каждый раз ПЕРЕД предыдущим.
                   
                  item = Added_Data[index];
                    
                  if (item in self.Set_) == False:
                        # Значит такого эелмента еще не доавбяллось:
                        self.Set_.add(item);
            
                        self.Obj.insert("", Add_pos, values=(item,))
           

            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            self._Set_Max_Width(Added_Data);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            self._Check_for_Empty_and_Call_Callback();    # Проверяем на переход списка с Пустого на Наполненный или с Наполненого на Пустой и оповещаем Пользователя.


        def Delete_Row_by_Index(self, Index:int):

            children = self.Obj.get_children("");
            if (Index == -1):

                if (children):
                    Row_ID = children[-1]
                    self.Set_.discard(self.Obj.item(Row_ID, "values")[0])
                    self.Obj.delete(children[-1]);

            elif (0 <= Index < len(children)):

                Row_ID = children[-1]
                self.Set_.discard(self.Obj.item(Row_ID, "values")[0])
                self.Obj.delete(children[Index]);

           
            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            #self._Set_Max_Width(List_RowID);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


            self._Check_for_Empty_and_Call_Callback();    # Проверяем на переход списка с Пустого на Наполненный или с Наполненого на Пустой и оповещаем Пользователя.

        def Delete_Row_by_Text(self, Text:str):

            for item_id in self.Obj.get_children(""):
                if (self.Obj.item(item_id, "values")[0] == Text):
                    self.Obj.delete(item_id);
                    break;  # удаляем только первое совпадение

            
            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            #self._Set_Max_Width(List_RowID);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            self.Set_.discard(Text);

            self._Check_for_Empty_and_Call_Callback();    # Проверяем на переход списка с Пустого на Наполненный или с Наполненого на Пустой и оповещаем Пользователя.

        def Delete_Row_by_List_Text(self, List_Text: list[str]):

            Set_Text = set(List_Text)

            List_RowID = list(self.Obj.get_children(""))

            for item_id in List_RowID:
                if self.Obj.item(item_id, "values")[0] in Set_Text:
                    self.Obj.delete(item_id)

            # Пересчитываем ширину один раз
            #self._Set_Max_Width(List_RowID)

            self.Set_.difference_update(Set_Text)

            self._Check_for_Empty_and_Call_Callback()

        def Delete_All(self):

            self.Obj.delete(*self.Obj.get_children(""));
          
            #----------------------------------------------------
            self.Obj.column("value", width=0, stretch=False);
            #----------------------------------------------------

            self.Set_.clear();

            self._Check_for_Empty_and_Call_Callback();    # Проверяем на переход списка с Пустого на Наполненный или с Наполненого на Пустой и оповещаем Пользователя.


        def Edit_Row_by_RowIndex(self, Index:int, NewValue:str)->bool:

            # Index - это оыбчный порядковый "видимый" индекс в самой таблице. Это НЕ внутренний ID на саму строку.
            # Меняем знаение строки указанное по его прядкову идексу на новое значение.
            # Index = -1 - последняя строка в списке.

            children = self.Obj.get_children("");

            if (Index == -1):
                Index = len(children) - 1;
            if not (0 <= Index < len(children)):
                return False;

            Row_ID = children[Index]
            OldValue = self.Obj.item(Row_ID, "values")[0]
            self.Set_.discard(OldValue)
            self.Set_.add(NewValue)
            Row_ID = children[Index];
            self.Obj.item(Row_ID, values=(NewValue,));


            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            self._Set_Max_Width([NewValue]);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            return True;

        def Edit_Row_by_RowText(self, Text:str, NewValue:str)->bool:

            # Меняем знаение строки указанное по его текстовому значения на новое значение.

            for item_id in self.Obj.get_children(""):

                if (self.Obj.item(item_id, "values")[0] == Text):

                    self.Set_.discard(Text)
                    self.Set_.add(NewValue)
                    self.Obj.item(item_id, values=(NewValue,));
                    return True;


            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            self._Set_Max_Width([NewValue]);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            return False;

        def Edit_Row_by_RowID(self, Row_ID: str, NewValue: str) -> bool:

            # Row_ID - это именно внутренний ID на саму строку в списке. Тот ID - который возвращается из функции "Get_Selected_ID"

            # Меняем значение строки, указанной по её item_id, на новое значение.

            if not self.Obj.exists(Row_ID):
                return False;

            OldValue = self.Obj.item(Row_ID, "values")[0]

            self.Set_.discard(OldValue)
            self.Set_.add(NewValue)
            self.Obj.item(Row_ID, values=(NewValue,));

            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выходящие за ширину Treeview бокса:----------------------------
            self._Set_Max_Width([NewValue]);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            return True;


        def Set_Size(self, Width:int, Height:int):

            self.Container.place(width=Width, height=Height);       
        
            self.Obj.column("value", width=Width, stretch=False);

        def Set_Pos(self, X:int, Y:int, Anchor_ID:Anchor_enum):

            self.Container.place(x=X, y=Y, anchor = Anchor_ID);


        def Set_Pos_AutoFollow_to_Widget(self, Widget_From_Anchor_ID:Anchor_enum, Widget_To, Widget_To_Anchor_ID:Anchor_Relative_enum, Offset_Anchor_X,  Offset_Anchor_Y):     

            # Функция устанавливаем автоматическое следование заданного угла одного Виджета за заданным углом друого виджета.

            # Widget_From                       - виджет которй должен следовать.
            # Widget_From_Anchor_ID             - угол-якорь виджета "Widget_From" которым он должен следовать за указанной позицией у виджета "Widget_To" в углке-якоре "Widget_To_Anchor_ID"
            # Widget_To                         - виджет за координатами которого должен следовать виджет "Widget_From"
            # Offset_Anchor_X и Offset_Anchor_Y - АБСОЛЮТНОЕ смещение смещение от координаты привязки, короче коррекитровка, если она нужна.


            relative_X, relative_Y = Widget_To_Anchor_ID.value;

            self.Container.place(in_ = Widget_To,  relx = relative_X, rely = relative_Y, x=Offset_Anchor_X, y=Offset_Anchor_Y, anchor = Widget_From_Anchor_ID);

        def Set_Size_AutoFollow_to_Widget(self, Widget_To, Relative_Width, Relative_Height, Width_Offset, Height_Offset):
        
            # Функция устанавливаем автоматическое следование размера одного Виджета за размером друого виджета.
        
            # Widget_From    - виджет которй должен следовать.
            # Widget_To      - виджет за размерами которого должен следовать виджет "Widget_From"
            # Relative_Width - ОТНОСИТЕЛЬНЫЙ размер виджета "Widget_To" который будет автоматически передаватся на виджет "Widget_From". Вообщем Relative_Width = 1, то значит это Полная Ширина виджета "Widget_To", Relative_Width = 0.5 - половина Ширины вижета и так далее, то есть Ширина Виджета "Widget_From" всегда будет автоматически подстраиватся под указанную Ширину.
            # Relative_Height - тоже самое, что и "Relative_Width" - только для высоты.
            # Width_Offset, Height_Offset - это АБСОЛЮТНОЕ смешение в Ширине или Высоте - если нужна более точная настрока. Потому что в относительных процентах не всегда увилирно можно настроить.

            # Если один из Relative_Width или Relative_Height указаны = -1, то значит автоследование по этому параметру не будет ставится.
            
            
            if (Relative_Width != -1 and Relative_Height != -1):
                self.Container.place(in_ = Widget_To, relwidth = Relative_Width, relheight = Relative_Height, width = Width_Offset, height = Height_Offset);
                return;

            if (Relative_Width == -1 and Relative_Height != -1):
                self.Container.place(in_ = Widget_To, relheight = Relative_Height, height = Height_Offset);
                return;

            if (Relative_Height == -1 and Relative_Width != -1):
                self.Container.place(in_ = Widget_To, relwidth = Relative_Width, width = Width_Offset);
                return;



        def Set_Color_Text(self, Color: str):
            style = tkinter.ttk.Style()
            style_name = f"Custom{id(self.Obj)}.Treeview"
            style.configure(style_name, foreground=Color)
            self.Obj.configure(style=style_name)


        def Set_Font_Name(self, Font_Name: str):
            style = tkinter.ttk.Style()
            style_name = f"Custom{id(self.Obj)}.Treeview"
            style.configure(style_name, font=(Font_Name, self.Font_Size))
            self.Obj.configure(style=style_name)

            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            self.Font_Measurement.config(family=Font_Name);
        
            List_RowID = list(self.Obj.get_children(""));

            self._Set_Max_Width_(List_RowID);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        def Set_Font_Size(self, Font_Size: int):

            style = tkinter.ttk.Style()
            style_name = f"Custom{id(self.Obj)}.Treeview"  # уникальное имя стиля для этой таблицы

            style.configure(style_name, font=("TkDefaultFont", Font_Size))
            style.configure(f"{style_name}.Heading", font=("TkDefaultFont", Font_Size, "bold"))  # шрифт заголовков (опционально)

            # высота строки под новый размер шрифта (иначе текст будет обрезаться)
            style.configure(style_name, rowheight=int(Font_Size * 2))

            self.Obj.configure(style=style_name)

            self.Font_Size = Font_Size;
 
            self.Inputbox_obj.place(height = Font_Size*2);                                              # Синхронизируем Высоту Inputbox с высотой строки при измении размера шрифта.
            self.Inputbox_obj.config(font=(self.Font_Name, Font_Size));    # Синхронизируем размер шрифта текста поля ввода.


            #------------------Находим саму длинную строку и высчитавем ее ширину и ставим эту ширину на обьект Treeview, чтобы H-скроллбар мог скролить строки выхоядщие за ширину Treeview бокса:----------------------------
            self.Font_Measurement.config(size=Font_Size);
        
            List_RowID = list(self.Obj.get_children(""));
        
            self._Set_Max_Width_(List_RowID);
            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


        def Reset_Filter(self):

            # Восстанавливает все элементы, скрытые предыдущим фильтром, обратно в дерево.
            for item_id, parent_id, index in self.Hidden_Items:

                self.Obj.reattach(item_id, parent_id, index)

            self.Hidden_Items.clear()

        def Filter_Elements_Contains(self, Filter_text: str) -> None:

            # Вообщем функция филтрует ВСЕ элементы по признаку "Содержит"

            # Попросил нейронку написать, мне уже было лень.

            # Скрывает элементы, чей текст НЕ содержит Filter_text.
            # Header остаётся видимым, если сам подходит ИЛИ хотя бы один потомок подходит.

            self.Reset_Filter();
            if Filter_text == "":
                return

            Filter_text_lower = Filter_text.lower()  # приводим один раз, до цикла

            def Walk(child_id) -> bool:
                parent_id = self.Obj.parent(child_id)
                text = self.Obj.item(child_id, "values")[0];       
                self_match = Filter_text_lower in text.lower()  # сравнение в нижнем регистре. Вообщем чтобы не было регитсрозависимости, когда к примеру я фильтрую по фразу "Апельсни", а в OneColumnTable_aka_Listbox он содержится, как "апельсин" - приводим все к нижнему регистру и уже сравниваем.
                any_child_match = False
                for grandchild_id in list(self.Obj.get_children(child_id)):
                    if Walk(grandchild_id):
                        any_child_match = True
                if self_match or any_child_match:
                    return True
                else:
                    index = self.Obj.index(child_id)
                    self.Hidden_Items.append((child_id, parent_id, index))
                    self.Obj.detach(child_id)
                    return False

            for top_id in list(self.Obj.get_children("")):
                Walk(top_id)


        def Sort_as_Text(self, Sort_enum:Tkinter_GUI__class.Sort_enum) -> None:
            if (Sort_enum == Tkinter_GUI__class.Sort_enum.none):
                return;
        
            Obj = self.Obj;
            children = list(Obj.get_children(""));
        
            # Сортировка как текст (строковое сравнение)
            items = [(Obj.item(item_id, "values")[0], item_id) for item_id in children];
            items.sort(key=lambda pair: str(pair[0]).lower(), reverse=(Sort_enum == Tkinter_GUI__class.Sort_enum.descending));
        
            for index, (value, item_id) in enumerate(items):
                Obj.move(item_id, "", index);

        def Sort_as_Value(self, Sort_enum:Tkinter_GUI__class.Sort_enum) -> None:
            if (Sort_enum == Tkinter_GUI__class.Sort_enum.none):
                return;
        
            Obj = self.Obj;
            children = list(Obj.get_children(""));
        
            # Сортировка как число
            def to_number(val):
                try:
                    return float(val);
                except (ValueError, TypeError):
                    return float("-inf");  # нечисловые значения уходят в начало при ascending
        
            items = [(Obj.item(item_id, "values")[0], item_id) for item_id in children];
            items.sort(key=lambda pair: to_number(pair[0]), reverse=(Sort_enum == Tkinter_GUI__class.Sort_enum.descending));
        
            for index, (value, item_id) in enumerate(items):
                Obj.move(item_id, "", index);


        def Get_Selected(self) -> list[str]:

            result = [];
            for item_id in self.Obj.selection():
                result.append(self.Obj.item(item_id, "values")[0]);
            return result;

        def Get_Selected_ID(self) -> tuple[str,...]:

            return self.Obj.selection();   # возврашает tuple строк, НО строка в данном случае представляет из себя ID на саму строку в Treeview. По ней потом можно получить дсотуп к самой строке "мгновенно"

        def Get_Selected_Text_and_ID(self) -> list[tuple[str,str]]:

            # Тоже самое что и Get_Selected, но в месте с ID Строки возвраще еще и сам текст строки.

            result:list[tuple[str,str]] = [];

            for item_id in self.Obj.selection():

                Row_Text = self.Obj.item(item_id, "values")[0];
                Row_ID   = item_id;

                result.append((Row_Text, Row_ID));

            return result;


        def Get_AllRows(self) -> list[str]:
            result = [];
            for item_id in self.Obj.get_children(""):
                result.append(self.Obj.item(item_id, "values")[0]);
            return result;


        def Get__TOP_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update();

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y());
                       
        def Get__TOP_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width() , self.Container.winfo_y());
            
        def Get__BOTTOM_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height() );

        def Get__BOTTOM_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()  # или update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width() , self.Container.winfo_y() + self.Container.winfo_height() );
  
        def Get__CENTRE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width()/2 , self.Container.winfo_y() + self.Container.winfo_height()/2 );

        def Get__TOP_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() +  self.Container.winfo_width()/2 , self.Container.winfo_y());

        def Get__BOTTOM_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x() + self.Container.winfo_width()/2 , self.Container.winfo_y());

        def Get__LEFT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height()/2 );

        def Get__RIGHT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Container.winfo_x(), self.Container.winfo_y() + self.Container.winfo_height()/2 );
   

        def Get__Size(self)->Tkinter_GUI__class.Size_struct:

             self.Window_struct_ref.Obj.update()  # или update()

             return Tkinter_GUI__class.Size_struct(self.Container.winfo_width() , self.Container.winfo_height() );

        #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------
        
        #------------------------------------------------------------------PRIVATE:-------------------------------------------------------------------
        def _Set_Max_Width_(self, List_RowID:list[str]):
            
            Max_width:int = 0;

            for item_ID in (List_RowID):
                row_text = self.Obj.item(item_ID, "values")[0];
                width =  len(row_text)*self.Font_Size; # self.Font_Measurement.measure(row_text); measure - просто эпически медленная операция. Придется заменить на примерное с запасом вычисления ширины.

                if(width > Max_width):
                    Max_width = width;

       
            self.Obj.column("value", width=Max_width+10, stretch=False);
            
        def _Set_Max_Width(self, List_RowText:list[str]):
            
            for row_text in (List_RowText):
                width =  len(row_text)*self.Font_Size; # self.Font_Measurement.measure(row_text); measure - просто эпически медленная операция. Придется заменить на примерное с запасом вычисления ширины.

                if(width > self.Max_width):
                    self.Max_width = width;

            self.Obj.column("value", width=self.Max_width+10, stretch=False);


        def _Inputbox_Enter_Callback(self, Enter_Text:str):
            
            if (Enter_Text == ""):
                self.Reset_Filter();
            else:
                # print(Enter_Text);
                self.Filter_Elements_Contains(Enter_Text);

        def _Check_for_Empty_and_Call_Callback(self):

            Current_Element_Size:int = len(self.Obj.get_children());

            if (self.Callback_for_Empty != None):

                if (Current_Element_Size != 0 and self.Element_Size == 0):
                    # Значит произошел переход от Пустого писка к Наполненному. Вызываем колбек и оповещаем Пользователя:
                    self.Callback_for_Empty.Callback(self, True, self.Callback_for_Empty.List_any);
                else:
                    if (Current_Element_Size == 0 and self.Element_Size != 0):
                        # Значит произошел переход от Наполненого списка к gecnjve. Вызываем колбек и оповещаем Пользователя:
                        self.Callback_for_Empty.Callback(self, False, self.Callback_for_Empty.List_any);


            self.Element_Size = Current_Element_Size;

    @dataclass(slots=True)
    class Entry_DateTime_Struct:
        Window_struct_ref:Tkinter_GUI__class.Window_struct = None;

        Name:str = "";
        Obj:tkinter.Entry = field(default_factory=tkinter.Entry);

        Font_Name:str = "Arial";
        Font_Size:int = 12;

        Prohibited_symbols  = {"-", ":", " "}  # символы-разделители, которые нельзя трогать.   Формат даты следующий: "%d-%m-%Y %H:%M"
        Formate_Date_string:str = "";  # "%d-%m-%Y";    # "%d-%m-%Y %H:%M"

        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------
        def Set_SymvSize(self, Width:int):
        
            # Высота подстраивается автомсатически.

            self.Obj.place_forget();   # Нужно для того, чтобы сбросить размер от устновки через "Set_PixelSize" - потому что если устаносить через .place() - потому установка размера через config() не работает.

            self.Obj.config(width=Width);

        def Set_PixelSize(self, Width:int, Height:int):

            self.Obj.place(width=Width, height=Height);

        def Set_Pos(self, X:int, Y:int, Anchor_ID:Anchor_enum):

            self.Obj.place(x=X, y=Y, anchor = Anchor_ID);


        def Set_Pos_AutoFollow_to_Widget(self, Widget_From_Anchor_ID:Anchor_enum, Widget_To, Widget_To_Anchor_ID:Anchor_Relative_enum, Offset_Anchor_X,  Offset_Anchor_Y):     

            # Функция устанавливаем автоматическое следование заданного угла одного Виджета за заданным углом друого виджета.

            # Widget_From                       - виджет которй должен следовать.
            # Widget_From_Anchor_ID             - угол-якорь виджета "Widget_From" которым он должен следовать за указанной позицией у виджета "Widget_To" в углке-якоре "Widget_To_Anchor_ID"
            # Widget_To                         - виджет за координатами которого должен следовать виджет "Widget_From"
            # Offset_Anchor_X и Offset_Anchor_Y - АБСОЛЮТНОЕ смещение смещение от координаты привязки, короче коррекитровка, если она нужна.


            relative_X, relative_Y = Widget_To_Anchor_ID.value;

            self.Obj.place(in_ = Widget_To,  relx = relative_X, rely = relative_Y, x=Offset_Anchor_X, y=Offset_Anchor_Y, anchor = Widget_From_Anchor_ID);

        def Set_Size_AutoFollow_to_Widget(self, Widget_To, Relative_Width, Relative_Height, Width_Offset, Height_Offset):
        
            # Функция устанавливаем автоматическое следование размера одного Виджета за размером друого виджета.
        
            # Widget_From    - виджет которй должен следовать.
            # Widget_To      - виджет за размерами которого должен следовать виджет "Widget_From"
            # Relative_Width - ОТНОСИТЕЛЬНЫЙ размер виджета "Widget_To" который будет автоматически передаватся на виджет "Widget_From". Вообщем Relative_Width = 1, то значит это Полная Ширина виджета "Widget_To", Relative_Width = 0.5 - половина Ширины вижета и так далее, то есть Ширина Виджета "Widget_From" всегда будет автоматически подстраиватся под указанную Ширину.
            # Relative_Height - тоже самое, что и "Relative_Width" - только для высоты.
            # Width_Offset, Height_Offset - это АБСОЛЮТНОЕ смешение в Ширине или Высоте - если нужна более точная настрока. Потому что в относительных процентах не всегда увилирно можно настроить.

            # Если один из Relative_Width или Relative_Height указаны = -1, то значит автоследование по этому параметру не будет ставится.
            
            
            if (Relative_Width != -1 and Relative_Height != -1):
                self.Obj.place(in_ = Widget_To, relwidth = Relative_Width, relheight = Relative_Height, width = Width_Offset, height = Height_Offset);
                return;

            if (Relative_Width == -1 and Relative_Height != -1):
                self.Obj.place(in_ = Widget_To, relheight = Relative_Height, height = Height_Offset);
                return;

            if (Relative_Height == -1 and Relative_Width != -1):
                self.Obj.place(in_ = Widget_To, relwidth = Relative_Width, width = Width_Offset);
                return;


        def Set_Font_Name(self, Font_Name:str):

            self.Font_Name = Font_Name;

            self.Obj.config(font=(Font_Name, self.Font_Size))

        def Set_Font_Size(self, Font_Size:int):

            self.Obj.config(font=(self.Font_Name, Font_Size));

            self.Font_Size = Font_Size;

    
        def GetDate_String(self)->str:
            return self.Obj.get();

        def GetDate_SplitString(self)->Tkinter_GUI__class.DateTime_struct:

            DateTime_string =  self.Obj.get();

            datetime_ = datetime.strptime(DateTime_string, self.Formate_Date_string);


            DateTime_struct_ = Tkinter_GUI__class.DateTime_struct();

            DateTime_struct_.Day   = f"{datetime_.day:02d}"            
            DateTime_struct_.Month = f"{datetime_.month:02d}"
            DateTime_struct_.Year  = f"{datetime_.year:04d}"
            #DateTime_struct_.Hour  = f"{datetime_.hour:02d}"
            #DateTime_struct_.Min   = f"{datetime_.minute:02d}"        # 02d - дополняет символ слева в случае, если к примеру значение минут будет 00, и если не указать оно сконвертируется в строку, как один 0.

            return DateTime_struct_;

        def Check(self)->bool:

            DateTime_string =  self.Obj.get();

            try:
                datetime_ = datetime.strptime(DateTime_string, self.Formate_Date_string)
                return True;
            except:
                return False;


        def Get__TOP_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y());
        
        def Get__TOP_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width(), self.Obj.winfo_y());
            
        def Get__BOTTOM_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height());
  
        def Get__BOTTOM_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width(), self.Obj.winfo_y() + self.Obj.winfo_height());

        def Get__CENTRE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width()/2, self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__TOP_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() +  self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__BOTTOM_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__LEFT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__RIGHT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);
       

        def Get__Size(self)->Tkinter_GUI__class.Size_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Size_struct(self.Obj.winfo_width(), self.Obj.winfo_height());

        #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------


        def _has_forbidden_in_selection(self):
            # Проверяем, есть ли в выделенном фрагменте запрещённые символы из "Prohibited_symbols"

            if self.Obj.selection_present():
                sel_start = self.Obj.index("sel.first")
                sel_end = self.Obj.index("sel.last")
                selected_text = self.Obj.get()[sel_start:sel_end]
                return any(ch in self.Prohibited_symbols for ch in selected_text)
            return False

        def _Check_Enter_Symv(self, event):

            text = self.Obj.get()
            index = self.Obj.index(tkinter.INSERT)

            if event.keysym == "BackSpace":
                if self.Obj.selection_present():
                    return "break" if self._has_forbidden_in_selection() else None
                if index == 0:
                    return "break"
                return "break" if text[index - 1] in self.Prohibited_symbols else None

            if event.keysym == "Delete":
                if self.Obj.selection_present():
                    return "break" if self._has_forbidden_in_selection() else None
                if index >= len(text):
                    return "break"
                return "break" if text[index] in self.Prohibited_symbols else None

            if event.keysym in ("Left", "Right", "Home", "End", "Tab"):
                return None

            if self.Obj.selection_present() and self._has_forbidden_in_selection():
                return "break"

            if event.char.isdigit():
                return None

            return "break"


    @dataclass(slots=True)
    class Label_Struct:
        Window_struct_ref:Tkinter_GUI__class.Window_struct = None;

        Name:str = "";
        Obj:tkinter.Label = field(default_factory=tkinter.Label);

        Font_Name:str = "Arial";
        Font_Size:int = 12;

        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------
        
        def Set_Size(self, Width:int, Height:int):

            self.Obj.place(width=Width, height=Height);

            self.Set_Font_Size(int(Height/2));

        def Set_AutoSize_by_Text(self):
            # Делает так, чтобы рамка вокруг текста сама автопостроилась под текст.
            self.Obj.place_configure(width="");

        def Set_Pos(self, X:int, Y:int, Anchor_ID:Anchor_enum):

            self.Obj.place(x=X, y=Y, anchor = Anchor_ID);


        def Set_Pos_AutoFollow_to_Widget(self, Widget_From_Anchor_ID:Anchor_enum, Widget_To, Widget_To_Anchor_ID:Anchor_Relative_enum, Offset_Anchor_X,  Offset_Anchor_Y):     

            # Функция устанавливаем автоматическое следование заданного угла одного Виджета за заданным углом друого виджета.

            # Widget_From                       - виджет которй должен следовать.
            # Widget_From_Anchor_ID             - угол-якорь виджета "Widget_From" которым он должен следовать за указанной позицией у виджета "Widget_To" в углке-якоре "Widget_To_Anchor_ID"
            # Widget_To                         - виджет за координатами которого должен следовать виджет "Widget_From"
            # Offset_Anchor_X и Offset_Anchor_Y - АБСОЛЮТНОЕ смещение смещение от координаты привязки, короче коррекитровка, если она нужна.


            relative_X, relative_Y = Widget_To_Anchor_ID.value;

            self.Obj.place(in_ = Widget_To,  relx = relative_X, rely = relative_Y, x=Offset_Anchor_X, y=Offset_Anchor_Y, anchor = Widget_From_Anchor_ID);

        def Set_Size_AutoFollow_to_Widget(self, Widget_To, Relative_Width, Relative_Height, Width_Offset, Height_Offset):
        
            # Функция устанавливаем автоматическое следование размера одного Виджета за размером друого виджета.
        
            # Widget_From    - виджет которй должен следовать.
            # Widget_To      - виджет за размерами которого должен следовать виджет "Widget_From"
            # Relative_Width - ОТНОСИТЕЛЬНЫЙ размер виджета "Widget_To" который будет автоматически передаватся на виджет "Widget_From". Вообщем Relative_Width = 1, то значит это Полная Ширина виджета "Widget_To", Relative_Width = 0.5 - половина Ширины вижета и так далее, то есть Ширина Виджета "Widget_From" всегда будет автоматически подстраиватся под указанную Ширину.
            # Relative_Height - тоже самое, что и "Relative_Width" - только для высоты.
            # Width_Offset, Height_Offset - это АБСОЛЮТНОЕ смешение в Ширине или Высоте - если нужна более точная настрока. Потому что в относительных процентах не всегда увилирно можно настроить.

            # Если один из Relative_Width или Relative_Height указаны = -1, то значит автоследование по этому параметру не будет ставится.
            
            
            if (Relative_Width != -1 and Relative_Height != -1):
                self.Obj.place(in_ = Widget_To, relwidth = Relative_Width, relheight = Relative_Height, width = Width_Offset, height = Height_Offset);
                return;

            if (Relative_Width == -1 and Relative_Height != -1):
                self.Obj.place(in_ = Widget_To, relheight = Relative_Height, height = Height_Offset);
                return;

            if (Relative_Height == -1 and Relative_Width != -1):
                self.Obj.place(in_ = Widget_To, relwidth = Relative_Width, width = Width_Offset);
                return;


        def Set_Text(self, Label_Text:str):

            self.Obj.config(text=Label_Text);

        def Set_Background_Color(self, Color:str):

            self.Obj.config(bg=Color);

        def Set_Text_Color(self, Color:str):

            self.Obj.config(fg=Color);


        def Set_Font_Name(self, Font_Name:str):

            self.Font_Name = Font_Name;

            self.Obj.config(font=(Font_Name, self.Font_Size))

        def Set_Font_Size(self, Font_Size:int):

            self.Obj.config(font=(self.Font_Name, Font_Size));

            self.Font_Size = Font_Size;


        def Set_HyperLink(self, URL:str):

            # Делает текст Лейбла - гипеорссылкой, при клике на которуб она открывается в Брузере, который установлен у Пользователя в системе, как оснвоной.

            self.Obj.config(fg="blue", cursor="hand2");  # Устанавливаем увет текста на синий, и вид курсорама мыши при навеедении на текст-гиперссылки.

            self.Obj.bind("<Button-1>", lambda e, URL=URL: webbrowser.open(URL));   # Устанавливам что бы при Левом Клике мыши по тексту-ссылке - она открывалась в Браузере Пользователя. 


        def Get__TOP_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y());
   
        def Get__TOP_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width(), self.Obj.winfo_y());
            
        def Get__BOTTOM_LEFT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height());

        def Get__BOTTOM_RIGHT_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width(), self.Obj.winfo_y() + self.Obj.winfo_height());
        
        def Get__CENTRE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width()/2, self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__TOP_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() +  self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__BOTTOM_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x() + self.Obj.winfo_width()/2, self.Obj.winfo_y());

        def Get__LEFT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);

        def Get__RIGHT_MIDDLE_Pos(self)->Tkinter_GUI__class.Pos_struct:

            self.Window_struct_ref.Obj.update()

            return Tkinter_GUI__class.Pos_struct(self.Obj.winfo_x(), self.Obj.winfo_y() + self.Obj.winfo_height()/2);
       
        def Get__Size(self)->Tkinter_GUI__class.Size_struct:

            self.Window_struct_ref.Obj.update();

            return Tkinter_GUI__class.Size_struct(self.Obj.winfo_width(), self.Obj.winfo_height());

        #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------

    @dataclass(slots=True)
    class Classic_Menu_Struct:
        Window_struct_ref:Tkinter_GUI__class.Window_struct = None;

        Name:str = "";
        Obj:tkinter.Menu = field(default_factory=tkinter.Menu);

        Font_Name:str = "Arial";
        Font_Size:int = 12;
    
        Background_Color:str = None;   # None - значит цвет не переопределён (используется дефолтный системный)
        Text_Color:str       = None;

        Dict_Callbacks_for_End_Element:dict = field(default_factory=dict);          # Хранилище колбеков для конечных элементов: ключ - tuple(путь), значение - список Callback_struct

        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------
           
        def Set_Background_Color(self, Color:str):
            # Устанавливает цвет на все элементы меню (и текущие, и все будущие добавленные - хранится в self.Background_Color).
            self.Background_Color = Color;

            for menu_widget in self._Collect_All_Menus(self.Obj):
                menu_widget.configure(bg=Color);

        def Set_Text_Color(self, Color:str):
            # Устанавливает цвет текста на все элементы меню (текущие и будущие).
            self.Text_Color = Color;

            for menu_widget in self._Collect_All_Menus(self.Obj):
                menu_widget.configure(fg=Color);

        def Set_Font_Name(self, Font_Name:str):
            # Устанавливает шрифт на все элементы меню (текущие и будущие).
            self.Font_Name = Font_Name;

            for menu_widget in self._Collect_All_Menus(self.Obj):
                menu_widget.configure(font=(self.Font_Name, self.Font_Size));

        def Set_Font_Size(self, Font_Size:int):
            # Устанавливает размер шрифта на все элементы меню (текущие и будущие).
            self.Font_Size = Font_Size;

            for menu_widget in self._Collect_All_Menus(self.Obj):
                menu_widget.configure(font=(self.Font_Name, self.Font_Size));

        def Add_HighLevel_Element(self, List_elements:list[str], Pos:int):
            # Добавляет элементы в самое верхнее меню (без родителя).
            self._Insert_Elements(self.Obj, List_elements, Pos);

        def Add_Child_Element(self, List_Dir_to_Parent_Element:list[str], List_Add_Element:list[str], Pos:int):
            # Добавляет дочерние элементы к указанному родителю. Если родитель по пути ещё был "листом" -
            # автоматически превратится в cascade.
            Parent_Menu = self._Navigate_and_Ensure_Cascades(List_Dir_to_Parent_Element);
            self._Insert_Elements(Parent_Menu, List_Add_Element, Pos);

        def Set_Menu_from_Dict(self, Dictonary_tree:dict):
            # Полностью пересоздаёт структуру меню с нуля из словаря. Удаляет всё, что было раньше.
            All_Menus = self._Collect_All_Menus(self.Obj);

            # Удаляем под-меню в обратном порядке (от листьев к корню), чтобы не пытаться уничтожить уже уничтоженный виджет.
            for menu_widget in reversed(All_Menus[1:]):
                try:
                    menu_widget.destroy();
                except tkinter.TclError:
                    pass;

            self.Obj.delete(0, "end");
            self.Dict_Callbacks_for_End_Element.clear();

            self._Build_From_Dict(self.Obj, Dictonary_tree);

        def Delete_Element(self, List_Dir_to_Element:list[str])->None|str:
            # Удаляет элемент. Если у него есть дети - удаляется всё поддерево.
            Parent_Menu = self._Navigate_to_Menu(List_Dir_to_Element[:-1]);
            Label       = List_Dir_to_Element[-1];

            idx = Parent_Menu.index(Label);
            if idx is None:
                return (f"Элемент '{Label}' не найден.");

            Item_Type = Parent_Menu.type(idx);

            if Item_Type == "cascade":
                Submenu_Name = Parent_Menu.entrycget(idx, "menu");
                if Submenu_Name:
                    Submenu_Obj = Parent_Menu.nametowidget(Submenu_Name);
                    Submenu_Obj.destroy();

            Parent_Menu.delete(idx);

            # Чистим колбеки, привязанные к этому элементу и (если это был cascade) ко всем его потомкам.
            Path_Prefix = tuple(List_Dir_to_Element);
            for key in list(self.Dict_Callbacks_for_End_Element.keys()):
                if key[:len(Path_Prefix)] == Path_Prefix:
                    del self.Dict_Callbacks_for_End_Element[key];

            return None;

        def Set_Active_Element(self, List_Dir__to_Element:list[str], Flag:bool)->None|str:
            # Делает активным/неактивным элемент. Если у него есть дети - применяется ко всему поддереву.
            Parent_Menu = self._Navigate_to_Menu(List_Dir__to_Element[:-1]);
            Label       = List_Dir__to_Element[-1];

            idx = Parent_Menu.index(Label);
            if idx is None:
                return (f"Элемент '{Label}' не найден.");

            State = "normal" if Flag == True else "disabled";

            Parent_Menu.entryconfigure(idx, state=State);

            if Parent_Menu.type(idx) == "cascade":
                Submenu_Name = Parent_Menu.entrycget(idx, "menu");
                if Submenu_Name:
                    Submenu_Obj = Parent_Menu.nametowidget(Submenu_Name);
                    self._Set_All_States_Recursive(Submenu_Obj, State);

            return None;

        def Set_Separator(self, List_add_Separator)->None|str:
            # Принимает как один Menu_Separator_struct, так и list[Menu_Separator_struct].
            if isinstance(List_add_Separator, Tkinter_GUI__class.Menu_Separator_struct):
                List_add_Separator = [List_add_Separator];

            for Sep_Item in List_add_Separator:
                Target_Menu = self._Navigate_to_Menu(Sep_Item.List_Path_to_Parent_element);

                idx = Target_Menu.index(Sep_Item.Element_name);
                if idx is None:
                    return (f"Элемент '{Sep_Item.Element_name}' не найден.");

                Offset = 1 if Sep_Item.Before_After_Flag == Tkinter_GUI__class.Before_After_enum.After else 0;
                Insert_Index = idx + Offset;

                Target_Menu.insert_separator(Insert_Index);

            return None;

        def Add_Callaback_for_End_Element(self, List_Path_to_End_Element, user_Callback, List_any:list[any])->None|str:
            # Добавляет колбек к конечному (не-cascade) элементу меню. Можно вызывать несколько раз для
            # одного и того же пути - все колбеки будут вызваны по очереди (по аналогии с кнопкой).
            Parent_Menu = self._Navigate_to_Menu(List_Path_to_End_Element[:-1]);
            Label       = List_Path_to_End_Element[-1];

            idx = Parent_Menu.index(Label);
            if idx is None:
                raise ValueError(f"Элемент '{Label}' не найден.");

            if Parent_Menu.type(idx) == "cascade":
                return (f"Элемент '{Label}' является родителем (подменю) - колбек можно назначать только конечным элементам.");

            Path_Key = tuple(List_Path_to_End_Element);

            if Path_Key not in self.Dict_Callbacks_for_End_Element:
                self.Dict_Callbacks_for_End_Element[Path_Key] = [];

            self.Dict_Callbacks_for_End_Element[Path_Key].append(Tkinter_GUI__class.Callback_struct(user_Callback, List_any));

            def _on_click(path_key=Path_Key):
                for callback_item in self.Dict_Callbacks_for_End_Element[path_key]:
                    callback_item.Callback(self, callback_item.List_any);

            if len(self.Dict_Callbacks_for_End_Element[Path_Key]) == 1:
                Parent_Menu.entryconfigure(idx, command=_on_click);


            return None;
        #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------

        #---------------------------------------------------------------PRIVATE:-------------------------------------------------------------------

        def _Apply_Style(self, Menu_Widget:tkinter.Menu):
            # Применяет ТЕКУЩИЕ сохранённые настройки стиля к ОДНОМУ конкретному виджету меню (используется при создании нового подменю).
            if self.Background_Color is not None:
                Menu_Widget.configure(bg=self.Background_Color);
            if self.Text_Color is not None:
                Menu_Widget.configure(fg=self.Text_Color);
            Menu_Widget.configure(font=(self.Font_Name, self.Font_Size));

        def _Collect_All_Menus(self, Menu_Obj:tkinter.Menu)->list:
            # Рекурсивно собирает САМ Menu_Obj и все вложенные под-меню (cascade) в один плоский список.
            Result_List = [Menu_Obj];

            try:
                Last_Index = Menu_Obj.index("end");
            except tkinter.TclError:
                Last_Index = None;

            if Last_Index is not None:
                for i in range(Last_Index + 1):
                    try:
                        Item_Type = Menu_Obj.type(i);
                    except tkinter.TclError:
                        continue;

                    if Item_Type == "cascade":
                        Submenu_Name = Menu_Obj.entrycget(i, "menu");
                        if Submenu_Name:
                            Submenu_Obj = Menu_Obj.nametowidget(Submenu_Name);
                            Result_List.extend(self._Collect_All_Menus(Submenu_Obj));

            return Result_List;

        def _Get_Submenu_Existing(self, Menu_Obj:tkinter.Menu, Label:str)->tkinter.Menu:
            # Находит СУЩЕСТВУЮЩЕЕ под-меню по label. Если элемента нет или он не cascade - кидает ошибку.
            try:
                idx = Menu_Obj.index(Label);
            except tkinter.TclError:
                idx = None;

            if idx is None:
                raise ValueError(f"Элемент '{Label}' не найден.");

            if Menu_Obj.type(idx) != "cascade":
                raise ValueError(f"Элемент '{Label}' не является родителем (нет вложенных элементов).");

            Submenu_Name = Menu_Obj.entrycget(idx, "menu");
            if not Submenu_Name:
                raise ValueError(f"Элемент '{Label}' не является родителем (нет вложенных элементов).");

            return Menu_Obj.nametowidget(Submenu_Name);

        def _Navigate_to_Menu(self, List_Path:list[str])->tkinter.Menu:
            # Проходит по пути СУЩЕСТВУЮЩИХ родителей и возвращает конечное под-меню. Пустой путь = корневое меню (self.Obj).
            current = self.Obj;
            for label in List_Path:
                current = self._Get_Submenu_Existing(current, label);
            return current;

        def _Get_or_Create_Submenu(self, Menu_Obj:tkinter.Menu, Label:str)->tkinter.Menu:
            # Находит под-меню по label. Если элемент существует, но это обычный "лист" (command) -
            # автоматически превращает его в cascade с новым под-меню, СОХРАНЯЯ его позицию.
            try:
                idx = Menu_Obj.index(Label);
            except tkinter.TclError:
                idx = None;

            if idx is None:
                raise ValueError(f"Элемент '{Label}' не найден. Сначала добавьте его через Add_HighLevel_Element/Add_Child_Element.");

            Item_Type = Menu_Obj.type(idx);

            if Item_Type == "cascade":
                Submenu_Name = Menu_Obj.entrycget(idx, "menu");
                if Submenu_Name:
                    return Menu_Obj.nametowidget(Submenu_Name);

            # Превращаем лист в cascade:
            Menu_Obj.delete(idx);

            New_Submenu = tkinter.Menu(Menu_Obj, tearoff=0);
            self._Apply_Style(New_Submenu);

            Menu_Obj.insert_cascade(idx, label=Label, menu=New_Submenu);

            return New_Submenu;

        def _Navigate_and_Ensure_Cascades(self, List_Path:list[str])->tkinter.Menu:
            # Как _Navigate_to_Menu, но при необходимости конвертирует "листы" в cascade по пути.
            current = self.Obj;
            for label in List_Path:
                current = self._Get_or_Create_Submenu(current, label);
            return current;

        def _Insert_Elements(self, Menu_Obj:tkinter.Menu, List_Elements:list[str], Pos:int):
            # Вставляет список текстовых элементов как обычные "command" (без колбека) в указанную позицию.
            if Pos == -1:
                for label in List_Elements:
                    Menu_Obj.add_command(label=label);
            else:
                for offset, label in enumerate(List_Elements):
                    Menu_Obj.insert_command(Pos + offset, label=label);

        def _Set_All_States_Recursive(self, Menu_Obj:tkinter.Menu, State:str):
            try:
                Last_Index = Menu_Obj.index("end");
            except tkinter.TclError:
                Last_Index = None;

            if Last_Index is None:
                return;

            for i in range(Last_Index + 1):
                Item_Type = Menu_Obj.type(i);

                if Item_Type == "separator":
                    continue;

                Menu_Obj.entryconfigure(i, state=State);

                if Item_Type == "cascade":
                    Submenu_Name = Menu_Obj.entrycget(i, "menu");
                    if Submenu_Name:
                        Submenu_Obj = Menu_Obj.nametowidget(Submenu_Name);
                        self._Set_All_States_Recursive(Submenu_Obj, State);

        def _Build_From_Dict(self, Menu_Obj:tkinter.Menu, Tree:dict):
            for key, value in Tree.items():
                if isinstance(value, dict):
                    Submenu = tkinter.Menu(Menu_Obj, tearoff=0);
                    self._Apply_Style(Submenu);
                    Menu_Obj.add_cascade(label=key, menu=Submenu);
                    self._Build_From_Dict(Submenu, value);

                elif isinstance(value, list):
                    Submenu = tkinter.Menu(Menu_Obj, tearoff=0);
                    self._Apply_Style(Submenu);
                    Menu_Obj.add_cascade(label=key, menu=Submenu);
                    for leaf_label in value:
                        Submenu.add_command(label=leaf_label);
                else:
                    raise TypeError(f"Значение для ключа '{key}' должно быть dict или list[str], получено {type(value)}");

        #--------------------------------------------------------------PRIVATE-методы:Конец----------------------------------------------------------

    @dataclass(slots=True)
    class Context_Menu_Struct:

        # !!!!! Днная структуру для контексного меню - на 100% повтряет структру "Classic_Menu_Struct" - для обычноого окнонного меню, разница в создании между Классическим и Контекснм меню - всего в пару строк в методах: Add__Context_Menu и Add__Classic_Menu и в том, что в структуре "Window_struct" - Поле под Классическое меню - это один обьект стукртуры "Classic_Menu" а под Context_Menu - это список, так как в окне невозможно доавбить более одного меню, и нет смысла хрнаить список множества этих меню(хотя можно было бы сделать и список) - вообщем можно было без проблем бы обьеденить эти две структуры в одну, чтобы не было дубоирование - но мне лень, так нагляднее.

        Window_struct_ref:Tkinter_GUI__class.Window_struct = None;

        Name:str = "";
        Obj:tkinter.Menu = field(default_factory=tkinter.Menu);

        Font_Name:str = "Arial";
        Font_Size:int = 12;
    
        Background_Color:str = None;   # None - значит цвет не переопределён (используется дефолтный системный)
        Text_Color:str       = None;

        Dict_Callbacks_for_End_Element:dict = field(default_factory=dict);          # Хранилище колбеков для конечных элементов: ключ - tuple(путь), значение - список Callback_struct

        #--------------------------------------------------------------PUBLIC-методы:Начало---------------------------------------------------------
           
        def Set_Show_and_Pos(self, X:int, Y:int):

            self.Obj.post(x=self.Window_struct_ref.Get__TOP_LEFT_Pos().x + X, y=self.Window_struct_ref.Get__TOP_LEFT_Pos().y + Y);

        def Set_Background_Color(self, Color:str):
            # Устанавливает цвет на все элементы меню (и текущие, и все будущие добавленные - хранится в self.Background_Color).
            self.Background_Color = Color;

            for menu_widget in self._Collect_All_Menus(self.Obj):
                menu_widget.configure(bg=Color);

        def Set_Text_Color(self, Color:str):
            # Устанавливает цвет текста на все элементы меню (текущие и будущие).
            self.Text_Color = Color;

            for menu_widget in self._Collect_All_Menus(self.Obj):
                menu_widget.configure(fg=Color);

        def Set_Font_Name(self, Font_Name:str):
            # Устанавливает шрифт на все элементы меню (текущие и будущие).
            self.Font_Name = Font_Name;

            for menu_widget in self._Collect_All_Menus(self.Obj):
                menu_widget.configure(font=(self.Font_Name, self.Font_Size));

        def Set_Font_Size(self, Font_Size:int):
            # Устанавливает размер шрифта на все элементы меню (текущие и будущие).
            self.Font_Size = Font_Size;

            for menu_widget in self._Collect_All_Menus(self.Obj):
                menu_widget.configure(font=(self.Font_Name, self.Font_Size));

        def Add_HighLevel_Element(self, List_elements:list[str], Pos:int):
            # Добавляет элементы в самое верхнее меню (без родителя).
            self._Insert_Elements(self.Obj, List_elements, Pos);

        def Add_Child_Element(self, List_Dir_to_Parent_Element:list[str], List_Add_Element:list[str], Pos:int):
            # Добавляет дочерние элементы к указанному родителю. Если родитель по пути ещё был "листом" -
            # автоматически превратится в cascade.
            Parent_Menu = self._Navigate_and_Ensure_Cascades(List_Dir_to_Parent_Element);
            self._Insert_Elements(Parent_Menu, List_Add_Element, Pos);

        def Set_Menu_from_Dict(self, Dictonary_tree:dict):
            # Полностью пересоздаёт структуру меню с нуля из словаря. Удаляет всё, что было раньше.
            All_Menus = self._Collect_All_Menus(self.Obj);

            # Удаляем под-меню в обратном порядке (от листьев к корню), чтобы не пытаться уничтожить уже уничтоженный виджет.
            for menu_widget in reversed(All_Menus[1:]):
                try:
                    menu_widget.destroy();
                except tkinter.TclError:
                    pass;

            self.Obj.delete(0, "end");
            self.Dict_Callbacks_for_End_Element.clear();

            self._Build_From_Dict(self.Obj, Dictonary_tree);

        def Delete_Element(self, List_Dir_to_Element:list[str])->None|str:
            # Удаляет элемент. Если у него есть дети - удаляется всё поддерево.
            Parent_Menu = self._Navigate_to_Menu(List_Dir_to_Element[:-1]);
            Label       = List_Dir_to_Element[-1];

            idx = Parent_Menu.index(Label);
            if idx is None:
                return (f"Элемент '{Label}' не найден.");

            Item_Type = Parent_Menu.type(idx);

            if Item_Type == "cascade":
                Submenu_Name = Parent_Menu.entrycget(idx, "menu");
                if Submenu_Name:
                    Submenu_Obj = Parent_Menu.nametowidget(Submenu_Name);
                    Submenu_Obj.destroy();

            Parent_Menu.delete(idx);

            # Чистим колбеки, привязанные к этому элементу и (если это был cascade) ко всем его потомкам.
            Path_Prefix = tuple(List_Dir_to_Element);
            for key in list(self.Dict_Callbacks_for_End_Element.keys()):
                if key[:len(Path_Prefix)] == Path_Prefix:
                    del self.Dict_Callbacks_for_End_Element[key];

            return None;

        def Set_Active_Element(self, List_Dir__to_Element:list[str], Flag:bool)->None|str:
            # Делает активным/неактивным элемент. Если у него есть дети - применяется ко всему поддереву.
            Parent_Menu = self._Navigate_to_Menu(List_Dir__to_Element[:-1]);
            Label       = List_Dir__to_Element[-1];

            idx = Parent_Menu.index(Label);
            if idx is None:
                return (f"Элемент '{Label}' не найден.");

            State = "normal" if Flag == True else "disabled";

            Parent_Menu.entryconfigure(idx, state=State);

            if Parent_Menu.type(idx) == "cascade":
                Submenu_Name = Parent_Menu.entrycget(idx, "menu");
                if Submenu_Name:
                    Submenu_Obj = Parent_Menu.nametowidget(Submenu_Name);
                    self._Set_All_States_Recursive(Submenu_Obj, State);

            return None;

        def Set_Separator(self, List_add_Separator)->None|str:
            # Принимает как один Menu_Separator_struct, так и list[Menu_Separator_struct].
            if isinstance(List_add_Separator, Tkinter_GUI__class.Menu_Separator_struct):
                List_add_Separator = [List_add_Separator];

            for Sep_Item in List_add_Separator:
                Target_Menu = self._Navigate_to_Menu(Sep_Item.List_Path_to_Parent_element);

                idx = Target_Menu.index(Sep_Item.Element_name);
                if idx is None:
                    return (f"Элемент '{Sep_Item.Element_name}' не найден.");

                Offset = 1 if Sep_Item.Before_After_Flag == Tkinter_GUI__class.Before_After_enum.After else 0;
                Insert_Index = idx + Offset;

                Target_Menu.insert_separator(Insert_Index);

            return None;

        def Add_Callaback_for_End_Element(self, List_Path_to_End_Element, user_Callback, List_any:list[any])->None|str:
            # Добавляет колбек к конечному (не-cascade) элементу меню. Можно вызывать несколько раз для
            # одного и того же пути - все колбеки будут вызваны по очереди (по аналогии с кнопкой).
            Parent_Menu = self._Navigate_to_Menu(List_Path_to_End_Element[:-1]);
            Label       = List_Path_to_End_Element[-1];

            idx = Parent_Menu.index(Label);
            if idx is None:
                raise ValueError(f"Элемент '{Label}' не найден.");

            if Parent_Menu.type(idx) == "cascade":
                return (f"Элемент '{Label}' является родителем (подменю) - колбек можно назначать только конечным элементам.");

            Path_Key = tuple(List_Path_to_End_Element);

            if Path_Key not in self.Dict_Callbacks_for_End_Element:
                self.Dict_Callbacks_for_End_Element[Path_Key] = [];

            self.Dict_Callbacks_for_End_Element[Path_Key].append(Tkinter_GUI__class.Callback_struct(user_Callback, List_any));

            def _on_click(path_key=Path_Key):
                for callback_item in self.Dict_Callbacks_for_End_Element[path_key]:
                    callback_item.Callback(self, callback_item.List_any);

            if len(self.Dict_Callbacks_for_End_Element[Path_Key]) == 1:
                Parent_Menu.entryconfigure(idx, command=_on_click);


            return None;
        #--------------------------------------------------------------PUBLIC-методы:Конец---------------------------------------------------------

        #---------------------------------------------------------------PRIVATE:-------------------------------------------------------------------

        def _Apply_Style(self, Menu_Widget:tkinter.Menu):
            # Применяет ТЕКУЩИЕ сохранённые настройки стиля к ОДНОМУ конкретному виджету меню (используется при создании нового подменю).
            if self.Background_Color is not None:
                Menu_Widget.configure(bg=self.Background_Color);
            if self.Text_Color is not None:
                Menu_Widget.configure(fg=self.Text_Color);
            Menu_Widget.configure(font=(self.Font_Name, self.Font_Size));

        def _Collect_All_Menus(self, Menu_Obj:tkinter.Menu)->list:
            # Рекурсивно собирает САМ Menu_Obj и все вложенные под-меню (cascade) в один плоский список.
            Result_List = [Menu_Obj];

            try:
                Last_Index = Menu_Obj.index("end");
            except tkinter.TclError:
                Last_Index = None;

            if Last_Index is not None:
                for i in range(Last_Index + 1):
                    try:
                        Item_Type = Menu_Obj.type(i);
                    except tkinter.TclError:
                        continue;

                    if Item_Type == "cascade":
                        Submenu_Name = Menu_Obj.entrycget(i, "menu");
                        if Submenu_Name:
                            Submenu_Obj = Menu_Obj.nametowidget(Submenu_Name);
                            Result_List.extend(self._Collect_All_Menus(Submenu_Obj));

            return Result_List;

        def _Get_Submenu_Existing(self, Menu_Obj:tkinter.Menu, Label:str)->tkinter.Menu:
            # Находит СУЩЕСТВУЮЩЕЕ под-меню по label. Если элемента нет или он не cascade - кидает ошибку.
            try:
                idx = Menu_Obj.index(Label);
            except tkinter.TclError:
                idx = None;

            if idx is None:
                raise ValueError(f"Элемент '{Label}' не найден.");

            if Menu_Obj.type(idx) != "cascade":
                raise ValueError(f"Элемент '{Label}' не является родителем (нет вложенных элементов).");

            Submenu_Name = Menu_Obj.entrycget(idx, "menu");
            if not Submenu_Name:
                raise ValueError(f"Элемент '{Label}' не является родителем (нет вложенных элементов).");

            return Menu_Obj.nametowidget(Submenu_Name);

        def _Navigate_to_Menu(self, List_Path:list[str])->tkinter.Menu:
            # Проходит по пути СУЩЕСТВУЮЩИХ родителей и возвращает конечное под-меню. Пустой путь = корневое меню (self.Obj).
            current = self.Obj;
            for label in List_Path:
                current = self._Get_Submenu_Existing(current, label);
            return current;

        def _Get_or_Create_Submenu(self, Menu_Obj:tkinter.Menu, Label:str)->tkinter.Menu:
            # Находит под-меню по label. Если элемент существует, но это обычный "лист" (command) -
            # автоматически превращает его в cascade с новым под-меню, СОХРАНЯЯ его позицию.
            try:
                idx = Menu_Obj.index(Label);
            except tkinter.TclError:
                idx = None;

            if idx is None:
                raise ValueError(f"Элемент '{Label}' не найден. Сначала добавьте его через Add_HighLevel_Element/Add_Child_Element.");

            Item_Type = Menu_Obj.type(idx);

            if Item_Type == "cascade":
                Submenu_Name = Menu_Obj.entrycget(idx, "menu");
                if Submenu_Name:
                    return Menu_Obj.nametowidget(Submenu_Name);

            # Превращаем лист в cascade:
            Menu_Obj.delete(idx);

            New_Submenu = tkinter.Menu(Menu_Obj, tearoff=0);
            self._Apply_Style(New_Submenu);

            Menu_Obj.insert_cascade(idx, label=Label, menu=New_Submenu);

            return New_Submenu;

        def _Navigate_and_Ensure_Cascades(self, List_Path:list[str])->tkinter.Menu:
            # Как _Navigate_to_Menu, но при необходимости конвертирует "листы" в cascade по пути.
            current = self.Obj;
            for label in List_Path:
                current = self._Get_or_Create_Submenu(current, label);
            return current;

        def _Insert_Elements(self, Menu_Obj:tkinter.Menu, List_Elements:list[str], Pos:int):
            # Вставляет список текстовых элементов как обычные "command" (без колбека) в указанную позицию.
            if Pos == -1:
                for label in List_Elements:
                    Menu_Obj.add_command(label=label);
            else:
                for offset, label in enumerate(List_Elements):
                    Menu_Obj.insert_command(Pos + offset, label=label);

        def _Set_All_States_Recursive(self, Menu_Obj:tkinter.Menu, State:str):
            try:
                Last_Index = Menu_Obj.index("end");
            except tkinter.TclError:
                Last_Index = None;

            if Last_Index is None:
                return;

            for i in range(Last_Index + 1):
                Item_Type = Menu_Obj.type(i);

                if Item_Type == "separator":
                    continue;

                Menu_Obj.entryconfigure(i, state=State);

                if Item_Type == "cascade":
                    Submenu_Name = Menu_Obj.entrycget(i, "menu");
                    if Submenu_Name:
                        Submenu_Obj = Menu_Obj.nametowidget(Submenu_Name);
                        self._Set_All_States_Recursive(Submenu_Obj, State);

        def _Build_From_Dict(self, Menu_Obj:tkinter.Menu, Tree:dict):
            for key, value in Tree.items():
                if isinstance(value, dict):
                    Submenu = tkinter.Menu(Menu_Obj, tearoff=0);
                    self._Apply_Style(Submenu);
                    Menu_Obj.add_cascade(label=key, menu=Submenu);
                    self._Build_From_Dict(Submenu, value);

                elif isinstance(value, list):
                    Submenu = tkinter.Menu(Menu_Obj, tearoff=0);
                    self._Apply_Style(Submenu);
                    Menu_Obj.add_cascade(label=key, menu=Submenu);
                    for leaf_label in value:
                        Submenu.add_command(label=leaf_label);
                else:
                    raise TypeError(f"Значение для ключа '{key}' должно быть dict или list[str], получено {type(value)}");

        #--------------------------------------------------------------PRIVATE-методы:Конец----------------------------------------------------------





    def __init__(self):
        self.List_Window:list[Tkinter_GUI__class.Window_struct] = [];



    def Call_MessageBox(self, Title_Name:str, Text:str):
        messagebox.showinfo(Title_Name, Text);


    #---------------------------------------------------------------------------------Window_Методы:Начало------------------------------------------------------------------------
    def Add_window(self, Window_Name:str, Window_Title:str,  Width:int, Height:int)->Tkinter_GUI__class.Window_struct:
        
        self.List_Window.append(Tkinter_GUI__class.Window_struct());

        Window_struct = self.List_Window[-1];

        Window_struct.Window_Name = Window_Name;

        Window_struct.Tkinter_GUI__Obj = self;


        Window_struct.Obj.title(Window_Title);
        Window_struct.Obj.geometry(f"{Width}x{Height}");  # Размер окна


        

        return self.List_Window[-1];

    def Get__Window_Struct_by_Name(self, Window_Name:str)->Tkinter_GUI__class.Window_struct | None:

        for item in self.List_Window:
            if (item.Window_Name == Window_Name):
                return item;

        return None;
    #---------------------------------------------------------------------------------Window_Методы:Конец------------------------------------------------------------------------

    #---------------------------------------------------------------------------------Button_Методы:Начало------------------------------------------------------------------------

    def Add__Button(self, Window_struct:Tkinter_GUI__class.Window_struct, Button_Name:str)->Tkinter_GUI__class.Button_Struct:

        Window_struct.List_Buttons.append(Tkinter_GUI__class.Button_Struct());

        Button_struct      = Window_struct.List_Buttons[-1];

        Button_struct.Name      = Button_Name;

        Button_struct.Obj  = tkinter.Button(Window_struct.Obj); # Создаем и Привязываем Кнопку к кокнетному окну.

        Button_struct.Window_struct_ref = Window_struct;

        return Button_struct;

    def Get__Button_Struct_by_Name(self, Window_Name:str, Button_Name:str)->Tkinter_GUI__class.Window_struct | None:

        Window_struct:Tkinter_GUI__class.Window_struct = self.Get__Window_Struct_by_Name(Window_Name);

        for item in Window_struct.List_Buttons:
            if (item.Name == Button_Name):
                return item;
        return None;

    #---------------------------------------------------------------------------------Button_Методы:Конец------------------------------------------------------------------------

    #---------------------------------------------------------------------------------Listbox_Методы:Начало------------------------------------------------------------------------

    def Add__Listbox(self, Window_struct:Tkinter_GUI__class.Window_struct, Listbox_Name:str)->Tkinter_GUI__class.Listbox_Struct:


        #-------------------------------------------------------------------------------
        Window_struct.List_Listbox.append(Tkinter_GUI__class.Listbox_Struct());

        Listbox_struct               = Window_struct.List_Listbox[-1];

        Listbox_struct.Name          = Listbox_Name;

        Listbox_struct.Container     = tkinter.Frame(Window_struct.Obj, borderwidth=1, relief="solid");

        Listbox_struct.Obj           = tkinter.Listbox(Listbox_struct.Container, borderwidth=0, highlightthickness=0); # Создаем и Привязываем Кнопку к кокнетному окну.

        Listbox_struct.Window_struct_ref = Window_struct;

        Listbox_struct.Obj.grid(row=0, column=0, sticky="nsew");   # nsew - Растянуть виджет по всему "Container".  row=0, column=0 - короче - это мы как-бы доавбляем условно первый квадратик "сетки" в Контейнер(при создании виджета за место Окна указывается Container). То есть Контейнер можно представмть как Ексель табилцу, 0,0 - это первая ячейка, в которую и помещаем сам виджет. То есть строка и колонка. К примеру Вертикальный и Горизонтальный скроллбары ниже добавим как: Вертикальный, как таже 0-строка, но уже 1-колонка, и Горизонтальный - как 1-строка, но 0 колонка. 
        #-------------------------------------------------------------------------------



        #--------------------------------------Создаем Scrollbar:-----------------------------------------     
        # Вертикальный:
        Listbox_struct.V_scroll_obj = tkinter.Scrollbar(Listbox_struct.Container, orient=tkinter.VERTICAL, command=Listbox_struct.Obj.yview);
        Listbox_struct.Obj.config(yscrollcommand=Listbox_struct.V_scroll_obj.set);     

        # Вертикальный:
        Listbox_struct.H_scroll_obj = tkinter.Scrollbar(Listbox_struct.Container, orient=tkinter.HORIZONTAL, command=Listbox_struct.Obj.xview);
        Listbox_struct.Obj.config(xscrollcommand=Listbox_struct.H_scroll_obj.set);


        Listbox_struct.V_scroll_obj.grid(row=0, column=1, sticky="ns");     # "ns" - прилипнуть к северу и югу (растянуть по вертикали, ширина не меняется);  row=0, column=1 - читать выше в "Listbox_struct.Obj.grid(row=0, column=0, sticky="nsew")"
        Listbox_struct.H_scroll_obj.grid(row=1, column=0, sticky="ew");     # "ew" - прилипнуть к востоку и западу (растянуть по горизонтали, высота не меняется)
        #-----------------------------------------------------------------------------------------------


        #------------------------------------
        Listbox_struct.Container.grid_rowconfigure(0,    weight=1);  # Короче - эта штука гооврит, чтобы ТО ЧТО что мы поместили в строку 0, то есть это сам виджет и Горизонтальный скролл - всегда автоматически полность растягивался на ширину Контейнера при измении его размера или чуть точнее, чтобы обьект в строке 0 - при изменении размера Конктейнера вснда растягвался на изменившееся достйпный размер внутри конейнереа. Доступный - значит, что к примеру у насв Контейнере есть колонка 1 с V-скроллбаром, и так как на него мы ни каких весов не ставили, то его размер будет постоянным при изменеии размера Контейнера и что он берет на себя часть дсотупного пространства Контейнера и строке 0 - эта часть НЕ принадлежит.
        Listbox_struct.Container.grid_columnconfigure(0, weight=1);  # Вообщем все тоже самое, но косаемо Столбца 0.
        #------------------------------------



        return Listbox_struct;

    def Get__Listbox_Struct_by_Name(self, Window_Name:str, Listbox_Name:str)->Tkinter_GUI__class.Listbox_struct | None:

        Window_struct:Tkinter_GUI__class.Window_struct = self.Get__Window_Struct_by_Name(Window_Name);

        for item in Window_struct.List_Listbox:
            if (item.Name == Listbox_Name):
                return item;
        return None;

    #---------------------------------------------------------------------------------Listbox_Методы:Конец------------------------------------------------------------------------

    #---------------------------------------------------------------------------------Tree_Методы:Начало------------------------------------------------------------------------

    def Add__Treeview(self, Window_struct:Tkinter_GUI__class.Window_struct, Treeview_Name:str)->Tkinter_GUI__class.Treeview_Struct:


        #-------------------------------------------------------------------------------
        Window_struct.List_Treeview.append(Tkinter_GUI__class.Treeview_Struct());

        Treeview_struct            = Window_struct.List_Treeview[-1];

        Treeview_struct.Name       = Treeview_Name;

        Treeview_struct.Container     = tkinter.Frame(Window_struct.Obj, borderwidth=1, relief="solid");

        Treeview_struct.Obj        = tkinter.ttk.Treeview(Treeview_struct.Container); # Создаем и Привязываем Кнопку к конкретному окну.

        Treeview_struct.Window_struct_ref = Window_struct;

        Treeview_struct.Obj.grid(row=0, column=0, sticky="nsew");   # nsew - Растянуть виджет по всему "Container".  row=0, column=0 - короче - это мы как-бы доавбляем условно первый квадратик "сетки" в Контейнер(при создании виджета за место Окна указывается Container). То есть Контейнер можно представмть как Ексель табилцу, 0,0 - это первая ячейка, в которую и помещаем сам виджет. То есть строка и колонка. К примеру Вертикальный и Горизонтальный скроллбары ниже добавим как: Вертикальный, как таже 0-строка, но уже 1-колонка, и Горизонтальный - как 1-строка, но 0 колонка. 
        #-------------------------------------------------------------------------------



        #--------------------------------------Создаем Scrollbar:-----------------------------------------     
        # Вертикальный:
        Treeview_struct.V_scroll_obj = tkinter.Scrollbar(Treeview_struct.Container, orient=tkinter.VERTICAL, command=Treeview_struct.Obj.yview);
        Treeview_struct.Obj.config(yscrollcommand=Treeview_struct.V_scroll_obj.set);     

        # Вертикальный:
        Treeview_struct.H_scroll_obj = tkinter.Scrollbar(Treeview_struct.Container, orient=tkinter.HORIZONTAL, command=Treeview_struct.Obj.xview);
        Treeview_struct.Obj.config(xscrollcommand=Treeview_struct.H_scroll_obj.set);


        Treeview_struct.V_scroll_obj.grid(row=0, column=1, sticky="ns");     # "ns" - прилипнуть к северу и югу (растянуть по вертикали, ширина не меняется);  row=0, column=1 - читать выше в "Listbox_struct.Obj.grid(row=0, column=0, sticky="nsew")"
        Treeview_struct.H_scroll_obj.grid(row=1, column=0, sticky="ew");     # "ew" - прилипнуть к востоку и западу (растянуть по горизонтали, высота не меняется)
        #-----------------------------------------------------------------------------------------------


        #--------------------------------------Создаем Inputbox и привязываем Callback:-----------------------------------------     

        Treeview_struct.Inputbox_obj =  tkinter.Entry(Window_struct.Obj);

        Treeview_struct.Inputbox_obj.config(relief="solid", borderwidth=1);   # Зададим ширину рамки Inputbox



        def on_change(change_text):
            Treeview_struct._Inputbox_Enter_Callback(change_text);
            return True         # обязательно True, иначе ввод не применится


        vcmd = (Treeview_struct.Inputbox_obj.register(on_change), '%P');              # Устанавливаем или регестриуем колбек - который будет вызыватся каждый раз при вводе в поле ввода какого либого символа/действия.
        Treeview_struct.Inputbox_obj.config(validate="key", validatecommand=vcmd); 


        Treeview_struct.Set_Font_Size(Treeview_struct.Font_Size);   # Просто поставим размер шрифта по умолчанию.

        self._Set__AutoFollow_Inputbox(my_Widget_Obj = Treeview_struct.Obj, Inputbox_obj = Treeview_struct.Inputbox_obj);   # Устанавливаем автоследование и ширину "поля ввода" за виджетом.
        #----------------------------------------------------------------------------------------------------------------------



        #------------------------------------
        Treeview_struct.Container.grid_rowconfigure(0,    weight=1);  # Короче - эта штука гооврит, чтобы ТО ЧТО что мы поместили в строку 0, то есть это сам виджет и Горизонтальный скролл - всегда автоматически полность растягивался на ширину Контейнера при измении его размера или чуть точнее, чтобы обьект в строке 0 - при изменении размера Конктейнера вснда растягвался на изменившееся достйпный размер внутри конейнереа. Доступный - значит, что к примеру у насв Контейнере есть колонка 1 с V-скроллбаром, и так как на него мы ни каких весов не ставили, то его размер будет постоянным при изменеии размера Контейнера и что он берет на себя часть дсотупного пространства Контейнера и строке 0 - эта часть НЕ принадлежит.
        Treeview_struct.Container.grid_columnconfigure(0, weight=1);  # Вообщем все тоже самое, но косаемо Столбца 0.
        #------------------------------------
        
        

        Treeview_struct.Font_Measurement = tkFont.Font(family=Treeview_struct.Font_Name, size=Treeview_struct.Font_Size);  # Обьект для измерения ширины текста.


        #------------------------------------
        Treeview_struct.Set_Font_Name(Treeview_struct.Font_Name);
        Treeview_struct.Set_Font_Size(Treeview_struct.Font_Size);
        #------------------------------------



        return Treeview_struct;

    def Get__Treeview_Struct_by_Name(self, Window_Name:str, Treeview_Name:str)->Tkinter_GUI__class.Treeview_struct | None:

        Window_struct:Tkinter_GUI__class.Window_struct = self.Get__Window_Struct_by_Name(Window_Name);

        for item in Window_struct.List_Treeview:
            if (item.Name == Treeview_Name):
                return item;
        return None;

    #---------------------------------------------------------------------------------Tree_Методы:Конец------------------------------------------------------------------------

    #---------------------------------------------------------------------------------Inputbox_Методы:Начало------------------------------------------------------------------------

    def Add__Inputbox(self, Window_struct:Tkinter_GUI__class.Window_struct, Inputbox_Name:str)->Tkinter_GUI__class.Inputbox_Struct:

        Window_struct.List_Inputbox.append(Tkinter_GUI__class.Inputbox_Struct());

        Inputbox_struct      = Window_struct.List_Inputbox[-1];

        Inputbox_struct.Name = Inputbox_Name;

        Inputbox_struct.Obj  = tkinter.Entry(Window_struct.Obj); # Создаем и Привязываем Кнопку к кокнетному окну.

        Inputbox_struct.Window_struct_ref = Window_struct;

        return Inputbox_struct;

    def Get__Inputbox_Struct_by_Name(self, Window_Name:str, Inputbox_Name:str)->Tkinter_GUI__class.Window_struct | None:

        Window_struct:Tkinter_GUI__class.Window_struct = self.Get__Window_Struct_by_Name(Window_Name);

        for item in Window_struct.List_Inputbox:
            if (item.Name == Inputbox_Name):
                return item;
        return None;

    #---------------------------------------------------------------------------------Inputbox_Методы:Конец------------------------------------------------------------------------

    #---------------------------------------------------------------------------------Table_Методы:Начало------------------------------------------------------------------------

    def Add__Table(self, Window_struct:Tkinter_GUI__class.Window_struct, Table_Name:str, List_Column_Name:list[tuple[str,str]])->Tkinter_GUI__class.Table_Struct:

        #List_Column_Name:  tuple[str,str] - [0] Name_ID столбца, [1] - само отображаемое текстовое имя столбца которые видит Пользователь в таблице.

        #-------------------------------------------------------------------------------
        Window_struct.List_Table.append(Tkinter_GUI__class.Table_Struct());

        Table_struct            = Window_struct.List_Table[-1];

        Table_struct.Name       = Table_Name;

        Table_struct.Container     = tkinter.Frame(Window_struct.Obj, borderwidth=1, relief="solid");

        Table_struct.Obj        = tkinter.ttk.Treeview(Table_struct.Container, show="headings"); 

        Table_struct.Window_struct_ref = Window_struct;

        Table_struct.Obj.grid(row=0, column=0, sticky="nsew");   # nsew - Растянуть виджет по всему "Container".  row=0, column=0 - короче - это мы как-бы доавбляем условно первый квадратик "сетки" в Контейнер(при создании виджета за место Окна указывается Container). То есть Контейнер можно представмть как Ексель табилцу, 0,0 - это первая ячейка, в которую и помещаем сам виджет. То есть строка и колонка. К примеру Вертикальный и Горизонтальный скроллбары ниже добавим как: Вертикальный, как таже 0-строка, но уже 1-колонка, и Горизонтальный - как 1-строка, но 0 колонка. 
        #-------------------------------------------------------------------------------


        #--------------------------------------Создаем Scrollbar:-----------------------------------------     
        # Вертикальный:
        Table_struct.V_scroll_obj = tkinter.Scrollbar(Table_struct.Container, orient=tkinter.VERTICAL, command=Table_struct.Obj.yview);
        Table_struct.Obj.config(yscrollcommand=Table_struct.V_scroll_obj.set);     

        # Вертикальный:
        Table_struct.H_scroll_obj = tkinter.Scrollbar(Table_struct.Container, orient=tkinter.HORIZONTAL, command=Table_struct.Obj.xview);
        Table_struct.Obj.config(xscrollcommand=Table_struct.H_scroll_obj.set);


        Table_struct.V_scroll_obj.grid(row=0, column=1, sticky="ns");     # "ns" - прилипнуть к северу и югу (растянуть по вертикали, ширина не меняется);  row=0, column=1 - читать выше в "Table_struct.Obj.grid(row=0, column=0, sticky="nsew")"
        Table_struct.H_scroll_obj.grid(row=1, column=0, sticky="ew");     # "ew" - прилипнуть к востоку и западу (растянуть по горизонтали, высота не меняется)
        #-----------------------------------------------------------------------------------------------



        Table_struct._Set_Column(List_Column_Name);  # Установим единоразово на табилцу колонки. Изменение, доплнение и вообще редактирование имен колонок не предусмотрено.


        #-------------------------------Установим колбек на клики по Заголовкам для вызов окна филтрации:--------
        Table_struct._Set_Header_Click_Callback(Table_struct._Click_for_Header_Callback);
        #--------------------------------------------------------------------------------------------------------


        Table_struct.Popup_Filter_for_Table_Obj =  self.Popup_Filter_for_Table__class(Table_struct);          # Создаем Popup-окно для филтрациию по признаку "Содержит"

        Table_struct._set_Popup_CellViewerText_for_Table();                                                   # Создаем Popup-окно для вывода туда текст из ячейки таблицы при двойном Правом клике по ней.

        

        #------------------------------------
        Table_struct.Container.grid_rowconfigure(0,    weight=1);  # Короче - эта штука гооврит, чтобы ТО ЧТО что мы поместили в строку 0, то есть это сам виджет и Горизонтальный скролл - всегда автоматически полность растягивался на ширину Контейнера при измении его размера или чуть точнее, чтобы обьект в строке 0 - при изменении размера Конктейнера вснда растягвался на изменившееся достйпный размер внутри конейнереа. Доступный - значит, что к примеру у насв Контейнере есть колонка 1 с V-скроллбаром, и так как на него мы ни каких весов не ставили, то его размер будет постоянным при изменеии размера Контейнера и что он берет на себя часть дсотупного пространства Контейнера и строке 0 - эта часть НЕ принадлежит.
        Table_struct.Container.grid_columnconfigure(0, weight=1);  # Вообщем все тоже самое, но косаемо Столбца 0.
        #------------------------------------



        Table_struct.List_Columns_Name.extend(List_Column_Name);


        return Table_struct;

    def Get__Table_Struct_by_Name(self, Window_Name:str, Table_Name:str)->Tkinter_GUI__class.Table_struct | None:

        Window_struct:Tkinter_GUI__class.Window_struct = self.Get__Window_Struct_by_Name(Window_Name);

        for item in Window_struct.List_Table:
            if (item.Name == Table_Name):
                return item;
        return None;

    #---------------------------------------------------------------------------------Table_Методы:Конец------------------------------------------------------------------------

    #---------------------------------------------------------------------------------ProgressBar_Методы:Начало------------------------------------------------------------------------

    def Add__ProgressBar(self, Window_struct:Tkinter_GUI__class.Window_struct, ProgressBar_Name:str)->Tkinter_GUI__class.ProgressBar_Struct:

        Window_struct.List_ProgressBar.append(Tkinter_GUI__class.ProgressBar_Struct());

        ProgressBar_struct       = Window_struct.List_ProgressBar[-1];

        ProgressBar_struct.Name  = ProgressBar_Name;

        ProgressBar_struct.Obj   = tkinter.ttk.Progressbar(Window_struct.Obj, length=0, mode='determinate');
        ProgressBar_struct.Label = tkinter.ttk.Label(Window_struct.Obj, text="", anchor='center');

        ProgressBar_struct.Window_struct_ref = Window_struct;

        return ProgressBar_struct;

    def Get__ProgressBar_Struct_by_Name(self, Window_Name:str, ProgressBar_Name:str)->Tkinter_GUI__class.Window_struct | None:

        Window_struct:Tkinter_GUI__class.Window_struct = self.Get__Window_Struct_by_Name(Window_Name);

        for item in Window_struct.List_ProgressBar:
            if (item.Name == ProgressBar_Name):
                return item;
        return None;

    #---------------------------------------------------------------------------------ProgressBar_Методы:Конец------------------------------------------------------------------------


    #---------------------------------------------------------------------------------OneColumnTable_aka_Listbox_Методы:Начало------------------------------------------------------------------------

    def Add__OneColumnTable_aka_Listbox(self, Window_struct:Tkinter_GUI__class.Window_struct, OneColumnTable_aka_Listbox_Name:str)->Tkinter_GUI__class.OneColumnTable_aka_Listbox_Struct:


        #-------------------------------------------------------------------------------
        Window_struct.List_OneColumnTable_aka_Listbox.append(Tkinter_GUI__class.OneColumnTable_aka_Listbox_Struct());

        OneColumnTable_aka_Listbox_struct            = Window_struct.List_OneColumnTable_aka_Listbox[-1];

        OneColumnTable_aka_Listbox_struct.Name       = OneColumnTable_aka_Listbox_Name;

        OneColumnTable_aka_Listbox_struct.Container     = tkinter.Frame(Window_struct.Obj, borderwidth=1, relief="solid");

        OneColumnTable_aka_Listbox_struct.Obj        = tkinter.ttk.Treeview(OneColumnTable_aka_Listbox_struct.Container, columns=("value",), show="headings"); 

        OneColumnTable_aka_Listbox_struct.Obj.heading("value", text="");

        OneColumnTable_aka_Listbox_struct.Window_struct_ref = Window_struct;

        OneColumnTable_aka_Listbox_struct.Obj.grid(row=0, column=0, sticky="nsew");   # nsew - Растянуть виджет по всему "Container".  row=0, column=0 - короче - это мы как-бы доавбляем условно первый квадратик "сетки" в Контейнер(при создании виджета за место Окна указывается Container). То есть Контейнер можно представмть как Ексель табилцу, 0,0 - это первая ячейка, в которую и помещаем сам виджет. То есть строка и колонка. К примеру Вертикальный и Горизонтальный скроллбары ниже добавим как: Вертикальный, как таже 0-строка, но уже 1-колонка, и Горизонтальный - как 1-строка, но 0 колонка. 
        #-------------------------------------------------------------------------------


        #--------------------------------------Создаем Scrollbar:-----------------------------------------     
        # Вертикальный:
        OneColumnTable_aka_Listbox_struct.V_scroll_obj = tkinter.Scrollbar(OneColumnTable_aka_Listbox_struct.Container, orient=tkinter.VERTICAL, command=OneColumnTable_aka_Listbox_struct.Obj.yview);
        OneColumnTable_aka_Listbox_struct.Obj.config(yscrollcommand=OneColumnTable_aka_Listbox_struct.V_scroll_obj.set);     

        # Вертикальный:
        OneColumnTable_aka_Listbox_struct.H_scroll_obj = tkinter.Scrollbar(OneColumnTable_aka_Listbox_struct.Container, orient=tkinter.HORIZONTAL, command=OneColumnTable_aka_Listbox_struct.Obj.xview);
        OneColumnTable_aka_Listbox_struct.Obj.config(xscrollcommand=OneColumnTable_aka_Listbox_struct.H_scroll_obj.set);


        OneColumnTable_aka_Listbox_struct.V_scroll_obj.grid(row=0, column=1, sticky="ns");     # "ns" - прилипнуть к северу и югу (растянуть по вертикали, ширина не меняется);  row=0, column=1 - читать выше в "Listbox_struct.Obj.grid(row=0, column=0, sticky="nsew")"
        OneColumnTable_aka_Listbox_struct.H_scroll_obj.grid(row=1, column=0, sticky="ew");     # "ew" - прилипнуть к востоку и западу (растянуть по горизонтали, высота не меняется)
        #-----------------------------------------------------------------------------------------------



        #--------------------------------------Создаем Inputbox и привязываем Callback:-----------------------------------------     

        OneColumnTable_aka_Listbox_struct.Inputbox_obj =  tkinter.Entry(Window_struct.Obj);

        OneColumnTable_aka_Listbox_struct.Inputbox_obj.config(relief="solid", borderwidth=1);   # Зададим ширину рамки Inputbox



        def on_change(change_text):
            OneColumnTable_aka_Listbox_struct._Inputbox_Enter_Callback(change_text);
            return True         # обязательно True, иначе ввод не применится


        vcmd = (OneColumnTable_aka_Listbox_struct.Inputbox_obj.register(on_change), '%P')
        OneColumnTable_aka_Listbox_struct.Inputbox_obj.config(validate="key", validatecommand=vcmd); 


        self._Set__AutoFollow_Inputbox(my_Widget_Obj = OneColumnTable_aka_Listbox_struct.Obj, Inputbox_obj = OneColumnTable_aka_Listbox_struct.Inputbox_obj);   # Устанавливаем автоследование и ширину "поля ввода" за виджетом.
        #----------------------------------------------------------------------------------------------------------------------

      
        #------------------------------------
        OneColumnTable_aka_Listbox_struct.Container.grid_rowconfigure(0,    weight=1);  # Короче - эта штука гооврит, чтобы ТО ЧТО что мы поместили в строку 0, то есть это сам виджет и Горизонтальный скролл - всегда автоматически полность растягивался на ширину Контейнера при измении его размера или чуть точнее, чтобы обьект в строке 0 - при изменении размера Конктейнера вснда растягвался на изменившееся достйпный размер внутри конейнереа. Доступный - значит, что к примеру у насв Контейнере есть колонка 1 с V-скроллбаром, и так как на него мы ни каких весов не ставили, то его размер будет постоянным при изменеии размера Контейнера и что он берет на себя часть дсотупного пространства Контейнера и строке 0 - эта часть НЕ принадлежит.
        OneColumnTable_aka_Listbox_struct.Container.grid_columnconfigure(0, weight=1);  # Вообщем все тоже самое, но косаемо Столбца 0.
        #------------------------------------


        OneColumnTable_aka_Listbox_struct.Font_Measurement = tkFont.Font(family=OneColumnTable_aka_Listbox_struct.Font_Name, size=OneColumnTable_aka_Listbox_struct.Font_Size);  # Обьект для измерения ширины текста.


        #------------------------------------
        OneColumnTable_aka_Listbox_struct.Set_Font_Name(OneColumnTable_aka_Listbox_struct.Font_Name);
        OneColumnTable_aka_Listbox_struct.Set_Font_Size(OneColumnTable_aka_Listbox_struct.Font_Size);
        #------------------------------------


        return OneColumnTable_aka_Listbox_struct;

    def Get__OneColumnTable_aka_Listbox_Struct_by_Name(self, Window_Name:str, OneColumnTable_aka_Listbox_Name:str)->Tkinter_GUI__class.OneColumnTable_aka_Listbox_struct | None:

        Window_struct:Tkinter_GUI__class.Window_struct = self.Get__Window_Struct_by_Name(Window_Name);

        for item in Window_struct.List_OneColumnTable_aka_Listbox:
            if (item.Name == OneColumnTable_aka_Listbox_Name):
                return item;
        return None;

    #---------------------------------------------------------------------------------OneColumnTable_aka_Listbox_Методы:Конец------------------------------------------------------------------------


    #---------------------------------------------------------------------------------Entry_DateTime_Методы:Начало------------------------------------------------------------------------

    def Add__Entry_DateTime(self, Window_struct:Tkinter_GUI__class.Window_struct, Entry_DateTime_Name:str, Start_DateTime:str, Format_DateTime:str)->Tkinter_GUI__class.Entry_DateTime_Struct:

        # Start_DateTime указывается в формате "30-01-2020" или "30.01.2020 12:00" - вообщем это та дата и время которые появятся изначално при создании данного виджет, формат можно указать любой самое главное чтобы ему строго соответвовал формат указанный в Format_DateTime: "%d.%m.%Y или "%d-%m-%Y %H:%M" и тому подобное.


        Window_struct.List_Entry_DateTime.append(Tkinter_GUI__class.Entry_DateTime_Struct());

        Entry_DateTime_struct      = Window_struct.List_Entry_DateTime[-1];

        Entry_DateTime_struct.Name = Entry_DateTime_Name;

        Entry_DateTime_struct.Obj  = tkinter.Entry(Window_struct.Obj);


        Entry_DateTime_struct.Obj.insert(0, Start_DateTime);  # Добавим шаблон ввода Даты и Времени, чтобы Пользвтаель сразу видел, как и чего тут заполнять.
        Entry_DateTime_struct.Formate_Date_string = Format_DateTime;



        Entry_DateTime_struct.Obj.bind("<KeyPress>", lambda event: Entry_DateTime_struct._Check_Enter_Symv(event)); # Короче провреяем, что вводит Пользователь и если вводит всякое непотребство типа - не чилосовых значенй, удаляет из шиблона Даты - пробел, точку или двоеточие - то блокируем такие дейтсвия.

        Entry_DateTime_struct.Obj.config(justify="center");     # Ставим чтобы дата всегда распологалась по центру поля ввода.


        Entry_DateTime_struct.Window_struct_ref = Window_struct;

        return Entry_DateTime_struct;

    def Get__Entry_DateTime_Struct_by_Name(self, Window_Name:str, Entry_DateTime_Name:str)->Tkinter_GUI__class.Window_struct | None:

        Window_struct:Tkinter_GUI__class.Window_struct = self.Get__Window_Struct_by_Name(Window_Name);

        for item in Window_struct.List_Entry_DateTime:
            if (item.Name == Entry_DateTime_Name):
                return item;
        return None;

    #---------------------------------------------------------------------------------Entry_DateTime_Методы:Конец------------------------------------------------------------------------


    #---------------------------------------------------------------------------------Label_Методы:Начало------------------------------------------------------------------------

    def Add__Label(self, Window_struct:Tkinter_GUI__class.Window_struct, Label_Name:str)->Tkinter_GUI__class.Label_Struct:

        Window_struct.List_Label.append(Tkinter_GUI__class.Label_Struct());

        Label_struct      = Window_struct.List_Label[-1];

        Label_struct.Name      = Label_Name;

        Label_struct.Obj  = tkinter.Label(Window_struct.Obj); # Создаем и Привязываем Кнопку к кокнетному окну.

        Label_struct.Window_struct_ref = Window_struct;

        return Label_struct;

    def Get__Label_Struct_by_Name(self, Window_Name:str, Label_Name:str)->Tkinter_GUI__class.Window_struct | None:

        Window_struct:Tkinter_GUI__class.Window_struct = self.Get__Window_Struct_by_Name(Window_Name);

        for item in Window_struct.List_Label:
            if (item.Name == Label_Name):
                return item;
        return None;

    #---------------------------------------------------------------------------------Label_Методы:Конец------------------------------------------------------------------------

    

    #---------------------------------------------------------------------------------Classic_Menu_Методы:Начало------------------------------------------------------------------------

    def Set__Classic_Menu(self, Window_struct:Tkinter_GUI__class.Window_struct, Menu_Name:str)->Tkinter_GUI__class.Label_Struct:

        Window_struct.Classic_Menu = Tkinter_GUI__class.Classic_Menu_Struct();

        Classic_Menu_Struct           = Window_struct.Classic_Menu;

        Classic_Menu_Struct.Name      = Menu_Name;

        Classic_Menu_Struct.Obj  = tkinter.Menu(Window_struct.Obj, tearoff=0); # Создаем и Привязываем Кнопку к кокнетному окну.

        Classic_Menu_Struct.Window_struct_ref = Window_struct;

        Window_struct.Obj.config(menu=Classic_Menu_Struct.Obj);


        return Classic_Menu_Struct;

    def Get__Classic_Menu_Struct_by_Name(self, Window_Name:str, Menu_Name:str)->Tkinter_GUI__class.Window_struct | None:

        Window_struct:Tkinter_GUI__class.Window_struct = self.Get__Window_Struct_by_Name(Window_Name);

        return Window_struct.Classic_Menu;

    #---------------------------------------------------------------------------------Classic_Menu_Методы:Конец------------------------------------------------------------------------


    
    #---------------------------------------------------------------------------------Context_Menu_Методы:Начало------------------------------------------------------------------------
    
    def Add__Context_Menu(self, Window_struct:Tkinter_GUI__class.Window_struct, Context_Menu_Name:str)->Tkinter_GUI__class.Context_Menu_Struct:

        Window_struct.List_Context_Menu.append(Tkinter_GUI__class.Context_Menu_Struct());

        Context_Menu_struct      = Window_struct.List_Context_Menu[-1];

        Context_Menu_struct.Name      = Context_Menu_Name;

        Context_Menu_struct.Obj  = tkinter.Menu(Window_struct.Obj, tearoff=False); # Создаем и Привязываем Кнопку к кокнетному окну.

        Context_Menu_struct.Window_struct_ref = Window_struct;

        return Context_Menu_struct;

    def Get__Context_Menu_Struct_by_Name(self, Window_Name:str, Context_Menu_Name:str)->Tkinter_GUI__class.Window_struct | None:

        Window_struct:Tkinter_GUI__class.Window_struct = self.Get__Window_Struct_by_Name(Window_Name);

        for item in Window_struct.List_Context_Menu:
            if (item.Name == Context_Menu_Name):
                return item;
        return None;
    
    #---------------------------------------------------------------------------------Context_Menu_Методы:Конец------------------------------------------------------------------------




    #---------------------------------------------------------------------------Диалоговое меню выбора файлов и папок:Начало--------------------------------------------------------------------

    def DialogMenu__Choose_Folder(self, Begin_Folder:str)->str:

        return filedialog.askdirectory(initialdir=Begin_Folder);   #  если возвращается пустая строка "" - значит Пользовтаель отменил выбор.

    def DialogMenu__Choose_Folder_and_EnterFileName(self, Begin_Folder:str)->str:

        # Диалоговное окно с выбором папки и возможность ввести имя файла в поле ввода(даже не существующий), вернется полнуть путь к веденному имени файлу.

        return filedialog.asksaveasfilename(initialdir=Begin_Folder);   #  если возвращается пустая строка "" - значит Пользовтаель отменил выбор.

    def DialogMenu__Choose_OneFile(self, Begin_Folder:str)->str:

        return filedialog.askopenfilename(initialdir=Begin_Folder);   #  если возвращается пустая строка "" - значит Пользовтаель отменил выбор.

    def DialogMenu__Choose_ManyFiles(self, Begin_Folder:str)->tuple[str,...]:

        return filedialog.askopenfilenames(initialdir=Begin_Folder);  # Возвращает tuple строк, если возвращается len(tuple) == 0 - значит Пользовтаель отменил выбор.
    #---------------------------------------------------------------------------Диалоговое меню выбора файлов и папок:Конец--------------------------------------------------------------------


    #----------------------------------------------------------------------------Другое:Начало--------------------------------------------------------------------------------------------------------------

    def Get__ExecuteFile_PathFolder(self)->str:

        return os.path.dirname(sys.executable if getattr(sys, "frozen", False) else __file__);  # Возвращает путь к папке исполняемого файла.

    def Get__Cursor_Pos_in_Window(self, Window_struct_:Window_struct)->Tkinter_GUI__class.Pos_struct:

        Pos_struct_ = Tkinter_GUI__class.Pos_struct();


        x = Window_struct_.Obj.winfo_pointerx()  # координата курсора на экране (X)
        y = Window_struct_.Obj.winfo_pointery()  # координата курсора на экране (Y)

        win_x = Window_struct_.Obj.winfo_rootx()  # координата окна на экране
        win_y = Window_struct_.Obj.winfo_rooty()

        Pos_struct_.x = x - win_x  # координата курсора относительно окна
        Pos_struct_.y = y - win_y

        return Pos_struct_;

    def Get__FullPath_to_Files_from_Folder(self, Path_Folder: str) -> list[str]:

    # Возвращает список имен файлов (с расширением) в указанной папке Path_Folder. Подпапки не включаются, только файлы.
    # Возвращаеются именна полный пути до этих файлов.

        list_result = [];  # сюда будем складывать имена файлов
    
        all_items = os.listdir(Path_Folder);  # получаем ВСЁ содержимое папки: и файлы, и подпапки
    
        for f in all_items:                   # проходим по каждому элементу
            full_path = os.path.join(Path_Folder, f);  # собираем полный путь до этого элемента
        
            if os.path.isfile(full_path):     # проверяем: это файл (не папка)?
                list_result.append(str(Path(Path_Folder) / f));        # если файл — добавляем в список ИМЯ (+ добавляем Path_Folder - для полного пути)
    
        return list_result;

    def Get__FullPath_to_Files_from_Folder__Sort_Files_as_Value_From_Less_to_More(self, Path_Folder: str) -> list[str]:

        # Возвращает список имен файлов (с расширением) в указанной папке Path_Folder. Подпапки не включаются, только файлы.
        # Возвращаеются именна полный пути до этих файлов.
        # ФУНКЦИЯ СПЕЦИАЛЬНО ДЛЯ СЛУЧАЯ, когда в указаннйо папке находятся только файлы с именами в виде числовых значений, функция гарантирнует, что файлы будут считаны, в порядке от Меньшего значения файла к Большему: то есть, если в папке файлы 123.txt, 12.txt, 75.txt, 2025.txt, 2023 - то есчитаны они будут и занемены в список в таком порядке: 12,75,123,2023,2025.


        list_result = []

        all_items = sorted(
            os.listdir(Path_Folder),
            key=lambda x: int(Path(x).stem)
        )

        for f in all_items:
            full_path = os.path.join(Path_Folder, f)

            if os.path.isfile(full_path):
                list_result.append(str(Path(Path_Folder) / f))

        return list_result

    def Get__FilesNames_from_Folder(self, Path_Folder: str) -> list[str]:

    # Возвращает список имен файлов (с расширением) в указанной папке Path_Folder. Подпапки не включаются, только файлы.
    # Возвращаеются только имена файлов.

        list_result = [];  # сюда будем складывать имена файлов
    
        all_items = os.listdir(Path_Folder);  # получаем ВСЁ содержимое папки: и файлы, и подпапки
    
        for f in all_items:                  # проходим по каждому элементу
            full_path = os.path.join(Path_Folder, f);  # собираем полный путь до этого элемента
        
            if os.path.isfile(full_path):    # проверяем: это файл (не папка)?
                list_result.append(f);        # если файл — добавляем в список ИМЯ (без пути)

        return list_result;

    def Check__Folder_Exist(self, Path_Folder:str)->bool:
        #Path_Folder - путь к папке должен быть указан без последнего слеша, по типу: "G:\VS2019\my_Folder"

        if Path(Path_Folder).is_dir():
            return True;
        else:
            return False;

    #----------------------------------------------------------------------------Другое:Конец--------------------------------------------------------------------------------------------------------------








    def Main_Loop(self):

        for item in self.List_Window:
            item.Obj.mainloop();



    #-------------------------------------------------------------------------------PRIVATE-вспомогательные методы:Начало---------------------------------------------------------------------------------

    def _Set__AutoFollow_Inputbox(self, *, my_Widget_Obj, Inputbox_obj):

        # Делаем автоследование по позиции и ширине, НО по высоте не делаем, так как height поля ввода - зависит от размера устаовленного шрифта, и поэтому высоту поля ввода меняет толко в функции изменения размера шрифта.

        Inputbox_obj.place(in_ = my_Widget_Obj, relx=0.0, rely=0.0, x=1, y=1, relwidth = 1.0, width = -2, anchor = self.Anchor_enum.TopLeft);




