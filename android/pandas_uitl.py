import pandas as pd


class PandasHandler:
    def __init__(self, file_path):
        """
        类初始化方法，读取 Excel 文件并存储在 DataFrame 中。

        参数：
            file_path (str): Excel 文件路径。
        """
        self.df = pd.read_excel(file_path)

    def read_excel(self):
        """
        读取 Excel 文件。

        返回：
            DataFrame: Excel 文件中的数据。
        """
        return self.df

    def write_excel(self, file_path):
        """
        将 DataFrame 写入 Excel 文件。

        参数：
            file_path (str): 新 Excel 文件路径。
        """
        self.df.to_excel(file_path)

    def append_excel(self, file_path):
        """
        将 DataFrame 追加到 Excel 文件。

        参数：
            file_path (str): 现有 Excel 文件路径。
        """
        with pd.ExcelWriter(file_path, mode='a') as writer:
            self.df.to_excel(writer, index=False, header=False)

    def create_pivot_table(self, index, columns, values):
        """
        创建透视表。

        参数：
            index (list): 行索引。
            columns (list): 列索引。
            values (list): 值。

        返回：
            DataFrame: 透视表。
        """
        return pd.pivot_table(self.df, index=index, columns=columns, values=values)

    def add_row(self, row_data):
        """
        添加一行数据。

        参数：
            row_data (dict): 待添加的数据，键为列名，值为数据。

        返回：
            DataFrame: 添加新行后的 DataFrame。
        """
        self.df = self.df.append(row_data, ignore_index=True)
        return self.df

    def delete_row(self, index):
        """
        删除一行数据。

        参数：
            index (int): 待删除行的索引。

        返回：
            DataFrame: 删除行后的 DataFrame。
        """
        self.df = self.df.drop(index)
        return self.df

    def update_row(self, index, new_data):
        """
        修改一行数据。

        参数：
            index (int): 待修改行的索引。
            new_data (dict): 新数据，键为列名，值为数据。

        返回：
            DataFrame: 修改行后的 DataFrame。
        """
        self.df.loc[index] = new_data
        return self.df

    def query_data(self, condition):
        """
        查询数据。

        参数：
            condition (str): 查询条件。

        返回：
            DataFrame: 满足条件的数据。
        """
        return self.df.query(condition)

    def set_column_names(self, new_column_names):
        """
        设置列名。

        参数：
            new_column_names (list): 新列名列表。
        """
        self.df.columns = new_column_names

    def set_row_index(self, new_row_index):
        """
        设置行索引。

        参数：
            new_row_index (list): 新行索引列表。
        """
        self.df.index = new_row_index

    def sort_data(self, column_name, ascending=True):
        """
        排序数据。

        参数：
            column_name (str): 排序的列名。
            ascending (bool): 是否升序。
        """
        self.df.sort_values(by=column_name, ascending=ascending, inplace=True)

    def drop_duplicates(self, column_names):
        """
        合并重复行。

        参数：
            column_names (list): 用于合并重复行的列名列表。
        """
        self.df.drop_duplicates(subset=column_names, inplace=True)

    def fillna(self, value):
        """
        填充缺失值。

        参数：
            value: 填充值。
        """
        self.df.fillna(value, inplace=True)
