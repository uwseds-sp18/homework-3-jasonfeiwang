from homework3 import create_dataframe 
import unittest 


class TestHomework3(unittest.TestCase):
    # test whether the dataframe returned contains the right column names
    def test_column_names(self):
        inputdf = create_dataframe('./class.db')
        inputdfColumns, testColumns = list(inputdf.columns), ['video_id', 'category_id', 'language']
        checkColumnInd = not bool(set(inputdfColumns).difference(set(testColumns))) 
        self.assertTrue(checkColumnInd)

    # test whether the dataframe returned contains the right number of rows
    def test_table_rows(self):
        inputdf = create_dataframe('./class.db')
        self.assertTrue(inputdf.shape[0] == 75005)
    
    # test whether the columns ['video_id', 'category_id' and 'language'] is a key
    def test_key_columns(self):
        inputdf = create_dataframe('./class.db')
        rows = inputdf.shape[0]
        uniqueValuesOfColumns = inputdf.groupby(['video_id', 'category_id', 'language']).size().shape[0]
        self.assertTrue(rows == uniqueValuesOfColumns)
    
    # test whether the correct exception is generated when an invalid path is provided.
    def test_exception_type(self):
       	with self.assertRaises(ValueError):
            create_dataframe('wrongDatabasePath')


if __name__ == '__main__':
    unittest.main()