from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder


class ProductRow(GridLayout):
    def remove_row(self):
        # Usunięcie wiersza z kontenera
        parent = self.parent
        parent.remove_widget(self)

class AddRowButton(Button):
    def add_row(self, *args):
        # Dodanie nowego wiersza do kontenera
        parent = self.parent
        new_row = ProductRow()
        parent.add_widget(new_row)
        
        # Usunięcie przycisku "Dodaj"
        parent.remove_widget(self)
        
        # Dodanie nowego przycisku "Dodaj" pod nowym wierszem
        
        add_button = AddRowButton(text="Dodaj", size_hint=(None, None), width = parent.width, height = 40)
        add_button.bind(on_release=add_button.add_row)
        parent.add_widget(add_button)
        
        # Wiązanie pozycji przycisku "Dodaj" z pozycją środka rodzica
        add_button.bind(center_x=parent.setter('center_x'))

class MainApp(App):
    def build(self):
        root = ScrollView()  # Zastosowanie ScrollView jako głównego kontenera
        
        # Wewnątrz ScrollView umieszczamy GridLayout z produktem
        layout = GridLayout(cols=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))  # Automatyczne dostosowanie wysokości
        
        # Dodaj wiersze (produktów) do kontenera
        for _ in range(4):
            layout.add_widget(ProductRow())
        
        # Dodaj przycisk "Dodaj" na szerokość wierszy
        add_button = AddRowButton(text="Dodaj", size_hint=(None, None), width=layout.width*8, height=40)
        add_button.bind(on_release=add_button.add_row)
        layout.add_widget(add_button)

        root.add_widget(layout)

        return root
    def move_row_up(self, row):
        container = row.parent
        index = container.children.index(row)
        if index > 0:
            container.remove_widget(row)
            container.add_widget(row, index + 1)
    def move_row_down(self, row):
        container = row.parent
        index = container.children.index(row)
        if index < len(container.children) - 1:
            container.remove_widget(row)
            container.add_widget(row, index - 1)


if __name__ == "__main__":
    MainApp().run()
