from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import join
 
class JoinTest(TestCase):
    string1 ='name,id,age\nAdam,0,15\nEwa,1,10\nOla,2,78\nPiotr,3,56\nAdam,8,25'
    string2 ='id,miasto,ulica\n3,Warszawa,Zielona\n0,Lublin,Ruska\n2,Kraków,Reymonta\n0,Lublin,Stara\n14,Kraków,Nowa'
    column='id'

    def test_right_join_output(self):
        file1=StringIO(self.string1)
        file2=StringIO(self.string2)
        
        expected_output="id,miasto,ulica,name,age\n3,Warszawa,Zielona,Piotr,56\n0,Lublin,Ruska,Adam,15\n2,Kraków,Reymonta,Ola,78\n0,Lublin,Stara,Adam,15\n14,Kraków,Nowa,NULL,NULL\n"

        with patch('sys.stdout', new=StringIO()) as output:
            join.right_join(file1,file2,self.column)
            self.assertEqual(output.getvalue(), expected_output)

    def test_inner_join_output(self):
        file1=StringIO(self.string1)
        file2=StringIO(self.string2)

        expected_output="name,id,age,miasto,ulica\nAdam,0,15,Lublin,Ruska\nAdam,0,15,Lublin,Stara\nOla,2,78,Kraków,Reymonta\nPiotr,3,56,Warszawa,Zielona\n"
        
        with patch('sys.stdout', new=StringIO()) as output:
            join.inner_join(file1,file2,self.column)
            self.assertEqual(output.getvalue(), expected_output)
    
    def test_left_join_output(self):
        file1=StringIO(self.string1)
        file2=StringIO(self.string2)

        expected_output="name,id,age,miasto,ulica\nAdam,0,15,Lublin,Ruska\nEwa,1,10,NULL,NULL\nOla,2,78,Kraków,Reymonta\nPiotr,3,56,Warszawa,Zielona\nAdam,8,25,NULL,NULL\n"

        with patch('sys.stdout', new=StringIO()) as output:
            join.left_join(file1,file2,self.column)
            self.assertEqual(output.getvalue(), expected_output)

    
    def test_column_chcek(self):
        expected_output=2
        column_names=['a','b','c']
        column='c'
        result=join.column_check(column_names,column)
        self.assertEqual( result,expected_output)

        
