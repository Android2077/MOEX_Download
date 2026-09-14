
from dataclasses import dataclass
import json
from datetime import datetime
from enum import Enum
from enum import IntEnum
from pathlib import Path
import sys

from MOEX_Download__class import MOEX_Download__class     # from "имя файла" import "имя класса"

import duckdb  # pip install duckdb
import time
from datetime import timedelta





class DuckDB_StockCandles__class():

	

	@dataclass(slots=True)
	class FullPath_struct:
		FullPath_string:str = "";
		Year_string:str     = "";
	

	class Exist_enum(IntEnum):
		Exist     = 0
		NotExist  = 1


	class CulumnsCandle_enum(Enum):    #["open", "close", "high", "low", "value", "volume", "begin", "end"]
		Open   = 0
		Close  = 1
		High   = 2
		Low    = 3
		Value  = 4
		Volume = 5
		Begin  = 6
		End    = 7



	def __init__(self, MOEX_Download_ref_:MOEX_Download__class):


		self.MOEX_Download_ref:MOEX_Download__class = MOEX_Download_ref_;  # Ссылка на обьект класса "MOEX_Download__class". Нужен тут для проверки корректности формата JSON - на всякий случай.

		self.List__Columns_Name_and_Format:list[tuple[str,str]] = [("open", "DOUBLE"), ("close", "DOUBLE"), ("high", "DOUBLE"), ("low", "DOUBLE"), ("value", "DOUBLE"), ("volume", "BIGINT"), ("begin_date", "TIMESTAMP"), ("end_date", "TIMESTAMP"), ];  # Список имено стоблцов и сооветтвующий им формат хранимых в столбце значений - СООТВЕТВУЮЩИЙ формату "columns" из JSON, который приходит с MOEX из класса "MOEX_Download".	# слово "end" зарезервировано в DuckDB, поэтому его не получится прямо использовать имени столбцов, как JSON от MOEX, поэтому добавил "_date".


		self._Check_Columns();  # Проверяем "List__Columns_Name_and_Format" на корректность правильному формату из "MOEX_Download__class"




		self._Duckdb_Obj:duckdb.DuckDBPyConnection = duckdb.connect()  # создаем подключение к Базе Данных, сама БД создается в памяти.


		
		#------------------------------Создаем пустую DuckDB таблицу в памяти и указываем формат и имя столбцов таблицы для записи в нее данных из пришедгих свечей с MOEX Json:Начало---------------------------------------
		self.DuckDB_Table_Name_for_JSON:str = "my_stock_table_for_JSON";  # Имя временной создаваемй таблицы, куда будет записывать данные свечей из пришедшего Json.
	
		result_1 = self._Create__Empty_DuckDB_Table(self.DuckDB_Table_Name_for_JSON, self.List__Columns_Name_and_Format);

		if (result_1 != None):
			print(result_1);
			return;
		#------------------------------Создаем пустую DuckDB таблицу в памяти и указываем формат и имя столбцов таблицы для записи в нее данных из пришедгих свечей с MOEX Json:Конец---------------------------------------


		#------------------------------Создаем пустую DuckDB таблицу в памяти и указываем формат и имя столбцов таблицы для записи в нее данных из существующих Parquet-файлов на диске(для обьединения с пришедшими свечами):Начало---------------------------------------
		self.DuckDB_Table_Name_for_ParquetFile:str = "my_stock_table_for_ParquetFile";  # Имя временной создаваемй таблицы, куда будет записывать данные свечей из существующих Parquet-файлов

		result_1 = self._Create__Empty_DuckDB_Table(self.DuckDB_Table_Name_for_ParquetFile, self.List__Columns_Name_and_Format);

		if (result_1 != None):
			print(result_1);
			return;
		#------------------------------Создаем пустую DuckDB таблицу в памяти и указываем формат и имя столбцов таблицы для записи в нее данных из существующих Parquet-файлов на диске(для обьединения с пришедшими свечами):Конец---------------------------------------


		#---------------Создаем пустую DuckDB таблицу в памяти и указываем формат и имя столбцов таблицы для записи в нее обьеденненых данных из пришедшего JSON MOEX с существующими данными из Parquet-файлов(нужно для "дозаписи"):Начало-------------
		self.DuckDB_Table_Name_for_Union:str = "my_stock_table_for_Union";  # Имя временной создаваемй таблицы, куда будет записывать данные свечей из существующих Parquet-файлов
	
		result_1 = self._Create__Empty_DuckDB_Table(self.DuckDB_Table_Name_for_Union, self.List__Columns_Name_and_Format);

		if (result_1 != None):
			print(result_1);
			return;
		#---------------Создаем пустую DuckDB таблицу в памяти и указываем формат и имя столбцов таблицы для записи в нее обьеденненых данных из пришедшего JSON MOEX с существующими данными из Parquet-файлов(нужно для "дозаписи"):Конец-------------




		#------------------------------Создаем пустую DuckDB таблицу в памяти и указываем формат и имя столбцов таблицы для записи в нее данных из Parqet-файлов для преобразования в CSV:Начало---------------------------------------
		self.DuckDB_Table_Name_for_CSV:str = "my_stock_table_for_CSV";  # Имя временной создаваемй таблицы, куда будет записывать данные свечей из пришедшего Json.
	
		result_1 = self._Create__Empty_DuckDB_Table(self.DuckDB_Table_Name_for_CSV, self.List__Columns_Name_and_Format);

		if (result_1 != None):
			print(result_1);
			return;
		#------------------------------Создаем пустую DuckDB таблицу в памяти и указываем формат и имя столбцов таблицы для записи в нее данных из Parqet-файлов для преобразования в CSV:Конец---------------------------------------


	def Save_Candle_Struct_Format(self, Main_Path:str, Candle_struct_from_MOEX_Download:MOEX_Download__class.Candle_struct, Format_Date_Candles_from_JSON_MOEX:str, Engine_name, Market_name, Board_name, Instrument_name, Interval_name)->None|str:

		# Main_Path -  Это папка верxнего увроня в которой находится сам каталог Parquet-файлов.


	
		#----------------------------------Заполянем созданную при инициализации класса таблицу данными свечей из JSON:Начало---------------------------------------------

		result_1 = self.Set__Data_to_DuckDB_Table__Candle_Struct_Format(Candle_struct_from_MOEX_Download, Format_Date_Candles_from_JSON_MOEX);

		if (result_1 != None):

			return result_1;

		#----------------------------------Заполянем созданную при инициализации класса таблицу данными свечей из JSON:Конец---------------------------------------------


		return self._Action(Main_Path, Engine_name, Market_name, Board_name, Instrument_name, Interval_name);

	def Save_Candle_JSON_List_String_Format(self, Main_Path:str, JSON_List_String_Format:str, Format_Date_Candles_from_JSON_MOEX:str, Engine_name, Market_name, Board_name, Instrument_name, Interval_name)->None|str:
		
		# Main_Path -  Это папка верxнего увроня в которой находится сам каталог Parquet-файлов.


	
		#----------------------------------Заполянем созданную при инициализации класса таблицу данными свечей из JSON:Начало---------------------------------------------

		result_1 = self.Set__Data_to_DuckDB_Table__JSON_List_String_Format(JSON_List_String_Format, Format_Date_Candles_from_JSON_MOEX);

		if (result_1 != None):

			return result_1;

		#----------------------------------Заполянем созданную при инициализации класса таблицу данными свечей из JSON:Конец---------------------------------------------


		return self._Action(Main_Path, Engine_name, Market_name, Board_name, Instrument_name, Interval_name, JSON_List_String_Format);



	#-----------------------------------------------------------------ДЛЯ ТРАНСОФРМАЦИИ в CSV:Начало---------------------------------------------------------------------

	def Transform_to_CSV(self, Date_Begin:str, Date_End:str, Path_High_Level_Folder:str, Engine:str, Market:str, Board:str, Intrument_Name:str, Interval:str, Format_Date:str, Path_to_Save_CSV:str, Delimiter_CSV:str)->str|None:
		
		try:

			# Path_High_Level_Folder - путь к папке где собсвенно и лежит весь каталог Parqet-файлов.

			self._Duckdb_Obj.execute(f"TRUNCATE TABLE {self.DuckDB_Table_Name_for_CSV}")  # очистка таблицы от предыдушиз данных.


			#-----------------------------------Ивзлечем значение Года из Date_Begin и Date_End:Начало----------------------------------------

			Year_Begin:int = self._Extract_YEAR_from_Date(Date_Begin, Format_Date);
		
			Year_End:int = self._Extract_YEAR_from_Date(Date_End, Format_Date);

			#-----------------------------------Ивзлечем значение Года из Date_Begin и Date_End:Конец----------------------------------------



			#----------------------------------------Сгенерим полные пути до Parqet-файлов с учетом запрошенной даты:Начало------------------------------
			List__FullPath_to_Files:list[str] = [];


			cntr:int = Year_End - Year_Begin + 1;

			for i in range(cntr):
				my_path = Path(Path_High_Level_Folder) / Engine / Market / Board / Intrument_Name / Interval / ((str(Year_Begin + i)) + ".parquet");


				#````````````````````````````````````````````````````````Проверим Сразу сущестование пути к сгенрированному parquet-файлу:Начало``````````````````````````````````````````````
				res = self._Check__File_Exist(str(my_path));

				if (res == False):
					#Значит файла Parqet с таким Годом нет.Просто не формируем этот путь и пропускаем его.
					continue;

				#````````````````````````````````````````````````````````Проверим Сразу сущестование пути к сгенрированному parquet-файлу:Конец``````````````````````````````````````````````


				List__FullPath_to_Files.append(my_path);

			#----------------------------------------Сгенерим полные пути до Parqet-файлов с учетом запрошенной даты:Конец------------------------------


			# List__FullPath_to_Files - так теперь тут все подвтержденные пути до Parqet-файлов соовтетвущих диапазону даты Пользвоательского запроса.




			#---------------------------------------------------------Читаем Parquet-файлы:Начало------------------------------------------------------------
			for item in List__FullPath_to_Files:

				SQL_DuckDB_request:str = f"INSERT INTO {self.DuckDB_Table_Name_for_CSV} SELECT * FROM read_parquet('{item}')";  # Вставляем данные в таблицу "DuckDB_Table_Name_for_CSV" из существующих Parquet-файла на диске.

				self._Duckdb_Obj.execute(SQL_DuckDB_request);  # Выполянем запрос.

			#---------------------------------------------------------Читаем Parquet-файлы:Конец------------------------------------------------------------




			#-----------------------------Фильтруем таблицу "DuckDB_Table_Name_for_CSV" по дате Пользовательского запроса От "Date_Begin" до "Date_End" и сохраняем в CSV на диск:Начало-------------------
			if (len(List__FullPath_to_Files) > 0):


				Path_to_Save_CSV_plus_FileNmae:str = Path(Path_to_Save_CSV) / str(f"{Engine}_{Market}_{Board}_{Intrument_Name}_{Interval}.csv");


				#Короче делаем: выбираем все строки из табилцы по столбцу "begin_date" все строки которые, которые удовлетворяет условию, что - дата в "begin_date" находится между переданными датами "Date_Begin" - "Date_End" ---> отфильрованное сортируем по Возрастанию и сохраняем в CSV.

				SQL_DuckDB_request = f"""
				COPY (
					SELECT * FROM {self.DuckDB_Table_Name_for_CSV}
					WHERE begin_date BETWEEN STRPTIME('{Date_Begin}', '{Format_Date}') AND STRPTIME('{Date_End}', '{Format_Date}')
					ORDER BY begin_date ASC
				) TO '{Path_to_Save_CSV_plus_FileNmae}' (FORMAT CSV, HEADER, DELIMITER '{Delimiter_CSV}')
				"""
				self._Duckdb_Obj.execute(SQL_DuckDB_request)

			#-----------------------------Фильтруем таблицу "DuckDB_Table_Name_for_CSV" по дате Пользовательского запроса От "Date_Begin" до "Date_End" и сохраняем в CSV на диск:Конец-------------------

			return None;

		except Exception as e:
			return(str(e));

		
	def Transform_to_CSV_Direct_Path(self, Date_Begin:str, Date_End:str, List_with_FullPath_to_ParqetFiles:str,  Engine:str, Market:str, Board:str, Intrument_Name:str, Interval:str, Format_Date:str, Path_to_Save_CSV:str, Delimiter_CSV:str)->str|None:
		
		try:

			# List_with_FullPath_to_ParqetFiles - список полных путей до Parqet-файлов из которых нужно сохрнаить строки, которые удоавблетворяют условию переданного диапазона дат:  Date_Begin - Date_End

			self._Duckdb_Obj.execute(f"TRUNCATE TABLE {self.DuckDB_Table_Name_for_CSV}")  # очистка таблицы от предыдушиз данных.


			#-----------------------------------Ивзлечем значение Года из Date_Begin и Date_End:Начало----------------------------------------

			Date_Begin = Date_Begin + " " + "00:00:00";
			Date_End   = Date_End   + " " + "23:59:59";

			Year_Begin:int = self._Extract_YEAR_from_Date(Date_Begin, Format_Date);
		
			Year_End:int = self._Extract_YEAR_from_Date(Date_End, Format_Date);

			#-----------------------------------Ивзлечем значение Года из Date_Begin и Date_End:Конец----------------------------------------



			#----------------------------------------Сгенерим полные пути до Parqet-файлов с учетом запрошенной даты:Начало------------------------------
			List__FullPath_to_Files:list[str] = [];

			for user_Path in (List_with_FullPath_to_ParqetFiles):

				#````````````````````````````````````````````````````````Проверим Сразу сущестование пути к сгенрированному parquet-файлу:Начало``````````````````````````````````````````````
				res = self._Check__File_Exist(str(user_Path));

				if (res == False):
					#Значит файла Parqet с таким Годом нет.Просто не формируем этот путь и пропускаем его.
					continue;

				#````````````````````````````````````````````````````````Проверим Сразу сущестование пути к сгенрированному parquet-файлу:Конец``````````````````````````````````````````````


				List__FullPath_to_Files.append(user_Path);

			#----------------------------------------Сгенерим полные пути до Parqet-файлов с учетом запрошенной даты:Конец------------------------------


			# List__FullPath_to_Files - так теперь тут все подвтержденные пути до Parqet-файлов соовтетвущих диапазону даты Пользвоательского запроса.



			#`````````````````````````````````````````````````````````````````````````````
			if (len(List__FullPath_to_Files) == 0):
				# Значит не один Parqet-файл не найден по предсотавленным путям.
				return "Не найдены Parque-файлы в указаннйо папке по даннмоу Инстурменту";
			#`````````````````````````````````````````````````````````````````````````````



			#---------------------------------------------------------Читаем Parquet-файлы:Начало------------------------------------------------------------
			for item in List__FullPath_to_Files:

				SQL_DuckDB_request:str = f"INSERT INTO {self.DuckDB_Table_Name_for_CSV} SELECT * FROM read_parquet('{item}')";  # Вставляем данные в таблицу "DuckDB_Table_Name_for_CSV" из существующих Parquet-файла на диске.

				self._Duckdb_Obj.execute(SQL_DuckDB_request);  # Выполянем запрос.
			#---------------------------------------------------------Читаем Parquet-файлы:Конец------------------------------------------------------------



			#----------------------------------Выводим все диапазоны дат:начало-----------------------------------

			#Ranges = self._Duckdb_Obj.execute(
				#f"""
				#SELECT YEAR(begin_date) AS yr, MIN(begin_date), MAX(begin_date), COUNT(*)
				#FROM {self.DuckDB_Table_Name_for_CSV}
				#GROUP BY yr
				#ORDER BY yr
				#"""
			#).fetchall()

			#for row in Ranges:
				#print(f"Год {row[0]}: {row[1]} - {row[2]} ({row[3]} строк)")

			#----------------------------------Выводим все диапазоны дат:конец-----------------------------------



			#-----------------------------Фильтруем таблицу "DuckDB_Table_Name_for_CSV" по дате Пользовательского запроса От "Date_Begin" до "Date_End" и сохраняем в CSV на диск:Начало-------------------
			if (len(List__FullPath_to_Files) > 0):


				Path_to_Save_CSV_plus_FileNmae:str = Path(Path_to_Save_CSV) / str(f"{Engine}_{Market}_{Board}_{Intrument_Name}_{Interval}.csv");


				#Короче делаем: выбираем все строки из табилцы по столбцу "begin_date" все строки которые, которые удовлетворяет условию, что - дата в "begin_date" находится между переданными датами "Date_Begin" - "Date_End" ---> отфильрованное сортируем по Возрастанию и сохраняем в CSV.

				SQL_DuckDB_request = f"""
				COPY (
					SELECT * FROM {self.DuckDB_Table_Name_for_CSV}
					WHERE begin_date BETWEEN STRPTIME('{Date_Begin}', '{Format_Date}') AND STRPTIME('{Date_End}', '{Format_Date}')
					ORDER BY begin_date ASC
				) TO '{Path_to_Save_CSV_plus_FileNmae}' (FORMAT CSV, HEADER, DELIMITER '{Delimiter_CSV}')
				"""

				# self._Duckdb_Obj.execute(SQL_DuckDB_request)
				Rows_cntr = self._Duckdb_Obj.execute(SQL_DuckDB_request).fetchone();
				
				if (Rows_cntr[0] == 0):
					return "В Parquet-файлах не найдно данных соответвующих указанной дате"
					
			#-----------------------------Фильтруем таблицу "DuckDB_Table_Name_for_CSV" по дате Пользовательского запроса От "Date_Begin" до "Date_End" и сохраняем в CSV на диск:Конец-------------------

			return None;

		except Exception as e:
			return(str(e));

    #-----------------------------------------------------------------ДЛЯ ТРАНСОФРМАЦИИ в CSV:Конец---------------------------------------------------------------------


	#---------------------------------------------------Получение данных из таблицы в станлартный конейтнер Python:Начало------------------------------------------------

	def Extract_Candle_Data_from_Parqet_Files(self, List_FullPath_to_Parqet_Files: list[str])->tuple[list]:
		"""
		Извлекает данные свечей из Parquet-файлов в 8 отдельных списков (по столбцам).

		List_FullPath_to_Parqet_Files - список полных путей до Parquet-файлов.

		ВАЖНО: порядок итоговых данных зависит от порядка элементов во входном списке
		List_FullPath_to_Parqet_Files. Функция НЕ делает ORDER BY по begin_date -
		предполагается, что:
			1) каждый Parquet-файл уже отсортирован по begin_date внутри себя;
			2) файлы в списке идут в хронологическом порядке (от раннего периода к позднему);
			3) диапазоны дат между файлами не пересекаются.
		Если эти условия не гарантированы вызывающей стороной - нужно вернуть ORDER BY begin_date ASC
		в SQL_Select_request ниже.

		Возвращает:
			tuple(list, list, list, list, list, list, list, list) -
			(open_list, close_list, high_list, low_list, value_list, volume_list, begin_date_list, end_date_list)
			либо str с текстом ошибки, если что-то пошло не так.
		"""
		try:

			# Очистка таблицы от предыдущих данных
			self._Duckdb_Obj.execute(f"TRUNCATE TABLE {self.DuckDB_Table_Name_for_CSV}")

			#----------------------------------------Проверка существования файлов и формирование итогового списка путей:Начало------------------------------
			List__FullPath_to_Files: list[str] = []

			for user_Path in List_FullPath_to_Parqet_Files:

				res = self._Check__File_Exist(str(user_Path))

				if res == False:
					# Файла нет - пропускаем
					continue

				List__FullPath_to_Files.append(user_Path)

			#----------------------------------------Проверка существования файлов и формирование итогового списка путей:Конец------------------------------


			# Если ни одного валидного файла не найдено - возвращаем 8 пустых списков
			if len(List__FullPath_to_Files) == 0:
				return [], [], [], [], [], [], [], []


			#----------------------------------------Читаем Parquet-файлы в DuckDB таблицу:Начало------------------------------------------------------------
			# Вставка идет строго последовательно в порядке List__FullPath_to_Files -
			# DuckDB не переупорядочивает INSERT-ы, поэтому итоговый порядок строк в таблице
			# зависит именно от порядка элементов в этом списке.

			for item in List__FullPath_to_Files:

				SQL_DuckDB_request: str = f"INSERT INTO {self.DuckDB_Table_Name_for_CSV} SELECT * FROM read_parquet('{item}')"

				self._Duckdb_Obj.execute(SQL_DuckDB_request)
			#----------------------------------------Читаем Parquet-файлы в DuckDB таблицу:Конец--------------------------------------------------------------


			#----------------------------------------Извлекаем данные построчно через fetchall():Начало-------------------------------------------------------
			# Без ORDER BY - порядок строк соответствует порядку вставки (см. допущение в docstring).
			# Это экономит время на сортировку, т.к. данные уже физически упорядочены нужным образом.

			SQL_Select_request: str = f"""
				SELECT open, close, high, low, value, volume, begin_date, end_date
				FROM {self.DuckDB_Table_Name_for_CSV}
			"""

			Rows: list[tuple] = self._Duckdb_Obj.execute(SQL_Select_request).fetchall()
			#----------------------------------------Извлекаем данные построчно через fetchall():Конец---------------------------------------------------------


			#----------------------------------------Транспонируем строки в столбцы через zip(*rows):Начало----------------------------------------------------
			# zip(*Rows) переворачивает список кортежей-строк в кортежи-столбцы, на C-уровне CPython.

			if len(Rows) == 0:
				return [], [], [], [], [], [], [], []

			Columns = list(zip(*Rows))

			open_list:list       = list(Columns[0])
			close_list:list      = list(Columns[1])
			high_list:list        = list(Columns[2])
			low_list:list          = list(Columns[3])
			value_list:list       = list(Columns[4])
			volume_list:list     = list(Columns[5])
			begin_date_list:list = list(Columns[6])
			end_date_list:list   = list(Columns[7])

			#----------------------------------------Транспонируем строки в столбцы через zip(*rows):Конец------------------------------------------------------


			return open_list, close_list, high_list, low_list, value_list, volume_list, begin_date_list, end_date_list

		except Exception as e:
			return str(e)

	#---------------------------------------------------Получение данных из таблицы в станлартный конейтнер Python:Конец------------------------------------------------






	#---------------------------------------------------------------------Private:Начало--------------------------------------------------------------------------

	def Set__Data_to_DuckDB_Table__JSON_List_String_Format(self, JSON_List_String_Format:str, Format_Date:str)->None|str:

		try:

			self._Duckdb_Obj.execute(f"TRUNCATE TABLE {self.DuckDB_Table_Name_for_JSON}")  # очистка таблицы от предыдушиз данных.


			def Insert_JSON_String_to_DuckDB(duckdb_conn: duckdb.DuckDBPyConnection, table_name: str, raw_json_str: str, Format_Date: str):
				SQL_string = f"""
				INSERT INTO {table_name}
				SELECT 
					unnest[1]::DOUBLE                          AS open,
					unnest[2]::DOUBLE                          AS close,
					unnest[3]::DOUBLE                          AS high,
					unnest[4]::DOUBLE                          AS low,
					unnest[5]::DOUBLE                          AS value,
					unnest[6]::BIGINT                          AS volume,
					STRPTIME(unnest[7], '{Format_Date}')       AS begin_date,
					STRPTIME(unnest[8], '{Format_Date}')       AS end_date
				FROM (
					SELECT unnest(from_json(?::JSON, '[["VARCHAR"]]')) AS unnest
				);
				"""
				duckdb_conn.execute(SQL_string, [raw_json_str])


			Insert_JSON_String_to_DuckDB(self._Duckdb_Obj, self.DuckDB_Table_Name_for_JSON, JSON_List_String_Format, Format_Date);  # Вставляем данные из "JSON_List_String_Format" в котором данные представлены в виде:
			"""
			[
		    [144.02, 143.89, 144.78, 143.03, 599770205.4000001, 4171150, "2014-06-09 10:00:00", "2014-06-09 10:59:59"],
		    [143.86, 144.97, 145.26, 143.57, 1206317361.0000002, 8338580, "2014-06-09 11:00:00", "2014-06-09 11:59:59"],
		    [144.96, 145.3, 146.2, 144.96, 1530742644.3999999, 10507930, "2014-06-09 12:00:00", "2014-06-09 12:59:59"]
			]
			"""
			# То есть list[list] - только в строковом json-формате. DuckDB сама парсит его в соответвии с указанным при INSERT INTO - формате таблицы.


		except Exception as e:
			return str(e);

	def Set__Data_to_DuckDB_Table__Candle_Struct_Format(self, Candle_struct_from_MOEX_Download:MOEX_Download__class.Candle_struct, Format_Date:str)->None|str:

		try:

			self._Duckdb_Obj.execute(f"TRUNCATE TABLE {self.DuckDB_Table_Name_for_JSON}")  # очистка таблицы от предыдушиз данных.


			#---------------------------------------------Теперь заполняем созданную в памяти таблицу DuckDB данными свечей из JSON:Начало------------------------------------
			
			SQL_string:str = "INSERT INTO " + self.DuckDB_Table_Name_for_JSON + f" VALUES (?, ?, ?, ?, ?, ?, STRPTIME(?, '{Format_Date}'), STRPTIME(?, '{Format_Date}'))";  # Формируем комманду

			self._Duckdb_Obj.executemany(SQL_string, Candle_struct_from_MOEX_Download.List_Candles_2D);   # Выполянем, беря каждый элемент из "List_data_Candles_2D", каж строку.
			# executemany, которая выполняется для каждой строки "List_Candles_2D" - эпически медленная, ПОЭТОМУ использовать "Set__Data_to_DuckDB_Table__JSON_List_String_Format" в котором свечи передаются не отдельным фищически python Списком, а одной JSON-Строкой в котором представлен Список списков - как строка, и DuckDB его без проблем парсит в 1000 раз быстрее ---> Set__Data_to_DuckDB_Table__JSON_List_String_Format()
			#---------------------------------------------Теперь заполняем созданную в памяти таблицу DuckDB данными свечей из JSON:Конец------------------------------------


			return None;

		except Exception as e:
			return str(e);


	def _Action(self, Main_Path, Engine_name, Market_name, Board_name, Instrument_name, Interval_name, String_dubg)->None|str:
		
		
		#----------------------------------------Возьмем из столбца "begin_date" значение Года и удалим все дубликаты - оставив только уникальные значения Годов:Начало----------------------------------------

		List_Year:list[str] = self.Separate__Year_in_BeginDateColumn("begin_date");  # begin_date - Устанавливался в "List__Columns_Name_and_Format"

		#for item in List_Year:
			#print(item);

		#----------------------------------------Возьмем из столбца "begin_date" значение Года и удалим все дубликаты - оставив только уникальные значения Годов:Начало----------------------------------------




		#-------------------------------------------------Так, теперь формируем полные пути к парцированным Parquet-файлам с учетом значениея Года:Начало-----------------------------------------
		
		List_Full_Path_to_Parquet_Files:list[DuckDB_StockCandles__class.FullPath_struct] = self.Get__Full_Path_List(Main_Path,Engine_name,Market_name,Board_name,Instrument_name,Interval_name,List_Year);


		# List_Full_Path_to_Parquet_Files - теперь тут список с полными потенциальными путями к файлам Parquet с разбивкой по годам. 

		#for item in List_Full_Path_to_Parquet_Files:
			#print(f"{item.FullPath_string} : {item.Year_string}")

		#-------------------------------------------------Так, теперь формируем полные пути к парцированным Parquet-файлам с учетом значениея Года:Конец-----------------------------------------



		#----------------------------------Теперь поверим какие рельно файлы Parquet существуют на диске из списка "List_Full_Path_to_Parquet_Files":Начало---------------------------------------------------

		List_PathFiles_Exist, List_PathFiles_NotExist = self.Check__Exist_Parquet_Files(List_Full_Path_to_Parquet_Files);


		#for Exist_item in List_PathFiles_Exist:        # Полные пути к существующим файлам Parquet
			#print(f"Exist File:{Exist_item.FullPath_string} : {Exist_item.Year_string}");

		#for NotExist_item in List_PathFiles_NotExist:   # Полные пути к НЕ существующим файлам Parquet - их нужно будет создать.
			#print(f"NotExist File:{NotExist_item.FullPath_string} : {NotExist_item.Year_string}");
	
		#----------------------------------Теперь поверим какие рельно файлы Parquet существуют на диске из списка "List_Full_Path_to_Parquet_Files":Конец---------------------------------------------------


		
		#----------------------------------Теперь для путей к несуществующим файлам "Tuple_TwoList_PathFiles[NotExist]" проверим существует ли папки к этим несуществующим файлам:Начало---------------------------------------------------
	
		List_PathFolder_Exist, List_PathFolder_NotExist= self.Check__Exist_Parquet_Folders(List_PathFiles_Exist, List_PathFiles_NotExist);
	
	
		#for Exist_item in List_PathFolder_Exist:        # Полные пути к существующим папкам Parquet
			#print(f"Exist Folder:{Exist_item}");

		#for NotExist_item in List_PathFolder_NotExist:   # Полные пути к НЕ существующим папкам Parquet
			#print(f"NotExist Folder:{NotExist_item}");

		#----------------------------------Теперь для путей к несуществующим файлам "Tuple_TwoList_PathFiles[NotExist]" проверим существует ли папки к этим несуществующим файлам:Конец---------------------------------------------------


	

		#--------------------------------------------Теперь создаим папки из Списка несуществуюших папок "Tuple_TwoList_PathFolder[NotExist]":Начало---------------------------------------------------

		res = self.Create_folders(List_PathFolder_NotExist);
	
		if (res != None):
			return res;

		#--------------------------------------------Теперь создаим папки из Списка несуществуюших папок "Tuple_TwoList_PathFolder[NotExist]":Конец---------------------------------------------------


		


		#-------------------------------------------------Так теперь наконец то переходим к записи данных свечей в файлы Parquet на диск:Начало--------------------------------------------------------

	

		#`````````````````````````````````````````````````````A:Записываем данные для файлов, которые еще не сущестовали на момент прихода данных свечей:Начало``````````````````````````````````````````````
	
		# Короче если в пришедших данных с MOEX свечей есть свечи с датой ГОДА, которой раньше еще не приходило, то просто записываем эти данные в новый созданный файл.

		res = self.Write__Candles_to_NotExistFile("begin_date", List_PathFiles_NotExist);

		if (res != None):
			return res;

		#`````````````````````````````````````````````````````A:Записываем данные для файлов, которые еще не сущестовали на момент прихода данных свечей:Начало``````````````````````````````````````````````




		#``````````````````````````````````````````````````````````````````````````b:Записываем данные для файлов, которые уже были:Начало``````````````````````````````````````````````

		# Короче если в пришедших данных с MOEX свечей есть свечи с датой ГОДА, которой раньше уже приходили, то "дозаписываем" эти данные в уже существующие файлы. 


		res = self.Write__Candles_to_ExistFile("begin_date", List_PathFiles_Exist);

		if (res != None):
			return res;

		#``````````````````````````````````````````````````````````````````````````b:Записываем данные для файлов, которые уже были:Конец``````````````````````````````````````````````

		return None;
		#-------------------------------------------------Так теперь наконец то переходим к записи данных свечей в файлы Parquet на диск:Конец--------------------------------------------------------

	def Separate__Year_in_BeginDateColumn(self, NameColumn_with_Year:str):


		SQL_string:str = "SELECT DISTINCT YEAR(" + NameColumn_with_Year + ") AS my_delete_DISTINCT FROM " + self.DuckDB_Table_Name_for_JSON + " ORDER BY my_delete_DISTINCT";  # Беремм имя переданной колонки, в которой должны быть значение даты, и выдергиваем оттуда только значение Года и удаляем дубли, то есть оставляем только уникальные значения годов из колонки.

		Years_In_Uniq:[list[tuple[int]]] = self._Duckdb_Obj.execute(SQL_string).fetchall();


		List_with_Year:list[str] = [];

		for item in Years_In_Uniq:
			List_with_Year.append(str(item[0]));


		return List_with_Year;

	def Get__Full_Path_List(self, Main_Path:str, Engine_name:str, Market_name:str, Board_name:str, Instrument_name:str, Interval_name:str, List_Year:list[str])->list[DuckDB_StockCandles__class.FullPath_struct]:


		List__Full_Path:list[DuckDB_StockCandles__class.FullPath_struct] = [];


		for item_year in List_Year:

			Path_string:str = str(Path(Main_Path) / Engine_name / Market_name / Board_name / Instrument_name / Interval_name / (item_year + ".parquet"));

			List__Full_Path.append(DuckDB_StockCandles__class.FullPath_struct(Path_string, item_year));


		return List__Full_Path;

	def Check__Exist_Parquet_Files(self, List_Full_Path_to_Parquet_Files:list[DuckDB_StockCandles__class.FullPath_struct])->tuple[list[DuckDB_StockCandles__class.FullPath_struct], list[DuckDB_StockCandles__class.FullPath_struct]]:

		res:bool = False;


		List_Exist_File:list[DuckDB_StockCandles__class.FullPath_struct]    = [];
		List_NotExist_File:list[DuckDB_StockCandles__class.FullPath_struct] = [];


		for item in List_Full_Path_to_Parquet_Files:

			res = self._Check__File_Exist(item.FullPath_string);

			if (res == True):
				List_Exist_File.append(DuckDB_StockCandles__class.FullPath_struct(item.FullPath_string, item.Year_string));
			else:
				List_NotExist_File.append(DuckDB_StockCandles__class.FullPath_struct(item.FullPath_string, item.Year_string));


		return (List_Exist_File, List_NotExist_File);

	def Check__Exist_Parquet_Folders(self, List_Exist_File:list[DuckDB_StockCandles__class.FullPath_struct], List_NotExist_File:list[DuckDB_StockCandles__class.FullPath_struct])->tuple[list[str], list[str]]:


		#``````````````````````````````Удалим путь к файлу из полнго пути, оставив только путь к папку, которую нужно будет проверить на сущесование:````````````````````````````````````````````
		
		List_Folder_without_PathFile:list[str] = [];


		for item in List_Exist_File:
			List_Folder_without_PathFile.append(Path(item.FullPath_string).parent);

		for item in List_NotExist_File:
			List_Folder_without_PathFile.append(Path(item.FullPath_string).parent);


		List_Folder_without_PathFile = list(set(List_Folder_without_PathFile));  # Удалим дубликаты.

		#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


		#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
		res:bool = False;
		
		List_Exist_Folder:list[str]    = [];
		List_NotExist_Folder:list[str] = [];


		for item in List_Folder_without_PathFile:

			res = self._Check__Folder_Exist(item);

			if (res == True):
				List_Exist_Folder.append(item);
			else:
				List_NotExist_Folder.append(item);
		#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

		return (List_Exist_Folder, List_NotExist_Folder);

	def Create_folders(self, List_Path:str)->str|None:

		for item in List_Path:

			res = self._Create_Folder_for_FullPath(item);

			if (res != None):
				return res;

		return None;

	def Write__Candles_to_NotExistFile(self, Begin_Date_Column_Name:str, List__NotExist_ParquetFile:list[DuckDB_StockCandles__class.FullPath_struct])->None|str:
		
		try:

			for item in List__NotExist_ParquetFile:
			
				SQL_DuckDB_request:str = f"COPY (SELECT * from {self.DuckDB_Table_Name_for_JSON} WHERE Year({Begin_Date_Column_Name}) = {item.Year_string} ORDER BY {Begin_Date_Column_Name} ASC) TO '{item.FullPath_string}' (FORMAT PARQUET)"; # Короче - берем из талицы колонку Даты "Begin_Date_Column_Name" из нее с помощью Year() вычленяем значение только Года равное значению года в поле элемета из списка путей к файлам(там список элементов структуры FullPath_struct, где специально для удобства сохранил отдельное значение года из сохраняемого Паркет-файла) сортируем по Убыванию и все отфилтрованные стркои свечей записываем в файл по полному пути "FullPath_string" в формате Паркет. И так для каждого элемента из "List__NotExist_ParquetFile" - напомню, что в "List__NotExist_ParquetFile" содержаться ТОЛЬКО Уникальные пути к файлам с названием Года.

				self._Duckdb_Obj.execute(SQL_DuckDB_request);  # Выполянем запрос.


			return None;

		except Exception as e:
			return str(e);

	def Write__Candles_to_ExistFile(self, Begin_Date_Column_Name:str, List__Exist_ParquetFile:list[DuckDB_StockCandles__class.FullPath_struct])->None|str:
		
		try:

			for item in List__Exist_ParquetFile:

				self._Duckdb_Obj.execute(f"TRUNCATE TABLE {self.DuckDB_Table_Name_for_ParquetFile}");  # очистка таблицы от предыдушиз данных.
				self._Duckdb_Obj.execute(f"TRUNCATE TABLE {self.DuckDB_Table_Name_for_Union}");        # очистка таблицы от предыдушиз данных.


				SQL_DuckDB_request:str = f"INSERT INTO {self.DuckDB_Table_Name_for_ParquetFile} SELECT * FROM read_parquet('{item.FullPath_string}')";  # Вставляем данные в таблицу "DuckDB_Table_Name_for_ParquetFile" из существующего Parquet-файла на диске.

				self._Duckdb_Obj.execute(SQL_DuckDB_request);  # Выполянем запрос.


				# Добавляем в таблицу "DuckDB_Table_Name_for_Union" следующее: делаем выборку из таблицы "DuckDB_Table_Name_for_ParquetFile", в которую чуть выше загрузили данные Parquet-файла за определенный Год, и обьеденяем с данными таблицы свечей из Json за тот же год. Сортируем их под двум парамтерами: по возрастанию Даты и значению Volume. Суть в том, что ЕСЛИ: в пришедших данных JSON будет свеча с датой которая уже ранее записывалась в Parquet файл - ее нужно как бы обьеденить с существующей(удалить дубликат), НО может быть так, что ранее записанная свеча может быть не закрытой, то есть сохранение было, когда свеча еще не закрылась, ПОЭТОМУ - если даата кокретной текущей пришедшей свечи совпадаеет с датой свечи, которая уже есть в Parquet-файле - нужно поосмтреть их обьем, если текущая пришедшая свеча имеет Volume Больший - ТО значит это более обвноленная свеча. ТАК КАК "DISTINCT ON" ставит первую попавшуюся дублированную строку, то нудно свечи с одинаковой датой отсортировать так - чтобы Voulme с бльшим значнием был выше, чтобы "DISTINCT ON" его оставила, о остальное удалила.
				
				SQL_DuckDB_request = f"""

				INSERT INTO {self.DuckDB_Table_Name_for_Union}
				SELECT DISTINCT ON ({Begin_Date_Column_Name}) *
				FROM (
					SELECT * FROM {self.DuckDB_Table_Name_for_ParquetFile}
					UNION ALL
					SELECT * FROM {self.DuckDB_Table_Name_for_JSON} WHERE YEAR({Begin_Date_Column_Name}) = {item.Year_string}
					)
				ORDER BY {Begin_Date_Column_Name} ASC, volume DESC
				"""

				self._Duckdb_Obj.execute(SQL_DuckDB_request);  # Выполянем запрос.



				SQL_DuckDB_request = f"COPY (SELECT * from {self.DuckDB_Table_Name_for_Union}) TO '{item.FullPath_string}' (FORMAT PARQUET)";

				self._Duckdb_Obj.execute(SQL_DuckDB_request);  # Выполянем запрос.


			return None;

		except Exception as e:
			return str(e);



	#---------------------------------------------------------------------Private:Начало--------------------------------------------------------------------------
	
	def _Create__Empty_DuckDB_Table(self, DuckDB_Table_Name_for_JSON:str, List__Columns_Name_and_Format:list[tuple[str,str]])->None|str:

		try:

			#-----------------------------------------Создаем пустую таблицу DuckDB в памяти с указанным форматом столбцов соответтвующих пришедщим с MOEX:Начало------------------------------
			
			String_execute = "CREATE TEMP TABLE " + DuckDB_Table_Name_for_JSON + "(";
			
			#```````````````````````````Софрмируем строку запрос типа: "CREATE TEMP TABLE my_Stock_Candles_Table(open DOUBLE, close  DOUBLE,...)":````````````````````````````````

			for item in List__Columns_Name_and_Format:
				String_execute = String_execute + item[0] + " " + item[1] + ",";

			String_execute = String_execute + ")";
			#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

			self._Duckdb_Obj.execute(String_execute);

			#-----------------------------------------Создаем пустую таблицу DuckDB в памяти с указанным форматом столбцов соответтвующих пришедщим с MOEX:Конец------------------------------

			return None;

		except Exception as e:
			return str(e);
	
	def _Check__File_Exist(self, Full_Path_to_File:str)->bool:

		if Path(Full_Path_to_File).exists():
			return True;
		else:
			return False;
	
	def _Check__Folder_Exist(self, Path_Folder:str)->bool:

		if Path(Path_Folder).is_dir():
			return True;
		else:
			return False;

	def _Create_Folder_for_FullPath(self, Path_Folder:str)->str|None:
		#Path_Folder - путь полность до папки, которую нужно создать включаю саму папку, которую нужно создать, по типу: "G:\VS2019\my_Folder\Folder_Create"

		try:
			my_path = Path(Path_Folder);

			Path(my_path).mkdir(parents=True, exist_ok=True) # parents=True, exist_ok=True - Значит что создатся вся цепочка папок в указанном пути, если какотой из них нет.

			return None;

		except Exception as e:
			return str(e);
		
	def _Extract_YEAR_from_Date(self, my_Date:str, Format_Date:str)->int:

		year:int = datetime.strptime(my_Date, Format_Date).year;

		return year;

	def _Check_Columns(self)->str|None:

		if (self.List__Columns_Name_and_Format[0][0].lower() != self.MOEX_Download_ref.list_benchmark_Columns_from_MOEX[0].lower()):
			return "_Check_Columns() False";
		
		if (self.List__Columns_Name_and_Format[1][0].lower() != self.MOEX_Download_ref.list_benchmark_Columns_from_MOEX[1].lower()):
			return "_Check_Columns() False";
		
		if (self.List__Columns_Name_and_Format[2][0].lower() != self.MOEX_Download_ref.list_benchmark_Columns_from_MOEX[2].lower()):
			return "_Check_Columns() False";
		
		if (self.List__Columns_Name_and_Format[3][0].lower() != self.MOEX_Download_ref.list_benchmark_Columns_from_MOEX[3].lower()):
			return "_Check_Columns() False";
		
		if (self.List__Columns_Name_and_Format[4][0].lower() != self.MOEX_Download_ref.list_benchmark_Columns_from_MOEX[4].lower()):
			return "_Check_Columns() False";
		
		if (self.List__Columns_Name_and_Format[5][0].lower() != self.MOEX_Download_ref.list_benchmark_Columns_from_MOEX[5].lower()):
			return "_Check_Columns() False";

		if ((self.List__Columns_Name_and_Format[6][0].lower()).replace("_date", "") != self.MOEX_Download_ref.list_benchmark_Columns_from_MOEX[6].lower()):
			return "_Check_Columns() False";

		if ((self.List__Columns_Name_and_Format[7][0].lower()).replace("_date", "") != self.MOEX_Download_ref.list_benchmark_Columns_from_MOEX[7].lower()):
			return "_Check_Columns() False";


		return None;
