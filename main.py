import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, WipeTransition, SwapTransition, FadeTransition, FallOutTransition, RiseInTransition
from kivy.graphics import RoundedRectangle
from kivy.uix.image import AsyncImage
def on_month_button_click(instance, month):
    month_screen.set_dates(month)
    sm.transition = get_random_transition()
    sm.switch_to(month_screen)
def on_back_to_months(instance):
    sm.transition = get_random_transition()
    sm.switch_to(month_list_screen)
def on_back_to_year_selection(instance):
    sm.transition = get_random_transition()
    sm.switch_to(main_screen)
def get_random_transition():
    transitions = [SlideTransition(), WipeTransition(), SwapTransition(), FadeTransition(), FallOutTransition(), RiseInTransition()]
    return random.choice(transitions)
class MonthScreen(Screen):
    def __init__(self, **kwargs):
        super(MonthScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10)
        self.label = Label(text="", font_size=32, size_hint=(1, 0.8))
        self.back_button = Button(text="Back to Months", size_hint=(1, 0.2), background_color=[0, 0.5, 1, 1])
        self.back_button.bind(on_press=on_back_to_months)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.back_button)
        self.add_widget(self.layout)
    def set_dates(self, month):
                        if month == "August":
                            self.label.text = f"Important dates for August:\n1. 28/8/23 - School Reopens for Yr. 1 -9\n2. 29/8/23 - FS2 Staggered Start"
                        elif month == "September":
                            self.label.text = f"Important dates for September:\n1. 4/9/23 - All FS2\n2. 29/9/23 - Prophet's Birthday (TBC)"
                        elif month == "October":
                            self.label.text = f"Important dates for October:\n1. 5/10/23 - World Teachers Day\n2. 13/10/23 - Pink Day/ Breast Cancer Awareness Day/ Sewa Day\n3. 16/10/23 - 20/10/23 - Half term\n4. 24/10/23 - United Nation Day "
                        elif month == "November":
                            self.label.text = f"Important dates for November:\n1. 3/11/23 - Flag Day\n2. 13/11/23 - World Kindness Day\n3. 17/11/23 - Dubai Fitness Challenge\n4. 20/11/23 - Children's Day 18th/ Dreams and Aspirations\n5. 24/11/23 - WSA National Day Celebration/ Thanksgiving Day\n6. 30/11/23 - Marty's Day"
                        elif month == "December":
                            self.label.text = f"Important dates for December:\n1. 1/12/23 - National Day Leave\n2. 7/12/23 - Arabic Day\n3. 8/12/23 - EY Christmas Jumper Day/ End of Term\n4. 11/12/23 - 30/12/23 - Winter Break"
                        elif month == "January":
                            self.label.text = f"Important dates for January:\n1. 1/1/23 - New Year\n2. 2/1/23 - Term 2 commence"
                        elif month == "February":
                            self.label.text = f"Important dates for February:\n1. 6/2/23 - Safer Internet Day\n2. 7/2/23 - World Read Aloud Day\n3. 8/2/23 - Israa we Al Mearaj (TBC)\n4. 9/2/23 - International Day (TBC)\n5. 19/2/23 - 21/2/23 - Half Term\n6. 23/2/23 - Gorgean (15 Shaabaan) (TBC)"
                        elif month == "March":
                            self.label.text = f"Important dates for March:\n1. 6/3/23 - International Women's Day\n2. 7/3/23 - World book day\n3. 8/3/23 - Ramadan Starts (TBC)\n4. 14/3/23 - Pi Day\n5. 18/3/23 - World Happiness Day\n6. 21/3/23 - Mother's Day\n7. 22/3/23 - End of Term\n8. 27/3/23 - 30/3/23 - Spring Break"
                        elif month == "April":
                            self.label.text = f"Important dates for April:\n1. 1/4/23 - 12/4/23 - Spring Break\n2. 15/4/23 -  Term 3 Commence\n3. 22/4/23 - Earth Day"
                        elif month == "May":
                            self.label.text = f"Important dates for May:\n1. Nothing lol"
                        elif month == "June":
                            self.label.text = f"Important dates for June:\n1. 17/6/23 - 18/6/23 - EID AL ADHA (TBC)\n2. 21/6/23 - Father's Day  "
                        elif month == "July":
                            self.label.text = f"Important dates for July:\n1. 5/7/23 - End of Acadamic Year\n"
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.year_button = Button(
            text="Year 9",
            font_size=32,
            size_hint=(1, 0.2),
            background_normal='',
            background_color=[1, 0, 0, 1],
        )
        self.year_button.bind(on_press=on_back_to_months)
        self.layout.add_widget(AsyncImage(source='https://i.ibb.co/98njrwn/image-2023-12-06-231206455.png', size=(300, 300)))  # Placeholder for image
        self.layout.add_widget(self.year_button)
        self.add_widget(self.layout)
        with self.year_button.canvas.before:
            RoundedRectangle(pos=self.year_button.pos, size=self.year_button.size, radius=[15, 15, 15, 15])
def on_back_to_months(instance):
    sm.transition = get_random_transition()
    sm.switch_to(month_list_screen)
def on_back_to_year_selection(instance):
    sm.transition = get_random_transition()
    sm.switch_to(main_screen)
sm = ScreenManager(transition=get_random_transition())
main_screen = MainScreen(name='main')
month_screen = MonthScreen(name='month')
month_list_screen = Screen(name='month_list')
month_list_layout = BoxLayout(orientation='vertical')
months = ["August", "September", "October", "November", "December", "January", "February", "March", "April", "May", "June", "July"]
for month in months:
    btn = Button(
        text=month,
        font_size=32,
        size_hint=(1, 0.8),
        background_color=[random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 1],
    )
    btn.bind(on_press=lambda instance, month=month: on_month_button_click(instance, month))
    month_list_layout.add_widget(btn)
back_to_year_button = Button(text="Back to Year Selection", size_hint=(1, 0.2), background_color=[1, 0, 0, 1])
back_to_year_button.bind(on_press=on_back_to_year_selection)
month_list_layout.add_widget(back_to_year_button)
month_list_screen.add_widget(month_list_layout)
sm.add_widget(main_screen)
sm.add_widget(month_screen)
sm.add_widget(month_list_screen)
# Run the app
class ChangeColorApp(App):
    def build(self):
        return sm
if __name__ == '__main__':
    ChangeColorApp().run()