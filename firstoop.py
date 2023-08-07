class item:
  all=[]
    def __init__(self,name,prise,quantity) :
        self.name=name
        self.prise=prise
        self.quantity=quantity
        assert prise >=0,F"prise {prise} is gerater than or 0"
        assert quantity >=0
       
        item.all.append(self)
        
    def calculate_total_prise(self):
        return self.prise * self.quantity


item1=item('ali',200,7)
item2=item('tahoora',224,5)
item3=item('arman',300,8)
item4=item('sara',100,4)
# item1.name='phone'
# item1.prise=200
# item1.quantity=7
# print(item1.calculate_total_prise(item1.prise,item1.quantity))
# print(item1.name,item1.prise,item1.quantity,item1.calculate_total_prise())

# for i in item.all:
#     print(i.name)
print(item.all)