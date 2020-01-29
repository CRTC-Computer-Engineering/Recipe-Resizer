import wx

whole_recipe = []
ingredient_name = ""
ingredient_number = ""
ingredient_type = ""

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent = None, title = 'Recipe Resizer', size = (400, 300))
        panel = wx.Panel(self)
        
        wx.StaticText(panel, id = -1, label = "Welcome to Ms Vashaw's very own recipe multiplier!", pos = (5, 0))
     
        wx.StaticText(panel, id = -1, label = "How many ingredients?", pos = (5, 35))
        self.total_ingredients = wx.text_ctrl = wx.TextCtrl(panel, pos = (5, 55))
               
        wx.StaticText(panel, id = -1, label = "Would you like to multiply or divide your recipe?", pos = (5, 90))
        self.multiply_or_divide = wx.text_ctrl = wx.TextCtrl(panel, pos = (5, 115))
       
        wx.StaticText(panel, id = -1, label = "By what?", pos = (5, 140))
        self.number = wx.text_ctrl = wx.TextCtrl(panel, pos = (5, 165))
             
        self.first_button = wx.Button(panel, label = "Resize", pos = (180, 180))
        self.first_button.Bind(wx.EVT_BUTTON, self.operation)

        self.report = wx.text_ctrl

        self.Show()
        wx.
    '''
    def get_box_value(self, event):
        print(self.total_ingredients.GetValue())
        print(self.multiply_or_divide.GetValue())
        print(self.number.GetValue())
    '''
    def operation(multiply_or_divide, number):
        if multiply_or_divide == "multiply":
            return (float(self.ingredient_number.GetValue() * self.number.GetValue()))

        if multiply_or_divide == "divide":
            return (float(self.ingredient_number.GetValue() / self.number.GetValue()))        
        '''
        total_ingredients = self.first_box
        multiply_or_divide = self.second_box
        number = self.third_box
        '''
    if self.multiply_or_divide == "divide" and self.number == 0:
        print ("You cannot divide by zero. Please try again. ")
        number = float(input("Divide your recipe by what? "))

    for i in range(self.total_ingredients):
        count = i + 1
        if count == 1:
            order = "st"
        elif count == 2:
            order = "nd"
        elif count == 3:
            order = "rd"
        elif count >= 4:
            order = "th"
        elif count > 11 and count % 10 == 1:
            order = "st"
        elif count > 12 and count % 10 == 2:
            order = "nd"
        elif count > 13 and count % 10 == 3:
            order = "rd"
        elif count % 100 == 0:
            order = ""
            
        ingredient_name = input("What will your " + str(count) + order + " ingredient be? ")
        ingredient_type = input("Units of measurement used for " + ingredient_name + ": ")
        ingredient_number = float(input("How many " + ingredient_type + "? "))
            
        if ingredient_type == "tsp" or "teaspoon":
            if ingredient_number * number % 3 == 0:
                ingredient_type = "tablespoons"
            
        print ("What you entered: " + str(ingredient_number) + " " + ingredient_type + " of " + ingredient_name)

        rounded_number = round(operation(multiply_or_divide, number), 3)

        math = str(rounded_number) + ingredient_type + " of " + ingredient_name
            
        whole_recipe.append(math)
        '''
    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
        '''
        def state():
            return


        self.report.SetValue(state())

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()